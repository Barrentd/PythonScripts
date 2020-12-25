#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Read XML file from API"""

#from xml.etree import ElementTree
import requests
from lxml import etree

def main():

    """Call and parse XML file from API"""

    header = {'keyapp': 'FvChCBnSetVgTKk324rO', 'cmd': 'getNextStopsRealtime', 'stopArea': '7'}
    response = requests.get("http://apixha.ixxi.net/APIX", params=header)

    tree = etree.fromstring(response.content)
    times = tree.xpath("/nextStopsRealtimeResultat/currentTime")
    lignes = tree.xpath("//lineId")
    for time in times:
        print("Time :", time.text)
    for ligne in lignes:
        print("Ligne :", ligne.text)

if __name__ == "__main__":
    main()
