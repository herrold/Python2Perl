#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from subset2 import Subset2
from grammar import CallExpr, BinaryOperator, NumExpr, Operator, PerlType, NameExpr, AttributeExpr, StrExpr
    
class Subset3(Subset2):
    '''
    Implements the requirements of subset 3.
    '''
    def rewrite_range(self, args):
        '''
        Defines the rewrite rule for the range method.
        '''
        op = Operator(op='..')
        left = args[0]
        right = NumExpr(value=args[1].value-1)
        return BinaryOperator(op=op, left=left, right=right,
                              perl_type=PerlType.ARRAY)
    
    def rewrite_len(self, args):
        '''
        Defines the rewrite rules for the len method.
        '''
        return CallExpr(name='scalar', args=args, suffix='',
                        perl_type=PerlType.SCALAR)
    
    def rewrite_sorted(self, args):
        '''
        Defines the rewrite rules for the sorted method.
        '''
        return CallExpr(name='sort', args=args, suffix='',
                        perl_type=PerlType.ARRAY)


    def rewrite_append(self, args):
        '''
        Defines the rewrite rules for the append method.
        '''
        return CallExpr(name='push', args=args, suffix='',
                        perl_type=PerlType.SCALAR)

    def rewrite_keys(self, args):
        '''
        Defines rewrite rules for the keys method. This actually
        just attaches a type signature.
        '''
        return CallExpr(name='keys', args=args, suffix='',
                        perl_type=PerlType.ARRAY)

    def rewrite_open(self, args):
        '''
        Preforms a rewrite rule on the open function in python.
        '''
        # Set up mode translations between python and perl.
        modes = {
                    "r" : "<", # Read translation.
                    "w" : ">", # Write translation.
                    "a" : ">>" # Append translation.
                }
        # Holds the translated arguments.
        new_args = []
        # Parse the python arguments into perl arguments.
        if len(args) == 2:
            new_args.append(args[0])
            if args[1].value in modes.keys():
                new_args.append(StrExpr(value=modes[args[1].value]))
        elif len(args) == 1:
            new_args.append(args[0])
            new_args.append(StrExpr(value=modes["r"]))
        # Return a call expression, that contains the new perl open.
        return CallExpr(name='open', args=new_args, suffix='',
                        perl_type=PerlType.SCALAR)

    def visit_Call(self, node):
        '''
        A call represents any call to  a function. The standard library
        is quite large and we cannot convert it all so we do it on a case by
        case basis.
        '''
        # Retrieve the function name.
        func = self.visit(node.func)
        # Retrieve the function arguments.
        args = [self.visit(arg) for arg in node.args]
        # For this rewriting system attributes are culled into
        # function calls, so we just pull the parent as arguments.
        if isinstance(func, AttributeExpr):
            if func.value:
                args = [func.value] + args
        dispatch = { 'range' : self.rewrite_range,
                     'len' : self.rewrite_len,
                     'sorted' : self.rewrite_sorted,
                     'append' : self.rewrite_append,
                     'keys' : self.rewrite_keys,
                     'open' : self.rewrite_open
                   }

        # Attempt to rewrite the specific function. 
        if func.name in dispatch:
            return dispatch[func.name](args)

        # If we cannot find it just try rewrite it in perl.
        return CallExpr(name=func.name, args=args, suffix='')

    def visit_Attribute(self, node):
        # Retrieve the name.
        name = node.attr
        # Retrieve the value.
        value = self.visit(node.value)
        return AttributeExpr(name=node.attr, value=value)
