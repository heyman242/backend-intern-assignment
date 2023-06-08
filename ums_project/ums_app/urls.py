from django.urls import path
from .views import (
    create_task,
)
app_name = 'ums_app'

urlpatterns = [
    path('', create_task),

]
