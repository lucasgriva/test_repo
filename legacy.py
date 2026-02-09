#!/usr/bin/env python
# -*- coding: utf-8 -*-

# In Python 2, strings are ASCII by default. 
# The line above is often required to handle non-ASCII characters.

import sys

def legacy_function():
    # 1. Print is a statement, not a function (no parentheses required)
    print "Starting legacy script..."

    # 2. Integer division returns an integer (3/2 = 1)
    # In Python 3, this would be 1.5
    result = 3 / 2
    print "3 / 2 =", result

    # 3. Handling User Input
    # 'input()' in Python 2 actually evaluates the code. 'raw_input()' is used for strings.
    name = raw_input("Enter your name: ")
    print "Hello, " + name

    # 4. Old-style classes (don't inherit from 'object') vs New-style
    class LegacyData:
        pass

def check_iteration():
    # 5. xrange vs range
    # 'range' creates a full list in memory. 'xrange' is the lazy generator.
    for i in xrange(5):
        print "Iteration:", i

if __name__ == "__main__":
    legacy_function()
    check_iteration()
