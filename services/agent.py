import json

from django.db.models import F
from django.conf import settings
from django.core import serializers
from django.utils.timezone import localdate
from google import generativeai as genai

from ai import prompts
from ai.models import AIResult
from products.models import Product
from outflows.models import Outflow


class SGEAgent:
    """
    This class handles the integration with a generative AI model from Google (Gemini).
    It allows interaction with the AI to process data related to products and outflows,
    returning results based on the provided API and model configuration.

    Attributes:
        __client (GenerativeModel or None): The client instance for interacting with the generative AI model.
    """

    def __init__(self):
        """
        Initializes the SGEAgent instance by checking the presence of the API key and model configuration.
        If either the GEMINI_API_KEY or GEMINI_MODEL is missing or empty, the client is not initialized.

        It configures the generative AI client with the provided API key and model, allowing the agent
        to interact with the AI service.

        If no valid API key or model is found in the settings, the agent will not attempt to interact with the AI.
        """
        if settings.GEMINI_API_KEY == '' or settings.GEMINI_MODEL == '':
            self.__client = None
            return

        genai.configure(api_key=settings.GEMINI_API_KEY)

        self.__client = genai.GenerativeModel(
            settings.GEMINI_MODEL,
            system_instruction=prompts.SYSTEM_INSTRUCTIONS
        )

    def __get_data(self):
        """
        Retrieves and serializes the data for products and outflows to be sent to the generative AI model.

        This method fetches all products and outflows from the database and prepares them as a JSON-formatted string.
        The data is serialized using Django's `serializers` module.

        Returns:
            str: A JSON string containing serialized data for products and outflows, or None if the AI client is not initialized.
        """
        if self.__client is None:
            return None

        products = Product.objects.all()
        outflows = Outflow.objects.all().select_related('product').annotate(
            product_selling_price=F('product__selling_price'),
            product_cost_price=F('product__cost_price')
        )

        return json.dumps({
            'products': serializers.serialize(format='json', queryset=products),
            'outflows': serializers.serialize(format='json', queryset=outflows)
        })

    def invoke(self):
        """
        Initiates communication with the generative AI model and sends the data for processing.

        This method starts a chat session with the AI model, sends a message containing the data retrieved from the
        `__get_data` method, and stores the response in the `AIResult` model. If no valid API client is available,
        this method returns `None` and does nothing.

        Returns:
            str: The result of the AI model's response, or a message indicating that no API key was provided.
        """
        if self.__client is None:
            return None

        current_date = localdate()

        try:
            if not AIResult.objects.filter(created_at__date=current_date).exists():
                chat = self.__client.start_chat()

                response = chat.send_message(prompts.USER_PROMPT.replace('{{data}}', self.__get_data()))

                result = response.text

                AIResult.objects.create(result=result)
                return f'AI Result: {result}'
        except Exception as e:
            return str(e)
