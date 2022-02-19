from pathlib import Path
import pandas as pd
import random
from multiprocessing import Pool

#-----------------------------------------------------------------
up=1000    #upstream size
down=0     #downstream size
n_ctrl=3
n=500      #number of  genes used

fd_out='./out/d00_motif_01_bed'
fd_in='./out/b01_convert-gene_01_convert'
f_ref=f'./out/d00_motif_00_promoter/ref.csv'
f_table='./out/b01_convert-gene_00_table/gene_name.csv'

##########################################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)
df_ref=pd.read_csv(f_ref, index_col=0)
df_table=pd.read_csv(f_table, index_col=0)

#-----------------------------------------------------------------
def mainf(l_gl, name):
    #pp
    df=df_ref.loc[df_ref.index.isin(l_gl), :].copy()
    #make bed
    l_col=['gene', 'chr', 'start', 'end', 'strand']
    l_data=[]
    for gene, row in df.iterrows():
    	try:
    		chro=row['seqid']
    		strand=row['strand']
    		if strand=='+':
    			end=row['start']+down
    			start=row['start']-up
    		elif strand=='-':
    			start=row['end']-down
    			end=row['end']+up
    		else:
    			continue
    		l_data.append((gene, chro, start, end, strand))
    	except Exception as e:
    		print(str(e))
    df=pd.DataFrame(l_data, columns=l_col)
    df=df.loc[df['chr']!='chrM', :]
    #save
    df=df.set_index('gene')
    df=df.loc[~df.index.duplicated(), :]
    df.to_csv(f'{fd_out}/{name}.csv')
    return


#------------------------------------------------------------------
#get genes
df_up=pd.read_csv(f'{fd_in}/Ctrl_Treated_up.csv', index_col=0)
l_up=df_up.index.tolist()[0:n]

df_down=pd.read_csv(f'{fd_in}/Ctrl_Treated_down.csv', index_col=0)
l_down=df_down.index.tolist()[0:n]

l_gene=l_up+l_down

#get random ctrl  genes
l_ctrl=[random.choices(df_table['gene_name'].tolist(), k=n*2) for i in range(n_ctrl)]

#make bed file
l_name=[f'ctrl_{i}' for i in range(n_ctrl)]+['de']
l_ctrl.append(l_gene)

l_param=zip(l_ctrl, l_name)
with Pool() as p: p.starmap(mainf, l_param)


