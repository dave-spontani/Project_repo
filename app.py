import streamlit as st
from Feature_01 import return_even
from Feature_02 import return_odd
import random

original_list = [i for i in range(10)]

even_list = return_even(original_list)

odd_list = return_odd(original_list)

st.write("Hooray, we connected everything")

st.write("Hello_02")

st.write(even_list)

st.write(odd_list)

st.write("A short demonstration of why list comprehensions are superior!")

st.write(random.randint(0,20))