from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from login.models import CustomUser

def view_consultas(request):

    return render(request, 'consulta/index.html')



def check_user_email(key,email,nones):
    key = key
    if key is not None:
        email = email
        if email is not None:
            if CustomUser.objects.filter(email=email).exists():
                return JsonResponse({"exists": True}, status=200)
            else:
                return JsonResponse({"exists": False}, status=404)
        else:
            return JsonResponse({"error": "Email not provided"}, status=400)
    else:
        return JsonResponse({"error": "Key not provided"}, status=400)

@require_http_methods(["GET"])
def check_username(request):
    key = request.GET.get('key', None)
    if key is not None:
        username = request.GET.get('username', None)
        if username is not None:
            if CustomUser.objects.filter(username=username).exists():
                return JsonResponse({"exists": True}, status=200)
            else:
                return JsonResponse({"exists": False}, status=404)
        else:
            return JsonResponse({"error": "Username not provided"}, status=400)
    else:
        return JsonResponse({"error": "Key not provided"}, status=400)

@require_http_methods(["GET"])
def get_all_users(request):
    key = request.GET.get('key', None)
    if key is not None:
        users = list(CustomUser.objects.values())
        return JsonResponse(users, safe=False, status=200)
    else:
        return JsonResponse({"error": "Key not provided"}, status=400)
