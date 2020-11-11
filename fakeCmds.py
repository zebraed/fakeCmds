#! /usr/bin/ python
# -*- coding:utf-8 -*-
# vim:fenc=utf-8
# name: faceCmds.py
# Created: <2020-10-21>

import sys

import _funcs
class fakeCmds(object):
    cmds = _funcs

class maya(fakeCmds):
    pass

sys.modules['package.module'] = fakeCmds