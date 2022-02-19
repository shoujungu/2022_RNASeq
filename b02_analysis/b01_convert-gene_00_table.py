#parse GTF to get gene name convert table

import pandas as pd
from pathlib import Path

#-------------------------------------------
fd_out='./out/b01_convert-gene_00_table'
f_in='/home/shoujun/Desktop/b01_tmp/z00/a01_tool/ref/gencode.v39.primary_assembly.annotation.gtf'

#################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in, comment='#', header=None, sep='\t')

#-------------------------------------------
#make table
l_data=[]

for _, row in df.iterrows():
    try:
        l_info=row[8].split(';')
        
        #gene id
        l_id=[i for i in l_info if 'gene_id' in i]
        gene_id=l_id[0].split('\"')[1]
        
        #gene name
        l_name=[i for i in l_info if 'gene_name' in i]
        gene_name=l_name[0].split('\"')[1]
    
        #append
        if gene_name!=gene_id.split('.')[0]:
            l_data.append((gene_id, gene_name))
    
    except Exception:
        continue

#concat to df
df=pd.DataFrame(l_data, columns=['gene_id', 'gene_name'])
df=df.drop_duplicates()
df=df.set_index('gene_id')

df.to_csv(f'{fd_out}/gene_name.csv')

