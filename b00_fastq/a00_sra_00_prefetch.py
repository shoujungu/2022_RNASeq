import subprocess
import pandas as pd
from pathlib import Path

#------------------------------------------
fd_out='./out/a00_sra_00_prefetch'
f_in='/home/shoujun/Desktop/b01_tmp/z00/a00_raw/SraRunTable.txt'
f_cmd='/home/shoujun/Desktop/b01_tmp/z00/a01_tool/sratools/bin/prefetch'

#######################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)
df=pd.read_csv(f_in)

#------------------------------------------
for srr in df['Run']:
    cmd=f'{f_cmd} {srr} --output-file {fd_out}/{srr}.sra'
    subprocess.run(cmd, shell=True)

    

