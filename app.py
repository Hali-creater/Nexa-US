import streamlit as st
import openai
import os

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

    st.sidebar.title("Configuration")
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")

    st.title("Nexa - Your AI Legal Assistant")

    # Legal Disclaimer
    st.warning(
        "I am an automated assistant for the law firm. "
        "I am not a lawyer and cannot provide legal advice. "
        "I collect information only for attorney review. "
        "All information you share is confidential."
    )

    if not api_key:
        st.info("Please enter your OpenAI API key in the sidebar to begin.")
        st.stop()

    if api_key:
        client = openai.OpenAI(api_key=api_key)

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f'<div class="user-bubble">{message["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="assistant-bubble">{message["content"]}</div>', unsafe_allow_html=True)

        user_input = st.text_input("Your message:", key="user_input")

        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})

            with open("prompt.md", "r") as f:
                system_prompt = f.read()

            messages = [{"role": "system", "content": system_prompt}] + st.session_state.messages

            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                )
                assistant_response = response.choices[0].message.content

                if "[URGENT]" in assistant_response:
                    st.error("This case has been flagged as potentially urgent and will be prioritized for attorney review.")
                    assistant_response = assistant_response.replace("[URGENT]", "").strip()

                st.session_state.messages.append({"role": "assistant", "content": assistant_response})

                if "schedule a consultation" in assistant_response.lower():
                    with st.form("consultation_form"):
                        st.subheader("Schedule a Consultation")
                        consultation_type = st.selectbox("Preferred consultation type:", ["Phone", "Video", "In-person"])
                        preferred_date = st.date_input("Preferred date:")
                        preferred_time = st.time_input("Preferred time:")
                        submitted = st.form_submit_button("Submit")

                        if submitted:
                            st.success(f"Thank you! We have received your request for a {consultation_type} consultation on {preferred_date} at {preferred_time}. We will contact you shortly to confirm.")

            except Exception as e:
                st.error(f"An error occurred: {e}")

            st.rerun()

if __name__ == "__main__":
    main()
