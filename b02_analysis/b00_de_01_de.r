library( "DESeq2" )

#----------------------------------------
fd_out='./out/b00_de_01_de'
fd_in='./out/b00_de_00_pp'

#####################################################
dir.create(fd_out)

#----------------------------------------
de_sample=function(sample, design_col='sample'){
    #load
    f_meta=paste(fd_in, sample, 'meta.csv', sep='/')
    f_cnt=paste(fd_in, sample, 'count.csv', sep='/')
    df_meta=read.csv(f_meta, header=TRUE)
    df_cnt=read.csv(f_cnt, header=TRUE, row.names=1)
    
    #DE (R will choose a reference level for factors based on alphabetical order, like Treated vs Ctrl)
    dds=DESeqDataSetFromMatrix(countData=df_cnt,  colData=df_meta, design=formula(paste('~', design_col)))
    dds=DESeq(dds)
    res=results(dds)
    
    #save
    f_out=paste(fd_out, sample, sep='/')
    f_out=paste(f_out, 'csv', sep='.')
    write.csv(res, f_out)
}

#----------------------------------------
# ctrl - treated
sample='Ctrl_Treated'
de_sample(sample, design_col='condition')

# pairwise  DE
v_sample=c('MFL_MFN', 'MFL_MFPA', 'MFN_MFPA')
for (sample in v_sample){
de_sample(sample)
}



