from typing import Dict

from genetic_barcode.utils.hashing import run_hash

def is_vcf_file(vcf_path: str) -> bool:
    """
    Check if a given file path corresponds to a VCF or compressed VCF file.

    Args:
        vcf_path (str): Path to a file.

    Returns:
        bool: True if file ends with '.vcf' or '.vcf.gz', else False.
    """
    return vcf_path.endswith('.vcf') or vcf_path.endswith('.vcf.gz') 


def compare_hashes(input1: str, input2: str) -> Dict[str, float]:
    """
    Compare two barcode-like hash strings and compute similarity.

    Args:
        input1 (str): VCF path or precomputed hash string
        input2 (str): VCF path or precomputed hash string

    Returns:
        dict: Dictionary with similarity and fraction of comparable positions.
    """
    h1 = run_hash(input1) if is_vcf_file(input1) else input1
    h2 = run_hash(input2) if is_vcf_file(input2) else input2

    m = mm = 0
    for c1, c2 in zip(h1, h2):
        if "." not in c1 and "." not in c2:
            if c1 == c2:
                m += 1
            else:
                mm += 1

    total = m + mm
    similarity = m / total if total > 0 else float('nan')
    fraction = total / len(h1)

    result = {
        "similarity": similarity,
        "fraction": fraction
    }
    print(result)
    return result
