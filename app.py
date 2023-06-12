import streamlit as st
import math 
import numpy as np
from streamlit_option_menu import option_menu
import scipy.stats as stats 

with st.sidebar : 
    selected = option_menu ('Distribution',
    ['Distribution T-Student',  
     'Distribution F'], 
    default_index=0)
 
if (selected == 'Distribution T-Student'):
    st.title('Distribution T-Student')

    sample_mean = st.number_input ("Masukkan nilai rata - rata sampel (Mean)", )
    population_mean = st.number_input ("Masukkan nilai rata - rata populasi (Mean)", )
    sample_std = st.number_input ("Masukkan simpangan baku sampel", )
    n = st.number_input ("Masukkan jumlah data", )
    hitung = st.button ("Hitung nilai t-score")

    t_score = ("Masukkan nilai t-score", )
    df = st.number_input ("Masukkan derajat kebebasan (n)")
    hitung = st.button ("Hitung Distribusi T-Student")

    if hitung : 
        hasil_t_score = (sample_mean - population_mean) / (sample_std / math.sqrt(n))
        st.write ("Nilai t-Score", hasil_t_score)

        hasil_p_value = stats.t.sf(abs(t_score), df) * 2 
        st.write ("Nilai P-Value", hasil_p_value)

if (selected == 'Distribution F'):
    st.title('Distribution F')

    variance_1 = st.number_input ("Masukkan nilai varaince group 1", )
    variance_2 = st.number_input("Masukkan nilai variance group 2", )
    hitung_2 = st.button ("Menghitung F statistik")

    f_stat = st.number_input ("Masukkan nilai F statistik", )
    df1 = st.number_input("Masukkan jumlah nilai group 1 (n-1)", 0)
    df2 = st.number_input("Masukkan jumlah nilai group 2 (n-1)", 0)
    hitung = st.button ("Menentukan derajat bebas group")

    if hitung : 
        f_stat = variance_1/variance_2
        st.write ("Menghitung F statistik", f_stat)

        p_value = 1 - stats.f.cdf(f_stat, df1, df2)
        st.write ("Menghitung nilai P-Value", p_value)
    