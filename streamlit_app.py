import streamlit
import pandas
streamlit.title("my parents new healthy dinnar")
streamlit.header("breakfast menu")
streamlit.text(" 🥣 omega 3 and Blueberry Oatmeal")
streamlit.text(" 🥬 kale spinach and rocket smoothie")
streamlit.text(" 🥚 hard boiled free range Egg")
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruit_selected=streamlit.multiselect("select any fruit from list : ",list(my_fruit_list.index),['Banana','Avocado'])
fruits_to_show=my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruits_to_show)

