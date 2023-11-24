import streamlit as st
from send_email import send_email

st.set_page_config(layout="wide")

st.header("Contact Me:")

with st.form(key="email_forms"):
	user_email = st.text_input("Your Email Address:")
	raw_message = st.text_area("Your Message:")
	message = f"""\
subject: New Email From {user_email}

From: {user_email}
{raw_message}
	"""
	button = st.form_submit_button("Submit")
	if button:
		send_email(message)
		st.info("Your Email Was Sent Successfully.")
