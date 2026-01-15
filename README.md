# Nexa - Legal Intake Assistant

Nexa is a scripted legal intake assistant for immigration law firms. It provides a professional and user-friendly chat interface to collect client information in a structured manner.

## Features

- **Scripted Conversation:** Guides users through a predefined set of questions to ensure all necessary information is collected.
- **Simple User Interface:** A clean, chat-like interface for a professional and intuitive user experience.
- **Self-Contained:** Has no external AI dependencies and does not require any API keys.

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

1. **Run the application:**
   ```bash
   streamlit run app.py
   ```
2. The application will start, and you can begin the intake process immediately.

## How It Works

The application uses Streamlit to create the user interface. The conversation flow is based on a hardcoded list of questions inside the `app.py` script, which were originally defined in the `prompt.md` file.
