from django.shortcuts import render
import json
from django.http import JsonResponse
import time




def chat(request, order_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get("message")

        # print("user_message ==>", user_message)
        if not user_message:
            return JsonResponse({"error": "Empty message"}, status=400)

        time.sleep(5)

    return JsonResponse({"reply": "here is the reply"})