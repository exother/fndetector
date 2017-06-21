import unittest
from fndetector import fndetector
import io
import sys

class TestFnDetector(unittest.TestCase):

	def testRealNews(self):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		fndetector.check_news('http://www.bbc.co.uk/news/uk-40169985')
		sys.stdout = sys.__stdout__	
		self.assertIn("This news is real.", capturedOutput.getvalue())

	def testFakeNewsBlackListed(self):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		fndetector.check_news('http://21stcenturywire.com/2017/06/21/white-helmets-severed-heads-of-syrian-arab-army-soldiers-paraded-as-trophies-endorsed-by-channel-4/')
		sys.stdout = sys.__stdout__	
		self.assertIn("This news is fake.", capturedOutput.getvalue())
		self.assertIn("blacklisted", capturedOutput.getvalue())

	def testFakeNewsClickBait(self):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		fndetector.check_news('https://www.conservativeoutfitters.com/blogs/news/83993025-video-school-official-explains-3-x-4-11-under-common-core#comment-2465749183')
		sys.stdout = sys.__stdout__	
		self.assertIn("This news is fake.", capturedOutput.getvalue())
		self.assertIn("clickbait", capturedOutput.getvalue())

if __name__ == '__main__':
    unittest.main()