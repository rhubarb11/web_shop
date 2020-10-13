from django.urls import path
from . views import addReviewView, UpdateReviewView
from . import views



urlpatterns = [
    path('add_review/<str:slug>/', views.addReviewView, name='add_review'),
    path('edit_review/<int:pk>/', views.UpdateReviewView.as_view(), name='edit_review'),

]
