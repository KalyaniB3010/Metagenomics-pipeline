for i in SRR3950486 SRR3950487 SRR5898915 SRR5898917
do
	echo "$i"
	echo "-----------------------------"
	cd $i
	
	echo "Running FastQC"
	#/home/BIB/Software/FastQC_v0.12.1/fastqc ${i}_1.fastq.gz ${i}_2.fastq.gz
	echo "Fastqc: Done"

	echo "Running Triommatic"
	#java -jar /home/BIB/Software/Trimmomatic-0.39/trimmomatic-0.39.jar PE -threads 8 ${i}_1.fastq.gz ${i}_2.fastq.gz ${i}_1P.fastq.gz ${i}_1U.fastq.gz ${i}_2P.fastq.gz ${i}_2U.fastq.gz ILLUMINACLIP:/home/BIB/Software/Trimmomatic-0.39/adapters/TruSeq3-PE.fa:2:30:10 LEADING:20 TRAILING:20 SLIDINGWINDOW:4:20 MINLEN:50 
	echo "Trimmoamatic: Done"

	echo "Running FastQC on paired trimmed reads"
	#/home/BIB/Software/FastQC_v0.12.1/fastqc ${i}_1P.fastq.gz ${i}_2P.fastq.gz
	echo "Fastqc: Done"

	echo "Alignment using bwa"
	
	#/home/BIB/Software/bwa/bwa mem /home/BIB/Database/HumanGenome_hg38/hg38_index ${i}_1P.fastq.gz ${i}_2P.fastq.gz  > ${i}_aligned.sam
	echo "Alignment: Done"

	echo "Convert sam to bam"
	#samtools view -S -b ${i}_aligned.sam -o ${i}_aligned.bam 
	echo "sam-bam conversion: Done"

	echo "Sorted bam"
	#samtools sort ${i}_aligned.bam  -o ${i}_sorted.bam
	echo "sortef bam: Done"

	echo "Extract umapped reads"
	#samtools view -b -f 4 ${i}_sorted.bam>${i}_unmapped.bam

	echo "convert unmapped BAM to Fastq"
	#samtools fastq -1 ${i}_unmapped_1.fastq.gz  -2 ${i}_unmapped_2.fastq.gz  -0 /dev/null -s /dev/null -n ${i}_unmapped.bam

	echo "Run Kraken (taxonomic classification)"
	#kraken2 --db /home/BIB/Database/Kraken2_8mer --paired --report ${i}_kraken2_repor.txt --output ${i}_kraken2_output.txt ${i}_unmapped_1.fastq.gz   ${i}_unmapped_2.fastq.gz

	echo "Run Bracken"
	#/home/BIB/Software/Bracken/bracken -d /home/BIB/Database/Kraken2_8mer -i ${i}_kraken2_repor.txt -o ${i}_bracken1_species.txt -r 100 -l S

	cd ..

done


echo "Merge bracken files"
#python3 2_merge_abundance.py

echo "shnaon index"
#python3 3_shanon_index.py

echo "comparative analysis"
#python3 4_t-test.py

echo "Heatmap"
#python3 5_heatmap.py

echo "Volcano plot"
python3 6_volcano_plot.py




