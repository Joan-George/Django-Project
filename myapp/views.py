from django.shortcuts import render , redirect
from .models import Register

from django.contrib import auth
from .forms import *
from django.forms.models import model_to_dict
# Create your views here.

def home(request,id):
	form=Register.objects.get(id=id)
	try:
		basic=BasicInformation.objects.get(Uid=id)
	except Exception as e:
		basic = False
	
	return render(request,'home.html',{'form':form,'basic':basic})
def index(request):
	return render(request,'index.html')

def register(request):

	if request.method=='POST':
		a=Register()
		a.Username=request.POST.get('r_uname')
		a.email=request.POST.get('r_email')
		a.Password=request.POST.get('r_pass')
		a.C_Password=request.POST.get('r_cpass')
		a.save()
		return redirect("/index")
	else:
		return HttpResponse("Nothing is inserted")
def login(request):
	if request.method=='POST':
		email=request.POST.get('l_email')
		password=request.POST.get('l_pass')

		if Register.objects.filter(Password=password,email=email).exists():
			form=Register.objects.get(email=email)
			#return render(request,"home.html",{"form":form})
			url="/home/"+str(form.id)
			return redirect(url)
		else:
			return render(request,'index.html',{"error":"Invalid Username or Password"})
def profile(request):
	return render(request,'profile.html',{})

def navi(request):
	return render(request,'navigation.html')

def uploadprof(request):
	return render(request,'profile.html')	
	

def sim(request):
	return render(request,'sim.html')

def editprofile(request,id):
	try:
		basicform=BasicInformation.objects.get(Uid=id)
		talentform=Talents.objects.filter(Uid=id)
		educationform=EducationQualification.objects.filter(Uid=id)
		examform=Exam.objects.filter(Uid=id)
		responseform=Responsibility.objects.filter(Uid=id)
		workingform=WorkingDetails.objects.filter(Uid=id)
		achiveform = Achivements.objects.filter(Uid=id)
		return render(request,'ViewProfile.html',{"basicform":basicform,"talentform":talentform,"educationform":educationform,"examform":examform,"responseform":responseform,"workingform":workingform,"id":id,"achiveform":achiveform})
	except:
		return render(request,'404-error.html',{'id':id})

def newviewprofile(request,id):
	mform=Register.objects.get(id=id)
	basicform=BasicInformationForm()
	responseform=ResponsibilityForm()
	achiveform=AchivementsForm()
	talentform=TalentForm()
	examform=ExamForm()
	workingform=WorkingDetailsForm()
	educationform=EducationQualificationForm()
	return render(request,'NewViewProfile.html',{"basicform":basicform,"responseform":responseform,"achiveform":achiveform,"talentform":talentform,"examform":examform,"workingform":workingform,"mform":mform,"educationform":educationform})

def viewcheck(request,id):
	if request.method == 'POST':
		form = BasicInformationForm(request.POST)
		form1=ResponsibilityForm(request.POST)
		form2=AchivementsForm(request.POST)
		form3=TalentForm(request.POST)
		form4=ExamForm(request.POST)
		form5=WorkingDetailsForm(request.POST)
		form6=EducationQualificationForm(request.POST)
		if form.is_valid() and form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and form6.is_valid():
			form6.save()
			form.save()
			form1.save()
			form2.save()
			form3.save()
			form4.save()
			form5.save()
			
		return render(request,"Success.html",{'id':id})
	else:
		form=BasicInformationForm()
		return HttpResponse("Failed to insert")

def allprofile(request,id):
	mform=Register.objects.get(id=id)
	form=BasicInformation.objects.all()
	return render(request,"AllProfile.html",{"form":form,'mform':mform})

def viewprofile(request,id):
	try:
		basicform=BasicInformation.objects.get(Uid=id)
		talentform=Talents.objects.filter(Uid=id)
		educationform=EducationQualification.objects.filter(Uid=id)
		examform=Exam.objects.filter(Uid=id)
		responseform=Responsibility.objects.filter(Uid=id)
		workingform=WorkingDetails.objects.filter(Uid=id)
		achiveform = Achivements.objects.filter(Uid=id)
		return render(request,'ViewProfile1.html',{"basicform":basicform,"talentform":talentform,"educationform":educationform,"examform":examform,"responseform":responseform,"workingform":workingform,"id":id,"achiveform":achiveform})
	except:
		return render(request,'404-error.html',{'id':id})

def editbasicinformation(request,id):
	basicinfo=BasicInformation.objects.get(id=id)
	basicform=BasicInformationForm(data=model_to_dict(BasicInformation.objects.get(id=id)))
	return render(request,'EditBasicInfo.html',{"basicform":basicform,'basicinfo':basicinfo})

def updatebasicinformation(request,id,id1):
	if request.method == 'POST':
		basic=BasicInformation.objects.get(id=id)
		form=BasicInformationForm(request.POST,instance=basic)
		if form.is_valid():
			form.save()
			url='/editprofile/'+str(id1)
			return redirect(url)
	
	return HttpResponse("Failed")

def editworkdetails(request,id):
	workinfo=WorkingDetails.objects.get(id=id)
	workform=WorkingDetailsForm(data=model_to_dict(WorkingDetails.objects.get(id=id)))
	return render(request,'EditWorkDetails.html',{"workform":workform,'workinfo':workinfo})

def updateworkdetails(request,id,id1):
	if request.method == 'POST':
		work=WorkingDetails.objects.get(pk=id)
		wform=WorkingDetailsForm(request.POST,instance = work)
		if wform.is_valid():
			wform.save(commit=True)
			url='/editprofile/'+str(id1)
			return redirect(url)

def editeducation(request,id):
	edu=EducationQualification.objects.get(id=id)
	eduform=EducationQualificationForm(data=model_to_dict(EducationQualification.objects.get(id=id)))
	return render(request,'EditEducation.html',{"eduform":eduform,'edu':edu})

def updateeducation(request,id,id1):
	if request.method == 'POST':
		edu=EducationQualification.objects.get(pk=id)
		eform=EducationQualificationForm(request.POST,instance = edu)
		if eform.is_valid():
			eform.save(commit=True)
			url='/editprofile/'+str(id1)
			return redirect(url)

def editskill(request,id):
	skill=Talents.objects.get(id=id)
	skillform=TalentForm(data=model_to_dict(Talents.objects.get(id=id)))
	return render(request,'EditSkill.html',{"skillform":skillform,'skill':skill})

def updateskill(request,id,id1):
	if request.method == 'POST':
		skill=Talents.objects.get(pk=id)
		sform=TalentForm(request.POST,instance = skill)
		if sform.is_valid():
			sform.save(commit=True)
			url='/editprofile/'+str(id1)
			return redirect(url)

def editexam(request,id):
	exam=Exam.objects.get(id=id)
	examform=ExamForm(data=model_to_dict(Exam.objects.get(id=id)))
	return render(request,'EditExam.html',{"examform":examform,'exam':exam})

def updateexam(request,id,id1):
	if request.method == 'POST':
		exam=Exam.objects.get(pk=id)
		eform=ExamForm(request.POST,instance = exam)
		if eform.is_valid():
			eform.save(commit=True)
			url='/editprofile/'+str(id1)
			return redirect(url)

def editresponsible(request,id):
	response=Responsibility.objects.get(id=id)
	responseform=ResponsibilityForm(data=model_to_dict(Responsibility.objects.get(id=id)))
	return render(request,'EditResponseibility.html',{"responseform":responseform,'response':response})

def updateresponsible(request,id,id1):
	if request.method == 'POST':
		response=Responsibility.objects.get(pk=id)
		rform=ResponsibilityForm(request.POST,instance = response)
		if rform.is_valid():
			rform.save(commit=True)
			url='/editprofile/'+str(id1)
			return redirect(url)

def editachivements(request,id):
	achivement=Achivements.objects.get(id=id)
	achivementform=AchivementsForm(data=model_to_dict(Achivements.objects.get(id=id)))
	return render(request,'EditAchivements.html',{"achivementform":achivementform,'achivement':achivement})

def updateachivements(request,id,id1):
	if request.method == 'POST':
		achivement=Achivements.objects.get(pk=id)
		aform=AchivementsForm(request.POST,instance = achivement)
		if aform.is_valid():
			aform.save(commit=True)
			url='/editprofile/'+str(id1)
			return redirect(url)



def addworkdetails(request,id):
	if request.method == 'POST':
		form=WorkingDetailsForm(request.POST)
		if form.is_valid():
			form.save()
			url='/editprofile/'+str(id)
			return redirect(url)
	else:
		form=WorkingDetailsForm()
		return render(request,"AddWorkDetails.html",{'form':form,'id':id})

def addeducation(request,id):
	if request.method == 'POST':
		form=EducationQualificationForm(request.POST)
		if form.is_valid():
			form.save()
			url='/editprofile/'+str(id)
			return redirect(url)
	else:
		form=EducationQualificationForm()
		return render(request,"AddEducation.html",{'form':form,'id':id})

def addskill(request,id):
	if request.method == 'POST':
		form=TalentForm(request.POST)
		if form.is_valid():
			form.save()
			url='/editprofile/'+str(id)
			return redirect(url)
	else:
		form=TalentForm()
		return render(request,"AddSkill.html",{'form':form,'id':id})

def addexam(request,id):
	if request.method == 'POST':
		form=ExamForm(request.POST)
		if form.is_valid():
			form.save()
			url='/editprofile/'+str(id)
			return redirect(url)
	else:
		form=ExamForm()
		return render(request,"AddExam.html",{'form':form,'id':id})

def addresponsible(request,id):
	if request.method == 'POST':
		form=ResponsibilityForm(request.POST)
		if form.is_valid():
			form.save()
			url='/editprofile/'+str(id)
			return redirect(url)
	else:
		form=ResponsibilityForm()
		return render(request,"AddResponsible.html",{'form':form,'id':id})

def addacivement(request,id):
	if request.method == 'POST':
		form=AchivementsForm(request.POST)
		if form.is_valid():
			form.save()
			url='/editprofile/'+str(id)
			return redirect(url)
	else:
		form=AchivementsForm()
		return render(request,"AddAchivement.html",{'form':form,'id':id})


def test(request):
	return render(request,'admin/AdminHome.html')