import unittest 
from put_button_count import increment_count
import requests

class TestPutButtonCount(unittest.TestCase):
	
	def test_api_failure(self):
		#Test that the PutButtonCount endpoint returns a status message of 200 when called
		response = requests.get('https://ax5xbg2mnk.execute-api.us-east-1.amazonaws.com/Prod/site/PutButtonCount')
		statusCode = response.status_code
		self.assertEqual(statusCode, 200)

#	def test_incrament_count(self):
#		#Test that the incrament_count function correctly inceases the 'count' of the 'presses' item by 13
#		
#		#get initial count
#		response = requests.get('https://ax5xbg2mnk.execute-api.us-east-1.amazonaws.com/Prod/site/getButtonCount')
#		print(response)
#		initial_count = (response['Attributes']['count'])
#		
#		#call increment_count function
#		increment_count()
#		#get updated count
#		response = requests.get('https://ax5xbg2mnk.execute-api.us-east-1.amazonaws.com/Prod/site/getButtonCount')
#		updated_count = (response['Attributes']['count'])
#
#		#validate data
#		self.assertEqual(updated_count, increment_count+1)