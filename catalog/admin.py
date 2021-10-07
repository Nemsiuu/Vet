from django.contrib import admin

# Register your models here.
from .models import Owner,Animal, Doctor, Specie, Patient_Card
class Patient_CardsInline(admin.TabularInline):
    model = Patient_Card
    extra = 0
class AnimalsInline(admin.TabularInline):
    model = Animal
    extra =0
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone_number', 'mail')
    fields = ['first_name', 'last_name', 'phone_number', 'mail']
    #inlines = [AnimalsInline]

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'about', 'phone_number', 'mail')
    fields = ['first_name', 'last_name','about', 'phone_number', 'mail' ]
    #inlines = [AnimalsInline]

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name','sex','specie', 'display_owner')
    inlines = [Patient_CardsInline]

@admin.register(Patient_Card)
class Patient_CardAdmin(admin.ModelAdmin):
     list_display = ('id','animal', 'disease','status', 'visit_date')
     list_filter = ('status', 'visit_date')
     fieldsets = (
        (None, {
            'fields': ('animal', 'disease', 'id')
        }),
        ('Visit', {
            'fields': ('doctor','doctor_db','status', 'visit_date')
        }),
    )




    
#admin.site.register(Movie)
#admin.site.register(Author)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Specie)
#admin.site.register(MovieInstance)
