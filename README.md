#   ⚙️ NETFIX

##  PRESENTATION
Netfix is a web application built using the Django framework that allows users to request and provide various home services. Whether you need your bidet fixed, walls painted, or your house cleaned, Netfix has got you covered. Users can register as either a Company (service provider) or a Customer (service requester).

## GETTING STARTED
These instructions will help you set up and run the Netfix project on your local machine.

### PREREQUISITES
- Python 3.x
- Django 3.1.14 (or the version specified in the project)

### INSTALLING
1. Clone the repository to your local machine:

```
git clone https://learn.zone01kisumu.ke/git/hanapiko/netfix
```

2. Navigate to the project directory:

```
cd netfix
```

3. Create a virtual environment (recommended):

```
python3 -m venv venv
```

4. Activate the virtual environment:

- On Windows:

```
venv\Scripts\activate
```

- On macOS and Linux:

```
source venv/bin/activate
```

5. Deactivate the virtual environment

- On macOS and Linux:

```
deactivate
```

6. Install the required dependencies:

```
pip install django
<!-- pip install -r requirements.txt -->
```

7. Apply database migrations:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

8. Create a superuser account to access the admin panel:

```
python3 manage.py createsuperuser
```

9. Run the development server:

```
python3 manage.py runserver
```

10. Access the application in your web browser at `http://127.0.0.1:8000/`.

## FEATURES
- [x] User registration and login (both Company and Customer)
- [x] User profile pages displaying information and requested services
- [x] Service creation by Companies
- [x] Service listing by category and creation order
- [x] Service details page with company information
- [x] Service request submission by Customers
- [x] Most requested services page
- [x] Proper error handling and status pages
- [x] HTTPS secure connection
- [ ] Rate limiting to prevent abuse
- [x] Encryption of client passwords and sessions

## BUILT WITH
- Django - The web framework used
- Python - Programming language
- HTML, CSS, JavaScript - Frontend technologies

## AUTHORS
- Hannah
- Adioz Daniel
