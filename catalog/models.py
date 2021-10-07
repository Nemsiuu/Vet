from django.db import models
from django.urls import reverse
import uuid
from datetime import date
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class Specie(models.Model):
   
    name = models.CharField(max_length=200, help_text='Enter a specie')

    def get_absolute_url(self):
     
        return reverse('specie-detail', args=[str(self.id)])

    def __str__(self):
        
        return self.name


class Animal(models.Model):
    
    name = models.CharField(max_length=50)
    specie =models.ForeignKey('Specie', on_delete=models.SET_NULL, null=True)
  
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    owner_db = models.ForeignKey('owner', on_delete=models.SET_NULL, null=True, blank=True)
    sex = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    

   
    

    def __str__(self):
        
        return self.name
        

    def get_absolute_url(self):
        
        return reverse('animal-detail', args=[str(self.id)])
    
    def display_owner(self):
        
        return self.owner.first_name +' ' +self.owner.last_name 

    display_owner.short_description = 'Owner'

   
    

class Patient_Card(models.Model):
   
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this card')
    animal = models.ForeignKey('Animal', on_delete=models.RESTRICT, null=True)
    disease = models.CharField(max_length=500)
    visit_date = models.DateField(null=True, blank=True)
    #owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    doctor = models.ManyToManyField(User,  null=True)
    doctor_db = models.ForeignKey('doctor', on_delete=models.SET_NULL, null=True, blank=True)
    VISIT_STATUS = (
        ('a', 'Awaiting'),
        ('c', 'Completed'),
        ('n', 'Not completed'),
        
    )

    status = models.CharField(
        max_length=1,
        choices=VISIT_STATUS,
        blank=True,
        default='a',
        help_text='Visit card',
    )

    class Meta:
        ordering = ['visit_date']
        permissions = (("can_mark_completed", "Set visit as completed"),)
    @property
    def is_overdue(self):
        if self.visit_date and date.today() > self.visit_date and self.status == 'a':
            self.status == 'n'
            return True
        return False
    def __str__(self):
        
        return f'{self.id} ({self.animal.name})'
    def display_doctor(self):
        
        return self.doctor.first_name +' ' +self.doctor.last_name 

    display_doctor.short_description = 'Doctor'



class Owner(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    mail = models.EmailField(max_length=100)
    
    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        
        return reverse('owner-detail', args=[str(self.id)])

    def __str__(self):
     
        return f'{self.first_name} {self.last_name}'



class Doctor(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    mail = models.EmailField(max_length=100)
    about = models.CharField(max_length=1000, blank=True)
    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        
        return reverse('doctor-detail', args=[str(self.id)])

    def __str__(self):
     
        return f'{self.first_name} {self.last_name}'