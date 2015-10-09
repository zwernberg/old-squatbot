from django import forms
from django.forms import ModelForm, TextInput, NumberInput
from django.forms.models import inlineformset_factory

from .models import Workout,Activity,Set


class WorkoutCreateForm(ModelForm):

	class Meta:
		model = Workout
		fields = ['name']
		widgets = {
			'name': TextInput(attrs={'class':'form-control','placeholder':'Workout Name'}),
		}

class WorkoutUpdateForm(ModelForm):

	class Meta:
		model = Workout
		fields = ['name']
		widgets = {
			'name': TextInput(attrs={'class':'form-control'}),
		}

class ActivityCreateForm(ModelForm):
	class Meta:
		model = Activity
		fields = ['name']
		widgets = {
			'name': TextInput(attrs={'class':'form-control','placeholder':'Activity Name'}),
		}

class ActivityUpdateForm(ModelForm):
	class Meta:
		model = Activity
		fields = ['name']
		widgets = {
			'name': TextInput(attrs={'class':'form-control'}),
		}

SetFormSet = inlineformset_factory(Activity,Set,extra=3,fields=['weight','reps'],can_delete = False,widgets = {
			'weight': NumberInput(attrs={'class':'form-control','placeholder':'weight'}),'reps': NumberInput(attrs={'class':'form-control','placeholder':'reps'})
		})

SetUpdateFormSet = inlineformset_factory(Activity,Set,extra=0,fields=['weight','reps'],can_delete = False,widgets = {
			'weight': NumberInput(attrs={'class':'form-control'}),'reps': NumberInput(attrs={'class':'form-control'})
		})


