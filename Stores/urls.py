from django.contrib import admin
from django.urls import path
from Stores import views as store_view

app_name = 'Stores'

urlpatterns = [
    path('signup/', store_view.signup, name="signup"),
    path('login/', store_view.login, name="login"),
    path('<name>/dashboard/', store_view.dashboard, name="dashboard"),
    path('<name>/dashboard/<int:order_id>/', store_view.deliver_order, name="deliver_order"),
    path('<name>/dashboard/<int:order_id>/', store_view.cancel_order, name="cancel_order"),
    path('logout/', store_view.logout, name="logout"),
]