'''
Run this from the directory containing all of your sets (i.e. 0M to 7M)
'''

import os

sets = ["0M", "1M", "2M", "3M", "4M", "5M", "6M", "7M"]

# run each sbatch script
for set in sets:
	os.chdir(set)
	os.system("sbatch job.mpi")
	os.chdir("..")
