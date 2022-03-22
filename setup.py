from setuptools import setup, find_packages

setup(
	name="regina-normalizer",
    package_dir={'': 'regina_normalizer_pkg'},
    packages=find_packages(where='regina_normalizer_pkg'),
	install_requires=[
		'setuptools',
		'pos @ git+https://github.com/cadia-lvl/POS.git@v3.0.0'],
	python_requires='>=3.5',
	)