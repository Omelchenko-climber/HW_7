from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.0',
    description='sort_your_folder',
    url='https://github.com/Origamiman/GoIT/tree/master/clean_folder',
    author='Anton Omelchenko',
    author_email='omelchenko230783@gmail.com',
    license='MIT',
    install_requires=['markdown'],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    entry_points={'console_scripts': ['clean-folder = clean_folder.main:run']}
)