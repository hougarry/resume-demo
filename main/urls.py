
from django.urls import path
from . import views

app_name = 'main'

#create models one by one
urlpatterns = [
    #path('', views.IndexView.as_view(), name='home'),
    #path('contact/', views.ContactView.as_view(), name='contact'),
    #path('portfolio/', views.PortfolioView.as_view(), name='portfolios'),
    #path('portfolio/<slug:slug>/', views.PortfolioDetailView.as_view(), name='portfolio'),
    #path('blog/', views.BlogDetailView.as_view(), name='blog'),
]
