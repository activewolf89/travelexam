from django.shortcuts import render, redirect
from .models import Registration
from django.contrib import messages
def index(request):
    return render(request, "loginapp/index.html")

def registration(request):

    output = Registration.objects.input(request.POST)
    if output['outcome'] == 'success':
        request.session['user'] = output['user'].id
        return redirect("First:my_index")
    else:
        for key, value in output.items():
            messages.error(request, value)
        return redirect ('Login:my_index')



def login(request):

    output = Registration.objects.input2(request.POST)
    if output['status'] == True:
        request.session['user'] = output['user'].id
        context = {
        "name":output
        }
        return redirect("First:my_index")
    else:
        messages.error(request, output['error'])
        return redirect('Login:my_index')


def logout(request):
    del request.session['user']
    return redirect('Login:my_index')
