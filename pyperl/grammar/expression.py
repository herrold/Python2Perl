#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from perl_node import PerlNode

class Expression(PerlNode):
    '''
    An expression is anything in Perl that can be boiled down to some
    value. These include most notably basic operations like 4 + 2 or
    even just a string.
    '''
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col  
