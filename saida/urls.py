from django.urls import path
from .views import notaSaidaList, notaSaidaNew, notaSaidaUpdate, notaSaidaDelete

app_name = 'saida'

urlpatterns = [
    path('notaSaidaList/', notaSaidaList, name='notaSaidaList'),
    path('notaSaidaNew/', notaSaidaNew, name='notaSaidaNew'),
    path('notaSaidaUpdate/<int:pk>/', notaSaidaUpdate, name='notaSaidaUpdate'),
    path('notaSaidaDelete/<int:pk>/', notaSaidaDelete, name='notaSaidaDelete'),
]