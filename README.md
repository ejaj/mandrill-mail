# Mailchimp Webhook

## Setup

The first thing to do is to clone the repository:

```sh
$  git clone https://kazi_ejaj@bitbucket.org/gpix/mandrill-mail.git
$ cd mandrill-mail
```

Then, active a virtual environment:

```sh
$ source venv/bin/activate
```

Create an .env file and paste all the variables from .env.keep file and set the value for them for example database
name, password, host etc.

## Run the project on localhost.

Then run these command.

install the dependencies

```sh
pip install -r requirements.txt
```

For migrations

```sh
python manage.py migrate
```

For running project.

```sh
python manage.py runserver
```

### Dependencies

```sh
- Database: PostgreSQL
```

### Api End Point

```sh
 https://domain/api/v1/mailchimp-webhook/
```
