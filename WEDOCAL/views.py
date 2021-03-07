from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from .models import Patient, Dose
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from django.contrib import messages
import pygal

#____________________________________________

def home(request):
    return render (request,'WEDOCAL/Home.html',{'title':'Accueil'})
def register(request):
    if request.method =='POST':
        form = forms.PatientForm(request.POST)
        if form.is_valid():
            cin = form.cleaned_data.get('cin').upper()
            name = form.cleaned_data.get('name')
            date = form.cleaned_data.get('birthdate')
            v6 = form.cleaned_data.get('v6')
            v7 = form.cleaned_data.get('v7')
            haplo = form.cleaned_data.get('haplo')
            patient = Patient(name=name,cin=cin,birthdate=date,v6=v6,v7=v7,haplo=haplo)
            patient.save()
            topatient = Patient.objects.get(cin=cin)
            dose = Dose(patient=topatient,dose_value=patient.dose())
            dose.save()
            return redirect('WeDoCal')
    else:
        form = forms.PatientForm()

    return render (request,'WEDOCAL/signein.html',{'title':'Accueil','form':form})
def consult (request):
    if request.method =='POST':
        form = forms.ChekingForm(request.POST)
        if form.is_valid():
            cin = form.cleaned_data.get('cin').upper()
            if Patient.objects.filter(cin=cin).exists():
                patient = Patient.objects.get(cin=cin)
                age = patient.age()
                doses = Dose.objects.filter(patient=patient).order_by('dose_date')
                final_dose = doses.last()
                calc_dose = patient.dose()
                d = []
                v = []
                for i in doses:
                    d.append(i.dose_date)
                    v.append(i.dose_value)
                l_chart = pygal.Line(x_label_rotation=20)
                l_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'),d)
                l_chart.title = 'Variation des Doses'
                l_chart.add('Dose',v)
                # for i in doses:
                #
                #     l_chart.add(i.dose_value)
                # for i in dic :
                #     l_chart.add(i,dic[i])
                chart = l_chart.render_data_uri()
                return render (request,'WEDOCAL/doses.html',{'patient':patient,'final_dose':final_dose,'calc_dose':calc_dose,'chart':chart,'age':age})
            else:
                messages.error(request,f'Ce patient n\'existe pas')
                return redirect('check')
    else:
        form = forms.ChekingForm()
    return render (request,'WEDOCAL/check.html',{'title':'Accueil','form':form})
def dose_create(request,pk):
    if request.method == 'POST':
        form = forms.DoseCreate(request.POST)
        if form.is_valid():
            dose_value = form.cleaned_data.get('dose_value')
            dose_date = form.cleaned_data.get('dose_date')
            comment = form.cleaned_data.get('comment')
            commenter = form.cleaned_data.get('commenter')
            patient = Patient.objects.get(id=pk)
            dose = Dose(patient = patient,dose_value=dose_value,comment=comment,commenter=commenter,dose_date=dose_date)
            dose.save()
            return redirect ('WeDoCal')
        else :
            return redirect ('check')
    else:
        form = forms.DoseCreate()
    return render (request, 'WEDOCAL/dose_form.html',{'form':form})
