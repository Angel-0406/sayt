from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .form import ContactForm
from .models import News, Category



def new_list(request):
    news=News.objects.all().filter(status=News.Status.Published)
    context={'news':news}
    return render(request,'news_list.html',context)
def news_detail(request,id):
    try:
        news=get_object_or_404(News,status=News.Status.Published,id=id)
        context={'news':news}
        return render(request,'news_detail.html',context)
    except:
        return HttpResponse('error')

def homePageView(request):
    news_list=News.objects.all().filter(status=News.Status.Published).order_by('publish_time')[:4]
    categoriy=Category.objects.all()
    business=News.objects.all().filter(status=News.Status.Published).filter(categoriy__name='Business')
    fashion = News.objects.all().filter(status=News.Status.Published).filter(categoriy__name='Fashion')
    sports = News.objects.all().filter(status=News.Status.Published).filter(categoriy__name='Sports')
    games = News.objects.all().filter(status=News.Status.Published).filter(categoriy__name='Games')
    technology = News.objects.all().filter(status=News.Status.Published).filter(categoriy__name='Technology')
    photopraphy= News.objects.all().filter(status=News.Status.Published).filter(categoriy__name='Photography')
    life_style = News.objects.all().filter(status=News.Status.Published).filter(categoriy__name='Life&style')
    context={
        'news_list':news_list,
        'categoriy':categoriy,
        'business':business,
        'fashion':fashion,
        'sports':sports,
        'games':games,
        'technology':technology,
        'photopraphy':photopraphy,
        'life_style':life_style
    }
    return render(request,'index.html',context)
def contactPageView(request):
    form=ContactForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        form.save()
        return redirect('index')
    context={'form':form}
    return render(request,'contact.html',context)

def page404(request):
    return render(request,'404.html')
def sinlePageView(request,id):
    news = News.objects.filter(status=News.Status.Published,id=id).first()
    # categoriy = Category.objects.all()
    # mahalliy = News.objects.all().filter(status=News.Status.Published).filter(categoriy__name='Mahalliy')
    context = {
        'news': news,
        # 'categoriy': categoriy,
        # 'mahalliy': mahalliy
    }
    return render(request, 'single_page.html', context)
def query(request):
    search = request.GET.get('q')
    yangi  = News.objects.filter(Q(title__icontains=search))
    context={'yangi':yangi}
    return render(request,'query.html',context)

def detail(request,slug):
    new=News.objects.get(slug=slug)
    context={'new':new}
    return render(request,'detail.html',context)






