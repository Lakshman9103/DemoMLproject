import streamlit as st
import pandas as pd
import numpy as np
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.exception import CustomException
from src.logger import logging
import sys  

# Page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="📊",
    layout="centered"
)

# App title and description
st.title("Student Exam Performance Indicator")
st.write("---")

logging.info("Streamlit app started.")

# Create main content
st.subheader("Student Exam Performance Prediction")

# Create form inputs in columns for better layout
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox(
        "Gender",
        ["Select your Gender", "male", "female"]
    )
    if gender == "Select your Gender":
        gender = ""
    
    race_ethnicity = st.selectbox(
        "Race or Ethnicity",
        ["Select Ethnicity", "group A", "group B", "group C", "group D", "group E"]
    )
    if race_ethnicity == "Select Ethnicity":
        race_ethnicity = ""
    
    
    parental_education = st.selectbox(
        "Parental Level of Education",
        [
            "Select Education Level",
            "some high school",
            "high school",
            "some college",
            "associate's degree",
            "bachelor's degree",
            "master's degree"
        ]
    )
    if parental_education == "Select Education Level":
        parental_education = ""
with col2:
        lunch = st.selectbox(
        "Lunch Type",
        ["Select Lunch Type", "free/reduced", "standard"]
    )
        if lunch == "Select Lunch Type":
            lunch = ""
    
        test_prep = st.selectbox(
        "Test Preparation Course",
        ["Select Test Course", "none", "completed"]
    )
        if test_prep == "Select Test Course":
            test_prep = ""
    
        reading_score = st.number_input(
        "Reading Score (out of 100)",
        min_value=0,
        max_value=100,
        value=50
    )

    # Writing score input
        writing_score = st.number_input(
        "Writing Score (out of 100)",
        min_value=0,
        max_value=100,
        value=50
)

st.write("---")

# Prediction button
if st.button("Predict Performance", use_container_width=True):
    # Validate inputs
    if not all([gender, race_ethnicity, parental_education, lunch, test_prep]):
        st.error("Please fill in all required fields!")
        logging.warning("User did not fill all required fields.")
    else:
        try:
            st.success("Inputs received. Making prediction...")
            logging.info("All inputs received. Proceeding to prediction.")
           

# Create custom data object
            data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_education,
            lunch=lunch,
            test_preparation_course=test_prep,
            reading_score=float(reading_score),
            writing_score=float(writing_score)
            )
            logging.info(f"CustomData object created with: gender={gender}, race_ethnicity={race_ethnicity}, parental_level_of_education={parental_education}, lunch={lunch}, test_preparation_course={test_prep}, reading_score={reading_score}, writing_score={writing_score}")

            # Get data as dataframe
            pred_df = data.get_data_as_dataframe()
            logging.info("CustomData converted to DataFrame for prediction.")

            # Make prediction
            predict_pipeline = PredictPipeline()
            logging.info("PredictPipeline initialized.")
            result = predict_pipeline.predict(pred_df)
            logging.info(f"Prediction completed. Result: {result}")

            # Display result
            st.success("Prediction completed!")
            st.metric(
                label="Predicted Math Score",
                value=f"{result[0]:.2f}"
            )

            # Display input summary
            with st.expander("View Input Summary"):
                summary_data = {
                    "Gender": gender,
                    "Race/Ethnicity": race_ethnicity,
                    "Parental Education": parental_education,
                    "Lunch Type": lunch,
                    "Test Preparation": test_prep,
                    "Reading Score": reading_score,
                    "Writing Score": writing_score
                }
                df_summary = pd.DataFrame(summary_data.items(), columns=["Field", "Value"])
                df_summary["Value"] = df_summary["Value"].astype(str)
                st.write(df_summary)
                
        except Exception as e:
            st.error(f"An error occurred during prediction: {str(e)}")        
            logging.error(f"Error during prediction: {str(e)}")
            
        except Exception as e:
            st.error("An error occurred while creating input data.")

