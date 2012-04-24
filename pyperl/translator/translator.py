#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)
# My solution works on parsing an abstract syntax tree and working with
# each requirement as a sub-tree. (>^_^)> CAN HAZ MARKS?

import ast
from grammar import CommentStmt

class Translator(ast.NodeVisitor):
    '''
    The translator is the base class which all translators inherit from.
    It simply applies a DFS (Depth First Search) against the entire AST with
    a generic visit method. As objects inherit they overwrite certain visit
    functions, adding more rewrite rules. The goal is to introduce a cascading
    system that adds functionality for each subset and expands as it goes along.
    '''
    def __init__(self, debug=False):
        # Sets the debugging information.
        self.debug = debug
    
    def translate(self, input_path):
        '''Preforms the translation on the python source code.'''
        # Load the initial data into the buffer.
        self.buffer = [CommentStmt(value='!/usr/bin/perl -w', row=0)]
        # Load the inputted python source code.
        python_source = open(input_path, 'rU').read()
        # Convert the python source code into an AST representation.
        tree = ast.parse(python_source)
        # Visit every node in the tree.
        self.visit(tree)
        # Converts the grammar buffer into a string representation.
        perl_source = '\n'.join(map(repr, self.buffer)) 
        return perl_source
    
    def generic_visit(self, node):
       print(type(node).__name__)
       ast.NodeVisitor.generic_visit(self, node)
