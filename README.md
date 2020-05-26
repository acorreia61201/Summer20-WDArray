This white dwarf array is based on the MESA preset make_co_wd, which allows for a much wider spectrum of initial masses to be evolved. The make_co_wd given has been edited to be compatible with variable metallicities by using 'create_pre_main_sequence_model = .true.' as well as allowing for editing and copying via Python.

create_directories.py copies the make_co_wd preset several times, each time assigning mass and z values within the mass range 0.25 to 7.75 M_sun and the z range 0.14 to 0.26. This program also organizes these directories by mass and copies a job.mpi script into each mass directory, again editing the name of the output and error files to match the given directory.

The directories are run in parallel with the use of three scripts. submit_jobs.py is run from the main directory and submits each of the job.mpi scripts in the mass directories. These job.mpi scripts, once submitted to CARNIE, then run the Python script execute_runs.py, which uses the ./rn command in each of the individual model directories.

cat_data.py is a script to be used once all of the models have completed or stopped. This program does a preliminary check for completion of any given model by searching for the second and third history.data files. If one or both are missing, the program will add to a counter that displays how many models failed and will continue the loop. If both are present, however, the program will concatenate the history.data files into a complete history file for the model.

plotHR.py is a rudimentary script that defines a function "plot", which uses mesa_reader to plot an HR diagram from a given concatenated history file.
