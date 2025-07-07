# Metagenomics-pipeline 
project title - Pipeline development in metagenomics using shotgun sequencing

# Shotgun Metagenomics Pipeline for Gut Microbiome Analysis

This project focuses on the development and implementation of a comprehensive **shotgun metagenomics analysis pipeline** to study microbial composition in **Parkinson's Disease (PD)** patients compared with healthy individuals.

>  *An initial test was performed on 2 TB and 2 healthy samples, but the Parkinson’s case study was used for detailed analysis due to better sample size and results.*

---

## Project Overview

The pipeline processes raw sequencing reads, removes low-quality and host sequences, classifies microbial species using **Kraken2**, refines abundance with **Bracken**, and performs **statistical and visual analysis** using Python. This project was completed as part of my MSc Bioinformatics internship at **Bruhaspathi Institute of Biosciences**.

---

## Dataset

- **10 Parkinson’s Disease samples + 10 Healthy controls**
- Source: [NCBI SRA](https://www.ncbi.nlm.nih.gov/sra)
- Bioproject -  PRJNA834801

---

##  Tools & Technologies Used

| Step | Tool/Software |
|------|---------------|
| Data Download | SRA Toolkit |
| Quality Control | FastQC |
| Trimming | Trimmomatic |
| Host Removal | BWA, SAMtools |
| Taxonomic Classification | Kraken2 |
| Abundance Estimation | Bracken |
| Merging & Stats | Python (pandas, scipy, seaborn, matplotlib) |

---

##  Pipeline Workflow

1. Download raw `.sra` files from SRA
2. Convert to `.fastq.gz` using `fastq-dump`
3. Run FastQC for quality assessment (before & after trimming)
4. Trim adapters and low-quality reads using Trimmomatic
5. Align reads to human genome (hg38) using BWA
6. Remove mapped reads (host) using SAMtools
7. Convert unmapped reads back to FASTQ
8. Classify microbial reads with Kraken2
9. Estimate species-level abundance with Bracken
10. Merge outputs and visualize results
11. Perform statistical tests (Shannon Index, t-test, etc.)

---

## Results Summary (PD vs Healthy)

- PD samples showed **increased abundance of pathogenic species** like *Salmonella enterica*
- Several **SCFA-producing species were reduced** in PD (e.g., *Faecalibacterium prausnitzii*, *Blautia luti*)
- PCA plots showed **clear separation** between PD and control groups
- Volcano and heatmaps identified **statistically significant microbial shifts**

---

##  Visual Outputs

-  Heatmaps of log2 fold change  
-  PCA clustering of samples  
-  Volcano plots for significant species  
-  Bar plots of top abundant microbes  
-  Shannon Index (alpha diversity)

---

##  Future Enhancements

- Add functional profiling (e.g., HUMAnN3)
- Test on larger datasets or additional disease models
- Integrate ML-based classifiers for disease prediction

---

## Acknowledgments

This project was completed as part of my MSc Bioinformatics internship at **Bruhaspathi Institute of Biosciences**.  
Special thanks to my guide for her constant support and guidance throughout the project.

---

## 🧾 License

This project is for academic and research purposes only.
