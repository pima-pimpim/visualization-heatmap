import streamlit as st
import pandas as pd
from io import StringIO

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide")

st.title("Visualization Heatmap")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    #bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)

    # To convert to a string based IO:
    #stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #st.write(stringio)

    # To read file as string:
    #string_data = stringio.read()
    #st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    try:
        dataframe = pd.read_csv(uploaded_file)
    except:
        dataframe = pd.read_excel(uploaded_file)
    st.markdown(dataframe.head())


#option = st.selectbox(
#    'Please select a criteria',
#    ('gender', 'age_group', 'bmi_group', 'region'))
#
#st.write('You criteria:', option)
#
##show_btn = st.button("Display!")
##if show_btn:
#for i in ('gender', 'age_group', 'bmi_group', 'region'):
#    if i in option:
#        # Create distplot with custom bin_size
#        fig = px.pie(region[option].value_counts(), values=region[option].value_counts().values, names=region[option].value_counts().index)
#        fig.update_traces(hoverinfo='label+value', textinfo='label+value+percent')
#
#        # Plot!
#        st.plotly_chart(fig)
#
#st.markdown("Last updated: Nov 19, 2024.")