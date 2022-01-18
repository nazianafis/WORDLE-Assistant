import streamlit as st
import nltk
from nltk.corpus import words

st.title("WORDLE Assistant")
st.image("wordle-1.jpg")

@st.cache 
def download():
    nltk.download("words")
download()

five_letters = [word for word in words.words() if len(word)==5]

st.markdown("### Inclusion Letters")
inclusions = st.text_input(label="Type in the letters in green/yellow:")

st.markdown("### Exclusion Letters")
exclusions = st.text_input(label="Type in the letters in grey:")

if (len(inclusions) != 0 or len(exclusions) != 0):
    st.markdown("## List of All Possible Words")
    clue_result=[]
    for word in five_letters:
        if all(c in word for c in inclusions)and not any(c in word for c in exclusions):
            clue_result.append(word)
    st.write(clue_result)
