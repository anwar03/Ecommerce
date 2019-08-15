# DjangoWith-Bootstrap
Simple E-commerce site with Login, Logout, Add product.. etc with AngularJs 

## Prerequisites
* Python
* Virtualenv

## Getting Started
1. Clone the repository.
2. Create virtual environment. 
```
virtualenv -p python3 envname --no-site-packages
```
3. Go to project_base directory
4. Install requirements 
```
pip install -r requirements.txt
```

5. Go to client directory 
6. Install npm packages
```
npm install
```

7. Migrate 
```
python manage.py migrate
```
8. Run project 
```
python manage.py runserver
```
## Built With

* [Django](https://www.djangoproject.com/) - The web framework used.
* [Django Rest Framework](http://www.django-rest-framework.org/) - Rest Api.
* [AngularJs](https://angularjs.org/) - Front end framework.

