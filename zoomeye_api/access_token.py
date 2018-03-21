# coding: utf-8
import unittest
import requests
import json

# POST /api/op/otp_login
# http://gruc.gnum.com/static/swagger/swagger-ui/dist/index.html#/

class GetAccessToken(unittest.TestCase):

	def setUp(self):
		self.domain = 'https://api.zoomeye.org'
		self.json_headers = {'content-type': 'application/json'}
		print 'before each test --> Start'

	def tearDown(self):
		print 'after each test --> End'

	def testGetAccessToken(self):
		print 'Get Zoomeye API access token -- POST'
		json_data = json.dumps({'username':'testerlyx@foxmail.com','password': '-TesterCC07-'})

		r = requests.post(self.url('/user/login'), data=json_data, headers=self.json_headers)
		result = r.json()

		self.assertEqual(r.status_code, 200)
		# print result #['access_token']
		print "Your Zoomeye API access_token is:\n %s " % result['access_token']


# set api rul
	def url(self, path):
		return self.domain + path


if __name__ == '__main__':
	unittest.main()