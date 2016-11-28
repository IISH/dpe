#!/usr/bin/python

import urllib2 
import simplejson
import json
from dataverse import Connection
import sys
import os
import re
from datetime import datetime
from subprocess import Popen, PIPE, STDOUT
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../modules')))
from config import configuration
from searchapi import search_by_keyword, search_by_handles, get_datasets_from_html

def loadjson(apiurl):
    jsondataurl = apiurl
    
    req = urllib2.Request(jsondataurl)
    opener = urllib2.build_opener()
    f = opener.open(req)
    dataframe = simplejson.load(f)
    return dataframe

config = configuration()
handle = "hdl:10622/DRIPQL"
handle = "hdl:10622/G5L8IO"
handle = "SAK48Q"

connection = Connection(config['hostname'], config['key'])
s = {}
s['q'] = 'gdp'
#s['q'] = "hdl:10622/EXA3CI hdl:10622/PU9ETX"
s['q'] = "QBACC4 XNGK4X KCBMKI SPBP7D AOQMAZ SO62N5 DG654S 4ZDPWP ORW1HI JQJIP6 GI7D06 DONJXY KORKQW N6BLB8 KC0ZHV G5L8IO 8FCYOX OTHFUK T2BLXB BSS0NQ MRQ2XJ MX7AIJ IAEKLA HKZPR9 VHYIAT FMI6L9 6OHMDS H83HEV UJ3H1Q Z5HDBU 2KHSYM QK8VRF XYJ2H2 LKWIXZ CYRM1P K879JA RA3SLU VCTVKE ZGRJQY NJ9PTI H4C6B7 M0PI4D GEQKCG 9J8MJG V6AEFF UOKWUF ACOPHR KRWHME HOPFWK OS5A57 RVRFKS EPD5LB OX6FCP IRT0YU WOTROV W2CS9J CCYQY7 UQV70P LKYT53 NKAQPL FHU70A W7GOD6 KN40ZF YXFPRL SNETZV RPUJDO RV5NJG Y9G2ZV KVRJPW KICLW5 LZ0Y36 NMYPT2 UEALPE 2EM9DE PU9ETX IHPUXP EXA3CI QZQOAO"
s['show_facets'] = 'true'
metadata = search_by_keyword(connection, s)
#metadata = search_by_handles(connection, s)
#print str(metadata)

action = 'gethandle'
#action = 'getlist1'
dv = "clioinfra"
dv = "labourconflicts"
#dv = "Micro"
#dv = "Aggregate"
dataverse = connection.get_dataverse(dv)
activedataverse = False

if action:
    if dataverse.get_contents():
        item = dataverse.get_contents()[0]
        try:
           if item['identifier']:
               activedataverse = True
        except:	
           activedataverse = False
    else:
        activedataverse = False

    if activedataverse:
        dothings = 'yes'
    else:
        query = get_datasets_from_html(config['dataverseroot'], dv)
        s['q'] = query
        metadata = search_by_keyword(connection, s)
        for item in metadata['items']:
	    print str(item)

a = datetime.now()
handles = ''
if action == 'getlist':
    for item in dataverse.get_contents():
	handles = handles + item['identifier'] + ' '
        # u'protocol': u'hdl', u'authority': u'10622' u'identifier': u'R8EJJF'
	#print item['id']
        try:
            handle = str(item['protocol']) + ':' + str(item['authority']) + "/" + str(item['identifier'])
            datasetid = item['identifier']
            #url = str(config['dataverseroot']) + "/api/datasets/" + str(datasetid) + "/versions/1.0?&key=" + str(config['key'])
	    #dataframe = loadjson(url)
            #for fileitem in dataframe['data']['files']:
	        #print fileitem
	    print handles
        except:
	    skip = 1
elif action == 'gethandle':
    #datasets = dataverse.get_datasets()
    datasets = dataverse.get_dataset_by_string_in_entry(handle)
    print handle
    #datasets = dataverse.get_dataset_by_doi(handle)
    print datasets.get_metadata()
    x = ''
    if x:
        for item in datasets:
  	    x = item.get_metadata()
	    print str(x)
	    b = datetime.now()
	    d = b - a
	    print "Download time: " + str(d.seconds) + " seconds"
	    #info = item.get_contents()
	    #print info['identifier']
	    #print item.id
	    #print item.title
	    #print item.edit_uri
	    #print "\n"
        #files = dataset.get_files('latest')
        #print files
b = datetime.now()
d = b - a
print "Download time: " + str(d.seconds) + " seconds"
