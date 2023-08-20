from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="youtube_data",
    version="0.1",
    packages=find_packages(),
    install_requires=required,
    author="Krzysztof Budnik",
    author_email="chris.studyx@gmail.com",
    description="A simple interface for extracting data from YouTube via offical v3 api.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/chrisbudnik/youtube-data",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)