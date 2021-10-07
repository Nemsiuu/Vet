from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Animal, Owner, Patient_Card, Doctor, Specie
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from catalog.forms import MarkVisitForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from catalog.forms import SignUpForm


def index(request):
    """View function for home page of site."""

    
    num_animals = Animal.objects.all().count()
    num_cards =Patient_Card.objects.all().count()

    
    num_cards_open = Patient_Card.objects.filter(status__exact='a').count()

    
    num_species = Specie.objects.count()   
    num_owners = Owner.objects.count()
    num_doctors = Doctor.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_animals': num_animals,
        'num_cards_open': num_cards_open,
        'num_cards': num_cards,
        'num_owners': num_owners,
        'num_doctors' : num_doctors,
        'num_species' : num_species,
        'num_visits': num_visits,
    }

    
    return render(request, 'index.html', context=context)

from django.views import generic

class AnimalListView(LoginRequiredMixin,generic.ListView):
    model = Animal
    paginate_by = 10


class AnimalDetailView(LoginRequiredMixin,generic.DetailView):
    model = Animal

    
class DoctorListView(generic.ListView):
    model = Doctor
    paginate_by = 10


class DoctorDetailView(generic.DetailView):
    model = Doctor

    
class OwnerListView(LoginRequiredMixin,generic.ListView):
    model = Owner
    paginate_by = 10


class OwnerDetailView(LoginRequiredMixin,generic.DetailView):
    model = Owner

class SpecieListView(LoginRequiredMixin,generic.ListView):
    model = Specie
    paginate_by = 10


class SpecieDetailView(LoginRequiredMixin,generic.DetailView):
    model = Specie

class Patient_CardsByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = Patient_Card
    template_name ='catalog/myanimals.html'
    paginate_by = 10

    def get_queryset(self):
        return Patient_Card.objects.filter(owner=self.request.user).filter(status__exact='a').order_by('visit_date')

class Patients(PermissionRequiredMixin,generic.ListView):
    permission_required = 'catalog.can_mark_completed'
    model = Patient_Card
    template_name ='catalog/patients.html'
    paginate_by = 10

    def get_queryset(self):
        return Patient_Card.objects.filter(status__exact='a').order_by('visit_date')


@login_required
@permission_required('catalog.can_mark_completed', raise_exception=True)
def mark_visit_doctor(request, pk):
    
    patient_card = get_object_or_404(Patient_Card, pk=pk)

    
    if request.method == 'POST':

       
        form = MarkVisitForm(request.POST)

       
        if form.is_valid():
            
            patient_card.status = form.cleaned_data['new_mark']
            patient_card.save()

           
            return HttpResponseRedirect(reverse('patients') )

    else:
        proposed_mark = "c"
        form = MarkVisitForm(initial={'mark_visit': proposed_mark})
    

    context = {
        'form': form,
        'patient_card': patient_card,
    }

    return render(request, 'catalog/mark_visit_doctor.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})