import pandas as pd
import scanpy as sc
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from multiprocessing import Pool
from scipy.stats import zscore

#------------------------------------------------
n=20  #number of genes to plot

fd_out='./out/c00_wilco_02_heatmap'
fd_in='./out/c00_wilco_01_wilco'
f_cnt='/home/shoujun/Desktop/b01_tmp/z00/b01_align/out/a00_star_02_count/count.csv'

#########################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)

#load
ada=sc.read(f'{fd_in}/ada.h5ad')
df_cnt=pd.read_csv(f_cnt, index_col=0)
df_gene=pd.read_csv(f'{fd_in}/gene.csv')

#------------------------------------------------
def plt_hm(df, f_out, sz=(8,7)):
    #plot
    fig, ax=plt.subplots(figsize=sz)
    sns.despine()
    ax=sns.heatmap(df, vmin=-2, vmax=2, cmap='coolwarm', linewidths=0.1)
    
    #adjust
    ax.xaxis.tick_top()
    plt.xticks(fontsize=11, rotation=90, weight='semibold')
    plt.yticks(fontsize=11, rotation=0, weight='semibold')
    plt.ylabel('')
    
    #save
    plt.tight_layout()
    plt.savefig(f_out, dpi=300)
    plt.close()    
    return


def mainf(sample, n=n):
    #get genes
    l_gene=df_gene[sample].tolist()[:n]
    
    #get gene id
    df_tmp=ada.var.reindex(l_gene)
    l_id=df_tmp['gene_id'].tolist()
    
    #get count table
    df=df_cnt.reindex(l_id) 
    df.index=l_gene
    
    #zscore scale
    df=df.apply(zscore, axis=1)

    #plot
    f_out=f'{fd_out}/{sample}.png'
    plt_hm(df, f_out)
    return


#------------------------------------------------
l_sample=ada.obs['sample'].unique().tolist()
#with Pool() as p: p.map(mainf, l_sample)

mainf('MFPA')
