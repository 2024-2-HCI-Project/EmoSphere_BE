from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def csrf_token_view(request):
    """
    CSRF 토큰 반환 뷰
    """
    return JsonResponse({"csrfToken": request.META.get("CSRF_COOKIE")})
