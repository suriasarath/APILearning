import jwt
from django.http import JsonResponse
from django.conf import settings


class JWTMiddleware:

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):

        token = request.headers.get("Authorization")
        print(token)
        if request.path in ["/api/token/"]:
             return self.get_response(request)

        if not token:
            return JsonResponse({"error":"No token"})
        
        try:
            payload = jwt.decode(token.split()[1],settings.SECRET_KEY,algorithms=['HS256'])
            print(payload)
            request.user_id =payload.get('user_id')
        except jwt.ExpiredSignatureError:
            return JsonResponse({"erroe":"Expired Signature Error"})
        
        return self.get_response(request)
