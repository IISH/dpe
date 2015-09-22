#!/usr/bin/python

import sys
sys.path.append('/home/strikes/clioinfra/modules')
from config import configuration, dataverse2indicators, load_dataverse, findpid, load_metadata, pidfrompanel

dataset = 'hdl:10622/XUH7BG:65:66'
dataset = "hdl:10622/I0YK5M:111:112"
(metadata, pid, fileid, clio) = load_metadata(dataset)
print pid
for item in metadata:
    print item['name']

branch = 'clio1clio'
#datasets = dataverse2indicators(branch)
#print datasets

pid = "Panel['hdl:10622/4X6NCK','hdl:10622/4X6NCG']"
pids = pidfrompanel(pid)
print pids
