#!/usr/bin/env python

import argparse
import dateutil.parser
parser = argparse.ArgumentParser(description='The Constant Frobulator')
parser.add_argument('-name', required=True,
                    help='The name of frobulator')
parser.add_argument('-age', required=True,
                    type=int,
                    help='The age of frobulator')
parser.add_argument('-date', required=True,
                    type=dateutil.parser.parse,
                    help='The precise date frobulation began')
args = parser.parse_args()
print(args)
