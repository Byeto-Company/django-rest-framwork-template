# Django Base Settings and Packages Template

This project provides a robust Django base with essential packages and configurations, helping you get up and running quickly. It includes an enhanced Django admin, JWT authentication, Swagger for API documentation, and utilities for cleanup, CORS, and messaging via Telegram.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Available Packages](#available-packages)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Enhanced Django Admin**: Custom admin interface using `django-unfold` for a modern look and feel.
- **JWT Authentication**: Secure access to REST API endpoints using JWT tokens.
- **Swagger API Documentation**: Integrated Swagger documentation with `drf-spectacular` for all API endpoints.
- **Automatic File Cleanup**: Automatically removes unused files using `django-cleanup`.
- **CORS Support**: Cross-origin request support via `django-cors-headers`.
- **Utilities Module**: Custom utilities for pagination, email sending, and Telegram bot messaging.
- **Environment-based Settings**: Manage environment variables via `.env` for better security and flexibility.

---

## Requirements

- Python 3.10 or higher
- Django 5.1.2
- PostgreSQL (recommended for production)

---

## Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory with the following variables:
   ```env
   DEBUG=False
   DB_NAME=<your_db_name>
   DB_USER=<your_db_user>
   DB_PASSWORD=<your_db_password>
   DB_HOST=<your_db_host>
   DB_PORT=<your_db_port>
   SECRET_KEY=<your_secret_key>
   EMAIL_BACKEND=<your_email_backend>
   EMAIL_HOST=<your_email_host>
   EMAIL_HOST_USER=<your_email_host_user>
   EMAIL_HOST_PASSWORD=<your_email_host_password>
   DEFAULT_FROM_EMAIL=<your_default_from_email>
   TELEGRAM_BOT_TOKEN=<your_telegram_bot_token>
   DOMAIN=<your_domain>
   API_DOMAIN=<your_api_domain>
   SITE_TITLE=<your_site_title>
   SITE_HEADER=<your_site_header>

	5.	Run migrations:

python manage.py migrate


	6.	Create a superuser:

python manage.py createsuperuser


	7.	Start the development server:

python manage.py runserver



Configuration

In settings.py, configure various aspects of the project, including:

	•	Database: Set up your PostgreSQL or other database information.
	•	Email: Configure email settings with variables from your .env file.
	•	JWT: Adjust ACCESS_TOKEN_LIFETIME and REFRESH_TOKEN_LIFETIME as needed.
	•	Theme Colors: Customize admin theme colors through the THEME_COLOR dictionary.

Usage

API Endpoints

	•	Swagger Documentation: Access Swagger documentation at http://<your-domain>/swagger/.
	•	JWT Authentication: Obtain JWT tokens by posting to /api/token/.

Utilities

	•	Email: Use the send_email() function from the utils module to send emails.

from django.core.mail import send_mail

def send_email(subject, message, recipient_list):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipient_list,
    )


	•	Pagination: The StructurePagination class can be used to paginate API responses.

from rest_framework.pagination import LimitOffsetPagination

class StructurePagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


	•	Telegram Bot: Use the send_telegram_message() function to send messages via Telegram.

import telebot
from django.conf import settings

bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)

def send_telegram_message(chat_id, message):
    bot.send_message(chat_id, message)



Available Packages

This project includes the following core packages:

	•	asgiref==3.8.1
	•	attrs==24.2.0
	•	Django==5.1.2
	•	django-cleanup==8.1.0: Automatically removes unused files.
	•	django-cors-headers==4.4.0: Manages cross-origin requests.
	•	django-unfold==0.39.0: Modern admin theme.
	•	djangorestframework==3.15.2: Core REST framework for API creation.
	•	djangorestframework-simplejwt==5.3.1: JWT support for secure API access.
	•	drf-spectacular==0.27.2: Swagger/OpenAPI documentation for DRF.
	•	whitenoise==6.7.0: Serves static files in production.

Refer to requirements.txt for the full list of dependencies.

Project Structure

<project-root>
├── manage.py
├── <project_name>/
│   ├── settings.py       # Core settings
│   ├── urls.py           # Project URLs
│   ├── wsgi.py           # WSGI configuration
│   ├── asgi.py           # ASGI configuration for async support
├── apps/
│   ├── <your_app>/       # Custom app with views, models, etc.
│   └── utils.py          # Contains utility functions like pagination and email
├── templates/            # HTML templates
├── static/               # Static files
└── .env                  # Environment variables

Contributing

	1.	Fork the project.
	2.	Create your feature branch:

git checkout -b feature/your-feature


	3.	Commit your changes:

git commit -m 'Add some feature'


	4.	Push to the branch:

git push origin feature/your-feature


	5.	Open a pull request.

License

This project is open-source and available under the MIT License.



