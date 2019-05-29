#!/usr/bin/env python

from setuptools import setup

if __name__ == '__main__':
    setup(
        name='render_jinja',
        version='1.0',
        description='Standalone script to Render Jinja2 templates.',
        author='Ricard Illa',
        author_email='r.illa.pujagut@gmail.com',
        url='https://github.com/gthar/render_jinja',
        py_modules=['render_jinja'],
        entry_points={'console_scripts': ["render_jinja=render_jinja:main"]},
        install_requires=['docopt', 'jinja2'])
