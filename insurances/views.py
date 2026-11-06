from django.shortcuts import render, redirect
from .models import Policy
from .forms import PolicyForm

# Create your views here.

from .models import Policy
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PolicySerializer
from rest_framework import generics 

def policy_list(request):
    # gettig all insurances from database
    policies = Policy.objects.all()
    return render(request, 'insurances/policy_list.html', {'policies': policies})
    # sending insurances to template for view

    context = {
        'policies': policies
    }

    return render(request, 'insurances/policy_list.html', context)


#a new view for registering insurances
def add_policy(request):
    if request.method == 'POST':
        form = PolicyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('policy_list')

    else:
        form = PolicyForm


    return render(request, 'insurances/add_policy.html', {'form': form})
    


#@api_view(['GET'])
#def policy_api_list(request):
#    policies = Policy.objects.all()
#    serializer = PolicySerializer(policies, many=True)
#    return Response(serializer.data)

class PolicyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer

