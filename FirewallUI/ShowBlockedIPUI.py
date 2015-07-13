'''
Created on Apr 11, 2015

@author: aron
'''
from CommonDataTypes import BlockedIP

def ShowBlockedIP(self,_CommonData):
    print "The Blocked IPs are"
    
    print "Attacker IP\t"+"Victim IP"+"Attacker MAC"+"Destination MAC" 
     
    for IP in _CommonData.BlockedIP:
        print ("Attacker IP Address"+ IP.AttackerIPAddress)
        print ("Victim IP Address"+ IP.VictimIPAddress)
        print "--------------------------------------"