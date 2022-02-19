import subprocess
import pandas as pd
from pathlib import Path
from multiprocessing import Pool

#------------------------------------------
fd_out='./out/a00_sra_04_trim-qc'
fd_in='./out/a00_sra_03_trim'
f_meta='/home/shoujun/Desktop/b01_tmp/z00/a00_raw/SraRunTable.txt'

################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_meta)

#-----------------------------------------
def mainf(srr):
    #fwd
    fname=f'{fd_in}/{srr}_1.fastq'
    cmd=f'fastqc {fname} -o {fd_out}'
    subprocess.run(cmd, shell=True)

    #rev
    fname=f'{fd_in}/{srr}_2.fastq'
    cmd=f'fastqc {fname} -o {fd_out}'
    subprocess.run(cmd, shell=True)
    return

#-----------------------------------------
#get run number
l_srr=df['Run'].tolist()

#main
with Pool() as p: p.map(mainf, l_srr)


