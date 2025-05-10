from setuptools import setup, find_packages

setup(
    name="genetic_barcode",
    version="0.1.0",
    packages=find_packages(),
    package_dir={'': '.'},
    install_requires=[
        "cyvcf2",
        "pdf417",
        "pillow"],
    entry_points={
        "console_scripts": [
            "gbtools=genetic_barcode.cli.main:main",
        ],
    },
    package_data={
        'genetic_barcode': ['data/*.py'],
    },
)
