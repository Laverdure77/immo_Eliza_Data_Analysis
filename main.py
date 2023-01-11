import numpy as np
import pandas as pd
#_____________________________________________________________________________

from scripts.colors import bcolors as bc
#_____________________________________________________________________________
file = './datas/Immoweb_data_ok_maite.csv'
data = pd.read_csv(file)
data.head()
