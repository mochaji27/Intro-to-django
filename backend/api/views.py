from django.http import JsonResponse

# Create your views here.
def api_home(request, *args, **kwargs):
    return JsonResponse({"Message" : "Hi there, this is your dhjango API response!!"})