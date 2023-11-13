from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from topics.models import Topic


def Home(request):
    return render(request,"screens/index.html")

def topic_detail(request, category_slug, topic_slug):
   topic_detail = Topic.objects.get(category__slug=category_slug, slug=topic_slug)
   context= {'topic_detail': topic_detail}
   return render(request, 'screens/singletopic.html', context )
