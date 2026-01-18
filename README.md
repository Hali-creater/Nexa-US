# Nexa - Legal Intake Assistant

Nexa is a scripted legal intake assistant for immigration law firms. It provides a professional and user-friendly chat interface to collect client information and, upon the client's confirmation, notifies the law firm via email.

## Features

- **Scripted Conversation:** Guides clients through a predefined set of questions.
- **Client-Controlled Submission:** The client's information is only sent after they explicitly click a "Send" button.
- **Email Notifications:** Automatically sends an email with the complete client intake form to the law firm.
- **Secure, Environment-Based Configuration:** Exclusively uses environment variables for securely managing email credentials.

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

### Configuration

The application requires SMTP credentials to send email notifications. These settings must be configured using environment variables. The application will not start if any of these are missing.

**Set the following environment variables:**
- `RECIPIENT_EMAIL`: The email address where intake forms should be sent.
- `SMTP_HOST`: The hostname of your SMTP server (e.g., `smtp.gmail.com`).
- `SMTP_PORT`: The port number for your SMTP server (e.g., `587`).
- `SMTP_USER`: The username for your SMTP account.
- `SMTP_PASS`: The password for your SMTP account.

### Running the Application

Once the environment variables are configured, run the application:
```bash
streamlit run app.py
```

## Client Experience

The client using the application will have a clean, focused experience. They will be guided through the questionnaire and, at the end, will be presented with a button to securely send their information to the firm. No configuration options are ever shown to the client.
