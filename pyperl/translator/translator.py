#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)
# My solution works on parsing an abstract syntax tree and working with
# each requirement as a sub-tree. (>^_^)> CAN HAZ MARKS?

import ast

class Translator(ast.NodeVisitor):
    '''
    The translator is the base class which all translators inherit from.
    It simply applies a DFS (Depth First Search) against the entire AST with
    a generic visit method. As objects inherit they overwrite certain visit
    functions, adding more rewrite rules. The goal is to introduce a cascading
    system that adds functionality for each subset and expands as it goes along.
    '''
    def __init__(self):
        print '#!/usr/bin/perl -w'
    def generic_visit(self, node):
       #print(type(node).__name__)
       ast.NodeVisitor.generic_visit(self, node)

if __name__ == '__main__':
    translator = Translator()
    source = '''
#!/usr/bin/python
answer = ''.join([1, 2, 3])
print answer
'''
    tree = ast.parse(source)
    parser.visit(tree)
