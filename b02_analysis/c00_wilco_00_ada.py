import pandas as pd
import scanpy as sc
import anndata as ad
from pathlib import Path

#-------------------------------------
fd_out='./out/c00_wilco_00_ada.py'
f_cnt='/home/shoujun/Desktop/b01_tmp/z00/b01_align/out/a00_star_02_count/count.csv'
f_table='./out/b01_convert-gene_00_table/gene_name.csv'

##############################################
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_cnt, index_col=0)
df_table=pd.read_csv(f_table, index_col=0)

#-------------------------------------
#convert gene name
df=df.merge(df_table, left_index=True, right_index=True)

#convert to  adata
df=df.reset_index()
df=df.set_index('gene_name')
df=df.loc[~df.index.duplicated(), :]

var=df.loc[:, ['gene_id']].copy()
df=df.drop('gene_id', axis=1)

df=df.T
ada=ad.AnnData(df, var=var)

ada.obs['sample']=ada.obs.index.str[:-2]
ada.obs['sample']=pd.Categorical(ada.obs['sample'], categories=['MFL', 'MFN', 'MFPA'], ordered=True)

#save
ada.write(f'{fd_out}/ada.h5ad')

