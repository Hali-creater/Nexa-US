# Nexa - Legal Intake Assistant

Nexa is a scripted legal intake assistant for immigration law firms. It provides a professional and user-friendly chat interface to collect client information and, upon the client's confirmation, notifies the law firm via email.

## Features

- **Scripted Conversation:** Guides clients through a predefined set of questions.
- **Client-Controlled Submission:** The client's information is only sent after they explicitly click a "Send" button.
- **Email Notifications:** Automatically sends an email with the complete client intake form to the law firm.
- **Secure Administrator Configuration:** Uses environment variables for securely managing email credentials in a production environment.

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

#### Administrator Configuration

The application requires SMTP credentials to send email notifications. **These settings are configured by the law firm's administrator and are never shown to the client.**

There are two ways to provide these settings:

**1. (Recommended for Production) Using Environment Variables**

For a deployed application, it is highly recommended to use environment variables to keep your email credentials secure.

Set the following environment variables:
- `RECIPI-ENT_EMAIL`: The email address where intake forms should be sent.
- `SMTP_HOST`: The hostname of your SMTP server (e.g., `smtp.gmail.com`).
- `SMTP_PORT`: The port number for your SMTP server (e.g., `587`).
- `SMTP_USER`: The username for your SMTP account.
- `SMTP_PASS`: The password for your SMTP account.

**2. (For Local Development) Using the Sidebar**

If the environment variables are not set, the application will display input fields in the sidebar. This is a convenient option for the administrator during local development and testing.

#### Running the App

Once configured by an administrator, run the application:
```bash
streamlit run app.py
```

## Client Experience

The client using the application will **never** see the sidebar or any configuration options. They will be guided through the questionnaire and, at the end, will be presented with a button to securely send their information to the firm.
