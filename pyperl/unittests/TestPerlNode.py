#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

import unittest
import pyperl.grammar.Token

class TestToken(unittest.TestCase):
    '''
    Defines a series of tests, against the valid tokens required.
    '''
    def test_print(self):
        '''Tests perl print tokens.'''
        token = PrintToken(prefix=Perl.PRINT_STMT, block=perl.ARG_BLOCK, args=[1,2], sep=perl.ARG_SEP);
        self.assertEquals(token, 'print(1, 2);')
    def test_assigment(self):
        '''Tests perl assignment tokens.'''
    def test_expression(self):
        '''Test basic perl expressions.'''
    def test_if(self):
        '''Test basic perl if statements.'''
    def test_while(self):
        '''Test basic perl while statements.'''
    def test_foreach(self):
        '''Test basic perl foreach statements.'''
    def test_sub(self):
        '''Test basic perl sub statements.'''

if __name__ == '__main__':
    # A series of tests.
    pass
