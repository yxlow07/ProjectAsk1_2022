from django.shortcuts import render

# Create your views here.


def perisian(request):
    return render(request, 'perisian.min.html', {})
