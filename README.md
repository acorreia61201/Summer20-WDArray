These programs and the two MESA presets, "1M_pre_ms_to_wd" and "make_co_wd", are used to create an array of models that evolve low-mass stars from main sequence to white dwarfs. Two presets are used to accommodate temperature and timestep issues throughout the desired mass range. 1M_pre_ms_to_wd is used to evolve stars below 1.5 M_sun, while make_co_wd is used to evolve the rest of the stars. Both presets have been edited to be compatible with variable metallicities by using 'create_pre_main_sequence_model = .true.' as well as to allow for editing and copying via Python.

create_directories.py copies the presets several times, each time assigning mass and z values within the mass range 0.25 to 7.75 M_sun and the z range 0.14 to 0.26. This program also organizes these directories by mass and copies a job.mpi script into each mass directory, again editing the name of the output and error files to match the given directory.

The directories are run in parallel on the CARNIE supercomputer with the use of three scripts. submit_jobs.py is run from the main directory and submits each of the job.mpi scripts in the mass directories. These job.mpi scripts, once submitted to CARNIE, then run the Python script execute_runs.py, which uses the ./rn command in each of the individual model directories.

flash_input.py is a script that converts the output of each model, "part3.mod", to a format friendly for FLASH. This script will be copied to each of the model directories and run from each.

stops.py is a script that can be run after the models have finished that reports the mass and metallicity of each model that did not complete.

More work will be required to resolve failed models in the array. Higher mass models (>7M) will run on either make_o_ne_wd or make_he_wd, and a resolution will have to be found for other groups of models that did not complete (i.e. 3M, 1.25M, and 1.5M).
