import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kwot",
    version="0.0.2",
    author="Rakesh Gautam",
    author_email="rkshrkshme@gmail.com",
    description="An awesome random quote generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rkshrksh/kwot",
    packages=setuptools.find_packages(),
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
