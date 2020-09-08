from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.detail, name='detail'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),

 ]


