from django.test import TestCase

# Create your tests here.
from django.urls import *
from .views import *



urlpatterns = [
    # path('test-api-view/', test_api_view),
    path('Category-api-view/', CategoryListAPIView.as_view()),
    # path('Category-api-view/create', CategoryCreateAPIView.as_view()),
    # path('Category-api-view/update/<int:pk>', CategoryUpdateAPIView.as_view()),
    # path('Category-api-view/delete/<int:pk>', CategoryDestroyAPIView.as_view()),
    # path('Category-api-view/detail/<int:pk>', CategoryDetailView.as_view()),
    
    # path('Category-api-view/<int:pk>/', Category_api_view),path('test-api-view/', test_api_view),
    
# Car   
    # path('test-api-view/', test_api_view),
    path('Car-api-view/', CarListAPIView.as_view()),
    # path('Car-api-view/create', CarCreateAPIView.as_view()),
    # path('Car-api-view/update/<int:pk>', CarUpdateAPIView.as_view()),
    # path('Car-api-view/delete/<int:pk>', CarDestroyAPIView.as_view()),
    # path('Car-api-view/detail/<int:pk>', CarDetailView.as_view()),
    
    # path('Car-api-view/<int:pk>/', Car_api_view),path('test-api-view/', test_api_view),
 

]