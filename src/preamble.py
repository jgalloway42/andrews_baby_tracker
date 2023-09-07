# Generic Jupyter Notebook Imports and Setup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

plt.style.use('ggplot')
plt.rcParams["figure.figsize"] = (15,5)
pd.set_option('display.max_columns',50)
np.set_printoptions(precision=3)


cwd = os.getcwd()
root_dir = os.path.abspath(os.path.join(cwd, os.pardir))
raw_data = os.path.join(root_dir,'data','raw')
processed_data = os.path.join(root_dir,'data','processed')
interim_data = os.path.join(root_dir,'data','interim')

def walk_directory(dir_to_walk,print_files = True):
    # print input files for dataset in raw data folder
    files_dict = {}   
    ignore = ['.gitkeep']
    for dirname, _, filenames in os.walk(dir_to_walk):     
        for filename in filenames:                      
            if filename in ignore:                              
                continue                      
            files_dict[filename.split('.')[0]] = os.path.join(dirname, filename)         
            if print_files:
                print(filename.split('.')[0],files_dict[filename.split('.')[0]])
    return files_dict