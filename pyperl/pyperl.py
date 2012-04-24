#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.21 (ISO 8601)

import argparse
from translator import subsets

class PyPerl:
    '''
    PyPerl is the core class of the translator. It parses the command line
    arguments and provides this information to the selected translator which
    parses the python script returning the perl source code which is then
    written to the corresponding address.
    '''
    def __init__(self):
        '''Parse command line arguments, and translates python to perl.'''
        parser = argparse.ArgumentParser(description='Python to Perl Translator.')
        parser.add_argument('--version', action='version', version='%(prog)s 1.0')
        parser.add_argument('-i', action='store', dest='input', default='/dev/stdin',
                            help='The python source file you wish to convert. Defaults to stdin.')
        parser.add_argument('-o', action='store', dest='output', default='/dev/stdout',
                            help='The path to the perl source file you wish to ouput to Defaults to stdout.')
        parser.add_argument('-s', action='store', dest='subset', type=int, default=5,
                            help='The subset of the translator you wish to use [0-5]. Defaults to 5')
        parser.add_argument('-d', action='store_true', dest='debug', default=False,
                            help='Enables debugging information outputted to stderr.')
        self.cmd_args = parser.parse_args()
        # Ensure that the subset is within a valid range.
        if self.cmd_args.subset not in range(6):
            self.cmd_args.subset = 5
    
    def translate(self):
        '''Translates the python source code into perl.'''
        try:
            # Select the appropriate translator.
            subset_translator = subsets[self.cmd_args.subset]
            translator = subset_translator(self.cmd_args.debug)
            # Preform the translation
            perl_source = translator.translate(self.cmd_args.input)
            # Open the output file and write the perl source code.
            with open(self.cmd_args.output, 'w') as f:
                f.write(perl_source)
        except IOError:
            # Output a message if there is an exception.
            print("The inputted files couldn't be found and / or accessed.")

if __name__ == '__main__':
    # Parse the arguments to PyPerl.
    pyperl = PyPerl()
    # Translate the program.
    pyperl.translate()
