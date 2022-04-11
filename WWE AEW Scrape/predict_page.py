import streamlit as st
import pickle
import numpy as np


def show_predict_page():

    def load_model():
        model = pickle.load(open('test_review.pkl', 'rb'))
        return model

    model = load_model()

    st.image('stevevincew38.jpeg')

    st.title("Are You a Mark?")
    st.write(
        "Write a few words or sentences about the top two wrestling brands and see how you rank.")

    review = st.text_area('How do you feel about WWE (or AEW)?')

    submit_button = st.button('Submit Review')

    if submit_button:
        result, mark = model(review)
        st.write(result)
        st.subheader(mark)
