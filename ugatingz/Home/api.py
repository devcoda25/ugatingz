from topics.models import Topic, Category

def news_topics(request):
    news_category = Category.objects.get(category_name='news')
    news_topics = Topic.objects.filter(category=news_category)[:4]
    return {'news_topics': news_topics}



def latest_topics(request):
    latest_topics = Topic.objects.order_by('-created_at')[:4]
    return {'latest_topics': latest_topics}

def trending_topics(request):
   trending_topics = Topic.objects.order_by('-created_at')#[:5]
   return {'trending_topics': trending_topics}

def other_topics(request):
   other_topics = Topic.objects.order_by('-created_at')[:5]
   return {'other_topics': other_topics}

def random_topics(request):
  random_topics = Topic.objects.order_by('?')[:6]
  return {'random_topics': random_topics}
