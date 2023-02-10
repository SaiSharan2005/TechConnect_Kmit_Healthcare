from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = "home"),
    path('sign_up/',views.sign_up,name = "sign_up"),
    path('log_in/',views.log_in,name = "log_in"),
    path('log_out/',views.log_out,name = "log_out"),
    path('type_user/',views.type_user,name = "type_user"),
    path('doctor_form/',views.doctor_form,name = "doctor_form"),
    path('patient_form/',views.patient_form,name = "patient_form"),
    path('choice_acc/',views.choice_acc,name = "choice_acc"),
    path('doctor_profile/',views.doctor_profile,name = "doctor_profile"),
    path('patient_profile/<str:pk>',views.patient_profile,name = "patient_profile"),
    path('medical_form/<str:pk>',views.medical_report,name="medical_form"),
    path('extra_form/<str:pk>',views.extra_fields_med,name="extra_medical"),
    path('medical_form_view/<str:pk>',views.medical_form_view,name="medical_form_view"),
    path('Doctor_profile',views.consult_doctor,name="consult_doctor"),
    path('all_form_user',views.all_medical_history,name="all_medical_history"),
    path('Doctor_profile_name/<int:pk>',views.doctor_data,name="doctor_data"),
    path('Doctor_profile_name/<int:pk>',views.doctor_data,name="doctor_data"),
    path('Message_doc/<int:pk>',views.Request_doc,name="Request_doc"),
    path('patient_doc/',views.patient_doc,name="patient_doc"),
    path('doc_pat_form/<int:pk>',views.doctoc_prepare_form,name="doctoc_prepare_form"),
    path('extra_doc_pati/<int:pk>',views.doctor_extra_prepare_form,name="doctor_extra_prepare_form"),
    path('add_remainder',views.add_remainder,name="add_remainder"),
    path('remainder',views.see_remainder,name="see_remainder"),
    path('check/<int:pk>',views.delete_remainder,name = "check"),
    path('predict/',views.predict,name = "predict"),


]