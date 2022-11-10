from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.autopark.api.v1.urls'))
]
