import pandas as pd
from pathlib import Path
from multiprocessing import Pool

#----------------------------------------
p=0.05 
fc=1

fd_out='./out/b00_de_04_filter'
fd_in='./out/b00_de_02_clean'

######################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)
l_fname=list(Path(fd_in).glob('*.csv'))

#-----------------------------------------
def mainf(fname):
    name=Path(fname).stem
    df=pd.read_csv(fname, index_col=0)
    
    #filter genes and split df
    df=df.loc[df['p']<p, :]
    df_up=df.loc[df['logfc']>fc, :].copy()
    df_down=df.loc[df['logfc']<-fc, :].copy()

    #filter by logfc
    df_up=df_up.sort_values('logfc', ascending=False)
    df_down['logfc']=-df_down['logfc']
    df_down=df_down.sort_values('logfc', ascending=False)
    
    #save
    df_up.to_csv(f'{fd_out}/{name}_up.csv')
    df_down.to_csv(f'{fd_out}/{name}_down.csv')
    return

#-----------------------------------------
with Pool() as p: p.map(mainf, l_fname)

