from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.shortcuts import render

from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


def blog(request):
    return render(request, "blog/index.html", {"MEDIA_URL": settings.MEDIA_URL})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def blog_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    print(request.user)
    cxt = [
      {
        'id': 1,
        'title': '',
        'code': 'foo = "bar"\n',
        'linenos': False,
        'language': 'python',
        'style': 'friendly'
      },
      {
        'id': 2,
        'title': '',
        'code': 'print("hello, world")\n',
        'linenos': False,
        'language': 'python',
        'style': 'friendly'
      },
      {
        'id': 3,
        'title': '',
        'code': 'print("hello, world")',
        'linenos': False,
        'language': 'python',
        'style': 'friendly'
      }
    ]
    return Response(cxt)