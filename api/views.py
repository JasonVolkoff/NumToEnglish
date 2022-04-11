from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from api.utils import ConvertToWords
# Create your views here.


class NumToEnglish(View):
    def get(self, request, *args, **kwargs):
        num = request.GET.get("number", "")
        converted = ConvertToWords(num)
        return JsonResponse({
            "status": "GET",
            "num_in_english": converted.response
        })

    def post(self, request, *args, **kwargs):
        return JsonResponse({"status": "POST"})
