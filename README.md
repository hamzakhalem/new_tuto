# Django CRUD Practice

A Django learning project that covers models, forms, class-based views and simple JSON views, built around employees, customers and event registrations.

## Features

- **Registrations:** full CRUD with Django's generic class-based views (`CreateView`, `ListView`, `DetailView`, `UpdateView`, `DeleteView`)
- **Subscribe form:** a simple email form page
- **Employees:** employee data shown as an HTML page and returned as JSON from two endpoints
- **Customers:** a second app (`employeeapp`) with employee and customer models
- Everything is manageable from the Django admin

## Pages and endpoints

| Path | What it does |
| --- | --- |
| `/` | Home page |
| `/subscribe` | Subscribe form |
| `/create` | Create a registration |
| `/list` | List registrations |
| `/detail/<id>` | Show one registration |
| `/update/<id>` | Edit a registration |
| `/delete/<id>` | Delete a registration (with confirmation) |
| `/displayEmployee` | Employees as an HTML page |
| `/displayEmployee2`, `/Employee/api/get/` | Employees as JSON |

## Built with

- Python 3, Django 4.2
- SQLite

## Run it locally

```bash
git clone https://github.com/hamzakhalem/new_tuto.git
cd new_tuto
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirement.txt
export DJANGO_SECRET_KEY="any-long-random-string"   # PowerShell: $env:DJANGO_SECRET_KEY="..."
cd myproject
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000.

## Project structure

```
myproject/
  myproject/     Project settings and root URLs
  newapp/        Registrations, subscribe form, employee pages and JSON views
  employeeapp/   Employee and customer models
```
