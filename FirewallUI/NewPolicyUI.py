from CommonDataTypes import CommonData

#print "Add new policy"
class PolicyAdder():
    def IPPolicyAdder(self,newType):
        IPSource = input("Enter the Source IP")
        IPDestination = input("Enter the Destination IP")
        
        newType.AddBlockedIP(IPSource,IPDestination)
        print "New policy added"
        print "Attacker IP = ",IPSource
        print "Victim IP = ",IPDestination