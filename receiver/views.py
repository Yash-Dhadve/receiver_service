import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

SENDER_CALLBACK_URL = "https://sender-service-bmar.onrender.com/api/ack/"

@csrf_exempt
def receive_ping(request):
    if request.method == "POST":
        data = json.loads(request.body)

        print("📩 Received from sender:", data)

        ack_payload = {
            "status": "received",
            "receiver": "receiver_service",
            "original_payload": data
        }

        try:
            requests.post(
                SENDER_CALLBACK_URL,
                json=ack_payload,
                timeout=5
            )
        except Exception as e:
            print("❌ Failed to send ACK:", e)

        return JsonResponse({
            "status": "ok",
            "message": "Request received & ACK sent"
        })

    return JsonResponse({"error": "Invalid method"}, status=405)
