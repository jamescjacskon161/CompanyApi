from django.urls import path,include
from api.views import CompanyViewSet
from rest_framework import routers
from api.views import EmployeesViewSet


router = routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'employees',EmployeesViewSet)
urlpatterns = [
    path ('',include(router.urls))
]