import os
from typing import Optional
from pdf417 import encode, render_image
from PIL import Image
from genetic_barcode.utils.hashing import run_hash

def save_png(
    image: Image.Image,
    vcf_path: str,
    output_filename: Optional[str],
    output_path: Optional[str]
) -> None:
    """
    Saves the barcode image as a PNG file. If no output path or filename is provided, 
    they will be derived from the input VCF path.
    Args:

    image: Rendered barcode image to be saved.
    vcf_path (str): Path to the input VCF file containing genotype data.
    output_filename (Optional[str]): Custom name for the output PNG file (without extension). If None, it's auto-generated.
    output_path (Optional[str]): Directory to save the PNG file. If None, saves in the current directory.
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
    Generates a visual genetic barcode image from a VCF file.

    This function processes the VCF file, encodes the genotype data into a compact string representation,
    and generates a PDF417 barcode based on this encoded string. The resulting image is saved as a PNG file.

    Args:
        vcf_path (str): Path to the input VCF file containing genotype data.
        output_filename (Optional[str]): Custom name for the output PNG file (without extension). If None, it's auto-generated.
        output_path (Optional[str]): Directory to save the PNG file. If None, saves in the current directory.

    Returns:
        object: The rendered barcode image object.
    """

    hash = run_hash(vcf_path)

    barcode = encode(hash, columns=6, security_level=3)
    image = render_image(barcode, scale = 1)

    save_png(image = image, vcf_path = vcf_path, output_filename = output_filename, output_path = output_path)
    print(f'Hashvalue: {hash}')



 
