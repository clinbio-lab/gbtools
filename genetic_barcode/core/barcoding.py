import os
from typing import Optional


from pdf417 import encode, render_image

from genetic_barcode.utils.hashing import run_hash



def save_png(image, vcf_path , output_filename, output_path) -> None:
    """
    Saves the barcode image as a PNG file. If no output path or filename is provided, 
    they will be derived from the input VCF path.

    :param image: Rendered barcode image to be saved.
    :param vcf_path: Path to the original VCF file, used to infer default paths.
    :param output_filename: Optional name for the output image file.
    :param output_path: Optional directory to save the image in.
    """
    if not output_filename:
        output_filename = os.path.basename(vcf_path) + "_barcode.png"
        
    if not output_path:
        output_path = os.path.dirname(os.path.abspath(vcf_path))
    
    os.makedirs(output_path, exist_ok=True)

    output_file = os.path.join(output_path, output_filename)

    image.save(output_file)
    print(f"Barcode image successfully generated and saved to {output_file}")

def generate_barcode_image(vcf_path: str, output_filename: Optional[str] = None, output_path: Optional[str] = None) -> object:

    """
    Generates a visual genetic barcode image from a VCF file by first creating a MinHash signature 
    and then compressing it. The resulting signature is used to generate a PDF417 barcode image.

    This function processes the VCF file, encodes the genotypes into an IUPAC string, generates 
    a MinHash signature, compresses the signature, and creates a barcode image representing 
    the compressed signature.

    :param vcf_path: The path to the VCF file that contains genotype data.
    :param columns: The number of columns in the PDF417 barcode (default is 10).
    :param encoding: The encoding to be used for the barcode (default is "utf-8").
    :param security_level: The security level of the barcode, affecting the error correction (default is 2).
    :return: None.
    """

    hash = run_hash(vcf_path)


    barcode = encode(hash, columns=8, security_level=3)
    image = render_image(barcode, scale = 1)



    save_png(image = image, vcf_path = vcf_path, output_filename = output_filename, output_path = output_path)
    return hash



 