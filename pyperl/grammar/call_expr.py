#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from expression import Expression
from itertools import cycle

class CallExpr(Expression):
    '''
    A call expression in perl relates to any method that uses a function
    call, open(), print() are some examples of expressions that would relate
    to this.
    '''
    def __init__(self, name='', args=[], suffix=';', row=0, col=0):
        super(CallExpr, self).__init__(row=row, col=col)
        self.name = name
        self.args = args
        self.suffix = suffix
        self.block = cycle(('(',')'))
        self.sep = cycle((','))

    def __repr__(self):
        # Generate the block for the representation.
        params = self.block.next()
        for arg in self.args[:-1]:
                params += repr(arg) + self.sep.next() + ' '
        params += repr(self.args[-1])
        params += self.block.next()
        # Create the final representation
        rep = ' ' * self.col + self.name + params + self.suffix
        return rep

if __name__ == '__main__':
    from str_expr import StrExpr
    print CallExpr(name='print', args=[StrExpr(s="Hello World"), StrExpr(s=r"\n")])
    
