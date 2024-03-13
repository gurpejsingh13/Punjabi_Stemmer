from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='punjabi_stemmer',
    version='1.0.0',
    packages=find_packages(),
    description='A Python library for stemming Punjabi language words, including preprocessing for noise removal.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Gurpej Singh',
    author_email='gurpejsingh462@gmail.com',
    url='https://github.com/gurpejsingh13/Punjabi_Stemmer.git',
    license='MIT',
    keywords=['stemmer', 'punjabi', 'Gurmukhi', 'nlp', 'punjabi language', 'natural language processing', 'text processing', 'noise removal',
              'Stemming', 'Brute Force Algorithm', 'Suffix Striping', 'Under-stemming', 'Over-stemming', 'Stemming Algorithm',],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',
    include_package_data=True,
    install_requires=[
        # No dependencies file required 
    ],
)
