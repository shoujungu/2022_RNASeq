import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns

#------------------------------------------------
fd_out='./out/a00_pca_00_pca'
fd_in='/home/shoujun/Desktop/b01_tmp/z00/b01_align/out/a00_star_02_count'

#########################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)

#load
df_meta=pd.read_csv(f'{fd_in}/meta.csv', index_col=0)
df_meta=df_meta.set_index('sample_id')
df=pd.read_csv(f'{fd_in}/count.csv', index_col=0).T

#-----------------------------------------------
def plt_scatter(df, f_out, sz=(5,6), title=None, hue='condition'):
    #plot
    sns.set()
    ax=sns.scatterplot(data=df, x='x', y='y', hue=hue, s=50)
    
    #adjust
    ax.set_title(title, fontsize=20, pad=10, weight='semibold')
    plt.xlabel('PCA_1',  fontsize=10, labelpad=5)
    plt.ylabel('PCA_2',  fontsize=10, labelpad=5)
    ax.tick_params(axis='both', which='major', labelsize=7)

    #save
    plt.tight_layout()
    plt.savefig(f_out, dpi=300)
    plt.close()
    return

#------------------------------------------------
#scale data
X=df.values
scaler=MinMaxScaler()
X=scaler.fit_transform(X)

#pca
pca=PCA(n_components=2)
X=pca.fit_transform(X)
df=pd.DataFrame(X, columns=['x', 'y'], index=df.index)

#add meta info 
df=df.merge(df_meta, left_index=True, right_index=True)
df.to_csv(f'{fd_out}/pca.csv')

#plot condition
f_out=f'{fd_out}/condition.png'
plt_scatter(df, f_out, title='Condition')

#plot sample
f_out=f'{fd_out}/sample.png'
plt_scatter(df, f_out, title='Sample', hue='sample')


