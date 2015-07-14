'''
Created on Apr 11, 2015

import BlockedIP
import AttackLog

class CommonData:
    def __init__(self):
        self.BlockedIPs=[] ## Array used to store BlockedIP data type
        self.AttackLogs=[] ## Array used to store AttackLog
    def AddBlockedIP(self, _ipaddrAttacker,_ipaddrVictim):
        self.BlockedIPs.append(BlockedIP(_ipaddrAttacker,_ipaddrVictim))
    
    def AddAttackDetails(self, _ipaddr,_mac):
        NewAttack=AttackLog(_ipaddr,_mac)
        self.AttackLogs.append((NewAttack))
