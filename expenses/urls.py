from django.urls import path
from .views import ExpenseCreateAPI, ExpenseListAPI


urlpatterns = [
    path("api/expense/create/", ExpenseCreateAPI.as_view()),
    path("api/expense/list/", ExpenseListAPI.as_view()),
]