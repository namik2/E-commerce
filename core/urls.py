from django.urls import path
from core.views import ContactView, AboutUs, Error404, FAQ, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('about/', AboutUs, name='about'),
    path ('contact_us/', ContactView.as_view(), name='contact'),
    path('404error/', Error404),
    path('faq/', FAQ),
]
