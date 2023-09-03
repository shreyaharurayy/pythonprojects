import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from colorama.ansi import set_title


def quad_plot(a, b, c ):
    x = np.linspace(-10, 10)
    y = a * x ** 2 + b * x + c
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    set_title(f"Quadratic Equation:{a}x**2 + {b}x + {c}")

    st.pyplot(fig)


def main():
    st.title("Math visualisation:Quadreatic Equation")
    st.sidebar.header("Quadratic sidebar equations")
    a = st.sidebar.slider("Coefficeint a",-10,10,0)
    b = st.sidebar.slider("Coefficient b",-10,0,10)
    c = st.sidebar.slider("Coefficient c",-10,0,10)
    quad_plot(a,b,c)
if __name__=="__main__":
    main()




