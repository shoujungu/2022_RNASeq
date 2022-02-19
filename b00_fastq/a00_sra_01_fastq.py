import subprocess
from pathlib import Path
from multiprocessing import Pool

#------------------------------------------
fd_out='./out/a00_sra_01_fastq'
fd_in='./out/a00_sra_00_prefetch'
f_cmd='/home/shoujun/Desktop/b01_tmp/z00/a01_tool/sratools/bin/fastq-dump'

#######################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)
l_fname=list(Path(fd_in).glob('*.sra'))

#------------------------------------------
def mainf(fname):
    cmd=f'{f_cmd} --outdir {fd_out} --skip-technical --readids --split-3 --clip {fname}'
    subprocess.run(cmd, shell=True)
    return

#-------------------------------------------
with Pool() as f: f.map(mainf, l_fname)
    

