#!/usr/bin/python
# -*- indent-tabs-mode: nil; tab-width: 4 -*-
# vi: et ts=4 sts=4 sw=4

'''
Use OptionParser to parse arguments, with callback action to process complicated args.
'''

import os
import datetime
from optparse import OptionParser

# http://stackoverflow.com/questions/4542352/python-import-from-parent-directory
PARENTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, PARENTDIR)
from utils import get_env, parse_dsn

def main():
    parser = OptionParser()
    parser.add_option('-e', '--env', default=get_env(), choices=['dev', 'stg', 'prd', 'dr'])
    parser.add_option('-n', '--networks', default=[], action='callback', callback=store_list, type='string', help='comma separated list of network ids; default: all (see below)')
    parser.add_option('-w', '--working-dir', default='.')
    parser.add_option('-i', '--dsn', default={}, action='callback', callback=store_dsn, type='string', help='data source, e.g. "host=localhost&port=3306&user=qa&passwd=...&db=fwmrm_rpt"')
    parser.add_option('-o', '--output-dir', default='.', help='upload revenue file to OUTPUT_DIR/partner_revenue_data/pending/, e.g. /mnt/sftponly/ or ads@rpm-ftp01:/home/sftponly/')
    parser.add_option('--to', help='notification email recipients')
    parser.add_option('--today', default=datetime.date.today(), action='callback', type='string', callback=store_date, help='YYYYMMDD')
    parser.add_option('--no-0', action='store_true', help='no output 0-revenue lines')
    (opts, args) = parser.parse_args()

def store_list(option, opt_str, value, parser):
    setattr(parser.values, option.dest, value.split(','))

def store_dsn(option, opt_str, value, parser):
    try:
        setattr(parser.values, option.dest, parse_dsn(value))
    except ValueError, e:
        parser.error('option %s: %s' % (option, e))

def store_date(option, opt_str, value, parser):
    try:
        setattr(parser.values, option.dest, datetime.datetime.strptime(value, '%Y%m%d').date())
    except ValueError, e:
        parser.error('option %s: %s' % (option, e))

if __name__ == '__main__':
    main()

