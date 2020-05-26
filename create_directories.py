'''
This script is run manually from a directory containing a master directory with the necessary variables and modifications for duplication. When executed, 
this script will make directories for every desired model and copy the make_co_wd directory into each, with modifications made by use of string.Template. These
individual models will then be organized by mass into mass directories, and a job.mpi script will be copied into each mass directory.
'''

import os
import numpy as np
from string import Template

mass_list = np.arange(0.25, 8, 0.25)
Z_list = [0.014, 0.017, 0.020, 0.023, 0.026]

for mass in mass_list:
	for Z in Z_list:
		#make a directory titled by mass and Z
		os.mkdir("WD_" + str(mass) + "_M_" + str(Z) + "_Z")

		#copy master 1M to each new directory
		os.system("cp -rf make_co_wd WD_" + str(mass) + "_M_" + str(Z) + "_Z/controls")

		#cd to each directory
		os.chdir("WD_" + str(mass) + "_M_" + str(Z) + "_Z")
		os.chdir("controls")

		#substitute the variables $mass and $z with the mass and Z values from the string
                d = {'mass':mass, 'z':Z}

                #inlist_common
                filein = open("/home/acorreia7/make_co_array/make_co_wd/inlist_common")
                src = Template(filein.read())
                result = src.substitute(d)
                out_inlist = open("inlist_common", "w")
                out_inlist.write(result)
                out_inlist.close()

		#cd back to the initial directory to continue the loop
		os.chdir("../..")

#organize directories into parent directories by mass
for i in range(0, 8):
	os.mkdir(str(i) + "M")
	os.system("mv WD_" + str(i) + "* " + str(i) + "M")

#copy the sbatch script into each parent directory
dir_list = [0M, 1M, 2M, 3M, 4M, 5M, 6M, 7M]

for dir in dir_list:
	#copy the job.mpi template from the project directory into each mass directory
	os.system("cp job.mpi " + str(dir)) 
	
	#cd to each mass directory and edit the $dir variable in the template
	os.system("cd " + str(dir))
	d = {'dir':dir}
	filein = open("job.mpi")
	src = Template(filein.read())
	result = src.substitute(d)
	out = open("job.mpi", "w")
	out.write(result)
	out.close()

	#continue the loop
	os.system("cd ..")
