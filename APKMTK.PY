import streamlit as st
import sympy as sp

# Setup
x = sp.Symbol('x')

st.title("🧮 Kalkulator Integral & Turunan")

# Input fungsi
fungsi_input = st.text_input("Masukkan fungsi (gunakan x sebagai variabel)", value="x**2")

# Pilih operasi
operasi = st.selectbox("Pilih operasi:", ["Turunan", "Integral Tak Tentu", "Integral Tentu"])

try:
    fungsi = sp.sympify(fungsi_input)

    if operasi == "Turunan":
        turunan = sp.diff(fungsi, x)
        st.latex(r"f'(x) = " + sp.latex(turunan))

    elif operasi == "Integral Tak Tentu":
        integral_tak_tentu = sp.integrate(fungsi, x)
        st.latex(r"\int f(x)\,dx = " + sp.latex(integral_tak_tentu) + " + C")

    elif operasi == "Integral Tentu":
        a = st.number_input("Batas bawah (a)", value=0.0)
        b = st.number_input("Batas atas (b)", value=1.0)
        integral_tentu = sp.integrate(fungsi, (x, a, b))
        st.latex(r"\int_{" + str(a) + "}^{" + str(b) + "} " + sp.latex(fungsi) + r"\,dx = " + str(integral_tentu))

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")

