from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from api.utils import ConvertToWords
import json


class NumToEnglish(View):
    def get(self, request, *args, **kwargs):
        num = request.GET.get("number", "")
        converted = ConvertToWords(num)
        return JsonResponse({
            "status": converted.status,
            "num_in_english": converted.response
        })

    def post(self, request, *args, **kwargs):
        num = json.loads(request.body.decode('utf-8')).get("number", "")
        converted = ConvertToWords(num)
        return JsonResponse({
            "status": converted.status,
            "num_in_english": converted.response
        })


class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, "base.html", {})
