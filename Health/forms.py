from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
from .models import Doctor,Patient,Medical_Report,Extra_Values,Room_doc,Patient_tablets,Remainder,Predict
from django.contrib.auth.models import User




# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)
# #     # profile_image = forms.FileField()
#     # type_user = forms.ChoiceField(choices=[('Pa')],required=True)


#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class DoctorCreationForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ["Name","email","mobile_number","Profile_pic","Date_of_birth","street","city","state","country","Experience","Position","Profession","About_me","Education_from"]

class PatientCreationForm(ModelForm):
    class Meta:
        model = Patient
        fields = ["user_name","profile_pic","Date_of_birth","user_relationship","father_name","mother_name","street","city","state","country"]

class MedicalReportForm(ModelForm):
    class Meta:
        model = Medical_Report
        fields = ["Report_name","Hospital","Patient_name","Doctor_name","description","Date_of_scan","Date_of_recieved","doctor_prescription","Blood_pressure","Sugar_level"]

class ExtraValuesForm(ModelForm):
    class Meta:
        model = Extra_Values
        fields = ["parameter_name","parameters_value"]
         
class RoomDocForm(ModelForm):
    class Meta:
        model = Room_doc
        # fields = '__all__'
        # exclude = ["doctor_name","Patient_name","prescription_data"]
        fields = ["message_to_doc"]
class Patient_tabletsForm(ModelForm):
    class Meta:
        model = Patient_tablets
        fields = "__all__"
        exclude = ["Extra_parameters"]
class RemainderForm(ModelForm):
    class Meta:
        model = Remainder
        fields = "__all__"
        exclude = ["host","coice"]
class PredictForm(ModelForm):
    class Meta:
        model = Predict
        fields = "__all__"
        exclude = ["patient"]
