from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse,reverse_lazy
from django.views import generic
from .models import Workout,Activity
from .forms import WorkoutCreateForm,ActivityCreateForm,SetFormSet,WorkoutUpdateForm,ActivityUpdateForm,SetUpdateFormSet

import datetime

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'workouts/index.html'
	model = Workout
	context_object_name = 'latest_workouts_list'

	def get_queryset(self):
		return Workout.objects.order_by('-date')[:5]

class WorkoutCreateView(generic.CreateView):
	model = Workout
	form_class = WorkoutCreateForm
	template_name = 'workouts/workout_add.html'

	def form_valid(self,form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.date = datetime.date.today()
		self.object.save()
		return HttpResponseRedirect(reverse('workouts:workout-detail', args=([self.object.id])))

class ActivityCreateView(generic.CreateView):
	template_name = 'workouts/activity_add.html'
	form_class = ActivityCreateForm

	def get_context_data(self, **kwargs):
		context = super(ActivityCreateView, self).get_context_data(**kwargs)
		if self.request.POST:
			context['formset'] = SetFormSet(self.request.POST)
			context['workout'] = Workout.objects.get(pk=self.kwargs['pk'])

		else:
			context['workout'] = Workout.objects.get(pk=self.kwargs['pk'])
			context['formset'] = SetFormSet()
		return context

	def form_valid(self, form):
		context = self.get_context_data()
		formset = context['formset']
		if formset.is_valid():
			self.object = form.save(commit=False)
			workout = Workout.objects.get(pk=self.kwargs['pk'])
			self.object.workout = workout
			self.object.save()
			formset.instance = self.object
			formset.save()
			return HttpResponseRedirect(reverse('workouts:workout-detail', args=([workout.id])))
		else:
			return self.render_to_response(self.get_context_data(form=form))

class WorkoutDetailView(generic.DetailView):
	model = Workout
	template_name='workouts/workout_detail.html'

class WorkoutUpdateView(generic.UpdateView):
	model = Workout
	form_class = WorkoutUpdateForm
	template_name='workouts/workout_update.html'

	def get_success_url(self):
		workout = Workout.objects.get(pk=self.kwargs['pk'])
		return reverse('workouts:workout-detail',kwargs={'pk':self.kwargs['pk']})

class ActivityUpdateView(generic.UpdateView):
	model = Activity
	template_name = 'workouts/activity_update.html'
	form_class = ActivityUpdateForm
	
	def get_context_data(self, **kwargs):
		context = super(ActivityUpdateView, self).get_context_data(**kwargs)
		if self.request.POST:
			context['formset'] = SetUpdateFormSet(self.request.POST,instance=self.object)

		else:
			context['formset'] = SetUpdateFormSet(instance=self.object)
			context['form_errors'] = context['formset'].errors
		return context

	def form_valid(self, form):
		context = self.get_context_data()
		formset = context['formset']
		if formset.is_valid():
			self.object = form.save()
			formset.instance = self.object
			formset.save()
			return HttpResponseRedirect(reverse('workouts:workout-detail',kwargs={'pk':self.kwargs['wpk']}))
		else:
			return self.render_to_response(self.get_context_data(form=form))

class WorkoutDeleteView(generic.DeleteView):
	model = Workout
	template_name = 'workouts/confirm_delete.html'
	success_url = reverse_lazy('workouts:index')

class ActivityDeleteView(generic.DeleteView):
	model = Activity
	template_name = 'workouts/confirm_delete.html'
	success_url = reverse_lazy('workouts:index')

