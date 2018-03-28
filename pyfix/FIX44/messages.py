#!/usr/bin/env python3

from pyfix.FIX44 import msgtype, fixtags
from pyfix.message import FIXMessage
from uuid import uuid4


class Messages(object):
    @staticmethod
    def logon(password: str):
        msg = FIXMessage(msgtype.LOGON)
        msg.setField(fixtags.EncryptMethod, 0)
        msg.setField(fixtags.HeartBtInt, 30)
        msg.setField(fixtags.ResetSeqNumFlag, 'Y')
        msg.setField(fixtags.Password, password)
        return msg

    @staticmethod
    def logout():
        msg = FIXMessage(msgtype.LOGOUT)
        return msg

    @staticmethod
    def heartbeat():
        msg = FIXMessage(msgtype.HEARTBEAT)
        return msg

    @staticmethod
    def test_request():
        msg = FIXMessage(msgtype.TESTREQUEST)
        msg.setField(fixtags.TestReqID, str(uuid4()))
        return msg

    @staticmethod
    def sequence_reset(respondingTo, isGapFill):
        msg = FIXMessage(msgtype.SEQUENCERESET)
        msg.setField(fixtags.GapFillFlag, 'Y' if isGapFill else 'N')
        msg.setField(fixtags.MsgSeqNum, respondingTo[fixtags.BeginSeqNo])
        return msg

    #
    # @staticmethod
    # def sequence_reset(beginSeqNo, endSeqNo, isGapFill):
    #     msg = FIXMessage(msgtype.SEQUENCERESET)
    #     msg.setField(fixtags.GapFillFlag, 'Y' if isGapFill else 'N')
    #     msg.setField(fixtags.MsgSeqNum, respondingTo[fixtags.BeginSeqNo])
    #     return msg


    @staticmethod
    def resend_request(beginSeqNo, endSeqNo='0'):
        msg = FIXMessage(msgtype.RESENDREQUEST)
        msg.setField(fixtags.BeginSeqNo, str(beginSeqNo))
        msg.setField(fixtags.EndSeqNo, str(endSeqNo))
        return msg
