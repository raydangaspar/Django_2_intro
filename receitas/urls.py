from django.urls import path

from . import views

# primeiro parâmetro é a rota. Segundo parâmetro é o view.
# Terceiro parâmetro namespace do aplicativo para a entrada url
urlpatterns = [
    path('', views.index, name='index'),
    path('receita', views.receita, name='receita')
]