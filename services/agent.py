import json

from django.db.models import F
from django.conf import settings
from django.core import serializers
from google import generativeai as genai

from ai import prompts
from ai.models import AIResult
from products.models import Product
from outflows.models import Outflow


class SGEAgent:

    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)

        self.__client = genai.GenerativeModel(
            settings.GEMINI_MODEL,
            system_instruction=prompts.SYSTEM_INSTRUCTIONS
        )

    def __get_data(self):
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
        try:
            chat = self.__client.start_chat()

            response = chat.send_message(prompts.USER_PROMPT.replace('{{data}}', self.__get_data()))

            result = response.text

            AIResult.objects.create(result=result)
            return f'AI Result: {result}'
        except Exception as e:
            return str(e)
