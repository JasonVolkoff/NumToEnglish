from django.urls import path
from api.views import NumToEnglish

urlpatterns = [
    path('num_to_english/', NumToEnglish.as_view(), name="num_to_english")
]
