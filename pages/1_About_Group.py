import streamlit as st

st.title("About the Group")
st.write("This page provides information about the group members.")

group_members = [
    {"Name": "Ruddi Sutomi", "Role": "Manager", "Email": "ruddi.sutomi@michelin.com", "Image": "C:\Users\LENOVO\Documents\ImageProcessingApp - Group 8 - Add Logo and Photo\assets\WhatsApp Image 2024-12-13 at 21.05.38_b1b3ada7.jpg"},
    {"Name": "Sandi Resta", "Role": "Team Leader", "Email": "sandi.resta@michelin.com", "Image": "C:\Users\LENOVO\Documents\ImageProcessingApp - Group 8 - Add Logo and Photo\assets\20220822_211922.jpg"},
    {"Name": "Raden Asep Ahmad Fadillah", "Role": "BU Leader", "Email": "raden.fadillah@michelin.com", "Image": "C:\Users\LENOVO\Documents\ImageProcessingApp - Group 8 - Add Logo and Photo\assets\WhatsApp Image 2024-12-13 at 21.06.02_107ccee3.jpg"},
]

# Display details with images
for member in group_members:
    st.subheader(member["Name"])
    st.image(member["Image"], caption=f"{member['Name']}'s Photo", width=150)
    st.write(f"**Role:** {member['Role']}")
    st.write(f"**Email:** {member['Email']}")
    st.write("---")