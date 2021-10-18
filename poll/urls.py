from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    # poll/
    path('poll_list/', views.poll_list, name='poll_list'),
    path('<int:question_id>/', views.poll_detail, name='poll_detail'),
    path('<int:question_id>/poll_vote/', views.poll_vote, name='poll_vote'),
    path('<int:question_id>/poll_result/', views.poll_result, name='poll_result'),
]