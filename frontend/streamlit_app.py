import streamlit as st
import pandas as pd
import requests


st.set_page_config(
    page_title="NotifyService",
    page_icon="📧",
    layout="wide"
)

supported_domains = ["gmail.com", "minitts.net"]

# ---------- SESSION STATE ----------
if "email" not in st.session_state:
    st.session_state.email = ""

if "message" not in st.session_state:
    st.session_state.message = ""

if "logs" not in st.session_state:
    st.session_state.logs = []


# ---------- FUNCTIONS ----------
def reset_form():
    st.session_state.email = ""
    st.session_state.message = ""

def valid_email(email: str):
    domain = email.split('@')[1]
    if domain in supported_domains:
        return True
    return False

# ---------- SIDEBAR ----------
st.sidebar.title("📧 NotifyService")

menu = st.sidebar.radio(
    "Navigation",
    ["Send Email", "Email Logs", "System Status"]
)

st.sidebar.markdown("---")
st.sidebar.info("Internal Notification Tool")


# ---------- HEADER ----------
st.title("📧 Email Notification Dashboard")
st.markdown("Send and monitor notification emails")

st.markdown("---")


# ---------- SEND EMAIL PAGE ----------
if menu == "Send Email":

    col1, col2 = st.columns([2,1])

    with col1:
        st.subheader("Compose Email")

        email = st.text_input(
            "Recipient Email",
            key="email",
            placeholder="example@email.com"
        )

        message = st.text_area(
            "Email Message",
            key="message",
            height=200,
            placeholder="Write your email message..."
        )

        b1, b2 = st.columns(2)

        with b1:
            if st.button("Send Email", use_container_width=True):

                if not message:
                    st.error(f"Please provide message.")
                    st.stop()
                if not email:
                    st.error(f"Please provide email address")
                    st.stop()

                if not valid_email(email):
                    st.error(f'Invalid email address, Supported email domain is [gmail.com]')
                    st.stop()

                # Core Logic To sent email request to backend server
                payload =  {
                    "message": message,
                    "receiver_email_address": email
                }

                response = requests.post(
                    "http://localhost:8080/sent_mail",
                    json=payload
                )
                response_data = response.json()
                print(response_data)

                if response.status_code == 200 and response_data['success']:
                    st.success(f"Email sent to {email}")

                    # Add log
                    st.session_state.logs.append({
                        "email": email,
                        "message": message
                    })

                else:
                    st.error(f"Email sent request failed, Error: {response_data['success']}")



        with b2:
            st.button(
                "Reset",
                on_click=reset_form,
                use_container_width=True
            )

    with col2:
        st.subheader("Tips")

        st.info(
            """
            ✔ Enter valid email address  
            ✔ Keep message concise  
            ✔ Check logs for delivery info
            """
        )


# ---------- EMAIL LOGS PAGE ----------
elif menu == "Email Logs":

    st.subheader("Email Delivery Logs")
    user_email = "soniaayush0044@gmail.com"
    response = requests.get(
                    "http://localhost:8080/mail_logs",
                    params={"user_email": user_email}
                )
    print(response.json())
    response_data = response.json()
    if response.status_code==200:
        df = pd.DataFrame(
            response_data, columns=("id", "user_name", "user_email", "mail_content", "receiver_email_address", "status", "sent_at")
        )
        st.dataframe(df)
    else:
        st.warning("No emails sent yet.")


# ---------- SYSTEM STATUS PAGE ----------
elif menu == "System Status":

    st.subheader("System Health")

    col1, col2, col3 = st.columns(3)

    col1.metric("Email API", "Running")
    col2.metric("Queue", "Idle")
    col3.metric("Failed Emails", "0")


# ---------- FOOTER ----------
st.markdown("---")

st.markdown(
    "<p style='text-align:center;color:gray;'>© 2026 NotifyService • Built with Streamlit</p>",
    unsafe_allow_html=True
)