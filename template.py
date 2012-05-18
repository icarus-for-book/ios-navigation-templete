#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import shutil

kThisDir = os.path.dirname(os.path.abspath(sys._getframe(0).f_code.co_filename))

def cmd_install():
    os.system('cp -R "%s"/Templates ~/Library/Developer/Xcode' % kThisDir )

    print 'installed template files'

def cmd_uninstall():
    # remote template folders
    os.system('rm -rf ~/Library/Developer/Xcode/Templates/Project\ Templates/Application/Navigation-based\ Application\ for\ ios4.xctemplate')
    os.system('rm -rf ~/Library/Developer/Xcode/Templates/Project\ Templates/Application/Split\ View-based\ Application\ for\ ios4.xctemplate')
    os.system('rm -rf ~/Library/Developer/Xcode/Templates/Project\ Templates/TemplateForiOS4')

    print 'uninstalled template files'

def usage_exit(status=0):
    print '''\

usage:  python template.py <command>

command : 
  * install   : install template files
  * uninstall : uninstall template files

 '''
    exit(status)

def main(argv):
    
    if len(argv) != 1:
        usage_exit(1)

    cmd = argv[0]
    
    func = globals().get('cmd_'+cmd, None)
    if not func or not callable(func):
        usage_exit(1)

    func()


if __name__ == '__main__':
    main(sys.argv[1:])
