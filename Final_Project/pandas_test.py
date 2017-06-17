import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

xray_data = pd.read_csv('Data/GOES_xray_flux/g15_xrs_2s_20120307_20120307.csv', skiprows=138, header=0)

print(xray_data)