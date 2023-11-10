from topics.models import Topic, Category

def news_topics(request):
    news_category = Category.objects.get(category_name='news')
    news_topics = Topic.objects.filter(category=news_category)[:4]
    return {'news_topics': news_topics}



def latest_topics(request):
    latest_topics = Topic.objects.order_by('-created_at')[:4]
    return {'latest_topics': latest_topics}
