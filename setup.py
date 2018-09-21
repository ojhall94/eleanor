from setuptools import setup


setup(
    name='eleanor',
    version='0.0.1',
    license='MIT',
    long_description=open('README.md').read(),
    author='Adina D. Feinstein',
    author_email='adina.d.feinstein@gmail.com',
    packages=[
        'eleanor',
        ],
    include_package_data=True,
    url='http://github.com/afeinstein20/ELLIE',
    description='Source Extraction for TESS Full Frame Images',
    package_data={'':['README.md', 'LICENSE']},
    install_requires=[
        'mplcursors', 'photutils', 'tqdm', 'lightkurve', 'astropy',
        'astroquery>=0.3.8', 'bokeh', 'muchbettermoments'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.0',
        ],
    )
