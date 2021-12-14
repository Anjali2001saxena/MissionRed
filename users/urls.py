from django.contrib import admin
from django.urls import path
from users import views as user_view

app_name = 'users'

urlpatterns = [
    path('signup/', user_view.signup, name="signup"),
    path('login/', user_view.login, name="login"),
    path('<name>/dashboard/', user_view.dashboard, name='dashboard'),
    path('<name>/doctors/', user_view.doctors, name="doctors"),
    path('<name>/doctors/<int:slot_id>/', user_view.book_slot, name="book_slot"),
    path('<name>/stores/', user_view.stores, name="stores"),
    path('<name>/stores/<store>/', user_view.place_order, name="place_order"),
    path('<name>/stories/', user_view.stories, name="stories"),
    path('<name>/stories/write_portal/', user_view.write_story, name="write_story"),
    path('<name>/stories/read_portal/', user_view.view_story_list, name="view_story_list"),
    path('<name>/stories/read_portal/<int:story_id>/', user_view.read_story, name="read_story"),
    path('logout/', user_view.logout, name="logout"),
]