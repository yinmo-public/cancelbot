from Cancel.linepy import *
from Cancel.akad.ttypes import *
from time import sleep
import time

yinmo = LINE()
oepoll = OEPoll(yinmo)

def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        yinmo.acceptGroupInvitation(op.param1)       
        group = yinmo.getGroup(op.param1)
        if group.invitee is None:
            yinmo.kickoutFromGroup(op.param1, [op.param2])
            yinmo.leaveGroup(op.param1)
        else:
            group = yinmo.getGroup(op.param1)
            groupinvitingmembersmid = [contact.mid for contact in group.invitee]
            for _mid in groupinvitingmembersmid:
                time.sleep(0.5)
                yinmo.cancelGroupInvitation(op.param1, [_mid])
                time.sleep(0.2)
            yinmo.leaveGroup(op.param1)
    except Exception as e:
        print(e)
        print("\n\nNOTIFIED_INVITE_INTO_GROUP\n\n")
        return


oepoll.addOpInterruptWithDict({
    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP
})

while True:
    oepoll.trace()
    
