from django.shortcuts import render,redirect,get_object_or_404
from . import forms,models
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def home_(r):
    return render(r,"home.html")
def Contect(r):
    return render(r,"contect.html")
def about(r):
    return render(r,"about.html")
def newaccound(r):
    if r.method=="POST":
        frm=forms.new_accound(r.POST)
        if frm.is_valid():
            fristName=frm.cleaned_data["frist_name"]
            lastName=frm.cleaned_data['last_name']
            email=frm.cleaned_data["email"]
            userName=frm.cleaned_data["user_name"]
            password=frm.cleaned_data["password"]
            confpassword=frm.cleaned_data["confpassword"]
            if not User.objects.filter(username=userName).exists():
                if password==confpassword:
                    user=User.objects.create_user(userName,email,password,first_name=fristName,last_name=lastName)
                    auth.login(r,user)
                    return redirect("homePage")

    frm=forms.new_accound()
    return render(r,"new-user.html",{"form":frm})
def login(r):
    if r.method=="POST":
        frm=forms.login(r.POST)
        if frm.is_valid():
            user_name=frm.cleaned_data["user_name"]
            password=frm.cleaned_data["password"]
            user=auth.authenticate(username=user_name,password=password)
            if user:
                auth.login(r,user)
                return redirect("homePage")
    frm=forms.login()
    return render(r,"login.html",{"form":frm})
@login_required
def logout(r):
    auth.logout(r)
    return redirect("homePage")
@login_required
def settings(r):
    return render(r,"profile.html")
@login_required
def deletacc(r):
    if r.method=="POST":
        frm=forms.delete(r.POST)
        if frm.is_valid():
            password=frm.cleaned_data["password"]
            user1=User.objects.get(username=r.user)
            if user1.check_password(password):
                User.delete(user1)
                return redirect("homePage")
    frm=forms.delete()
    return render(r,"deleteAccount.html",{"form":frm})
@login_required
def changePassword(r):
    if r.method=="POST":
        frm=forms.ChangePassword(r.POST)
        if frm.is_valid():
            password=frm.cleaned_data["currentPassword"]
            newpassword=frm.cleaned_data["newPassword"]
            confnewpassword=frm.cleaned_data["confNewPassword"]
            user1=User.objects.get(username=r.user)
            if user1.check_password(password):
                if newpassword==confnewpassword:
                    user1.set_password(newpassword)
                    user1.save()
                    auth.login(r,user1)
                    return redirect("homePage")
    frm=forms.ChangePassword()
    return render(r,"change_password.html",{"form":frm})
@login_required
def createNewNote(r):
    if r.method=="POST":
        frm=forms.CreateNewNote(r.POST)
        if frm.is_valid():
            title=frm.cleaned_data["title"]
            body=frm.cleaned_data["body"]
            user=get_object_or_404(User,username=r.user)
            note=models.notes()
            note.title=title
            note.body=body
            note.user=user
            note.save()
            return redirect("viewNote",user_name=user.username,pk=note.pk)
    frm=forms.CreateNewNote()
    return render(r,"createNewNote.html",{"form":frm})
@login_required
def myNotes(r):
    user=get_object_or_404(User,username=r.user)
    result=models.notes.objects.filter(user=user).order_by("-date")
    return render(r,"notes.html",{"results":result})
def viewNote(r,user_name,pk):
    user=get_object_or_404(User,username=r.user)
    note=get_object_or_404(models.notes,pk=pk)
    if note.user==user:
        return render(r,"viewNote.html",{"note":note})
def deleteNote(r,user_name,pk):
    user=get_object_or_404(User,username=r.user)
    note=get_object_or_404(models.notes,pk=pk)
    if r.method=="POST":
        note.delete()
        return redirect("homePage")
    return render(r,"deleteNote.html")