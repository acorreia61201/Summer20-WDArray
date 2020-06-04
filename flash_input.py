'''
This program converts the output from MESA to a format that is able to be read by FLASH.
'''

import pandas as pd
import numpy as np
import os

#copy the raw mesa output for editing
os.system("cp controls/part3.mod .")

#delete last few lines
os.system("head -n -8 part3.mod > output.csv")

#replace the "D" used by mesa for scientific notation with "E" in a new output file:
f = open("output.csv", 'r')
filedata = f.read()
f.close()
newdata = filedata.replace("D", "E")
f = open("output.csv", 'w')
f.write(newdata)
f.close()

#read the required columns in the new output file
data = pd.read_csv("output.csv", skiprows = 16, usecols = [0, 1, 2, 3, 11, 16], sep = '   ', engine = 'python')
df = pd.DataFrame(data)

#revert ln operator on lnR, lnT, and lnd columns
df1 = df.apply(lambda x: np.exp(x) if x.name == 'Unnamed: 1' else x)
df2 = df1.apply(lambda x: np.exp(x) if x.name == 'Unnamed: 2' else x)
df3 = df2.apply(lambda x: np.exp(x) if x.name == 'Unnamed: 3' else x)

#apply these changes to a new file
df3.to_csv('input.csv', sep = ',')

#edit input.csv to be more intuitive
os.system("sed -i '1s/.*/#zone,lnd,lnT,lnR,c12,ne22/' input.csv")

#remove intermediate files
os.system('rm part3.mod && rm output.csv')
