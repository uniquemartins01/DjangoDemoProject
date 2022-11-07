from myblog import views
from django.urls import path, include

urlpatterns = [
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('reversed_prg',views.reversed_prg,name='reversed_prg'),
]