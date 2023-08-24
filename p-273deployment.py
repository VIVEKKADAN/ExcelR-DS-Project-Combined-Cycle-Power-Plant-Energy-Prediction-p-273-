import streamlit as st
import pandas as pd
import pickle

# Load the trained regression model from the pickle file
with open('Stackmodel.pkl', 'rb') as model_file:
    regression_model = pickle.load(model_file)

st.set_page_config(page_title="Energy Production Prediction", layout="wide")
st.title("Energy Production Prediction")

# Input fields for the four features
temperature = (st.number_input("Temperature:(Degree celcius)")-19.651231)/7.452473
exhaust_vacuum = (st.number_input("Exhaust Vacuum:(cm Hg)")-54.305804)/12.707893
amb_pressure = (st.number_input("Ambient Pressure:(millibar)")-1013.259078)/5.938784
r_humidity = (st.number_input("Relative Humidity:(%)")-73.308978)/14.600269

if st.button('Predict'):
# Create a DataFrame with the input features
     input_data = pd.DataFrame({
        'temperature': [temperature],
        'exhaust_vacuum': [exhaust_vacuum], 
        'amb_pressure': [amb_pressure],
        'r_humidity': [r_humidity]
        })

# Make a prediction using the loaded regression model
     predicted_energy = (regression_model.predict(input_data)[0]*17.066995)+454.365009
# Display the predicted energy production
     st.write("Predicted Energy Production:", predicted_energy,"MW")
if st.button('Developed by:'):
            st.subheader('P-273 Group -1,Team Members')
            st.write('Vivek K')
            st.write('Vaibhav Dongre')
            st.write('Abhishek Singh')
            st.write('Anamika Birari')
            st.write('Saipallavi Prakhya')
            st.write('Venkat Pulavarthi')

            st.subheader("We have used STACK Model to predict the Energy In MW in CCPP")
            st.image("https://www.erg.eu/o/erg2020-infographics-files/ciclo-combinato/images/ciclo-combinato.gif")


st.subheader("🧑‍💻 Thank you! 👋")