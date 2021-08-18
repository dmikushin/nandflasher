import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dumpflash-ohjeongwook",
    version="0.0.1",
    author="Matt Oh",
    author_email="jeongoh@darungrim.com",
    description="DumpFlash Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ohjeongwook/dumpflash",
    packages=setuptools.find_packages(),
    install_requires=[
          'pyusb', 'pyftdi',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "dumpflash = dumpflash.dumpflash:main",
            "dumpjffs2 = dumpjffs2.dumpjffs2:main",
        ]
    },
    python_requires='>=2.7',
)
