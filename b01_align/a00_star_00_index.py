import subprocess
from pathlib import Path

#---------------------------------------
fd_out='./out/a00_star_00_index'
f_fa='/home/shoujun/Desktop/b01_tmp/z00/a01_tool/ref/GRCh38.primary_assembly.genome.fa'
f_gtf='/home/shoujun/Desktop/b01_tmp/z00/a01_tool/ref/gencode.v39.primary_assembly.annotation.gtf'
f_star='/home/shoujun/Desktop/b01_tmp/z00/a01_tool/star/STAR'

###############################################
Path(fd_out).mkdir(exist_ok=True, parents=True)

#---------------------------------------
cmd=f'{f_star} --runThreadN 20 --runMode genomeGenerate --genomeDir {fd_out} --genomeFastaFiles {f_fa} --sjdbGTFfile {f_gtf} --limitGenomeGenerateRAM 100087828576'
subprocess.run(cmd, shell=True)

