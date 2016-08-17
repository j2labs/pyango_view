Pyango View
===========

Pyango View is a Python library for calling pango-view.

Pyango View is licensed under the [Apache Licence, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)

Features
--------

Pyango View is simply a mapping and some pythonish documentation for accessing the pango-view command line tool.

Goopytrans supports translating a single body of text.

    >>> from pyango_view import str2img
    >>> str2img('texty text', font='Courier New')
    0

![image of text](/j2labs/pyango_view/raw/master/docs/images/textytext.png)

Urdu works nicely. Pango is very robust!

    >>> str2img('اس صفحہ کو ترامیم کیلیۓ نـیـم محفوظ کر دیا گیا ہے اور صارف کو اندراج کر کے داخل نوشتہ ہونا لازم ہے۔', 
    ...         pango_view='/opt/local/bin/pango-view',
    ...         output='/Users/jd/Desktop/urdu_works.png',
    ...         width=538)
    0

![image of text](/j2labs/pyango_view/raw/master/docs/images/urdu_works.png)

It can handle newlines and print programming code nicely.

    >>> text = """
    ... >>> def foo():
    ... ...     print 'foo foo foo foo foo'
    ... ...
    ... >>>
    ... """
    >>> text
    "\n>>> def foo():\n...     print 'foo foo foo foo foo'\n...\n>>>\n"
    >>> str2img(text, font='Courier New', output='/Users/jd/Desktop/programming_code.jpg')
    0

![image of text](/j2labs/pyango_view/raw/master/docs/images/programming_code.jpg)
    
Install
-------

python ./setup.py install

James Dennis <<jd@j2labs.net>>
