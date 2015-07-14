'''
Created on Apr 11, 2015


from ipaddr import IPAddress

class BlockedIPData:
    def __init__(self, _Attacker_ipaddr,_Victim_ipaddr):
        self.AttackerIPAddress=_Attacker_ipaddr
        self.VictimIPAddress=_Victim_ipaddr
