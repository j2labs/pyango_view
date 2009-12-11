#!/usr/bin/env python

import sys
import subprocess

PANGO_VIEW="/opt/local/bin/pango-view"
DEFAULT_FONT="Helvetica"
DEFAULT_OUTPUT="viewb.png"
DEFAULT_WIDTH=538
DEFAULT_WRAP='word'

def str2img(text, pango_view=PANGO_VIEW, font=DEFAULT_FONT, output=DEFAULT_OUTPUT, width=DEFAULT_WIDTH, wrap=DEFAULT_WRAP):
    """
    This funciton takes a string and creates an image from that string using
    the executable `pango-view`. It can take multiple options.

    pango_view :: The full path to where pango-view is installed.
    font       :: The name of the font
    output     :: This is the name of the file to create.
    width      :: Pango defaults to as much width as necessary unless you
                  set one.
    wrap       :: The default wrap for use if a width is set.
    
    """
    cmd_list = []
    cmd_list.append('%s' % pango_view)
    cmd_list.append('--output="%s"' % output)
    cmd_list.append('--font="%s"' % font)
    cmd_list.append('--no-display')
    cmd_list.append('--width=%s' % width)
    cmd_list.append('--wrap=%s' % wrap)
    cmd_list.append('--text="%s"' % text)
 
    try:
        retcode = subprocess.call(' '.join(cmd_list), shell=True)
        return retcode
    except OSError, e:
        print >>sys.stderr, "Error :: ", e
        raise


if __name__ == "__main__":
    str2img('This is some text for an example', output="awesome.jpg")
