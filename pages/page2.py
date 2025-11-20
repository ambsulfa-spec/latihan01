import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt

st.title("data visualization")

# generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)
# plot data 
fig, ax = plt.subplost()
ax.plot(x, y)
# display the plot
st.pyplot(fig)