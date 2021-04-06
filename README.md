# MYexample
This package is LICENSED under MIT. 

In the examle_packaging folder are all my files to make the package.

I opened the terminal and write the following lines:
```
$ python3 -m pip install -U setuptools twine wheel

$ cd /Users/mandi/Desktop/example_packaging   

$ python3 setup.py sdist bdist_wheel       

$ python3 -m twine upload --repository testpypi dist/*

Then i installad it:

$ python3 -m pip install --user -i https://test.pypi.org/simple/ MYexmaple
```
print out a card:

>>> import MYexample 

>>> cards = MYexample.Cardgame()

>>> print(cards.give())

♠ Kn

Don't use version 0.1 because i use now an another email

OUTDATED package, very bad to use it.
