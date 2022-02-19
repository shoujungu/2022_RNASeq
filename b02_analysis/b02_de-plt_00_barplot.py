import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from multiprocessing import Pool

#------------------------------------------
n=20    #number of top genes to plot

fd_out='./out/b02_de-plt_00_barplot'
fd_in='./out/b01_convert-gene_01_convert'

######################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)
l_fname=list(Path(fd_in).glob('*.csv'))

#-----------------------------------------
def plt_bar(df, f_out, title=None, sz=(4,8)):
    #plot
    sns.set()
    fig, ax=plt.subplots(figsize=sz)
    ax=sns.barplot(data=df, x='logfc', y=df.index, color='grey')
    
    #adjust
    ax.set_title(title, fontsize=15, pad=8, weight='semibold')
    plt.xlabel('Log2FC',  fontsize=10, labelpad=5)
    plt.ylabel('')
    plt.yticks(fontsize=11, rotation=0, weight='semibold')
    ax.tick_params(axis='y', which='major', pad=0)
    
    #save
    plt.tight_layout()
    plt.savefig(f_out, dpi=300)
    plt.close()
    return


def mainf(fname):
    name=Path(fname).stem
    df=pd.read_csv(fname, index_col=0)
    df=df.iloc[:n]
    
    #plot
    f_out=f'{fd_out}/{name}.png'
    sample1, sample2, reg=name.split('_')
    title=f'{sample2} vs {sample1} ({reg})'
    plt_bar(df, f_out, title=title)
    return

#-----------------------------------------
with Pool() as p: p.map(mainf, l_fname)
