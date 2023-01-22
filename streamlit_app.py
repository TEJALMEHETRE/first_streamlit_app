import streamlit
import pandas
streamlit.title("my parents new healthy dinnar")
streamlit.header("breakfast menu")
streamlit.text(" 🥣 omega 3 and Blueberry Oatmeal")
streamlit.text(" 🥬 kale spinach and rocket smoothie")
streamlit.text(" 🥚 hard boiled free range Egg")
my_fruit_lists=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_lists=my_fruit_lists.set_index('fruit')
streamlit.multiselect("select any fruit from list : ",my_fruit_lists.index)
streamlit.dataframe(my_fruit_lists)
