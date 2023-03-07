from rest_framework import serializers
from api.models import Company
from api.models import Employees

class CompanySerilizer(serializers.HyperlinkedModelSerializer):
    company_id =serializers.ReadOnlyField()
    class  Meta:
        model = Company
        fields='__all__'


class EmployeesSerilizer(serializers.HyperlinkedModelSerializer):
    company_id =serializers.ReadOnlyField()
    class Meta:
        model = Employees
        fields= '__all__'
