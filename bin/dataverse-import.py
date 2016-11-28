#!/usr/bin/python

import urllib2 
import simplejson
import json
from dataverse import Connection
import sys
import os
from subprocess import Popen, PIPE, STDOUT
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../modules')))
from config import configuration

def loadjson(apiurl):
    jsondataurl = apiurl
    
    req = urllib2.Request(jsondataurl)
    opener = urllib2.build_opener()
    f = opener.open(req)
    dataframe = simplejson.load(f)
    return dataframe

config = configuration()
host = "datasets.socialhistory.org"
token = config['key']
connection = Connection(host, config['key'])
dataverse = connection.get_dataverse('clioinfra')

thishandle = "QBACC4"
for item in dataverse.get_contents():
    handle = str(item['protocol']) + ':' + str(item['authority']) + "/" + str(item['identifier'])
    #print handle
    # u'protocol': u'hdl', u'authority': u'10622' u'identifier': u'R8EJJF'
    if item['identifier'] == thishandle:
        handle = str(item['protocol']) + ':' + str(item['authority']) + "/" + str(item['identifier'])
        datasetid = item['id']
        url = "https://" + str(host) + "/api/datasets/" + str(datasetid) + "/?&key=" + str(token)
        #url = "https://" + str(host) + "/api/datasets/" + str(datasetid) + "/versions/1.0?&key=" + str(token)
	#url = "https://" + str(host) + "/api/datasets/" + str(datasetid) + "/versions/1.0?&key=" + str(token)
	print url
        print item
	dataframe = loadjson(url)
	try:
	    index = dataframe['data']['latestVersion']['files']
	except:
	    index = dataframe['data']['files']

        for fileitem in index:
	    runimport = os.path.abspath(os.path.join(os.path.dirname(__file__)))
	    runimport = str(runimport) + "/import.py -d 'https://" + str(host) + "' -H '" + str(handle) + ":" + str(datasetid) + ":" + str(fileitem['datafile']['id']) + "' -k " + str(token)
	    print runimport
	    print fileitem['datafile']['id']
            p = Popen(runimport, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
            response = p.stdout.read()
	    #print response

