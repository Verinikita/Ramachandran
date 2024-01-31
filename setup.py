import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='AlphaRamachan',
    version='0.2.4',
    author='Verinikita',
    author_email='verronicabaronetto@gmail.com',
    description='Ramachandran plotting tool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Verinikita/AlphaRamachandran.git',
    packages=['AlphaRamachan'],
    package_data={'AlphaRamachan': ['data/density_estimate.dat']},
    install_requires=[
        'biopython>=1.75',
        
        'matplotlib>=3.1.2',
        'rich>=9.3'
    ],

    python_requires='>=3.6',
)
