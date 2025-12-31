import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def receive_ping(request):
    if request.method == "POST":
        data = json.loads(request.body)

        print("📩 Received data:", data)

        return JsonResponse({
            "status": "ok",
            "message": "Data received",
            "data": data
        })

    return JsonResponse({"error": "Invalid method"}, status=405)
