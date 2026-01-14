# Nexa - AI Legal Assistant

Nexa is an AI-powered legal intake assistant for immigration law firms. It provides a professional and user-friendly chat interface to collect client information, flag urgent cases, and schedule consultations.

## Features

- **Conversational AI:** Powered by OpenAI, Nexa engages users in a natural and intuitive conversation.
- **Urgent Case Flagging:** Automatically detects and flags cases that require immediate attention.
- **Consultation Scheduling:** Allows users to request a consultation directly from the chat interface.
- **Secure API Key Management:** Uses environment variables for secure API key management in a production environment.

## Getting Started

### Prerequisites

- Python 3.7+
- An OpenAI API key

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd nexa-ai-assistant
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

There are two ways to provide your OpenAI API key:

#### 1. (Recommended for Production) Using Environment Variables

For a deployed application, it is highly recommended to use environment variables to keep your API key secure.

Set the `OPENAI_API_KEY` environment variable:

- **Linux/macOS:**
  ```bash
  export OPENAI_API_KEY='your-api-key'
  ```
- **Windows:**
  ```bash
  set OPENAI_API_KEY='your-api-key'
  ```

Then, run the Streamlit application:
```bash
streamlit run app.py
```

#### 2. (For Local Development) Using the Sidebar

If the `OPENAI_API_KEY` environment variable is not set, the application will display a text input in the sidebar where you can enter your API key. This is a convenient option for local development and testing.

1. **Run the application:**
   ```bash
   streamlit run app.py
   ```
2. **Enter your API key in the sidebar.**

## How It Works

The application uses Streamlit to create the user interface and the OpenAI API to power the chat functionality. The AI's behavior is guided by a system prompt defined in `prompt.md`.
