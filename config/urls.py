
from django.contrib import admin
from django.urls import path
from insurances import views #adding views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('policies/', views.policy_list, name='policy_list'),# new address
    path('policies/add/', views.add_policy, name= 'add_policy'),
    path('api/policies/', views.policy_api_list, name='api_policy_list'), # new api address
]

