# Nexa - Legal Intake Assistant

Nexa is a scripted legal intake assistant for immigration law firms. It provides a professional and user-friendly chat interface to collect client information and automatically notifies the law firm via email upon completion.

## Features

- **Scripted Conversation:** Guides users through a predefined set of questions to ensure all necessary information is collected.
- **Email Notifications:** Automatically sends an email with the complete client intake form to the law firm.
- **Secure Configuration:** Uses environment variables for securely managing email credentials in a production environment.
- **Simple User Interface:** A clean, chat-like interface for a professional and intuitive user experience.

## Getting Started

### Prerequisites

- Python 3.7+

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd nexa-legal-assistant
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

#### Configuration

The application requires SMTP credentials to send email notifications. There are two ways to provide these settings:

**1. (Recommended for Production) Using Environment Variables**

For a deployed application, it is highly recommended to use environment variables to keep your email credentials secure.

Set the following environment variables:
- `RECIPIENT_EMAIL`: The email address where intake forms should be sent.
- `SMTP_HOST`: The hostname of your SMTP server (e.g., `smtp.gmail.com`).
- `SMTP_PORT`: The port number for your SMTP server (e.g., `587`).
- `SMTP_USER`: The username for your SMTP account.
- `SMTP_PASS`: The password for your SMTP account.

**2. (For Local Development) Using the Sidebar**

If the environment variables are not set, the application will display input fields in the sidebar where you can enter the notification settings. This is a convenient option for local development and testing.

#### Running the App

Once configured, run the application:
```bash
streamlit run app.py
```

## How It Works

The application uses Streamlit to create the user interface. The conversation flow is based on a hardcoded list of questions inside the `app.py` script. When the questionnaire is complete, it uses Python's `smtplib` to send the collected answers to the configured email address.
