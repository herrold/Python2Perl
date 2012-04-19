#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

import ast

class Parser(ast.NodeVisitor):
    def visit_Str(self, node):
        print(node.s)

