import streamlit as st
import pandas as pd
import plotly.express as px
from backend import get_data

st.title('Weather Forecast for the Next Days')

place = st.text_input('Place: ')
days = st.slider('Forecast Days', min_value=1, max_value=5)
option = st.selectbox('Select data to view', ('Temperature', 'Sky'))

st.subheader(f"{option} for the next {days} days in {place}")

try:
    if place:
        filtered_data = get_data(place, days)
        if option == "Temperature":
            temperature = [dict["main"]["temp"] for dict in filtered_data]
            temperatures = [temp/10 for temp in temperature]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images / snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_path = [images[condition] for condition in sky_conditions]
            st.image(image_path, width=100)
except KeyError:
    st.info("Please type a real city")
