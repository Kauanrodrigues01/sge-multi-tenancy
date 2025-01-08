import logging
from evolutionapi.client import EvolutionClient
from evolutionapi.models.message import TextMessage
from decouple import config
from evolutionapi.models.message import ButtonMessage, Button


class EvolutionAPI:
    def __init__(self):
        """
        Initializes the Evolution API client using configuration settings.
        """
        self.__base_url: str = config('EVOLUTION_API_BASE_URL', cast=str, default='base-url')
        self.__api_token: str = config('EVOLUTION_API_TOKEN', cast=str, default='api-token')
        self.__instance_name: str = config('INSTANCE_NAME', cast=str, default='instance-name')
        self.__instance_token: str = config('INSTANCE_TOKEN', cast=str, default='instance-token')
        self.__my_number: str = config('MY_NUMBER', cast=str, default='my-number')
        self.__client: EvolutionClient = EvolutionClient(
            base_url=self.__base_url,
            api_token=self.__api_token
        )
        self.logger = logging.getLogger(__name__)

    def send_text_message(self, instance_name: str = None, instance_token: str = None, number: str = None, text: str = None, delay: int = 0) -> dict:
        """
        Sends a text message using the Evolution API.

        :param instance_name: Instance name.
        :param instance_token: Token for the instance.
        :param number: Recipient's phone number in international format (e.g., "5511999999999").
        :param text: Message text.
        :param delay: Optional delay in milliseconds before sending the message.
        :return: API response as a dictionary or an error message.
        """
        message = TextMessage(
            number=number if number else self.__my_number,
            text=text,
            delay=delay
        )

        try:
            response = self.__client.messages.send_text(
                instance_id=instance_name if instance_name else self.__instance_name,
                message=message,
                instance_token=instance_token if instance_token else self.__instance_token,
            )
            return response
        except Exception as e:
            # Log the error and return a fallback response
            self.logger.error(f"Failed to send message: {str(e)}")
            return {"status": "error", "message": "Failed to send the message"}
        
        
    def send_message_with_buttons(self, instance_name: str = '', instance_token: str = '', number: str = None, title : str = '', description : str = '', footer : str = '', buttons : list[Button] = []):
        """
        Sends a message with buttons using the Evolution API.

        :param instance_name: Instance name.
        :param instance_token: Token for the instance.
        :param number: Recipient's phone number in international format.
        :param title: Title of the button message.
        :param description: Description of the button message.
        :param footer: Footer of the button message.
        :param buttons: List of Button objects.
        :return: A dictionary containing the status and response from the API.
        """
        message = ButtonMessage(
            number=number if number else self.__my_number,
            title=title,
            description=description,
            footer=footer,
            buttons=buttons
        )
        
        try:
            response = self.__client.messages.send_buttons(
                instance_id=instance_name if instance_name else self.__instance_name, 
                message=message, 
                instance_token=instance_token if instance_token else self.__instance_token
            )
            
            return response
        except Exception as e:
            # Log the error and return a fallback response
            self.logger.error(f"Failed to send message: {str(e)}")
            return {"status": "error", "message": "Failed to send the button message"}
        
        
if __name__ == '__main__':
    evolution = EvolutionAPI()
    evolution.send_text_message(
        text='TEST',
        delay=0
    )