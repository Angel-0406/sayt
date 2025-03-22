from django.urls import path

from .views import homePageView, page404, sinlePageView, contactPageView, new_list, news_detail, query, detail

urlpatterns=[
    path('',homePageView,name='index'),
    path('page404/',page404,name='page404'),
    path('single/<int:id>',sinlePageView,name='news_detail_page'),
    path('contact/',contactPageView,name='contact'),
    path('all/',new_list,name='about'),
    path('contact-page/',contactPageView,name='contactPageView'),
    path('query/',query,name='query'),
    path('<slug:slug>',detail,name='detail'),
]
