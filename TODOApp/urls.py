from django.urls import path
from .views import index,login,signup,add_todo,signout,delete_todo,change_todo
urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('add-todo/',add_todo),
    path('logout/',signout),
    path('delete-todo/<int:id>',delete_todo),
    path('change-status/<int:id>/<str:status>', change_todo)
]
