from django.urls import path
from .views import ExpenseCreateAPI, ExpenseListAPI, ExpenseDeleteAPI


urlpatterns = [
    path("api/expense/create/", ExpenseCreateAPI.as_view()),
    path("api/expense/list/", ExpenseListAPI.as_view()),
    path("api/expense/delete/", ExpenseDeleteAPI.as_view()),
]