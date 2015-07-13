'''
Created on Apr 11, 2015

@author: aron
'''

from NewPolicyUI import PolicyAdder
from CommonDataTypes import CommonData
from ShowBlockedIPUI import ShowBlockedIP

def main():
    
    _CommonData = CommonData()
    _policyAdder=PolicyAdder()
    print "1) Add a new policy"
    print "2) Show all blocked IPs"
    print "3) Status of all blocked IPs"

    option = input("Select an option")

    if option==1:
        _policyAdder.IPPolicyAdder(_CommonData)
    elif option==2:
        ShowBlockedIP(_CommonData)

main()