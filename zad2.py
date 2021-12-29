import unittest
from unittest.mock import *


class Subscriber:
    def __init__(self):
        self.clients = []

    def addClient(self, id, client):
        if id is int and client in str:
            self.clients.append({'id': id, 'client': client})
            return self.clients
        else:
            raise TypeError('error')

    def deleteClient(self, id):
        if id is int:
            for i in self.clients:
                if i['id'] == id:
                    self.clients.remove(i)
                    return self.clients
            raise Exception('brak')
        else:
            raise TypeError('error')

    def sendMsg(self, id, msg):
        pass


class TestSubscriber(unittest.TestCase):
    def setUp(self):
        self.temp = Subscriber()

    def test_add_client(self):
        clients = [{'id': 1, 'client': 'client1'}]
        self.temp.addClient = MagicMock(return_value=clients)
        self.assertEqual(self.temp.addClient(1, 'client1'), clients)

    def test_add_to_cients(self):
        clients = [{'id': 1, 'client': 'client1'}, {'id': 2, 'client': 'client2'}, {'id': 3, 'client': 'client3'}]
        self.temp.addClient = MagicMock(return_value=clients)
        self.assertEqual(self.temp.addClient(3, 'client3'), clients)

    def test_add_err_id(self):
        self.temp.addClient = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.addClient, '1', 'x')

    def test_add_err_id_none(self):
        self.temp.addClient = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.addClient, None, 'x')

    def test_add_err_id_bool(self):
        self.temp.addClient = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.addClient, False, 'x')

    def test_add_err_cl(self):
        self.temp.addClient = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.addClient, 1, [])

    def test_add_err_cl_dict(self):
        self.temp.addClient = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.addClient, 1, {})

    def test_add_err_cl_none(self):
        self.temp.addClient = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.addClient, 1, None)

    def test_delete_client(self):
        clients = [{'id': 1, 'client': 'client1'}, {'id': 2, 'client': 'client2'}]
        self.temp.deleteClient = MagicMock(return_value=clients)
        self.assertEqual(self.temp.deleteClient(3), clients)

    def test_delete_err_noClient(self):
        self.temp.deleteClient = MagicMock(side_effect=Exception)
        self.assertRaises(Exception, self.temp.deleteClient, 5)

    def test_delete_err_str(self):
        self.temp.deleteClient = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.deleteClient, '5')

    def test_delete_err_arr(self):
        self.temp.deleteClient = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.deleteClient, [])

    def test_delete_err_tup(self):
        self.temp.deleteClient = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.deleteClient, ())

    def test_delete_err_fl(self):
        self.temp.deleteClient = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.deleteClient, 1.2)

    def test_msg(self):
        self.temp.sendMsg = MagicMock(return_value='Hello')
        self.assertEqual(self.temp.sendMsg(1, 'Hello'), 'Hello')

    def test_msg_err_noClient(self):
        self.temp.sendMsg = MagicMock(side_effect=Exception)
        self.assertRaises(Exception, self.temp.sendMsg, 111, 'hi')

    def test_msg_err_id_str(self):
        self.temp.sendMsg = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.sendMsg, '1', 'hello')

    def test_msg_err_id_tup(self):
        self.temp.sendMsg = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.sendMsg, (), 'hello')

    def test_msg_err_msg_int(self):
        self.temp.sendMsg = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.sendMsg, 1, 1)

    def test_msg_err_msg_bool(self):
        self.temp.sendMsg = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.sendMsg, 1, True)

    def tearDown(self):
        self.temp = None
