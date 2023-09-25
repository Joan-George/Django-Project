from django import forms
from django.forms import ModelForm
from .models import *
from datetimepicker.widgets import DateTimePicker
from bootstrap_datepicker.widgets import DatePicker

class Date(forms.DateInput):
	input_type='date'


class BasicInformationForm(forms.ModelForm):
    class Meta:
        model = BasicInformation
        fields = "__all__"

        widgets={'DOB':Date(),
                'Uid':forms.HiddenInput,
                'JoinedDate':Date()}

        help_texts = {'Name': "Enter Your Name",
                      'DOB':"Select Your Date of Birth",
                      'Gender':"Select Your Gender",
                      'JoinedDate':"The date you joined in M.Sc.Computer Science",
                      'Email':"Your current email",
                      'MobileNo':"Your MobileNo",
                      'Address':"Your native address"}

class ResponsibilityForm(forms.ModelForm):
    class Meta:
        model = Responsibility
        fields = "__all__"
        widgets={'Uid':forms.HiddenInput}
        help_texts = {'Responsible': "Ex:Worked as secratery in my ug 3rd year or worked as leader for any groups",}

class AchivementsForm(forms.ModelForm):
    class Meta:
        model = Achivements
        fields = "__all__"
        widgets={'Uid':forms.HiddenInput}

class TalentForm(forms.ModelForm):
    class Meta:
        model = Talents
        fields = "__all__"
        widgets={'Uid':forms.HiddenInput}


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = "__all__"
        widgets={'Uid':forms.HiddenInput}

class WorkingDetailsForm(forms.ModelForm):
    class Meta:
        model = WorkingDetails
        fields = "__all__"
        widgets={'Uid':forms.HiddenInput,
                'JoinedDate':Date(),
                'DismissalDate':Date()}
class EducationQualificationForm(forms.ModelForm):
    class Meta:
        model = EducationQualification
        fields = "__all__"
        widgets={'Uid':forms.HiddenInput}
    
    
    
    
