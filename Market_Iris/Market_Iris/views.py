from django.shortcuts import render
from django.http import JsonResponse
from visualizer.models import BankRecord

def get_data(request):
    data = list(BankRecord.objects.values())
    return JsonResponse(data, safe=False)