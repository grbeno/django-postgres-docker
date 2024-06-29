from .views import home_page_view
from django.urls import path

urlpatterns = [
	path('', home_page_view, name="home"),

]