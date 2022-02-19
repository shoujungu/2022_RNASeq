import pandas as pd
from pathlib import Path
from multiprocessing import Pool

#------------------------------------------
fc=3 #min fold change

fd_out='./out/b03_go_00_gene'
fd_in='./out/b01_convert-gene_01_convert'

#####################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)
l_fname=list(Path(fd_in).glob('*.csv'))

#------------------------------------------
def mainf(fname):
    name=Path(fname).stem
    df=pd.read_csv(fname, index_col=0)
    #filter by fc
    df=df.loc[df['logfc']>fc, :]
    #save gene list
    Path(f'{fd_out}/{name}.txt').write_text('\n'.join(df.index.tolist()))
    return

#------------------------------------------
with Pool() as p: p.map(mainf, l_fname)
