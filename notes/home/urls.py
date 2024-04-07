from django.urls import path
from . import views
urlpatterns=[
    path("",views.home_,name="homePage"),
    path("contect/",views.Contect,name="contect"),
    path("about/",views.about,name="about"),
    path("accounts/new",views.newaccound,name="newaccound"),
    path("accounts/login",views.login,name="login"),
    path("accounts/logout",views.logout,name="logout"),
 path("accounts/settings",views.settings,name="accountSettings")   ,
 path("accounts/delete",views.deletacc,name="deleteaccount"),
 path("accounts/changePassword",views.changePassword,name="changePassword"),
 path("myNotes/new",views.createNewNote,name="CreateNewNote"),
 path("myNotes",views.myNotes,name="notes"),
 path("<str:user_name>/note/<int:pk>",views.viewNote,name="viewNote"),
 path("<str:user_name>/note/<int:pk>/delete",views.deleteNote,name="deleteNote"),
]