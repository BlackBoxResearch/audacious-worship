import streamlit as st

st.logo(image="e1d92e3e-43a1-458e-bea9-6917bbc56fd8.png", icon_image="19c1a7b9-f165-46a4-a2b1-4f5ccae4419e.png", size="large")

pages = {
    "Home": [
        st.Page("home.py", title="Home", icon="🏠"),
    ],
    "Events": [
        st.Page("nights_of_fire.py", title="Nights of Fire 2025", icon="🔥"),
        st.Page("culture_summit.py", title="Culture Summit 2025", icon="🔥"),
    ],
}

pg = st.navigation(pages)
pg.run()