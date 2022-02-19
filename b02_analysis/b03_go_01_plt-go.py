import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

#------------------------------------------
n=10  #number of GO terms to plot

fd_out='./out/b03_go_01_plt-go'
fd_in='./out/b03_go_00_gene/go'

#####################################################
Path(fd_out).mkdir(exist_ok=True)
l_fname=list(Path(fd_in).glob('*-GO.txt'))

#-------------------------------------------
def load_go(fname, n=n):
    #load
    df=pd.read_csv(fname, sep='\t')
    df=df.loc[:, ['Term', 'Combined Score', 'Adjusted P-value']].copy()
    df=df.sort_values(['Combined Score', 'Adjusted P-value'], ascending=False) 
    df=df.iloc[:n, :]
    #clean term
    df['Term']=df['Term'].apply(clean_term)
    return df

def clean_term(term, i=9):
    go=term.split('(GO:')[-1].strip(')')
    #get name
    name=term.split('(GO:')[0].strip()
    if len(l_name:=name.split(' '))>i:
        name=f'{" ".join(l_name[0:i])}...'
    #concat
    term=f'(GO: {go}) {name}'
    return term


def plt_go(df, f_out, cmap='Grey', title=None, sz=(10, 4.5)):
    #plot
    fig, ax=plt.subplots(figsize=sz)
    ax=sns.barplot(x='Combined Score', y='Term', data=df, alpha=0.7, color=cmap)
    #adjust
    ax.xaxis.tick_top()
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.set_title(title, fontsize=18, pad=20, weight='semibold')
    plt.xlabel('')
    ax.axes.get_yaxis().set_visible(False)
    plt.xticks(fontsize=10, weight='semibold')
    #add text
    l_txt=df['Term'].tolist()
    for idx, txt in enumerate(l_txt):
        x=1
        y=idx+0.1
        plt.text(x, y, txt, horizontalalignment='left', fontsize=12, weight='semibold')
    #save
    plt.tight_layout()
    plt.savefig(f_out, dpi=300)
    plt.close()
    return


def mainf(fname):
    #get names
    name=Path(fname).stem
    name=name.split('-')[0]
    sample1, sample2, reg=name.split('_')

    #load df
    df=load_go(fname)
    df.to_csv(f'{fd_out}/{name}.csv')
    
    #plot
    title=f'{sample2} vs {sample1} ({reg})'
    f_out=f'{fd_out}/{name}.png'
    plt_go(df, f_out, title=title)
    return

#--------------------------------------------
for fname in l_fname: mainf(fname)
