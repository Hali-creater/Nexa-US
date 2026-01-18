import streamlit as st
import os
import smtplib
from email.message import EmailMessage

def main():
    st.set_page_config(page_title="Nexa - AI Legal Assistant", layout="wide")

    # Custom CSS for styling
    st.markdown("""
        <style>
            /* Chat bubbles */
            .user-bubble {
                background-color: #007bff;
                color: white;
                border-radius: 15px 15px 0 15px;
                padding: 10px 15px;
                align-self: flex-end;
                max-width: 70%;
                margin-bottom: 10px;
                display: table;
                margin-left: auto;
            }
            .assistant-bubble {
                background-color: #e9ecef;
                color: #333;
                border-radius: 15px 15px 15px 0;
                padding: 10px 15px;
                align-self: flex-start;
                max-width: 70%;
                margin-bottom: 10px;
                display: table;
            }
        </style>
    """, unsafe_allow_html=True)

    st.sidebar.title("Notification Settings")
    recipient_email = os.getenv("RECIPIENT_EMAIL") or st.sidebar.text_input("Recipient Email")
    smtp_host = os.getenv("SMTP_HOST") or st.sidebar.text_input("SMTP Host")
    smtp_port = os.getenv("SMTP_PORT") or st.sidebar.number_input("SMTP Port", min_value=1, max_value=65535, value=587)
    smtp_user = os.getenv("SMTP_USER") or st.sidebar.text_input("SMTP Username")
    smtp_pass = os.getenv("SMTP_PASS") or st.sidebar.text_input("SMTP Password", type="password")

    st.title("Nexa - Your AI Legal Assistant")

    # Legal Disclaimer
    st.warning(
        "I am an automated assistant for the law firm. "
        "I am not a lawyer and cannot provide legal advice. "
        "I collect information only for attorney review. "
        "All information you share is confidential."
    )

    # Define the questions based on prompt.md
    questions = [
        "What is your full legal name (as shown on your passport)?",
        "Have you ever used any other names?",
        "What is your date of birth?",
        "What is your country of birth?",
        "What is your country of citizenship?",
        "What is your marital status?",
        "What is your current U.S. address?",
        "What is the best phone number to reach you?",
        "What is your email address?",
        "What is your preferred language?",
        "Are you currently inside the United States?",
        "When did you first enter the U.S.?",
        "How did you enter the U.S.? (e.g., with a visa, border entry)",
        "What type of visa did you enter on?",
        "Did you enter the U.S. with inspection by an officer?",
        "Have you ever overstayed a visa?",
        "What is your current immigration status?",
        "When did or will your status expire?",
        "Have you ever applied for any immigration benefit?",
        "What type of application was it?",
        "Was any application ever denied, withdrawn, or revoked?",
        "Have you ever been in removal or deportation proceedings?",
        "Have you ever received a Notice to Appear (NTA)?",
        "Have you ever left the U.S. after overstaying?",
        "Are you currently married?",
        "Is your spouse a U.S. citizen or green card holder?",
        "When and where did you get married?",
        "Have you ever been married before?",
        "Do you have children?",
        "Are any of your parents U.S. citizens or residents?",
        "Do you have any other U.S. citizen or permanent resident relatives?",
        "Are you currently employed?",
        "What is your employer’s name and location?",
        "What is your job title?",
        "When did you start this job?",
        "What is your highest level of education?",
        "What is your field of study?",
        "Which country did you obtain your degree from?",
        "Have you ever worked without authorization in the U.S.?",
        "Have you ever used CPT or OPT?",
        "Have you ever been arrested?",
        "Have you ever been charged with a crime?",
        "Have you ever been convicted of a crime?",
        "Have you ever received a DUI?",
        "Have you ever used false documents?",
        "Have you ever given false information to an immigration officer?",
        "Have you ever claimed U.S. citizenship when you were not a citizen?",
        "What immigration benefit are you seeking?",
        "Is your situation urgent?",
        "Do you have any upcoming deadlines or court dates?",
        "Have you spoken with another attorney before?",
        "Would you like to schedule a consultation with an attorney? (Yes/No)"
    ]

    # Initialize session state
    if 'messages' not in st.session_state:
        st.session_state.messages = []
        st.session_state.question_index = 0
        st.session_state.answers = {}
        # Initial greeting
        st.session_state.messages.append({"role": "assistant", "content": "Hello! I am here to help you with your immigration intake."})
        st.session_state.messages.append({"role": "assistant", "content": questions[0]})

    # Display chat messages
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div class="user-bubble">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-bubble">{message["content"]}</div>', unsafe_allow_html=True)

    # Define the callback function to process the user's answer
    def handle_submit():
        user_answer = st.session_state.input_box
        if user_answer:
            # Store user's answer
            st.session_state.messages.append({"role": "user", "content": user_answer})
            st.session_state.answers[questions[st.session_state.question_index]] = user_answer
            st.session_state.question_index += 1

            # Ask the next question or end the conversation
            if st.session_state.question_index < len(questions):
                st.session_state.messages.append({"role": "assistant", "content": questions[st.session_state.question_index]})
            else:
                st.session_state.messages.append({"role": "assistant", "content": "Thank you for providing your information. Please review and click the button below to send your details to the firm."})

            # Clear the input box value in the state
            st.session_state.input_box = ""

    # Show the input box while there are questions, otherwise show the send button
    if st.session_state.question_index < len(questions):
        st.text_input("Your answer:", key="input_box", on_change=handle_submit)
    else:
        if st.button("Send My Information to the Firm"):
            # Format the answers for the email
            email_body = "A new client has completed the intake form.\n\n"
            for question, answer in st.session_state.answers.items():
                email_body += f"**{question}**\n{answer}\n\n"

            # Send the email
            try:
                msg = EmailMessage()
                msg.set_content(email_body)
                msg['Subject'] = f"New Client Intake: {st.session_state.answers.get('What is your full legal name (as shown on your passport)?', 'N/A')}"
                msg['From'] = smtp_user
                msg['To'] = recipient_email

                server = smtplib.SMTP(smtp_host, int(smtp_port))
                server.starttls()
                server.login(smtp_user, smtp_pass)
                server.send_message(msg)
                server.quit()

                st.success("Your intake form has been submitted. The law firm has been notified.")
                st.session_state.messages.append({"role": "assistant", "content": "Your information has been securely submitted. Thank you."})
                st.rerun() # Rerun to update the message display
            except Exception as e:
                st.error(f"An error occurred while sending the email: {e}")

if __name__ == "__main__":
    main()
