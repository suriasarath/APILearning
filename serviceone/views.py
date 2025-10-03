from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer,ProductSerializer,PolicySerializer
from django.contrib.auth.models import User
from rest_framework import generics
from . models import Product, Policy
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class CustomResponseViewset(ModelViewSet):
    def finalize_response(self,request,response,*args,**kwargs):
        response.data={'data':response.data,'status':response.status_code}
        return super().finalize_response(request,response,*args,**kwargs)
    
@api_view(['GET'])
def service_func(request):
    return Response({"main":"hello AI world","User Id":request.user_id})

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer 

class ProductViewset(CustomResponseViewset):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PolicyViewset(CustomResponseViewset):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    




    