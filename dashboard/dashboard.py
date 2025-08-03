import streamlit as st
import pandas as pd
from pydantic import BaseModel, parse_obj_as
import requests


response =  requests.get('http://127.0.0.1:8000/dash/wines')
data = response.json()
df = pd.DataFrame(data['wines'])

st.write("""My first app: Hello World""")
st.dataframe(df, hide_index=True)
