from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Report
from django.contrib import messages
import json

# Create your views here.
def index(request):
    return render(request, "index.html")

def get_incident_report(request):
    if request.user.is_anonymous:
        return redirect('/')
    elif request.method == "POST":
        location = request.POST.get("location")
        incident_description = request.POST.get("incident_description")
        date = request.POST.get("date")
        time = request.POST.get("time")
        incident_location = request.POST.get("incident_location")
        initial_severity = request.POST.get("initial_severity")
        suspected_cause = request.POST.get("suspected_cause")
        immediate_actions_taken = request.POST.get("immediate_actions_taken")
        sub_incident_type = json.dumps(request.POST.getlist("checks[]"))
        print(sub_incident_type, type(sub_incident_type))
        reported_by = request.user
        print(location,incident_description,date,time,incident_location,initial_severity,suspected_cause,
        immediate_actions_taken,sub_incident_type,reported_by,end='\n')
        report = Report(location=location, incident_description=incident_description, date=date, time=time,
        incident_location=incident_location, initial_severity=initial_severity,
        suspected_cause=suspected_cause, immediate_actions_taken=immediate_actions_taken,
        sub_incident_type=sub_incident_type, reported_by=reported_by)
        report.save()
        messages.success(request, 'Incident report saved.')
        return redirect('/')
    return render(request, 'form.html')
    

# login password suhail$$$***
def loginUser(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Success: You are logged in.")
            return redirect('/')
        else:
            error = {"error":"User does not exist"}
    return render(request, "login.html", error)

def logoutUser(request):
    logout(request)
    return redirect('/')   