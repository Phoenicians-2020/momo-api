from django.urls import path, include

urlpatterns = [
    path('products/', include('products.api.v1.urls')),
    path('sellers/', include('users.api.v1.urls'))
]
