#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from perl_node import PerlNode

class Statement(PerlNode):
    '''
    A statement is defined generally of anything that can consist of
    multiple lines, function definitions, if statements etc. Generally
    having a block. But really in perl any statment must evaluate to 
    value.
    '''
    def __init__(self, prefix='', suffix='', sep=(''), args=[], row=0, col=0):
        self.prefix = prefix
        self.suffix = suffix
        self.sep = sep
        self.args = args
        self.row = row
        self.col = col  
