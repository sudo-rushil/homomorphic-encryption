#!/usr/bin/env python

import streamlit as st

from pve import *
import numpy as np


st.set_page_config(layout="wide") 
st.title('Pair Value Encryption Demonstration')

st.sidebar.title("Input Panel")