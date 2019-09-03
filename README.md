[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.2.4-brightgreen.svg)](https://djangoproject.com)
# Card-generator-and-authenticator
RESTful endpoint for generating and validating cards
# Card verification and Generator RESTful APIs 

This project Creates an API that can validate and Generate credit cards and debit cards based solely on the
card number using Django.

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/TaiwoTech/Card-generator-and-authenticator.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.

## Accessing the card validation endpoint from local machine
E.g:
```bash
http://127.0.0.1:8000/credit_auth/?card_number=(8398393939434) <---- number to authenticate.
http://127.0.0.1:8000/credit_auth/?card_number=8398393939434
```
## Accessing the valid card number generator endpoint from local machine, this only works for visa,amex and mastercard.
E.g:
```bash
http://127.0.0.1:8000/credit_gen/?visa=(3)<---- number of cards to generate of type visa.
http://127.0.0.1:8000/credit_gen/?amex=30 ---> returns 30 amex cards.
http://127.0.0.1:8000/credit_gen/?mastercard=1 ---> returns 1 mastercard.
http://127.0.0.1:8000/credit_gen/    ----> returns a valid card number of type visa,amex or mastercard.
```
