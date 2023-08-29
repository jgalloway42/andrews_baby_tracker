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
