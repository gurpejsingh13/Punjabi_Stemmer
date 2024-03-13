from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='punjabi_stemmer',  # Package name
    version='1.0.0',  # Initial version
    packages=find_packages(),  # Automatically find and include all packages
    description='A Python library for stemming Punjabi language words, including preprocessing for noise removal.Our stemmer is meticulously crafted to handle the rich morphological variations in Punjabi, offering accurate stemming through an extensive set of rules tailored to the language's specific characteristics. It addresses various grammatical scenarios, including proper nouns, pronouns, verbs, adverbs, adjectives, and more, ensuring a comprehensive understanding and processing of text.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Gurpej Singh',  
    author_email='gurpejsingh462@gmail.com',  
    url='https://github.com/gurpejsingh13/Punjabi_Stemmer.git',  # Replace with your repository URL
    license='MIT',
    keywords=['stemmer', 'punjabi', 'nlp', 'punjabi language', 'Gurmukhi Lanuae', natural language processing', 'text processing', 'noise removal', 'Stemming',
    'Brute Force Algorithm', 'Suffix Striping', 'Under-stemming', 'Over-stemming', 'Stemming Algorithm'],
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
    include_package_data=True,  # To include data files from the 'data' directory in the package
    # Dependencies: assuming no external libraries were used beyond Python's standard library
    install_requires=[
        # List any third-party libraries your package needs here.
        # Example: 'requests>=2.25.1',
    ],
)
