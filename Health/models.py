from django.db import models
from django.contrib.auth.models import User

class Remainder(models.Model):
    host=models.ForeignKey(User ,on_delete=models.CASCADE)
    Remainder_date = models.DateField()
    Remainder_time = models.TimeField()
    Remainder_message = models.CharField(max_length=100)
    coice = models.BooleanField(default=False,null=True)


class Doctor(models.Model):
    host = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    Profile_pic = models.ImageField(null=True ,default="doctor.png")
    Date_of_birth = models.DateField(null=True)

    street = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)  

    Experience = models.PositiveIntegerField()
    Position = models.CharField(max_length=30)
    Profession = models.CharField(max_length=100)
    About_me = models.TextField(max_length=500)
    Education_from = models.CharField(max_length=100)
    email = models.EmailField(blank= False)
    mobile_number = models.IntegerField(blank = True)
 
 
class Patient(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user_name = models.CharField(max_length=30)
    profile_pic = models.ImageField( null=True, default="avater.svg")
    Date_of_birth = models.DateField(null=True)
    user_relationship = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)  

    def __str__(self):
        return self.user_name


class Medical_Report(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True)
    description = models.TextField(max_length=300,default="None ")
    Report_name = models.CharField(max_length=100)    
    Hospital = models.CharField(max_length=100)
    Patient_name = models.CharField(max_length=100)
    Doctor_name = models.CharField(max_length=100)
    Date_of_scan = models.DateTimeField()
    Date_of_recieved = models.DateTimeField()
    doctor_prescription= models.TextField(max_length=300,default="None ")
    Blood_pressure = models.IntegerField()
    Sugar_level = models.IntegerField()

    def __str__(self):
        return self.Report_name

class Extra_Values(models.Model):
    Extra_parameters = models.ForeignKey(Medical_Report,on_delete= models.CASCADE,null=True)
    parameter_name = models.CharField(max_length=100)
    parameters_value = models.CharField(max_length=100)

class Patient_tablets(models.Model):
    Extra_parameters = models.ForeignKey(Medical_Report,on_delete= models.CASCADE,null=True)
    parameter_name = models.CharField(max_length=100,null=True)
    parameters_value = models.CharField(max_length=100,null=True)    
    parameter_date_time = models.DateTimeField()
    def __str__(self):
        return str(self.parameter_name)


class Room_doc(models.Model):
    Doctor_name = models.ForeignKey(Doctor,on_delete=models.CASCADE,null = True)
    Patient_name = models.ForeignKey(Patient,on_delete =models.CASCADE,null=True)
    message_to_doc = models.CharField(max_length=300)
    message_to_pat = models.CharField(max_length=500 , null = True)
    # prescription_data = models.ForeignKey(Prescription,on_delete=models.CASCADE,null=True)

class Predict(models.Model):
    Yes_No=(
        ("1",'Yes'),
        ("0",'No')
    )
    male_female=(
        ("1","Male"),
        ("0","Female")
    )
    other_con = (
        ("0","other"),
        ("1","Contact with confirmed"),
        ("2","Abroad")
    )

    # patient = models.ForeignKey(Patient,on_delete =models.CASCADE,null=True)
    Cough = models.CharField(
        max_length = 20,
        choices = Yes_No,
        default = '0'
        )
    Fever = models.CharField(
        max_length = 20,
        choices = Yes_No,
        default = '0'
        )
    Sore_Throat = models.CharField(
        max_length = 20,
        choices = Yes_No,
        default = '0'
        )
    shortness_of_breath = models.CharField(
        max_length = 20,
        choices = Yes_No,
        default = '0'
        )
    head_ache = models.CharField(
        max_length = 20,
        choices = Yes_No,
        default = '0'
        )
    Are_You_Above_60 = models.CharField(
        max_length = 20,
        choices = Yes_No,
        default = '0'
        )
    Gender = models.CharField(
        max_length = 20,
        choices = male_female,
        default = '0'
        )
    test_indication = models.CharField(
        max_length = 20,
        choices = other_con,
        default = '0'
        )


    def __str__(self):
        return str(self.Cough)
