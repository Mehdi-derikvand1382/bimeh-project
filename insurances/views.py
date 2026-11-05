from django.shortcuts import render

# Create your views here.

from .models import Policy
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PolicySerializer

def policy_list(request):
    # gettig all insurances from database
    policies = Policy.objects.all()

    # sending insurances to template for view

    context = {
        'policies': policies
    }

    return render(request, 'insurances/policy_list.html', context)

@api_view(['GET'])
def policy_api_list(request):
    policies = Policy.objects.all()
    serializer = PolicySerializer(policies, many=True)
    return Response(serializer.data)
