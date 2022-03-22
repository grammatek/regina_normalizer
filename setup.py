from setuptools import setup, find_packages

setup(
	name="regina-normalizer",
    package_dir={'': 'regina_normalizer_pkg'},
    packages=find_packages(where='regina_normalizer_pkg'),
	install_requires=['setuptools'],#, 'pos >= v2.1.0'],
	python_requires='>=3.5',

	)