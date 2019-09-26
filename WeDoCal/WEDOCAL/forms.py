from django import forms
from . import models
class PatientForm(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'Nom'}))
    cin = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'CIN'}))
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','class' : 'form-control',}))
    v6_choices=(('GG','GG'),('GA','GA'),('AA','AA'))
    v7_choices =(('CC','CC'),('CT','CT'),('TT','TT'))
    haplo_choices = (('1/1','1/1'),('1/2','1/2'),('1/3','1/3'),('2/2','2/2'),('2/3','2/3'))
    v6 = forms.ChoiceField(choices=v6_choices,widget=forms.Select(attrs={'class' : 'form-control','placeholder':'Votre Genotype'}))
    v7 = forms.ChoiceField(choices=v7_choices,widget=forms.Select(attrs={'class' : 'form-control','placeholder':'Votre Genotype'}))
    haplo = forms.ChoiceField(choices=haplo_choices,widget=forms.Select(attrs={'class' : 'form-control','placeholder':'Votre Genotype'}))
    # v7 = forms.CharField(max_length=2,choices =(('CC','CC'),('CT','CT'),('TT','TT')))
    # haplo = forms.CharField(max_length=2,choices = (('1/1','1/1'),('1/2','1/2'),('1/3','1/3'),('2/2','2/2'),('2/3','2/3')))
class ChekingForm(forms.Form):
    cin = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'CIN'}))
class DoseCreate(forms.Form):
    dose_value = forms.DecimalField(max_digits=10,decimal_places=3,widget=forms.NumberInput(attrs={'min':0,'value':0,'step':0.001,'class':'form-control'}))
    comment = forms.CharField(max_length=1000,widget=forms.Textarea(attrs={'class':'form-control', 'placeholder' : ' Commentaire'}))
    commenter = forms.ChoiceField(choices = (('Moi Meme','Moi Meme'),('Un Proche','Un Proche'),('Mon Medecin','Mon Medecin')), widget=forms.Select(attrs={'class' : 'form-control','placeholder':'CIN'}))
    dose_date = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date','class' : 'form-control'}))
