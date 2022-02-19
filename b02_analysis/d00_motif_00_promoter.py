from pathlib import Path
import pandas as pd

#---------------------------------------------------
fd_out='./out/d00_motif_00_promoter'
f_in='/home/shoujun/Desktop/b01_tmp/z00/a01_tool/ref/gencode.v39.primary_assembly.annotation.gff3'
l_col=['seqid', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes']

#--------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)

############################################################
#load df
df=pd.read_csv(f_in, comment='#', sep='\t', header=None)
df.columns=l_col

#filter
df=df.loc[df['type']=='gene', :]
df['gene']=df['attributes'].apply(lambda x: x.split('gene_name=')[-1].split(';')[0])
df=df.loc[:, ['gene', 'seqid', 'start', 'end', 'strand']]

df.to_csv(f'{fd_out}/ref.csv', index=False)
