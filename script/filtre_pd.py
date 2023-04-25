import os 
import numpy as np
import pandas as pd
print("Pandas, version", pd.__version__)

from pathlib import Path
home = Path.home()
# print(home)

data = pd.read_csv(os.path.join(home, "Documents/Master_2/Projet_long/Flux_metabo/data/seurat_gene_exp.csv"))
mat = data.set_index(data['Unnamed: 0'],  verify_integrity = True)
red_mat = mat.iloc[ : , 1:]
print(red_mat.head())
print(red_mat.dtypes)

red_mat.to_csv(os.path.join(home, "Documents/Master_2/Projet_long/Flux_metabo/data/seurat_gene_exp_pd.csv"))
