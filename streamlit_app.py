# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(f":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")


name_on_order = st.text_input('Name on Smoothie:')
st.write('The name on your Smoothie will be:', name_on_order)

st.write(
  """Choose the fruits you want in your custom Smoothie!
  """
)

cnx =  st.connection('snowflake')
session = cnx.session()

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    'Choose up to 5 ingredients:',
    my_dataframe
)

#new section to display smoothie froot nutrition info
import requests
smoothiefroot_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(smoothiefroot_response)
