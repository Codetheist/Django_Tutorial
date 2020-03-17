from django.http import HttpResponse

# Create your views here.
def homePaigeView(request):
    return  HttpResponse('Hello, World!')