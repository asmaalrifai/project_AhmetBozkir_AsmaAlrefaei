from setuptools import setup, find_packages

setup(
    name='project_AhmetBozkir_AsmaAlrefaei',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'nltk',
    ],
    description='A package for various data preprocessing and feature engineering tasks.',
    author='Ahmet Bozkir, Asma Alrefaei',
    author_email='ahmbozkir@gmail.com, asma.o.alrifai@gmail.com',
    url='file://.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
