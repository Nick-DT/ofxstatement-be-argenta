#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import click
import logging

from ofxstatement.ofx import OfxWriter
from ofxstatement.plugins import argenta

@click.command()
@click.argument('path')
@click.option('--debug', is_flag=True, default=False)
def convert(path, debug):
    """Parse and write transactions from Argenta downloadTransactionHistoryXLS.xlsx file."""

    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

    with argenta.ArgentaPlugin(ui=None, settings=None).get_parser(path) as parser:
        statement = parser.parse()

    if debug:
        for line in statement.lines:
            print(line)
        return
    
    date_suffix = statement.lines[-1].date.strftime("-%y%m%d")
    ext = os.path.splitext(path)[1]
    dir = os.path.dirname(path)
    base_filename = os.path.join(dir, statement.account_id + date_suffix)
    output_file = base_filename + '.ofx'

    with open(output_file, 'w') as out:
        writer = OfxWriter(statement)
        out.write(writer.toxml())
        
    path_new = base_filename + ext
    os.rename(path, path_new)

if __name__ == '__main__':
    convert()
