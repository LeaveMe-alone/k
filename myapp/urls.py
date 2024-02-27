from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('portfolio_details/', views.portfolio_details, name='portfolio_details'),
    path('blog_single/<slug:slug>/', views.blog_single, name='blog_single'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)