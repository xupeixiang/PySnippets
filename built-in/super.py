#!/usr/bin/python
# -*- indent-tabs-mode: nil; tab-width: 4 -*-
# vi: et ts=4 sts=4 sw=4

# Ref:https://fuhm.net/super-harmful/

def main():
    print "F MRO:", [x.__name__ for x in F.__mro__]
    F()
    print "C2 MRO:", [x.__name__ for x in C2.__mro__]
    C2()

class A(object):
    def __init__(self):
        print "enter A"
        super(A, self).__init__()  # need in diamond inheritance
        print "leave A"

class B(object):
    def __init__(self):
        print "enter B"
        super(B, self).__init__()  # need in diamond inheritance
        print "leave B"

class A2(object):
    def __init__(self):
        print "enter A2"
        #super(A2, self).__init__()  # no need in simple inheritance
        print "leave A2"

class C(A):
    def __init__(self):
        print "enter C"
        super(C, self).__init__()
        print "leave C"

class C2(A2):
    def __init__(self):
        print "enter C2"
        super(C2, self).__init__()
        print "leave C2"

class D(A):
    def __init__(self):
        print "enter D"
        super(D, self).__init__()
        print "leave D"

class E(B, C):
    def __init__(self):
        print "enter E"
        super(E, self).__init__()
        print "leave E"

class F(E, D):
    def __init__(self):
        print "enter F"
        super(F, self).__init__()
        print "leave F"

if __name__ == '__main__':
    main()

