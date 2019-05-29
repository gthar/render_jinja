#!/usr/bin/env python3

"""
Render Jinja2 templates.
Variables to use in the template are specified as optional command-line options
(i.e., foo=x).

Usage:
    render_jinja <input_file> [options] [<variables>...]
    render_jinja (-h | --help)

Arguments:
    input_file             Input file. Jinja2 expected.

Options:
    -h --help              Show this screen.
    -o FILE --output=FILE  File where the output will be saved
"""


import os

import docopt
import jinja2


def render_template(path, kwargs):
    """
    Render from a template file and a dictionary of kwargs
    """
    dirname, fname = os.path.split(path)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(dirname))
    out_str = env.get_template(fname).render(**kwargs)

    return out_str


def main():
    """
    Parse the arguments and do the thing
    """
    args = docopt.docopt(__doc__)
    kwargs = dict(x.split('=') for x in args['<variables>'])
    out_str = render_template(args['<input_file>'], kwargs)

    if args['--output'] is None:
        print(out_str)
    else:
        with open(args['--output'], 'w') as out_fh:
            out_fh.write(out_str + '\n')

    return 0
