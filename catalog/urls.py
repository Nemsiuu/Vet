from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('animals/', views.AnimalListView.as_view(), name='animals'),
    path('animal/<int:pk>', views.AnimalDetailView.as_view(), name='animal-detail'),
    path('owners/', views.OwnerListView.as_view(), name='owners'),
    path('owner/<int:pk>', views.OwnerDetailView.as_view(), name='owner-detail'),
    path('doctors/', views.DoctorListView.as_view(), name='doctors'),
    path('doctor/<int:pk>', views.DoctorDetailView.as_view(), name='doctor-detail'),
    path('species/', views.SpecieListView.as_view(), name='species'),
    path('specie/<int:pk>', views.SpecieDetailView.as_view(), name='specie-detail'),
    path('myanimals/', views.Patient_CardsByUserListView.as_view(), name='my-animals'),
    path('patients/', views.Patients.as_view(), name='patients'),
    path('animal/<uuid:pk>/MarkVisit/', views.mark_visit_doctor, name='mark_visit_doctor'),
    path('signup/', views.signup, name='signup'),
]
