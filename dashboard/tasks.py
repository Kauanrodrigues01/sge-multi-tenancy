from celery import shared_task
from services.agent import SGEAgent


agent = SGEAgent()


@shared_task
def generate_ai_feedback():
    response = agent.invoke()
    return response
