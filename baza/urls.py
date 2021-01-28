from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'baza'
urlpatterns = [
    path('', views.home, name='home'),
    path('min_prices/', views.min_prices, name='min_prices'), 
    path('minimum/', views.minimum, name='minimum'),  
    path('max_prices/', views.max_prices, name='max_prices'),   
    path('maximum/', views.maximum, name='maximum'),   
    path('models-chart/', views.models_chart, name='models-chart'),  
    path('modelsByProducer/', views.modelsByProducer, name='modelsByProducer'), 
    path('producerSearch/', views.producerSearch, name='producerSearch'),  
    path('searchProducerMinMax/', views.searchProducerMinMax, name='searchProducerMinMax'),  
    path('min_max_for_producer/', views.min_max_for_producer, name='min_max_for_producer'),  
    path('max_comments_for_phone/', views.max_comments_for_phone, name='max_comments_for_phone'),
    path('top_active_users/', views.top_active_users, name='top_active_users')  

]