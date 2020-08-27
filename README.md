# MYexample
This package is LICENSED under MIT. 

In the examle_packaging folder are all my files to make the package.

Then i open the terminal and write the following lines:

$ cd /Users/mandi/Downloads/example_packaging   

$ python3 setup.py sdist bdist_wheel       

$ python3 -m twine upload --repository testpypi dist/*

Then i installad it:

$ pip3 install --user -i https://test.pypi.org/simple/ MYexmaple
