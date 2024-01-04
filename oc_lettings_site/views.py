from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def error_500(request):
    # 500 error simulation
    1 / 0
    return render(request, 'index.html')


def custom_error_500(request):
    return render(request, '500.html', status=500)
