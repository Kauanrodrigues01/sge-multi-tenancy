from django.core.cache import cache
from django.http import JsonResponse


class RateLimitingMiddleware:
    RATE_LIMIT = 5

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_ip = request.META.get('REMOTE_ADDR')
        cache_key = f"rate_limit_{user_ip}"
        requests = cache.get(cache_key, 0)

        if requests >= self.RATE_LIMIT:
            return JsonResponse({'error': 'Rate limit exceeded'}, status=429)

        cache.set(cache_key, requests + 1, timeout=60)  # Reset após 1 minuto
        return self.get_response(request)
