'''urls'''
from django.urls import path
from .views import sign_up, sign_in, sign_out, modify_password, view_history

urlpatterns = [
    path('sign_up', sign_up, name='sign_up'),
    path('sign_in', sign_in, name='sign_in'),
    path('sign_out', sign_out, name='sign_out'),
    path('modify_password', modify_password, name='modify_password'),
    path('view_history', view_history, name='view_history')
]
