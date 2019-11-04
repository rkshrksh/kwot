import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kwot",
    version="0.0.1",
    author="Rakesh Gautam",
    author_email="rkshrkshme@gmail.com",
    description="An awesome random quote generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rkshrksh",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    data_files=[('.', ['kwot/quotes.json'])],
    entry_points='''
        [console_scripts]
        kwot=kwot.main:quote
    ''',
)
