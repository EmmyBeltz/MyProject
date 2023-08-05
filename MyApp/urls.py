from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('pricing.html', views.pricing, name='pricing'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('courses.html', views.courses, name='courses'),
    path('trainers.html', views.trainers, name='trainers'),
    path('events.html', views.events, name='events'),
    path('course-details.html/<str:pk>/', views.coursedetails, name='coursedetails'),
    path('contact.html', views.contact, name='contact'),
    path('send-email', views.send_email, name='send_email')


]