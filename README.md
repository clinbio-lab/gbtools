
# Genetic Barcoding Tool

## Motivation and idea

In clinical or population genomics, it is often neccessary to check sample identity in a fast, reliable and privacy-preserving way.
The purpose of this project is to generate a compact, privacy-aware representation of an individual's genotype using a selected set of informative SNPs.

**Our method fully obscures the underlying genotypes, making it completely impossible to infer them even in trios.**

The resulting hash string of a sample can be output as a 2D barcode to be included in lab reports.

For working with human data, we also generated an optimal set of 462 biallelic SNPs that are highly informative in all major populations and located in exonic regions.
This universal SNP set can be used as an efficient genotyping panel for both WES and WGS.

### Created by:

* Giulgaz Muradova
* Fedor Konovalov

### Genotype Encoding Strategy

<p align="center">
  <img src="figs/SNP_encoding.png" width="600" height="180"/>
</p>

The variant genotypes are encoded as semi-randomly picked pairs in such a way that the resulting value, while retaining some information about the variants' relative states within the pair, always allows for any single genotype (0/0, 0/1 or 1/1) to occur at each of the positions.

## Preparing Input Data

Before using the tool, you must generate a VCF file from your BAM (or CRAM) file using a predefined set of filtered variant positions. Use the following command:

```bash
bcftools mpileup -Ou \
  -R <snp_regions.bed> \
  -f <reference.fasta> <input.bam> | \
bcftools call -A -C alleles \
  -T <snps.tsv.gz> \
  -i -m -Ov > <output>.vcf
```

### Requirements:

* Input CRAM/BAM files **must be aligned to the GRCh38 (hg38) reference genome**.
* The following files with variant positions/alleles and the surrounding regions are provided in the cloud link below:
gnomad.exomes.v4.1.sites.distancefilt500k.ALL.tsv.gz
gnomad.exomes.v4.1.sites.distancefilt500k.ALL.regions.bed

* Replace the placeholders with appropriate files:

  * `<reference.fasta>` — the GRCh38 reference genome FASTA file.
  * `<regions.bed>` — a BED file with intervals surrounding each SNP (provided)
  * `<input.bam>` — your input CRAM or BAM file.
  * `<snps.tsv.gz>` — a TSV file with SNP positions and alleles (provided)
  * `<output>.vcf` — the name of the resulting VCF file.


## Example hashing output

The hash string for publicly available sample HG001 (NA12878) from 1000GP looks like this:
*c0b9b6a71999420ebbebe9669e6b7e266ab661a172795e9716e14b97bb119a1491976962990e6*


## Installation

To install the tool with required dependencies, run the following command from the root directory of the project:
```bash
pip install -e .
```

## Usage

The tool has two main functionalities, which can be invoked from the command line:

1. **Barcode Generation:** To compute a barcode from a single VCF file.
2. **Barcode Comparison:** To compare signatures between a VCF files or a previously generated string.

### Barcode Generation

To generate a barcode from a VCF file, use the following command:

```bash
gbtools barcode <path_to_vcf_file> --output_filename <output_filename> --output_path <output_directory>
```

* `<path_to_vcf_file>` — the path to the VCF file.
* `--output_filename` — (optional) the name of the output barcode image file.
* `--output_path` — (optional) the directory where the barcode image will be saved.

### Barcode Comparison

To compare the signature of a VCF file with a previously generated barcode, run:

```bash
gbtools compare <input1> <input2>
```

* <input1> - VCF path or precomputed hash string
* <input2> - VCF path or precomputed hash string

The command will output the Hamming distance between the two hashes, as well as the fraction of non-missing hash positions being compared.

## Example Data

For testing the tool, you can use genomic and exomic data available [data](https://disk.yandex.ru/d/1rNcQ4uTQmV8Ew).

## Project Structure

```
├── LICENSE
├── README.md
├── figs
│   ├── Combination.png
│   └── Full_pipeline.png
├── genetic_barcode
│   ├── __init__.py
│   ├── cli
│   │   ├── __init__.py
│   │   └── main.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── barcoding.py
│   │   └── comparing_hashes.py
│   └── utils
│       ├── __init__.py
│       └── hashing.py
├── requirements.txt
└── setup.py
```
