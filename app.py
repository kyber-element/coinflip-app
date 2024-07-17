import streamlit as st
import random

st.header('Tossing a Coin')

st.write('It is not a functional application yet. Under construction.')

def flip_coin():
    return 'Heads' if random.randint(0, 1) == 0 else 'Tails'

if __name__ == "__main__":
    result = flip_coin()
    print(result)