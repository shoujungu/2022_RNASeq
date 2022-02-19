import scanpy as sc
import pandas as pd
from pathlib import Path

#--------------------------------------------
fd_out='./out/c00_wilco_01_wilco'
f_in='./out/c00_wilco_00_ada.py/ada.h5ad'

###################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)
ada=sc.read(f_in)

#-------------------------------------------
#noirmalize
sc.pp.normalize_total(ada)
sc.pp.log1p(ada)

#wilcoxon
sc.tl.rank_genes_groups(ada, 'sample', method='wilcoxon', pts=True)
ada.write(f'{fd_out}/ada.h5ad')

#make df
df_name=pd.DataFrame(ada.uns['rank_genes_groups']['names'])
df_name.to_csv(f'{fd_out}/gene.csv', index=False)

df_score=pd.DataFrame(ada.uns['rank_genes_groups']['scores'])
df_score.to_csv(f'{fd_out}/score.csv', index=False)

df_pts=pd.DataFrame(ada.uns['rank_genes_groups']['pts'])
df_pts.to_csv(f'{fd_out}/pts.csv', index=False)

df_pval=pd.DataFrame(ada.uns['rank_genes_groups']['pvals_adj'])
df_pval.to_csv(f'{fd_out}/pval.csv', index=False)

