
import random
import hashlib
from itertools import chain

from cyvcf2 import VCF


CHUNCK_SIZE = 3

def parse_vcf(vcf_path: str) -> VCF:
    """
    Read a VCF file and return a VCF object.

    :param vcf_path: Path to the VCF file.
    :return: cyvcf2.VCF object for iterating variants.
    """
    return VCF(vcf_path)

def resample_genotypes(gt_string: str, seed = 42) -> str:

    """
    Randomly shuffle genotype string characters using a fixed seed.

    :param gt_string: Genotype string to shuffle.
    :param seed: Random seed for reproducibility (default: 42).
    :return: Shuffled genotype string.
    """

    random.seed(seed)
    gt_lst = list(gt_string)
    gt_string_re = ''.join(random.sample(gt_lst, k = len(gt_string)))
    return gt_string_re

def gt_encode(vcf_path: str) -> str:

    """
    Encode genotypes from a VCF file into a string of numeric codes:
    '0' for homozygous reference, '1' for heterozygous, '2' for homozygous alt, 'N' otherwise.

    :param vcf_path: Path to the VCF file.
    :return: Encoded genotype string.
    """

    vcf = parse_vcf(vcf_path)
    gt_list, ref_list, alt_list, genotype_list = [], [], [], []
    for var in vcf:
        ref_list.append(var.REF)
        alt_list.append(var.ALT)
        genotype_list.append(var.genotypes[0][:2])
    alt_list = list(chain.from_iterable(alt_list))

    for ref, alt, gt in zip(ref_list, alt_list, genotype_list):
        if gt == [0,0]:
            gt_list.append("0")
        elif sorted(gt)==[0,1]:
            gt_list.append("1")
        elif gt==[1,1]:
            gt_list.append("2")
        else:
            gt_list.append("N")
    gt_string = ''.join(gt_list)
    return gt_string

def get_chunks(gt_string: str, chunk_size: int):
    """
    Split a genotype string into fixed-size chunks.

    :param gt_string: String of encoded genotypes.
    :param chunk_size: Size of each chunk.
    :return: List of genotype chunks.
    """
    return [gt_string[i:i+chunk_size] for i in range(0, len(gt_string), chunk_size)]

def gt_recode(gt_string: str) -> str:
    gt_chunks = get_chunks(gt_string, 2)
    recoded = ''
    for gt in gt_chunks:
        if gt in ('00', '11', '22'):
            recoded += '1'
        elif gt in ('01', '12', '20'):
            recoded += '2'
        elif gt in ( "02", "10", "21"):
            recoded += '3'
        else:
            recoded += '0'
    return recoded

def run_hash(path: str) -> str:
    """
    Run the full pipeline: encode, shuffle, recode genotypes,
    split into chunks, and hash each valid chunk.

    :param path: Path to VCF file.
    :return: Concatenated hash result as a string.
    """
    hash_result = ""
    gt_str_rec = gt_recode(resample_genotypes(gt_encode(path)))
    
    for chunk in get_chunks(gt_str_rec, CHUNCK_SIZE):
        if "0" not in chunk:
            h = hashlib.md5(chunk.encode()).hexdigest()[0]
        else:
            h = "."
        hash_result += h
    return hash_result
