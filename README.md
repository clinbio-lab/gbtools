
# Genetic Barcode Tool

This tool allows you to generate barcodes from VCF files or compare them with previously generated barcodes. It provides two main functionalities:

1. **Barcode Generation:** To compute a barcode from a single VCF file.
2. **Barcode Comparison:** To compare signatures between a VCF file and a previously generated string (e.g., from a database).

## Installation

To install the tool with required dependencies, run the following command from the root directory of the project:
```bash
pip install -e .
```

## Usage

The tool has two main functionalities, which can be invoked from the command line:

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
gbtools compare <path_to_vcf_file> <hash_string>
```

* `<path_to_vcf_file>` — the VCF file to compare.
* `<hash_string>` — the string representing the second hash.

The command will output the Hamming distance between the two hashes.

## Example Data

For testing the tool, you can use genomic and exomic data available [data](https://disk.yandex.ru/d/1rNcQ4uTQmV8Ew).

## Project Structure

```
├── README.md
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
├── setup.py
└── tests
    └── __init__.py
```

