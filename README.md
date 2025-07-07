# Metagenomics-pipeline 
project title - Pipeline development in metagenomics using shotgun sequencing

# Shotgun Metagenomics Pipeline for Gut Microbiome Analysis

This project focuses on the development and execution of a comprehensive **shotgun metagenomics analysis pipeline** to study microbial composition in **human gut microbiome samples** from **Tuberculosis (TB)** and **Parkinson's Disease (PD)** patients, compared with healthy controls.

---

##  Project Overview

The pipeline processes raw sequencing reads, removes low-quality and host sequences, classifies microbial species using **Kraken2**, refines abundance with **Bracken**, and performs **statistical and visual analysis** using Python. The project is part of my MSc Bioinformatics internship at **Bruhaspathi Institute of Biosciences**.

---

##  Datasets

- **Case 1:** 2 TB samples + 2 Healthy controls (Human gut microbiome)
- **Case 2:** 10 Parkinson’s samples + 10 Healthy controls (Human gut microbiome)
- Source: [NCBI SRA](https://www.ncbi.nlm.nih.gov/sra)

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

## Results Summary

- **TB vs Healthy:** Enrichment of *Prevotella*, *Dialister*, and depletion of *Faecalibacterium* in TB samples.
- **PD vs Healthy:** PD samples showed increase in *Salmonella enterica* and loss of SCFA-producing species.
- PCA, volcano plots, and heatmaps confirmed clear separation between disease and control groups.

---

## Visual Outputs

-  Heatmaps of log2 fold change
-  PCA clustering of samples
-  Volcano plots showing significant species
-  Bar plots of top abundant taxa
-  Alpha diversity (Shannon Index)

---

##  Future Enhancements

- Add functional profiling (HUMAnN3)
- Automate pipeline with Snakemake or bash scripting
- Integrate ML-based prediction of disease state
- Expand to larger datasets for statistical strength

---

##  Acknowledgments

This project was completed as part of my MSc Bioinformatics internship at **Bruhaspathi Institute of Biosciences**.  
Special thanks to my guide for continuous support and mentoring throughout the project.

---

## 🧾 License

This project is for educational and research purposes only.

