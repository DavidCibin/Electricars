from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # route for cars index
  path('cars/', views.cars_index, name='index'),
  # route for cars details
  path('cars/<int:car_id>/', views.cars_detail, name='detail'),
  # route used to show a form and create a car
  path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
  # routes to update and delete
  path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
  path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
  # route for the booking/insurance
  path('cars/<int:car_id>/add_booking/', views.add_booking, name='add_booking'),
  # route for the add profile
  path('cars/<int:car_id>/add_profile/', views.add_profile, name='add_profile'),
  # route to signup
  path('accounts/signup/', views.signup, name='signup'),
  path('accounts/', views.account, name='account'),
  # route for photos
  path('cars/<int:car_id>/add_photo/', views.add_photo, name='add_photo'),
]