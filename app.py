import streamlit as st

pages = [
    st.page(page="pages/page1.py", title="home", icon="🏡"),
    st.page(page="pages/page2.py",  title="visualisasi data", icon="📊"),
     st.page(page="pages/page3.py",  title="settings", icon="⚙️"),



pg = st.nagivation(
    pages,
    position="sidebar",
    expanded=True
)

pg.run()



