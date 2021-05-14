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
  # route to signup
  path('accounts/signup/', views.signup, name='signup'),
  path('accounts/', views.account, name='account'),
  # route for photos
  path('cars/<int:car_id>/add_photo/', views.add_photo, name='add_photo'),

  # route for booking and extra profile form
  path('cars/<int:car_id>/addbooking/', views.addbooking, name='addbooking'),

  # route to update profile
  path('accounts/<int:pk>/update/', views.ProfileUpdate.as_view(), name='accounts_update'),

  # route for email subscription
  path("subscription/", views.subscription, name="subscription"),

  # path to cancel a reservation
  path('account/booking/<int:pk>/delete/', views.BookingDelete.as_view(), name='cancel_rental'),
  # path to contact form
  path('contact/', views.contact, name='contact'), 
]