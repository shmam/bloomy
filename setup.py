import setuptools

with open("PYPI.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="bloomy",
	version="0.0.2",
	author="Sam Crochet",
	author_email="samuel.d.crochet@gmail.com",
	description="An efficient and scalable bloom filter module built in pure python.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/shmam/bloomy",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)