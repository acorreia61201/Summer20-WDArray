'''
This program creates model directories varied by mass and metallicity (z). Lower mass models use 1M_pre_ms_to_wd, while higher mass models use make_co_wd. In the
future, extra functionality will be added to make the highest mass models run on make_o_ne_wd or make_he_wd. The individual directories are then organized into
mass directories, and these mass directories are placed into a "models" directory.
'''

import os
import numpy as np
from string import Template

#create an array using the low-mass suitable 1M_pre_ms_to_wd and the higher-mass suitable make_co_wd

#1M_pre_ms_to_wd
mass_list = np.arange(0.25, 1.75, 0.25)
Z_list = [0.014, 0.017, 0.020, 0.023, 0.026]

for mass in mass_list:
	for Z in Z_list:
		#make a directory titled by mass and Z
                os.mkdir("WD_" + str(mass) + "_M_" + str(Z) + "_Z")

                #copy master model to each new directory
                os.system("cp -rf 1M_pre_ms_to_wd WD_" + str(mass) + "_M_" + str(Z) + "_Z/controls")

                #cd to each directory
                os.chdir("WD_" + str(mass) + "_M_" + str(Z) + "_Z")

                #cp flash_input.py and change directores to controls
                os.system("cp ../flash_input.py .")
                os.chdir("controls")

		#substitute the variables $mass and $z with the mass and Z values from the string
                d = {'mass':mass, 'z':Z}

                #inlist_start
                filein = open("/home/acorreia7/make_co_array/1M_pre_ms_to_wd/inlist_start")
                src = Template(filein.read())
                result = src.substitute(d)
                out_inlist = open("inlist_start", "w")
                out_inlist.write(result)
                out_inlist.close()

 		#inlist_to_end_agb 
                filein = open("/home/acorreia7/make_co_array/1M_pre_ms_to_wd/inlist_to_end_agb")
                src = Template(filein.read())
                result = src.substitute(d)
                out_inlist = open("inlist_to_end_agb", "w")
                out_inlist.write(result)
                out_inlist.close()

		#inlist_to_wd
                filein = open("/home/acorreia7/make_co_array/1M_pre_ms_to_wd/inlist_to_wd")
                src = Template(filein.read())
                result = src.substitute(d)
                out_inlist = open("inlist_to_wd", "w")
                out_inlist.write(result)
                out_inlist.close()

                #cd back to the initial directory to continue the loop
                os.chdir("../..")

#make_co_wd
mass_list = np.arange(1.75, 8, 0.25)
Z_list = [0.014, 0.017, 0.020, 0.023, 0.026]

for mass in mass_list:
	for Z in Z_list:
		#make a directory titled by mass and Z
		os.mkdir("WD_" + str(mass) + "_M_" + str(Z) + "_Z")

		#copy master model to each new directory
		os.system("cp -rf make_co_wd WD_" + str(mass) + "_M_" + str(Z) + "_Z/controls")

		#cd to each directory
		os.chdir("WD_" + str(mass) + "_M_" + str(Z) + "_Z")

		#cp flash_input.py and change directores to controls
                os.system("cp ../flash_input.py .")
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
dir_list = ['0M', '1M', '2M', '3M', '4M', '5M', '6M', '7M']

for dir in dir_list:
	#copy the job.mpi template and cat_data.py from the project directory into each mass directory
	os.system("cp job.mpi " + dir)
	os.system("cp cat_data.py " + dir) 
	
	#cd to each mass directory and edit the $dir variable in the template
        os.chdir(dir)
	d = {'dir':dir}
	filein = open("job.mpi")
	src = Template(filein.read())
	result = src.substitute(d)
	out = open("job.mpi", "w")
	out.write(result)
	out.close()

	#continue the loop
	os.chdir("..")

#put the mass directories into a larger project directory for organization
os.mkdir("models")
os.system("mv *M models")
