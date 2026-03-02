from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

# In-memory storage
orders = []
id_counter = 1

@csrf_exempt
@require_http_methods(["GET", "POST"])
def orders_list(request):
    global id_counter
    if request.method == 'GET':
        return JsonResponse(orders, safe=False)
    elif request.method == 'POST':
        order = json.loads(request.body)
        order['id'] = id_counter
        order['status'] = 'PENDING'
        id_counter += 1
        orders.append(order)
        return JsonResponse(order, status=201)

@csrf_exempt
@require_http_methods(["GET"])
def order_detail(request, id):
    for order in orders:
        if order['id'] == id:
            return JsonResponse(order)
    return JsonResponse({"error": "Order not found"}, status=404)
