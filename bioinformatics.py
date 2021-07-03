import pandas as pd 
import streamlit as st  
import altair as alt 
from PIL import Image

#################
#Page Title
#################

image = Image.open("logo.png")

st.image(image, use_column_width=True)

st.write("""
    # DNA Nucleotide Count Web App

    This app counts the nucleotide composition of query DNA

    ***
    """)


#################
# Input Text Box
#################

st.header('Enter DNA Sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()

sequence = sequence[1:]
sequence

sequence  = ''.join(sequence)

st.write("""
***
    """)

#Prints the input DNA sequence
st.header('INPUT (DNA QUERY)')

sequence  

#DNS nucletide count
st.header('OUTPUT (DNA Nucleotide count)')

#1. Print Dictionary
st.subheader('1. Print Dictionary')

def DNA_nucletide_count(seq):
    d = dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C'))
        ])

     return d

X = DNA_nucletide_count(sequence)

X_label = list(X)
X_values = list(X.values())


 