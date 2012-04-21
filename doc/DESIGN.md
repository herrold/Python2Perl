DESIGN
------
Overview
--------
When dealing with languages you can parse it directly by understanding
its grammar or you can approach it from a higher level and work with
manipulating the abstract grammar. Python offers a utility module
called ast (abstract syntax tree) that allows you to traverse (through a
depth first search) any inputted python program. Each "node" in this
tree can consist of a number of children. This approach keeps things
idiomatic to python and means I do not have to reinvent the wheel to
build something useful.

The core of my solution essentially preforms this DFS on the tree and
preforms a rewrite rule for each "known" ADSL component and places it
in a second Perl Abstract Syntax Tree. After travelling through the
entire Python Abstract Syntax Tree (assuming it is within the subset
we have specified) a complete valid Perl AST Tree will
also be generated that matches the same form as that of Python. Each
node of the Perl AST is responsible for compiling
itself into a valid "syntax" and so by chaining these together you
generate a Perl script that is equivelant to that of the python
program.

Modules
--------
The project is split into two distinct modules, translator and
grammar.

Grammar
-------
The grammar component defines a series of perl "nodes"
that relate to expressions and statements that are required
to build the Perl AST (on the given subset). These include
for example PrintStmt which is a class that takes a series of
arguments and generates a valid Perl print statement. This
approach keeps things very formal, yet flexible and allows
manipulating with Perl Abstract Syntax from within Python
while retaining important type information.

This type based approach ensures  less errors then simply
manipulating a string which has no restrictions on what
can be modified.

Translator
-----------
The translator is based off the python module ast.NodeVisitor and provides
the basic generic means to visit each node in the tree. Then, each subset
inherits the previous subset with subset0 directly inheritting from this
translator. This allows me to build a cascading system that builds on
the work of previous subsets. The goal is to use an agile methodology
that forces me to get everything in a previous subset working before
I add more :).
