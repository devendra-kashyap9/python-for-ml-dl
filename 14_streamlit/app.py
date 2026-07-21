### to run stramlit app
# CMD streamlit run app.py  i.e.<name_of_file>

import streamlit as st
import pandas as pd
import numpy as np

# Title of the application
st.title("Hello Streamlit")

# Display simple text
st.write("This is a Simple text line.")

# create a DataFrame
df = pd.DataFrame({
    "first Column": [1,2,3,4],
    "Seocnd Column": [10,20,30,40]
})

# display the dataframe
st.write("This is our DataFranme")
st.write(df)

# create line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a', 'b', 'c']
)
st.line_chart(chart_data)