from django.shortcuts import redirect


def python_redirect(request):
    return redirect('https://ru.wikipedia.org/wiki/Python')


def setup_redirect(request):
    return redirect('https://www.djangoproject.com/')