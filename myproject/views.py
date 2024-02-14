from django.http import HttpResponse
def handler404(request,exception):
    return HttpResponse("<h1 style='coloe:red'>Page hi nahi hai bhai !!</h1>", status=401
                        )