from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/1/
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/1/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/1/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]  # TypeError: 'set' object is not reversible Internal Server Error: /polls/ :https://www.yht7.com/news/113039
