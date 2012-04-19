#!/usr/bin/env python

import argparse

class PyPerl:
    '''Parse command line arguments, and translates python to perl.'''
    def __init__(self, cmd_arguments):
        self.parse_cmd(cmd_arguments)
    def parse_cmd(self, cmd_arguments):
        '''Parses the command line arguments and delegates.'''
        return NotImplemented
    def translate(self):
        return NotImplemented

if __name__ == '__main__':
    # Creates the command line parser.
    parser = argparse.ArgumentParser(description='Python to Perl Translator.')
    # Populate the parser with arguments.
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    # Retrieve Valid Arguments.
    cmd_arguments = parser.parse_args()
    # Parse the arguments to PyPerl.
    pyperl = PyPerl(cmd_arguments)
    # Translate the program.
    pyperl.translate()
