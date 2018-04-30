#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
import time
import click
import logging

from ofxstatement.ofx import OfxWriter
# TODO Can't import ofxstatement.ofx here or ofxstatement.parser in argenta
from ofxstatement.plugins import argenta

@click.command()
@click.argument('path')
@click.option('--debug', is_flag=True, default=False)
def convert(path, debug):
    """Parse and write transactions from Argenta downloadTransactionHistoryXLS.xlsx file."""

    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
    
    root, ext = os.path.splitext(path)
    date_suffix = time.strftime("-%y%m%d")
    output_file = root + date_suffix + '.ofx'

    parser = argenta.ArgentaPlugin(ui=None, settings=None).get_parser(path)
    statement = parser.parse()

    if debug:
        for line in statement.lines:
            print(line)
        return

    with open(output_file, 'w') as out:
        writer = OfxWriter(statement)
        out.write(writer.toxml())
    
    path_new = root + date_suffix + ext
    os.rename(path, path_new)

if __name__ == '__main__':
    convert()
