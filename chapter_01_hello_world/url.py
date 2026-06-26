from django.urls import path

from.views import home_page_view

urlspatterns =[
    path(" ", home_page_view),
]