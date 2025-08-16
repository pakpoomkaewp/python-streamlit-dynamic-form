import streamlit as st
import pandas as pd

st.title('Simple Contact Form')

# Create a form using st.form()
with st.form("contact_form"):
    st.subheader("Contact Information")

    # Text inputs
    name = st.text_input("Full Name", placeholder="Enter your full name")
    email = st.text_input("Email", placeholder="your.email@example.com")

    # Select box (dropdown)
    department = st.selectbox(
        "Department",
        ["Sales", "Support", "Marketing", "Technical"]
    )

    # Text area for longer text
    message = st.text_area(
        "Message",
        placeholder="Enter your message here...",
        height=100
    )

    # Number input
    priority = st.slider("Priority Level", 1, 5, 3)

    # Checkbox
    newsletter = st.checkbox("Subscribe to newsletter")

    # Form submit button
    submitted = st.form_submit_button("Submit Form")

    # Handle form submission
    if submitted:
        # Check if required fields are filled
        if name and email and message:
            st.success("Form submitted successfully!")

            # Display submitted data
            st.subheader("Submitted Information:")
            st.write(f"**Name:** {name}")
            st.write(f"**Email** {email}")
            st.write(f"**Department:** {department}")
            st.write(f"**Message:** {message}")
            st.write(f"**Priority:** {priority}")
            st.write(f"**Newsletter:** {'Yes' if newsletter else 'No'}")

            # You can also save to a DataFrame or database here
            form_data = {
                'Name': [name],
                'Email': [email],
                'Department': [department],
                'Message': [message],
                'Priority': [priority],
                'Newsletter': [newsletter]
            }
            df = pd.DataFrame(form_data)
            st.subheader("Data as DataFrame:")
            st.dataframe(df)

        else:
            st.error("Please fill in all required fields (Name, Email, Message)")

# Instructions for the user
st.sidebar.markdown("""
## How to use this form:
1. Fill in your name and email
2. Select your department
3. Write your message
4. Adjust priority level (1-5)
5. Check newsletter if interested
6. Click Submit Form
""")