from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('create/', views.CreatePoll.as_view(), name='create'),
    path('all/', views.PollList.as_view(), name='all'),
    path('vote/<poll_id>/', views.vote, name='vote'),
    path('results/<poll_id>/', views.results, name='results'),
    path('users/<str:username>/', views.UserPollList.as_view(), name='user_poll_list'),
    path('delete/<int:pk>/', views.DeletePoll.as_view(), name='delete')
]
