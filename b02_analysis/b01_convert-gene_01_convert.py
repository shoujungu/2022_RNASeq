import pandas as pd
from pathlib import Path
from multiprocessing import Pool

#-------------------------------------------
fd_out='./out/b01_convert-gene_01_convert'
fd_in='./out/b00_de_04_filter'
f_table='./out/b01_convert-gene_00_table/gene_name.csv'

#######################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)
df_table=pd.read_csv(f_table, index_col=0)
l_fname=list(Path(fd_in).glob('*.csv'))

#-------------------------------------------
def mainf(fname):
    name=Path(fname).stem
    df=pd.read_csv(fname, index_col=0)
    df=df.merge(df_table, left_index=True, right_index=True)
    
    #clean
    df.index.name='gene_id'
    df=df.reset_index()
    df=df.set_index('gene_name')
    df=df.loc[~df.index.duplicated(), :]
    df.to_csv(f'{fd_out}/{name}.csv')
    return

#------------------------------------------
with Pool() as p: p.map(mainf, l_fname)

