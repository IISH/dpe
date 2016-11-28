#!/usr/bin/python

from __future__ import absolute_import
from pymongo import MongoClient
import json
import sys
import os
import re
import simplejson
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname("__file__"), '../')))
from cliocore.storage import Storage
from sys import argv

script, action, keyword = argv

database = 'datasets'
storage = Storage(database)

if action == 'keyword':
    field = 'units'
    d = storage.search_by_key(field, keyword)
    for x in d:
        print "%s - %s (%s)" % (x['title'], x['units'], x['handle'])

elif action == 'list':
    handles = []
    handle = "hdl:10622/4X6NCK"
    handles.append(handle)
    handle = "hdl:10622/I0YK5M"
    handles.append(handle)
    handle = "hdl:10622/CSNWOF"
    handles.append(handle)
   
    key = "handle"
    val = handles[2]
    print val
    result = storage.readdata(key, val)
    for x in result:
        print "%s - %s (%s)" % (x['title'], x['units'], x['handle'])

