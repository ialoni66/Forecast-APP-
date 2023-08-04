import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days forecasted")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

try:
    if place:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict['main']["temp"] for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]

            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}

            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            print(sky_conditions)
            image_paths = [images[condition] for condition in sky_conditions]
            print(image_paths)
            st.image(image_paths, width=115)
except KeyError:

    st.write("The place you entered does not exist")