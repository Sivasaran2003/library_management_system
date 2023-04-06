from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.login),
    path('show_books',views.show_books),
    path('add_book',views.add_book),
    path('delete_book',views.delete_book),
    path('borrow',views.borrow),
    path('users',views.users),
    path('return_book',views.return_book)
]
