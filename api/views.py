from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from api.serializer import CompanySerilizer
from api.models import Company
from api.serializer import EmployeesSerilizer
from api.models import Employees
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class= CompanySerilizer

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset=Employees.objects.all()
    serializer_class= EmployeesSerilizer