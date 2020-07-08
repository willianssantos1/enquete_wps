from django.urls import path

from . import views

app_name = 'votacoes'

urlpatterns = [
    # ex: /votaces/
    path('', views.IndexView.as_view(), name='index'),
     # ex: /votaces/5/
    path ('<int:pk>/', views.DetalhesView.as_view, name='detalhes'),
    # ex: /votaces/5/resultados/
    path('<int:pk>/resultados', views.ResultadosView.as_view, name='resultados'),
    # ex: /votaces/5/votar
    #path('int:questao_id>/votar/', views.votar, name='votar'),
]