from django.shortcuts import render, redirect
from ..loginapp.models import Registration
from .models import Travel
from django.contrib import messages
def index(request):

    if 'user' not in request.session:
        return redirect('Login:my_index')
    user = Registration.objects.get(id = request.session['user'])
    context = {
    'user': user, 'travel': Travel.objects.filter(traveller = request.session['user']),
    'othertravel': Travel.objects.exclude(traveller = request.session['user']),
    }
    print "at the index"
    return render(request, "travelbuddyapp/success.html", context)

def add(request):
    print "at the add"
    return render(request, "travelbuddyapp/add.html")

def create(request):
    Output = Travel.objects.add_destination(request.POST, request.session['user'])
    if Output['outcome'] == "fail":
        for key, value in Output.items():
            messages.error(request, value)
        return redirect("First:add")
    else:
        return redirect("First:my_index")

def offset(request, id):
    context = {
    "trip": Travel.objects.filter(id = id)
    }
    return render(request, "travelbuddyapp/show.html", context)
def update(request, id):
    print "got to the update redirect"
    Update_output = Travel.objects.update_destination(id,request.session['user'])
    print "got after the upgrade"
    return redirect("First:my_index")
