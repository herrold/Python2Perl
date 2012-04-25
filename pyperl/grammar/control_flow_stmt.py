#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from statement import Statement
from itertools import cycle

class ControlFlowStmt(Statement):
    '''Generic statement for implementing control flow statements.'''

    def __init__(self, row=0, col=0, keyword='', condition=None,
                cond_sep=cycle(('(',')')), body=None, orelse=None):
        '''Minimizes what is required of a typical flow control statement'''
        super(ControlFlowStmt, self).__init__(row=row, col=col)
        self.keyword = keyword
        self.body = body
        self.condition = condition
        self.block = cycle(('{\n','\n}'))
        self.cond_sep = cond_sep
        self.orelse = orelse

    def __repr__(self):
        '''Builds a generic rep of a control flow statement in perl'''
        # Set up the keyword.
        rep = self.keyword
        rep += ' ' + self.cond_sep.next()
        if self.condition:
            rep += repr(self.condition)
        rep += self.cond_sep.next() + ' '
        # Start the block
        rep += self.block.next()
        # Convert the body, line by line into a string.
        #rep += '\n'.join(map(repr, self.body))
        indented_body = [' ' * node.col + repr(node) for node in self.body]
        rep += '\n'.join(indented_body)
        # Close the block
        rep += self.block.next()
        # Deal with each optional else, or elif
        '''
        for node in self.orelse:
            if type(node) == IfStmt:
                rep += repr(node)
            else:
                rep += repr(ControlFlowStmt(keyword=' else',
                        cond_sep=cycle(('','')), body=self.orelse,
                        col=0))
                break
        '''
        # Return the rep
        return rep 
