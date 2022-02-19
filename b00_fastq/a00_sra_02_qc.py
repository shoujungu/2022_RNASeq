import subprocess
from pathlib import Path
from multiprocessing import Pool

#------------------------------------------
fd_out='./out/a00_sra_02_qc'
fd_in='./out/a00_sra_01_fastq'

################################################
Path(fd_out).mkdir(exist_ok=True, parents=True)
l_fname=list(Path(fd_in).glob('*.fastq'))

#-----------------------------------------
def mainf(fname):
    cmd=f'fastqc {fname} -o {fd_out}'
    subprocess.run(cmd, shell=True)
    return

#-----------------------------------------
with Pool() as p: p.map(mainf, l_fname)
