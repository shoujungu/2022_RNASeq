from pathlib import Path
import pandas as pd

#-----------------------------------------------------
name='de'  #file name of DE genes

fd_out='./out/d00_motif_03_clean'
fd_in='./out/d00_motif_02_fa/meme'

###############################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)

df=pd.read_csv(f'{fd_in}/{name}.tsv', sep='\t', comment='#', index_col=0)
df=df.loc[:, ['motif_ID', 'motif_alt_ID', 'adj_p-value']]

#---------------------------------------------------
#load ctrl
l_fname=list(Path(fd_in).glob(f'ctrl_*.tsv'))
l_df=[pd.read_csv(fname, sep='\t', comment='#', index_col=0) for fname in l_fname]
l_ctrl=[dfi['motif_ID'].tolist() for dfi in l_df]

#count motif
l_cnt=[sum([(motif in i) for i in l_ctrl]) for motif in df['motif_ID']]

#make df
df=df.loc[:, ['motif_ID', 'motif_alt_ID', 'adj_p-value']]
df['cnt']=l_cnt
df=df.sort_values('adj_p-value')

#save
df.to_csv(f'{fd_out}/{name}.csv')

dfi=df.loc[df['cnt']==0, :]
dfi.to_csv(f'{fd_out}/{name}_uniq.csv')
