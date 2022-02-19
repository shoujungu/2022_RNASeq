# **RNA-Seq Analysis**

## 1. **Raw Data Source**
### \- RNASeq data  
[https://www.ncbi.nlm.nih.gov/bioproject/PRJNA806949](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA806949)  
### \- Reference
- GRCh38.p13 (primary assembly ):   [https://www.gencodegenes.org/human/](https://www.gencodegenes.org/human/)
---
## 2.  **Tools**  
### \- Python (v3.9.7 )  
- Pandas (v1.3.3),   Numpy (v1.21.2), Matplotlib (v3.5.1), Seaborn (v0.11.2), Scikit-Learn (v1.0), Scanpy (v1.8.1)
  
### \- R (v4.0.4)
- DESeq2 (v1.30.1)  
  
### \- Sratools (v3.0.0)  
### \- FastQC (v0.11.9)  
### \- Trimmomatic (v0.39)  
### \- STAR (v2.7.10a)
### \- Enrichr:  [Link](https://maayanlab.cloud/Enrichr/)  
### \- AME (v5.4.1):  [Link](https://meme-suite.org/meme/tools/ame) 
---
## 3. **Folder Structure**  
### \- a00_raw
Original files downloaded from SRA database.  
### \- a01_tool
Softwares and reference genome data.  
### \- b00_fastq
Fetch SRA data, convert to fastq, and QC.  
### \- b01_align  
Index reference, and map the reads to reference genome.
### \- b02_analysis  
Downstream analysis.  

---
## Note:  
Due to file size, some results are not deposited. 
