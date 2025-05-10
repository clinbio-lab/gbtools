

from genetic_barcode.utils.hashing import run_hash




def compare_hashes(vcf_path: str, hash_str: str) -> float:
    """
    Compares a MinHash signature generated from a VCF file with a decomressed signature,
    and computes their Jaccard similarity.

    Args:
        vcf_path (str): Path to the input VCF file used to generate the first MinHash signature.
        b64_str (str): Base64-encoded string representing the serialized second LeanMinHash signature.

    Returns:
        float: Jaccard similarity score between the two MinHash signatures.
    """
    h1 = run_hash(vcf_path)
    h2 = hash_str

    m = mm = 0
    for c1, c2 in zip(h1, h2):
        if c1 != "." and c2 != ".":
            if c1 == c2:
                m += 1
            else:
                mm += 1
    total = m + mm
    return {
        "similarity": m / total if total > 0 else float('nan'),
        "fraction": total / len(h1)
    }
