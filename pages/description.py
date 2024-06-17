import streamlit as st

st.title("STREAMLIT APPLICATION DESCRIPTION")


st.header('APPLICATION OF MACHINE LEARNING')
st.image("./pict/sentiment.png")
st.image("./pict/sentiment1.png")

with st.expander("EMOTION ANALYZER"):
    st.markdown("""
    #
                This app uses pre-trained machine learning models that are stored as files to figure out emotions from text you enter. 
                It's made using Streamlit, a tool for creating web apps. You can type in text, and the app will predict emotions like happiness, sadness, anger, nervousness, and fear. This helps people understand the emotions in what they've written.

                
    """, unsafe_allow_html=True)

st.header('IMAGE CLASSIFICATION')
st.image("./pict/classify.png")
st.image("./pict/classify1.png")

with st.expander("ROOM IMAGE CLASSIFICATION"):
    st.markdown("""
    #
                This app uses machine learning models trained on a dataset from Kaggle to decide if a room in a picture is clean or messy. The models are saved as pickled files and included in a Streamlit web interface for simple setup.
                Users can upload room images through the app. It then analyzes the image and predicts if the room is clean or messy based on what it learned from the dataset. The interface is easy to use, so anyone can upload a picture and 
                quickly find out if the room is considered clean or messy according to the trained model."
    """, unsafe_allow_html=True)

st.header('PREDICTION')
st.image("./pict/predictmilk.png")
st.image("./pict/predictmilk1.png")
st.image("./pict/predict2.png")
st.image("./pict/predict3.png")

with st.expander("MILK QUALITY PREDICTOR"):
    st.markdown("""
    #
                To create a milk quality predictor using machine learning, we start by downloading datasets from platforms like Kaggle. 
                These datasets contain historical records of milk samples.
                Once downloaded, we store these datasets in a format called 'pickled files,' which allows us to efficiently store and access the data.
                Using these datasets, we can then train machine learning models to predict various aspects of milk quality. 

    """, unsafe_allow_html=True)