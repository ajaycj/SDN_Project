'''
Created on Apr 11, 2015



from datetime import datetime
from dns.rdatatype import NULL
import BlockedIP

class AttackLogDetails:
    def __init__(self, _attcker_ipaddr,_victim_ipaddr,_attacker_mac,_dest_mac):
        self.AttackTime=datetime.now()
        self.AttackIP= BlockedIP(_attcker_ipaddr,_victim_ipaddr)
        self.AttackMac=_attacker_mac
        self.DestinationMac=_dest_mac
        
