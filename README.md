Pyango View
===========

Pyango View is a Python library for calling pango-view.

Pyango View is licensed under the [Apache Licence, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)

Features
--------

Pyango View is simply a mapping and some pythonish documentation for accessing the pango-view command line tool.

Goopytrans supports translating a single body of text.

    >>> str2img('texty text', font='Courier New')
    0

<a href="/j2labs/pyango_view/raw/master/docs/images/textytext.png"><img src="/j2labs/pyango_view/raw/master/docs/images/shrunk/textytext.png" /></a>

Urdu works nicely. Pango is very robust!

    >>> str2img('اس صفحہ کو ترامیم کیلیۓ نـیـم محفوظ کر دیا گیا ہے اور صارف کو اندراج کر کے داخل نوشتہ ہونا لازم ہے۔', 
    ...         pango_view='/opt/local/bin/pango-view',
    ...         output='/Users/jd/Desktop/urdu_works.png',
    ...         width=538)
    0

<a href="/j2labs/pyango_view/raw/images/urdu_works.png"><img src="/j2labs/pyango_view/raw/master/docs/images/shrunk/urdu_works.png" /></a>

It can handle newlines and print programming code nicely.

    >>> text = """
    ... >>> def foo():
    ... ...     print 'foo foo foo foo foo'
    ... ...
    ... >>>
    ... """
    >>> text
    "\n>>> def foo():\n...     print 'foo foo foo foo foo'\n...\n>>>\n"
    >>> str2img(text, font='Courier New', output='/Users/jd/Desktop/couriernew.jpg')
    0

<a href="/j2labs/pyango_view/raw/images/programming_code.png"><img src="/j2labs/pyango_view/raw/master/docs/images/shrunk/programming_code.png" /></a>
    
Install
-------

python ./setup.py install

James Dennis <<jd@j2labs.net>>
