import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Mom\'s New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale,Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#let's pick a fruit list here so they can pick fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display the table on the page
streamlit.dataframe(fruits_to_show)

#import requests
#fruitvice_response=requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruitvice_response.json())--------------------to delete the line
#fruitvice_normalized=pandas.json_normalize(fruitvice_response.json())
#streamlit.dataframe(fruitvice_normalized)

'''
streamlit.header('fruityvice fruit Advice!')
fruit_choice = streamlit.text_input('what fruit would you like information about?','Kiwi')
streamlit.write('The user entered', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruitvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruitvice_normalized)'''


''' streamlit.header('Fruity Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("please select a fruit to get the information.")
  else:
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
     fruitvice_normalized=pandas.json_normalize(fruityvice_response.json())
     streamlit.dataframe(fruitvice_normalized)
except URLError as e:
    streamlit.error() '''
''' def get_fruityvice_data(this_fruit_choice):
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
     fruitvice_normalized=pandas.json_normalize(fruityvice_response.json())
     return fruitvice_normalized

streamlit.header('Fruity Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
        streamlit.error("please select a fruit to get the information.")
  else:
        back_from_function =get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error() '''
    
def get_fruit_load_list():
   with my_cnx.cursor as my_cur:
         my_cur.execute("select * from FRUIT_LOAD_LIST")
         return my_cur.fetchall()
if streamlit.button('get fruit load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows=get_fruit_load_list()
    streamlit.dataframe(my_data_rows)
    
 
        

#streamlit.stop()
#import snowflake.connector


