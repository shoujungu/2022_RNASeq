import subprocess
import pandas as pd
from pathlib import Path
from multiprocessing import Pool

#------------------------------------------
fd_out='./out/a00_sra_03_trim'
fd_in='./out/a00_sra_01_fastq'
f_meta='/home/shoujun/Desktop/b01_tmp/z00/a00_raw/SraRunTable.txt'

##################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_meta)

#-----------------------------------------
def mainf(srr):
    #param
    r1=f'{fd_in}/{srr}_1.fastq'
    r2=f'{fd_in}/{srr}_2.fastq'
    r1_out=f'{fd_out}/{srr}_1.fastq'
    r1_out_up=f'{fd_out}/{srr}_1_up.fastq'
    r2_out=f'{fd_out}/{srr}_2.fastq'
    r2_out_up=f'{fd_out}/{srr}_2_up.fastq'
    
    #trim
    cmd=f'TrimmomaticPE {r1} {r2} {r1_out} {r1_out_up} {r2_out} {r2_out_up} ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15'
    subprocess.run(cmd, shell=True)
    return

#-----------------------------------------
#get run number
l_srr=df['Run'].tolist()

#main
with Pool() as p: p.map(mainf, l_srr)
