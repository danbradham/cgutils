# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
cgutils search_replace
======================
Find a pattern in all filenames in the current directory and replace it. Be careful...

Usage::

    cgutils search_replace new old

Here a file named new.01.exr in the current working directory would be renamed to old.01.exr.
'''

from ..packages import click
import sys
import os


def search_replace(search_str, replace_str, root):
    for root, subdirs, files in os.walk(root):

        print '\nINSIDE: ', root

        for f in files:
            if search_str in f:

                source = os.path.join(root, f)
                dest_name = f.replace(search_str, replace_str)
                dest = os.path.join(root, dest_name)

                try:
                    os.rename(source, dest)
                    print '    {} -> {}'.format(f, dest_name)
                except OSError:
                    print '    FAILED ', '{} -> {}'.format(f, dest_name)


@click.command()
@click.argument('search_str')
@click.argument('replace_str')
def cli(search_str, replace_str):
    '''Find a pattern in all filenames in the current directory and replace it.

    Example::

        cgutils search_replace new old

    Here a file named new.01.exr would be renamed to old.01.exr
    '''

    confirm_msg = 'Search for {} and replace with {}?'
    do_it = click.confirm(confirm_msg.format(search_str, replace_str))

    if do_it:
        search_replace(search_str, replace_str)


if __name__ == '__main__':
    cli()
