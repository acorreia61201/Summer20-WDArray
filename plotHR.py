'''
This program defines a function that plots an HR diagram from a concatenated history file for make_co_wd.
'''

import mesa_reader as mr
import matplotlib.pyplot as plt

def plot(x):
	h = mr.MesaData(x)
	plt.plot(h.log_Teff, h.log_L)
	plt.gca().invert_xaxis()
	plt.xlabel('log Effective Temp')
	plt.ylabel('log Luminosity')
	plt.show()
