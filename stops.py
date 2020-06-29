'''
This program checks if models reached part 3 of evolution. Models that failed will have their mass and z printed to screen.
'''

import os
import numpy as np

mass = [0, 1, 2, 3, 4, 5, 6, 7]
m = np.arange(0.25, 8, 0.25)
z = [0.014, 0.017, 0.02, 0.023, 0.026]

for i in mass:
	for j in m:
		if j < i:
			print()
		elif j < i + 1 and j >= i:
			print()
			for k in z:
				if os.path.exists(str(i) + "M/WD_" + str(j) + "_M_" + str(k) + "_Z/controls/LOGS_part1/history.data") and os.path.exists(str(i) + "M/WD_" + str(j) + "_M_" + str(k) + "_Z/controls/LOGS_part2/history.data") and os.path.exists(str(i) + "M/WD_" + str(j) + "_M_" + str(k) + "_Z/controls/LOGS_part3/history.data"):
					os.system("cd ..")
				else:
					print(j, k)
					os.system("cd ..")
		else:
			os.system("cd ..")
	os.system("cd ..")
