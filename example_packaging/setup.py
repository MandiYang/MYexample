from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
    print('readed')
    
setup(name='MYexmaple',
      version='0.1.1',
      description='A exmaple package',
      author='Mandi Yang',
      author_email='yangmandi2008@gmail.com',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/MandiYang/MYexample',
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
      ],
      python_requires='>=3.5',
      license='MIT',
      packages=find_packages()
)

