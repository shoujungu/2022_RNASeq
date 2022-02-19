import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from multiprocessing import Pool

#-----------------------------------------------
p=0.05
fc=1

fd_out='./out/b00_de_03_plt-voc'
fd_in='./out/b00_de_02_clean'

#######################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)
l_fname=list(Path(fd_in).glob('*.csv'))

#-----------------------------------------------
def make_df(df):
    df=df.loc[df['p']>0, :].copy()
    x=-np.log10(p)
    #convert p
    df['logp']=df['p'].apply(np.log10)
    df['logp']=-df['logp']
    #assign color
    df['hue']='0'
    df.loc[(df['p']<p) & (df['logfc']<-fc), ['hue']]='1'
    df.loc[(df['p']<p) & (df['logfc']>fc), ['hue']]='2'
    df['hue']=pd.Categorical(df['hue'], categories=['0', '1', '2'], ordered=True)
    return df


def plt_vol(df, f_out, title=None, sz=(7,5), cmap=['#8a8a8a', '#ff0000', '#00d138']):
    #plot
    fig, ax=plt.subplots(figsize=sz)
    sns.despine()
    ax=sns.scatterplot(data=df, x='logfc', y='logp', hue='hue', s=6, legend=False, palette=cmap)
    #adjust
    ax.set_title(title, fontsize=20, pad=10, weight='semibold')
    plt.xlabel('Log2FC',  fontsize=10, labelpad=5)
    plt.ylabel('-Log10(p)',  fontsize=10, labelpad=5)
    plt.xlim([-12, 12])
    #save
    plt.tight_layout()
    plt.savefig(f_out, dpi=300)
    plt.close()
    return


def mainf(fname):
    name=Path(fname).stem
    df=pd.read_csv(fname, index_col=0)
    #preprocess df
    df=make_df(df)
    #plot
    sample1, sample2=name.split('_')
    f_out=f'{fd_out}/{name}.png'
    title=f'{sample2} vs {sample1}'
    plt_vol(df, f_out, title=title)
    return

#------------------------------------------------
with Pool() as p: p.map(mainf, l_fname)
