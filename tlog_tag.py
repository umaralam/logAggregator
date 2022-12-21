# from tlog import Tlog
from enum import Enum

class TlogErrorTag(Enum):
    """
    Enum error tag
    """
    SUB_TYPE_CHECK = "STCK=3"
    CHECK_BALANCE = "CBAL=3"
    RESERVE = "RSRV=3"
    CHARGING = "CHG=3"
    REMOTE_ACT = "RMAC=3"
    REMOTE_DCT = "RMD=3"
    DECTIVATION = "DCT=3"
    CALLBACK = "CBCK=3"
    CDR = "CRM=3"
    INFORM_CSS = "CSS=3"
    REFUND = "RFD=3"
    INFORM_OMF = "OMF=3"
    GENERIC_TASK1 = "GT1=3"
    GENERIC_TASK2 = "GT2=3"
    GENERIC_TASK3 = "GT3=3"
    GENERIC_TASK4 = "GT4=3"
    GENERIC_TASK5 = "GT5=3"


class TlogRetryTag(Enum):
    """
    Enum retry tag
    """
    SUB_TYPE_CHECK = "STCK=0"
    CHECK_BALANCE = "CBAL=0"
    RESERVE = "RSRV=0"
    CHARGING = "CHG=0"
    REMOTE_ACT = "RMAC=0"
    REMOTE_DCT = "RMD=0"
    DECTIVATION = "DCT=0"
    CALLBACK = "CBCK=0"
    CDR = "CRM=0"
    INFORM_CSS = "CSS=0"
    REFUND = "RFD=0"
    INFORM_OMF = "OMF=0"
    GENERIC_TASK1 = "GT1=0"
    GENERIC_TASK2 = "GT2=0"
    GENERIC_TASK3 = "GT3=0"
    GENERIC_TASK4 = "GT4=0"
    GENERIC_TASK5 = "GT5=0"
    
    
class TlogLowBalTag(Enum):
    """
    Enum low bal tag
    """
    CHECK_BALANCE = "CBAL=4"
    CHARGING = "CHG=4"

class TlogNHFTag(Enum):
    """
    Enum no handler found tag
    """
    NHF = "NHF:NO handler configured for request"

class TlogAwaitPushTag(Enum):
    """
    Enum await push tag
    """
    SUB_TYPE_CHECK = "STCK=8"
    CHECK_BALANCE = "CBAL=8"
    RESERVE = "RSRV=8"
    CHARGING = "CHG=8"
    REMOTE_ACT = "RMAC=8"
    REMOTE_DCT = "RMD=8"
    DECTIVATION = "DCT=8"
    CALLBACK = "CBCK=8"
    CDR = "CRM=8"
    INFORM_CSS = "CSS=8"
    REFUND = "RFD=8"
    INFORM_OMF = "OMF=8"
    GENERIC_TASK1 = "GT1=8"
    GENERIC_TASK2 = "GT2=8"
    GENERIC_TASK3 = "GT3=8"
    GENERIC_TASK4 = "GT4=8"
    GENERIC_TASK5 = "GT5=8"
    
class TlogAwaitPushTimeOutTag(Enum):
    """
    Enum timeout tag
    """
    SUB_TYPE_CHECK = "#TIMEOUT"
    CHECK_BALANCE = "#TIMEOUT"
    RESERVE = "#TIMEOUT"
    CHARGING = "#TIMEOUT"
    REMOTE_ACT = "#TIMEOUT"
    REMOTE_DCT = "#TIMEOUT"
    DECTIVATION = "#TIMEOUT"
    CALLBACK = "#TIMEOUT"
    CDR = "#TIMEOUT"
    INFORM_CSS = "#TIMEOUT"
    REFUND = "#TIMEOUT"
    INFORM_OMF = "#TIMEOUT"
    GENERIC_TASK1 = "#TIMEOUT"
    GENERIC_TASK2 = "#TIMEOUT"
    GENERIC_TASK3 = "#TIMEOUT"
    GENERIC_TASK4 = "#TIMEOUT"
    GENERIC_TASK5 = "#TIMEOUT"
    
class TlogHandlerExp(Enum):
    CHARGING = "CHG=30"
    CHG = "CHG=41"

class TlogSmsTag(Enum):
    SMS_INVALID = "I"
    SMS_RETRY_EXCEEDED = "E"
    SMS_PENDING = "P"
    SMS_SUSPENDED = "S"
    SMS_QUEUED = "Q"
    
class webapps(Enum):
    servlet_mapping = ["/subscription/ActivateSubscription?", "/subscription/DeactivateSubscription?", 
                       "/subscription/EventCharge?", "/subscription/UpgradeSubscription?", 
                       "/subscription/TriggerCharge?", "/subscription/ChargeGift?", 
                       "/subscription/AddRenewalTrigger?", "/subscription/RealTimeActivate?", 
                       "/subscription/RealTimeDeactivate?", "/subscription/RealTimeCharge?", 
                       "/subscription/RealTimeTransactionRefund?"]

class TaskType(Enum):
    """
    Task type class
    """
    SUB_TYPE_CHECK = "S"
    CHECK_BALANCE = "Q"
    RESERVE = "RA"
    CHARGING = "B"
    CHG = "B"
    REMOTE_ACT = "R"
    REMOTE_DCT = "H"
    DECTIVATION = "D"
    CALLBACK = "C"
    CDR = "L"
    INFORM_CSS = "M"
    REFUND = "W"
    INFORM_OMF = "IO"
    GENERIC_TASK1 = "G1"
    GENERIC_TASK2 = "G2"
    GENERIC_TASK3 = "G3"
    GENERIC_TASK4 = "G4"
    GENERIC_TASK5 = "G5"
    
# if __name__ == '__main__':
#     for status in webapps:
#         print(status.value)
