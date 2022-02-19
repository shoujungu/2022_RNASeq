import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from multiprocessing import Pool
from scipy.stats import zscore

#------------------------------------------------
n=20

fd_out='./out/b02_de-plt_01_heatmap'
fd_in='./out/b01_convert-gene_01_convert'
f_cnt='/home/shoujun/Desktop/b01_tmp/z00/b01_align/out/a00_star_02_count/count.csv'

##########################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)
df_cnt=pd.read_csv(f_cnt, index_col=0)
l_fname=list(Path(fd_in).glob('*.csv'))

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


def mainf(fname):
    name=Path(fname).stem

    #get gene ids to plot
    df=pd.read_csv(fname, index_col=0)
    df=df.iloc[:n, :]
    l_id=df['gene_id'].tolist()

    #get cnt table, and convert index to gene name
    df_hm=df_cnt.reindex(l_id)
    df_hm.index=df.index
    
    #zscore
    df_hm=df_hm.apply(zscore, axis=1)
    
    #plot
    f_out=f'{fd_out}/{name}.png'
    plt_hm(df_hm, f_out)
    return

#-------------------------------------------------
with Pool() as p: p.map(mainf, l_fname)
