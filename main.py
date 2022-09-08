import pandas as pd
import streamlit as st
st.header("house rent predication")
df = pd.read_csv('House_Rent_Dataset.csv')
st.write(df)
genre = st.radio(
     "What's your favorite movie genre",
     ('a', 'b', 'c'))
if genre == 'a':
    st.table(df)
    st.write('now u can see the table')
elif genre == 'b':
    st.bar_chart(data=df, x='City', y='Rent', width=0, height=0, use_container_width=True)
    st.write('your analysis is ready based on city')
elif genre == 'c':
    st.line_chart(data=df, x='City', y='Size', width=0, height=0, use_container_width=True)
    st.write('your analysis is ready based on size')
else:
    st.write('get out')
