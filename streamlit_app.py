import streamlit

streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('\N{blueberries}\N{bowl with spoon} Omega 3 & Blueberry Oatmeal')
streamlit.text('\N{leafy green}\N{rocket} Kale, Spinach & Rocket Smoothie')
streamlit.text('\N{chicken}\N{egg} Hard-Boiled Free-Range Egg')
streamlit.text('\N{avocado}\N{bread} Avocado Toast')

streamlit.header('\N{banana}\N{strawberry} Build Your Own Fruit Smoothie \N{kiwifruit}\N{mango}')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
                      
#display the table on the page
streamlit.dataframe(my_fruit_list)
