import subprocess
import pandas as pd
from pathlib import Path

#------------------------------------------
fd_out='./out/a00_star_01_align'
fd_in='/home/shoujun/Desktop/b01_tmp/z00/b00_fastq/out/a00_sra_03_trim'
f_meta='/home/shoujun/Desktop/b01_tmp/z00/a00_raw/SraRunTable.txt'
fd_ref='./out/a00_star_00_index'
f_star='/home/shoujun/Desktop/b01_tmp/z00/a01_tool/star/STAR'

######################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_meta)

#----------------------------------------
#get run number
l_srr=df['Run'].tolist()

#align
for srr in l_srr:
    #param
    r1=f'{fd_in}/{srr}_1.fastq'
    r2=f'{fd_in}/{srr}_2.fastq'
    out=f'{fd_out}/{srr}'

    #align
    cmd=f'{f_star} --runThreadN 20 --genomeDir {fd_ref} --readFilesIn {r1} {r2} --outFileNamePrefix {out} --quantMode GeneCounts'
    subprocess.run(cmd, shell=True)

