import pandas as pd
from pathlib import Path

#-----------------------------------------------
fd_out='./out/a00_star_02_count'
fd_in='./out/a00_star_01_align'
f_meta='/home/shoujun/Desktop/b01_tmp/z00/a00_raw/SraRunTable.txt'

#########################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)
df_meta=pd.read_csv(f_meta, index_col=0)

#-----------------------------------------------
#clean treatment column
df_meta=df_meta.loc[:, ['Sample Name', 'treatment']]
df_meta['condition']=df_meta['treatment'].map(lambda x: 'Treated' if ('Punicalagin' in x) else 'Ctrl')

#clean sample name
df_meta['sample']=df_meta['Sample Name'].str[0:-2]

#clean and save  meta
df_meta=df_meta.drop('treatment', axis=1)
df_meta.columns=['sample_id', 'condition', 'sample']
df_meta=df_meta.sort_values('sample_id')
df_meta.to_csv(f'{fd_out}/meta.csv')

#----------------------------------------------
#collect individual counts
l_df=[]
for srr in df_meta.index:
    col=df_meta['sample_id'][srr]
    
    #load counts
    df=pd.read_csv(f'{fd_in}/{srr}ReadsPerGene.out.tab', sep='\t', header=None)
    df.columns=['gene_id', col, '2', '3']
    
    #clean df
    df=df.loc[df['gene_id'].str.contains('ENSG'), ['gene_id', col]]
    df=df.set_index('gene_id')
    
    l_df.append(df)


#make count table
df=pd.concat(l_df, axis=1)
df=df.fillna(0)


#remove gene with 0 counts
df=df.loc[df.sum(axis=1)>0, :]
df.to_csv(f'{fd_out}/count.csv')


