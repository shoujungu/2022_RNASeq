import pandas as pd
from pathlib import Path

#-----------------------------------------
fd_out='./out/b00_de_00_pp'
fd_in='/home/shoujun/Desktop/b01_tmp/z00/b01_align/out/a00_star_02_count'

#################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)

#load
df_cnt=pd.read_csv(f'{fd_in}/count.csv', index_col=0)
df_meta=pd.read_csv(f'{fd_in}/meta.csv', index_col=0)

#------------------------------------------
def de_pp(l_sample1, l_sample2, name):
    Path(f'{fd_out}/{name}').mkdir(exist_ok=True, parents=True)
    l_sample=l_sample1+l_sample2

    #design table
    dfi_meta=df_meta.loc[df_meta['sample'].isin(l_sample), :].copy()
    dfi_meta.to_csv(f'{fd_out}/{name}/meta.csv')

    #count table
    dfi_cnt=df_cnt.reindex(dfi_meta['sample_id'], axis=1)
    dfi_cnt.to_csv(f'{fd_out}/{name}/count.csv')
    return

#------------------------------------------
# ctrl - treated
name='Ctrl_Treated'
l_sample1=['MFL', 'MFN']
l_sample2=['MFPA']
de_pp(l_sample1, l_sample2, name)

# MFL - MFN
name='MFL_MFN'
l_sample1=['MFL']
l_sample2=['MFN']
de_pp(l_sample1, l_sample2, name)

# MFL - MFPA
name='MFL_MFPA'
l_sample1=['MFL']
l_sample2=['MFPA']
de_pp(l_sample1, l_sample2, name)

# MFN - MFPA
name='MFN_MFPA'
l_sample1=['MFN']
l_sample2=['MFPA']
de_pp(l_sample1, l_sample2, name)


