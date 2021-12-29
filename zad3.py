import unittest
from unittest.mock import *


class TemplateEngine:
    def msg(self, msg):
        pass


class MailServer:
    def send(self, rec, msg):
        pass

    def receive(self, msg):
        pass


class Messenger:
    def __init__(self):
        self.te = TemplateEngine()
        self.ms = MailServer()

    def send(self, rec, msg):
        return self.ms.send(rec, self.te.msg(msg))

    def receive(self, msg):
        return self.ms.receive(msg)


class TestMessenger(unittest.TestCase):
    def setUp(self):
        self.temp = Messenger()

    def test_send(self):
        self.temp.te = MagicMock()
        self.temp.ms = MagicMock()
        self.temp.te.msg = MagicMock(return_value='Hello')
        self.temp.ms.send = MagicMock(return_value=True)
        self.assertTrue(self.temp.send('aaa', 'Hello'))

    def test_send_false(self):
        self.temp.te = MagicMock()
        self.temp.ms = MagicMock()
        self.temp.te.msg = MagicMock(return_value='Hello')
        self.temp.ms.send = MagicMock(return_value=False)
        self.assertFalse(self.temp.send('aaa', 'Hello'))

    def test_send_err_te_int(self):
        self.temp.te = MagicMock()
        self.temp.ms = MagicMock()
        self.temp.te.msg = MagicMock(side_effect=TypeError)
        self.temp.ms.send = MagicMock(return_value=False)
        self.assertRaises(TypeError, self.temp.send, 'aaa', 1)

    def test_send_err_te_none(self):
        self.temp.te = MagicMock()
        self.temp.ms = MagicMock()
        self.temp.te.msg = MagicMock(side_effect=TypeError)
        self.temp.ms.send = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.send, 'aaa', None)

    def test_send_err_te_bool(self):
        self.temp.te = MagicMock()
        self.temp.ms = MagicMock()
        self.temp.te.msg = MagicMock(side_effect=TypeError)
        self.temp.ms.send = MagicMock(return_value=False)
        self.assertRaises(TypeError, self.temp.send, 'aaa', False)

    def test_send_err_ms_int(self):
        self.temp.te = MagicMock()
        self.temp.ms = MagicMock()
        self.temp.te.msg = MagicMock(return_value='Hello')
        self.temp.ms.send = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.send, 1, 'Hello')

    def test_send_err_ms_tup(self):
        self.temp.te = MagicMock()
        self.temp.ms = MagicMock()
        self.temp.te.msg = MagicMock(return_value='Hello')
        self.temp.ms.send = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.send, (), 'Hello')

    def test_send_err_ms_none(self):
        self.temp.te = MagicMock()
        self.temp.ms = MagicMock()
        self.temp.te.msg = MagicMock(return_value='Hello')
        self.temp.ms.send = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.send, None, 'Hello')

    def test_send_err_ms_arr(self):
        self.temp.te = MagicMock()
        self.temp.ms = MagicMock()
        self.temp.te.msg = MagicMock(return_value='Hello')
        self.temp.ms.send = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.send, [], 'Hello')

    def test_send_err_ms_fl(self):
        self.temp.te = MagicMock()
        self.temp.ms = MagicMock()
        self.temp.te.msg = MagicMock(return_value='Hello')
        self.temp.ms.send = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.send, 1.5, 'Hello')

    def test_receive(self):
        self.temp.ms = MagicMock()
        self.temp.ms.receive = MagicMock(return_value=True)
        self.assertTrue(self.temp.receive('Hello'))

    def test_receive_false(self):
        self.temp.ms = MagicMock()
        self.temp.ms.receive = MagicMock(return_value=False)
        self.assertFalse(self.temp.receive('Hello'))
