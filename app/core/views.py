from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # html_content = """

    # """
    # return HttpResponse(html_content)
    return render(request, 'core/home.html')