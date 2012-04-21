#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

import ast

class PerlNode(ast.AST):
    '''
    A node defines a generic component of a abstract domain specific language.
    It is the base class of all other nodes. The goal is to add more and more
    specific nodes to this heirarchy as they are required. This models off a
    similar approach to pythons ADSL but for perl. Clearly perl 5 has no
    strictly defined abstract grammar, but it will suffice for the subset
    I am working with.
    '''

    def __init__(self):
        super(PerlNode, self).__init__()


if __name__ == '__main__':
    node = PerlNode()
    print node.lineno
