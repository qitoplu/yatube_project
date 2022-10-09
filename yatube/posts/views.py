from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('Is it the main page, Captain?')


def group_posts(request, slug):
    return HttpResponse(f'Page {slug}')
    