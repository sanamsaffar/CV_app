import streamlit as st

def create_cv():
    st.set_page_config(
        page_title="CV Creator",
        page_icon="✨",
        layout="wide"
    )

    st.title("Curriculum Vitae (CV) Creator")

    # Personal Information
    personal_expander = st.expander("Personal Information")  # Use `expander` instead of `beta_expander`
    with personal_expander:
        col1, col2, col3, col4 = st.columns([1, 1, 1, 2])
        with col1:
            first_name = st.text_input("First Name")
        with col2:
            last_name = st.text_input("Last Name")
        with col3:
            email = st.text_input("Email")
        with col4:
            phone = st.text_input("Phone Number")

    # ... (Rest of your code with similar updates for other expander sections)

    # Display the generated CV
    st.title("Generated CV")
    st.write(f"**Name:** {first_name} {last_name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Phone:** {phone}")

    # ... (Rest of your CV generation code)

if __name__ == '__main__':
    create_cv()
