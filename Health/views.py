from django.shortcuts import render, redirect
from .forms import DoctorCreationForm, PatientCreationForm, MedicalReportForm,PredictForm, ExtraValuesForm,PredictForm,RoomDocForm,Patient_tabletsForm,RemainderForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import User,Patient, Doctor, Medical_Report, Extra_Values,Room_doc,Patient_tablets,Remainder

# Create your views here.


def home(request):
    try:
        if Doctor.objects.get(host=request.user) is not None:
            return redirect('doctor_profile')
            # print("i am in doctoe")
    except:
        pass
    try:
        if Patient.objects.filter(host=request.user) is not None:
            return redirect('choice_acc')
    except:
        pass

    return render(request, "Health/home.html")


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('type_user')

    context = {"form": form}
    return render(request, "Health/sign_up.html", context)


def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(username + "   "+password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            pass
    return render(request, 'Health/log_in.html')


def log_out(request):
    logout(request)
    return redirect('home')


def type_user(request):
    if request.method == "POST":
        choice = request.POST.get('image')
        if choice == 'doctor':
            return redirect('doctor_form')
        if choice == 'patient':
            return redirect('patient_form')
        print(choice)

    return render(request, "Health/type_user.html")


def doctor_form(request):
    form = DoctorCreationForm()
    if request.method == "POST":
        form = DoctorCreationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.host = request.user
            user.save()
            return redirect('doctor_profile')
    context = {'form': form}
    return render(request, 'Health/doctor_form.html', context)


def doctor_profile(request):
    form = Doctor.objects.get(host=request.user)
    context = {"form": form}
    return render(request, 'Health/doctor_profile.html', context)


def patient_form(request):
    form = PatientCreationForm()
    if request.method == "POST":
        # form.host = request.user
        form = PatientCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.host = request.user
            user.save()
            print(user)
            return redirect('home')

    context = {'form': form}
    return render(request, 'Health/doctor_form.html', context)


def patient_profile(request, pk):
    form = Patient.objects.get(user_name=pk)
    medical_report = Medical_Report.objects.filter(person=form)
    remainder = Remainder.objects.filter(host = request.user)

    context = {"form": form, "medical_report": medical_report}
    return render(request, 'Health/patient_profile.html', context)


def choice_acc(request):
    form = Patient.objects.filter(host=request.user)

    context = {"form": form}
    return render(request, "Health/choice_acc.html", context)


def medical_report(request, pk):
    form_basic = MedicalReportForm()
    form_extra = ExtraValuesForm()
    patient = Patient.objects.get(user_name=pk)

    # print("dsaf")
    if request.method == "POST":
        print("POST")
        form_basic = MedicalReportForm(request.POST)
        # form_extra = ExtraValuesForm(request.POST)
        if form_basic.is_valid():
            basic = form_basic.save(commit=False)
            basic.person = patient
            basic.host = request.user
            basic.save()
           
            return redirect("/extra_form/"+basic.Report_name)
          
    context = {"form_basic": form_basic}
    return render(request, "Health/medical_form.html", context)


def extra_fields_med(request, pk):
    form_entry = ExtraValuesForm()
    form_data = Medical_Report.objects.get(Report_name=pk)
    form = Extra_Values.objects.filter(Extra_parameters=form_data)
  
    if request.method == "POST":
        form_entry = ExtraValuesForm(request.POST)
        if form_entry.is_valid():
            form_before = form_entry.save(commit=False)
            form_before.Extra_parameters = form_data
            form_before.save()
            if request.POST.get("choice") is not None:
                return redirect("home")

    context = {"form": form, "form_data": form_data, "form_entry": form_entry}
    return render(request, "Health/extra_medi_field.html", context)



def medical_form_view(request, pk):
    data_medi = Medical_Report.objects.get(id=int(pk))
    extra_data_medi = Extra_Values.objects.filter(Extra_parameters=data_medi)
    data_added_by_doctor = Patient_tablets.objects.filter(Extra_parameters = data_medi)
    # print(data_medi)
    context = {"data_medi": data_medi, "extra_data_medi": extra_data_medi,"data_added_by_doctor":data_added_by_doctor}
    return render(request, "Health/medical_form_view.html", context)


def consult_doctor(request):
    all_doc = Doctor.objects.all()
    context={"all_doc":all_doc}
    return render(request,"Health/Consult_Doctor.html",context)

def all_medical_history(request):
    doc_data= Medical_Report.objects.filter(host = request.user)
    # print(doc_data)
    context={"doc_data":doc_data}

    return render(request,"Health/report_all_data.html",context)

def doctor_data(request,pk):
    form = Doctor.objects.get(id=pk)
    # form2 = Patient.objects.get(id=)
    context = {"form": form,"opt":False}
    return render(request, 'Health/patient_doc_view.html', context)


def Request_doc(request,pk):
    # form = Patient.objects.get(id = request.user)
    form = Doctor.objects.get(id = pk)
    form_patient = Patient.objects.filter(host = request.user) 
    # print(form_patient.id)
    
    print(form_patient)
    form_data = RoomDocForm()
    if request.method == "POST":
        form_data = RoomDocForm(request.POST)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.Doctor_name = form
            temp = request.POST.get('option_sel')
            data.Patient_name = Patient.objects.get(host = request.user,user_name=temp)
            data.save()
        else:
            print("somthing went wrong")

    context = {"form": form ,"opt":True,"form_data":form_data,"form_patient":form_patient}
    return render(request, 'Health/patient_doc_view.html', context)

def patient_doc(request):
    doctor_data= Doctor.objects.get(host = request.user)
    form = Room_doc.objects.filter(Doctor_name=doctor_data)
    
    context={"form":form}
    return render(request,"Health/doc_patient_req.html",context)

def doctoc_prepare_form(request,pk):
    form_basic = MedicalReportForm()
    room = Room_doc.objects.get(id=pk)
    patient = Patient.objects.get(user_name=room.Patient_name)

    if request.method == "POST":
        form_basic = MedicalReportForm(request.POST)
        if form_basic.is_valid():
            basic = form_basic.save(commit=False)
            basic.person = patient
            basic.host = patient.host
            basic.save()
            return redirect("/extra_doc_pati/"+str(basic.id))

    context={"form_basic":form_basic}
    return render(request,"Health/medical_form.html",context)

def doctor_extra_prepare_form(request,pk):
    form = Patient_tabletsForm()
    form2= Medical_Report.objects.get(id =pk)
    data = Patient_tablets.objects.filter(Extra_parameters=form2)
    if request.method=="POST":
        form= Patient_tabletsForm(request.POST)
        if form.is_valid():
            basic = form.save(commit=False)
            basic.Extra_parameters = form2
            basic.save()

    context={"form":form,"data":data}
    return render(request,"Health/medical_schdule.html",context)


def add_remainder(request):
    form = RemainderForm()
    if request.method == "POST":
        form = RemainderForm(request.POST)
        if form.is_valid():
            user2 = form.save(commit=False)
            user2.host = request.user
            user2.save()
            return redirect('home')
    context = {"form":form}
    return render(request,"Health/add_remainder.html",context)

def see_remainder(request):
    form = Remainder.objects.filter(host = request.user)
    context={"form":form}
    return render(request,"Health/see_remainder.html",context)

def delete_remainder(request,pk):
    form = Remainder.objects.get(id = pk)
    if request.user == form.host:
        form.delete()
        return redirect('home')
    else:
        return HttpResponse('You are not allowed to do the task')


def predict(request):
    form = PredictForm()
    if request.method == "POST":
        form = PredictForm(request.POST)
        # patient = Patient.objects.get(user_name=request.user)
        if form.is_valid():
            data = form.save(commit = False)
            # data.host = patient
            data.save()
            # return render('')
            # print(data.test_indication)
            probabilty = int(data.Cough)*0.07055676+int(data.Fever)*1.68623095+int(data.Sore_Throat)*1.5854057 + int(data.shortness_of_breath)*1.73702772 + int(data.head_ache)*2.19033765 + int(data.Are_You_Above_60)*0.09462715 + int(data.Gender)*0.179707+int(data.test_indication)*1.89852105 - 2.98588864
            print(probabilty)
            return HttpResponse('<h1>Your Probalilty of being a Covid Postive is '+str(probabilty*10)+'</h1>')
            
    context = {"form_basic":form}
    return render(request,"Health/predict.html",context)



