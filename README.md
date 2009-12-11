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

Urdu works nicely. Pango is very robust!

    >>> str2img('اس صفحہ کو ترامیم کیلیۓ نـیـم محفوظ کر دیا گیا ہے اور صارف کو اندراج کر کے داخل نوشتہ ہونا لازم ہے۔', 
    ...         pango_view='/opt/local/bin/pango-view',
    ...         output='/Users/jd/Desktop/urdu_works.png',
    ...         width=538)
    0

Install
-------

python ./setup.py install


James Dennis <<jd@j2labs.net>>
