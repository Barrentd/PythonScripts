#!/usr/bin/python3

import requests
import time
from xml.etree import ElementTree
from lxml import html,etree


header = {'keyapp': 'FvChCBnSetVgTKk324rO', 'cmd': 'getNextStopsRealtime', 'stopArea': '7'}
response = requests.get("http://apixha.ixxi.net/APIX", params=header)

tree = etree.fromstring(response.content)
retour = tree.xpath("/nextStopsRealtimeResultat/currentTime")
lignes = tree.xpath("//lineId")
prochArret = tree.xpath("//nextStopTime")
for r in retour:
    print("Time :", r.text)
for i, r in enumerate(lignes):
    print("Ligne :", r.text)
    


