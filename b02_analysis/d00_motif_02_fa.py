from pathlib import Path
import pandas as pd
from multiprocessing import Pool

#-------------------------------------------------------
fd_out='./out/d00_motif_02_fa'
fd_in='./out/d00_motif_01_bed'
f_fa='/home/shoujun/Desktop/b01_tmp/z00/a01_tool/ref/GRCh38.primary_assembly.genome.fa'

#------------------------------------------------------
Path(fd_out).mkdir(exist_ok=True, parents=True)
l_fname=list(Path(fd_in).glob('*.csv'))

#load fa (dic of chromosome seq)
dic_fa={}
l_fa=Path(f_fa).read_text().split('>')[1:]
for fa in l_fa:
	seq=fa.strip().split('\n')
	dic_fa[seq[0].split(' ')[0]]=''.join(seq[1:])

#---------------------------------------------------
def rev_com(seq):
	trans=str.maketrans("ATCG","TAGC")
	seq=seq.translate(trans)
	seq=seq[::-1]
	return seq
	
def mainf(fname):
	#load
	name=Path(fname).stem
	df=pd.read_csv(fname, index_col=0)
	df=df.loc[~df.index.duplicated(), :]
	#get fa
	l_data=[]
	for gene, row in df.iterrows():
		try:
			chro=row['chr']	
			start=row['start']
			end=row['end']
			strand=row['strand']	
			#get seq
			seq=dic_fa[chro][start:end]
			#rev comp
			if strand=='-':
				seq=rev_com(seq)
			#append
			l_data.append(f'>{gene}')
			l_data.append(f'{seq}\n')
		except Exception:
			print(gene)
			continue
	fasta='\n'.join(l_data)
	#save
	Path(f'{fd_out}/{name}.fa').write_text(fasta)
	return

##################################################################
with Pool() as p:
	p.map(mainf, l_fname)

