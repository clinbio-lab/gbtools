import argparse

from genetic_barcode.core.comparing_hashes import compare_hashes
from genetic_barcode.core.barcoding import generate_barcode_image


def main() -> None:

    """
    Command-line interface for genetic barcode tools.

    Supports two subcommands:
    - `barcode`: Generates a barcode from a VCF file.
    - `compare`: Compares a VCF file's hash to a base64-encoded signature.
    """
    parser = argparse.ArgumentParser(prog="gbtools", description="Generate a barcode from a VCF file or compare it to a previously encoded barcode.")   
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_barcode = subparsers.add_parser("barcode", help="Compute the barcode of a single vcf file")
    parser_barcode.add_argument("file", help="Path to VCF-file")
    parser_barcode.add_argument("--output_filename", type=str, default=None, help="Name of the output barcode image file")
    parser_barcode.add_argument("--output_path", type=str, default=None, help="Directory to save the output image")



    parser_cmp = subparsers.add_parser("compare", help="Compare two barcodes or VCF files")
    parser_cmp.add_argument("input1", help="First VCF file path or precomputed hash string")
    parser_cmp.add_argument("input2", help="Second VCF file path or precomputed hash string")


    args = parser.parse_args()

    if args.command == "barcode":
        generate_barcode_image(
            vcf_path=args.file,
            output_filename=args.output_filename,
            output_path=args.output_path,
        )
        
    elif args.command == "compare":
        similarity = compare_hashes(args.input1, args.input2)
        print(similarity)
if __name__ == '__main__':
    main()