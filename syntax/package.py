#!/usr/bin/python
# -*- indent-tabs-mode: nil; tab-width: 4 -*-
# vi: et ts=4 sts=4 sw=4

#from submodule import *    // ModuleTwo is invisible using *, as submodule.__all__ doesn't contain it. 

from submodule import ModuleTwo
from submodule import ModuleOne
#from submodule import ModuleThree    //Not import in submodule/__init__.py, so can't import outside

def main():
    print globals()
    ModuleOne()
    ModuleTwo()

if __name__ == '__main__':
    main()

