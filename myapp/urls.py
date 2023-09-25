
from django.urls import path , include ,reverse 
from . import views
from sample import settings

app_name='myapp'

urlpatterns = [
    #path('',views.home,name='home'),
    path('home/<int:id>',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('navigation',views.navi,name='navi'),
    path('uploadprof',views.uploadprof,name='uploadprof'),
    path('sim',views.sim,name='sim'),
    path('editprofile/<int:id>',views.editprofile,name='editprofile'),
    path('allprofile/<int:id>',views.allprofile,name='allprofile'),
    path('viewprofile/<int:id>',views.viewprofile,name='viewprofile'),

    path('newviewprofile/<int:id>',views.newviewprofile,name='newviewprofile'),
    path('viewcheck/<int:id>',views.viewcheck,name='viewcheck'),

    path('editbasicinformation/<int:id>',views.editbasicinformation,name='editbasicinformation'),
    path('editworkdetails/<int:id>',views.editworkdetails,name='editworkdetails'),
    path('editeducation/<int:id>',views.editeducation,name='editeducation'),
    path('editskill/<int:id>',views.editskill,name='editskill'),
    path('editexam/<int:id>',views.editexam,name='editexam'),
    path('editresponsible/<int:id>',views.editresponsible,name='editresponsible'),
    path('editachivements/<int:id>',views.editachivements,name='editachivements'),


    path('updatebasicinformation/<int:id>/<int:id1>',views.updatebasicinformation,name="updatebasicinformation"),
    path('updateworkdetails/<int:id>/<int:id1>',views.updateworkdetails,name="updateworkdetails"),
    path('updateeducation/<int:id>/<int:id1>',views.updateeducation,name="updateeducation"),
    path('updateskill/<int:id>/<int:id1>',views.updateskill,name="updateskill"),
    path('updateexam/<int:id>/<int:id1>',views.updateexam,name="updateexam"),
    path('updateresponsible/<int:id>/<int:id1>',views.updateresponsible,name="updateresponsible"),
    path('updateachivements/<int:id>/<int:id1>',views.updateachivements,name="updateachivements"),


    path('addworkdetails/<int:id>',views.addworkdetails,name='addworkdetails'),
    path('addeducation/<int:id>',views.addeducation,name='addeducation'),
    path('addskill/<int:id>',views.addskill,name='addskill'),
    path('addexam/<int:id>',views.addexam,name='addexam'),
    path('addresponsible/<int:id>',views.addresponsible,name='addresponsible'),
    path('addacivement/<int:id>',views.addacivement,name='addacivement'),


    path('test',views.test,name='test'),
]

