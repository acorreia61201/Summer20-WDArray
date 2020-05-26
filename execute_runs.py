'''
This script will run through the slurm script "job.mpi," which is found in each of the mass directories. When executed, this script will run each of the models
found within the set.
'''

import os

models = [f for f in os.listdir('.') if os.path.isdir(f)]

#cd to each model within the set
for model in models:
	os.chdir(model)
	os.chdir("controls")

#run the model and cd back to the set directory
	os.system("./rn")
	os.chdir("../..")
		
