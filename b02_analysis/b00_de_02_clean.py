import pandas as pd
from pathlib import Path
from multiprocessing import Pool

#------------------------------------------------
fd_out='./out/b00_de_02_clean'
fd_in='./out/b00_de_01_de'

##########################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)
l_fname=list(Path(fd_in).glob('*.csv'))

#------------------------------------------------
def mainf(fname):
    name=Path(fname).stem
    df=pd.read_csv(fname, index_col=0)
    
    #clean
    df=df.dropna()
    df=df.loc[:, ['log2FoldChange', 'padj']]
    df.columns=['logfc', 'p']
    
    df.to_csv(f'{fd_out}/{name}.csv')
    return

#-----------------------------------------------
with Pool() as p: p.map(mainf, l_fname)
