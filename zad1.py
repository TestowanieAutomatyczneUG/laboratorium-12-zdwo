import unittest
from unittest.mock import *
import requests


class RUser:
    def __init__(self):
        self.link = 'https://randomuser.me/api'
        self.nat = ['AU', 'BR', 'CA', 'CH', 'DE', 'DK', 'ES', 'FI', 'FR', 'GB', 'IE', 'IR', 'NO', 'NL', 'NZ', 'TR', 'US']
        self.gen = ['male', 'female']

    def getUser(self):
        r = requests.get(self.link)
        return r.json()['results'][0]

    def getGender(self, gender):
        if gender in self.gen:
            r = requests.get(f'{self.link}?gender={gender}')
            return r.json()['results'][0]
        else:
            raise TypeError('error')

    def getNat(self, nat):
        if nat in self.nat:
            r = requests.get(f'{self.link}?nat={nat}')
            return r.json()['results'][0]
        else:
            raise TypeError('error')



class TestRUser(unittest.TestCase):
    def setUp(self):
        self.temp = RUser()

    def test_get_user(self):
        self.assertIsInstance(self.temp.getUser(), dict)

    def test_get_gender(self):
        self.assertIsInstance(self.temp.getGender('female'), dict)

    def test_gender_female(self):
        self.assertEqual(self.temp.getGender('female')['gender'], 'female')

    def test_gender_male(self):
        self.assertEqual(self.temp.getGender('male')['gender'], 'male')

    def test_gender_err(self):
        self.assertRaises(TypeError, self.temp.getGender, 'x')

    def test_gender_err_int(self):
        self.assertRaises(TypeError, self.temp.getGender, 1)

    def test_get_nat(self):
        self.assertIsInstance(self.temp.getNat('AU'), dict)

    def test_nat_br(self):
        self.assertEqual(self.temp.getNat('BR')['location']['country'], 'Brazil')

    def test_nat_err(self):
        self.assertRaises(TypeError, self.temp.getNat, 'x')

    def test_nat_err_int(self):
        self.assertRaises(TypeError, self.temp.getNat, 1)

    def tearDown(self):
        self.temp = None


class TestRUserMock(unittest.TestCase):
    def setUp(self):
        self.temp = RUser()

    def test_get_user(self):
        user = {"results":[{"gender":"male","name":{"title":"Mr","first":"Mehmet","last":"Tüzün"},"location":{"street":{"number":9777,"name":"Anafartalar Cd"},"city":"Kırşehir","state":"Artvin","country":"Turkey","postcode":36094,"coordinates":{"latitude":"70.0314","longitude":"-90.0553"},"timezone":{"offset":"+5:30","description":"Bombay, Calcutta, Madras, New Delhi"}},"email":"mehmet.tuzun@example.com","login":{"uuid":"adbf1714-990e-4fa6-afd1-0518f16b38b6","username":"ticklishcat147","password":"world","salt":"LJc48OA4","md5":"ccba24c0d9fe984dfc0bcce16573c9f9","sha1":"40f3ef1ac36e5890d49cd9547ec5f6079c8f297b","sha256":"080b6bd183cb014db50bb433fc717902830416e67eaac459964d2cf487568f9a"},"dob":{"date":"1962-09-20T05:17:29.767Z","age":59},"registered":{"date":"2004-04-28T01:42:47.319Z","age":17},"phone":"(903)-715-7487","cell":"(896)-287-0130","id":{"name":"","value":""},"picture":{"large":"https://randomuser.me/api/portraits/men/54.jpg","medium":"https://randomuser.me/api/portraits/med/men/54.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/54.jpg"},"nat":"TR"}],"info":{"seed":"b22a72e5d46e46b4","results":1,"page":1,"version":"1.3"}}
        self.temp.getUser = MagicMock(return_value=user)
        self.assertEqual(self.temp.getUser(), user)

    def test_get_gender_f(self):
        user = {"results":[{"gender":"female","name":{"title":"Miss","first":"Magdalena","last":"Herrera"},"location":{"street":{"number":5414,"name":"Calle de Alberto Aguilera"},"city":"Albacete","state":"Castilla y León","country":"Spain","postcode":20044,"coordinates":{"latitude":"-21.5179","longitude":"30.8314"},"timezone":{"offset":"+4:00","description":"Abu Dhabi, Muscat, Baku, Tbilisi"}},"email":"magdalena.herrera@example.com","login":{"uuid":"63983051-1095-4132-9722-0a69f99fab1d","username":"blackcat109","password":"hootie","salt":"gaJteojw","md5":"6d65edf3d242f97a96ead4aa0389c21a","sha1":"ec4456e2989e2101594fc4a9fa22ebe23fc31536","sha256":"f4fabe396cb80ce47687cc54e31d3c37d9949911b26a63fdb44a6d997914ee3f"},"dob":{"date":"1979-05-25T22:04:11.883Z","age":42},"registered":{"date":"2009-01-30T20:31:20.602Z","age":12},"phone":"996-596-718","cell":"650-280-447","id":{"name":"DNI","value":"56667839-U"},"picture":{"large":"https://randomuser.me/api/portraits/women/58.jpg","medium":"https://randomuser.me/api/portraits/med/women/58.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/women/58.jpg"},"nat":"ES"}],"info":{"seed":"ff8c8a0aedc161b8","results":1,"page":1,"version":"1.3"}}
        self.temp.getGender = MagicMock(return_value=user)
        self.assertEqual(self.temp.getGender('female'), user)

    def test_get_gender_m(self):
        user = {"results":[{"gender":"male","name":{"title":"Mr","first":"Jimmy","last":"Watson"},"location":{"street":{"number":8535,"name":"Manor Road"},"city":"Coventry","state":"Lincolnshire","country":"United Kingdom","postcode":"RK19 5HY","coordinates":{"latitude":"13.8594","longitude":"0.4793"},"timezone":{"offset":"+8:00","description":"Beijing, Perth, Singapore, Hong Kong"}},"email":"jimmy.watson@example.com","login":{"uuid":"fdd63979-b7cc-474a-ac2c-6dde0b95dcfe","username":"silverdog810","password":"nasty","salt":"KTBWXDrN","md5":"3890fae0d8a8f0425bb308f8636d0cdb","sha1":"51cfbd36839ebd955621377dfbc476cb00b2d851","sha256":"748061406af6cbc0d203d3918e5967f10cd54e699cdba69ec0299c600067215d"},"dob":{"date":"1967-10-10T05:57:41.669Z","age":54},"registered":{"date":"2016-07-06T19:48:09.162Z","age":5},"phone":"015242 61133","cell":"0780-826-425","id":{"name":"NINO","value":"WA 74 32 21 Z"},"picture":{"large":"https://randomuser.me/api/portraits/men/87.jpg","medium":"https://randomuser.me/api/portraits/med/men/87.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/87.jpg"},"nat":"GB"}],"info":{"seed":"61b0ac3b4b0a0843","results":1,"page":1,"version":"1.3"}}
        self.temp.getGender = MagicMock(return_value=user)
        self.assertEqual(self.temp.getGender('male'), user)

    def test_get_nat_au(self):
        user = {"results":[{"gender":"female","name":{"title":"Ms","first":"Courtney","last":"Brooks"},"location":{"street":{"number":7844,"name":"Westheimer Rd"},"city":"Devonport","state":"Tasmania","country":"Australia","postcode":9733,"coordinates":{"latitude":"-76.4564","longitude":"121.5444"},"timezone":{"offset":"-4:00","description":"Atlantic Time (Canada), Caracas, La Paz"}},"email":"courtney.brooks@example.com","login":{"uuid":"31e4cf5b-ae3f-4842-b184-5dee5ed74470","username":"crazygoose836","password":"lister","salt":"4p0Frk8f","md5":"891c53fc5319f4c585725edfe82cd5ed","sha1":"192bc7cca3c3d78f257022953d838db0d8a75358","sha256":"5394245d0af1fe194db36e1a7c65d1786ce02af99343e8633e2f7f62c39b8e7d"},"dob":{"date":"1994-11-18T16:37:52.736Z","age":27},"registered":{"date":"2017-12-02T18:39:08.913Z","age":4},"phone":"09-8423-4078","cell":"0423-294-686","id":{"name":"TFN","value":"465051944"},"picture":{"large":"https://randomuser.me/api/portraits/women/31.jpg","medium":"https://randomuser.me/api/portraits/med/women/31.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/women/31.jpg"},"nat":"AU"}],"info":{"seed":"47e26f3d192c0cda","results":1,"page":1,"version":"1.3"}}
        self.temp.getNat = MagicMock(return_value=user)
        self.assertEqual(self.temp.getNat('AU'), user)

    def test_get_nat_br(self):
        user = {"results":[{"gender":"female","name":{"title":"Ms","first":"Mayara","last":"Ramos"},"location":{"street":{"number":1090,"name":"Rua Pernambuco "},"city":"Bragança Paulista","state":"Amazonas","country":"Brazil","postcode":46720,"coordinates":{"latitude":"-25.6614","longitude":"129.5662"},"timezone":{"offset":"+9:00","description":"Tokyo, Seoul, Osaka, Sapporo, Yakutsk"}},"email":"mayara.ramos@example.com","login":{"uuid":"addd1821-67db-4c9d-bf69-dff10afa10ec","username":"organicsnake982","password":"girl","salt":"B2TWKYB7","md5":"06c6a080bffba7bbcedb45a3f0ff4e14","sha1":"811d76f428d0e937b7514dffbf8742a7d9d2dea5","sha256":"f033ca375fe0f51ba3a249285aad3f8897bd2bc7cbfd1029e06617676a92599a"},"dob":{"date":"1997-06-16T21:34:21.531Z","age":24},"registered":{"date":"2003-11-24T20:07:28.745Z","age":18},"phone":"(69) 6108-7999","cell":"(69) 6570-5839","id":{"name":"","value":""},"picture":{"large":"https://randomuser.me/api/portraits/women/2.jpg","medium":"https://randomuser.me/api/portraits/med/women/2.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/women/2.jpg"},"nat":"BR"}],"info":{"seed":"2101766ac854bae7","results":1,"page":1,"version":"1.3"}}
        self.temp.getNat = MagicMock(return_value=user)
        self.assertEqual(self.temp.getNat('BR'), user)



