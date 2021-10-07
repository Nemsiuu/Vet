# Vet
Veterinary website app made in django


Bigger django application which creates website for vet clinic. Animal owners can create accounts on website, which gives them option to check visit dates and descriptions for their animals. Doctors have their own accounts, giving them acces to their patients. They can also mark visits status. 

Main features that have been implemented:

- There are models for animals, owners, doctors.
- Users can view their animals and patient cards.
- Doctors can check their patients and visits.


There is only basic frontend, since this project is made to show django options, rather than front.


Quick Start

To check the project, enter https://dry-dawn-32956.herokuapp.com/catalog/

Then create new account if you want, or use:
- Owner account ( Login = Owner1 | Password = testuser , Login = User2 | Password = testuser )
- Doctor account ( Login = Doctor1 | Password = testuser ,  Login = Doctor2 | Password = testuser)
- Admin account ( Login = su | Password = testuser)

To open admin site, open https://dry-dawn-32956.herokuapp.com/admin/


To get this project up and running locally on your computer:

Set up the Python development environment. 
Assuming you have Python setup, run the following commands:

git clone https://github.com/Nemsiuu/Vet.git
pip3 install -r requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py collectstatic



python3 manage.py createsuperuser # Create a superuser

python3 manage.py runserver

Open a browser to http://127.0.0.1:8000/admin/ to open the admin site

Create a few test objects of each type.
Open tab to http://127.0.0.1:8000 to see the main site, with your new objects.
