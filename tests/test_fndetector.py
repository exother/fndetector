import unittest
from fndetector import fndetector
import StringIO
import sys

class TestFnDetector(unittest.TestCase):

	def testRealNews(self):
		capturedOutput = StringIO.StringIO()
		sys.stdout = capturedOutput
		fndetector.check_news('http://www.bbc.co.uk/news/uk-40169985')
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "# This news is real.")