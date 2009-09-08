#!/usr/bin/env python
# -*- coding: utf-8 -*-
# haraldupdate.py
# September 2009
# Terence Stenvold <tstenvold@gmail.com>
#
#Updating script for the running of harald scan

#This file is part of Haraldscan.
#
#Haraldscan is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License Version 3 as
#published by the Free Software Foundation.
#
#Haraldscan is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License Version 3 for more details.
#
#You should have received a copy of the GNU General Public License
#Version 3 along with Haraldscan.  If not, see <http://www.gnu.org/licenses/>.

import haraldsql
import sys,os
import urllib


def reporthook(*a): print a


def check_now():

    rlines = 0
    llines = 0
    
    flocal = open('MACLIST', 'rb')
    
    for line in flocal:
        llines+=1
        
    print llines

    url = 'http://haraldscan.googlecode.com/svn/trunk/MACLIST'
    fweb = urllib.urlopen(url)
    
    for lines in fweb.readlines():
        rlines+=1
        
    print rlines
        
    if rlines > llines:
        urllib.urlretrieve(url, 'MACLIST', reporthook)
        print "Updated MACLIST Retrieved"
        print "Rebuilding Database Now"
        return True
        
    return False

if __name__ == '__main__':
  haraldusage.usage()