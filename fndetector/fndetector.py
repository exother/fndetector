from fndetector.detectors.clickbait import ClickBaitDetector
from fndetector.detectors.domain	import DomainDetector
from fndetector.detectors.tweeter import TwitterDetector

from newspaper import Article

def check_news(url):
	news = Article(url)
	news.download()
	news.parse()

	detectors = []

	detectors.append( ClickBaitDetector(news.title) )
	detectors.append( DomainDetector(url) )
	detectors.append( TwitterDetector(url) )

	positive_score = 0
	negative_score = 0
	informations = []

	for detector in detectors:
		detector.check()
		positive_score += detector.positive_ind
		negative_score += detector.danger_ind
		informations.append(detector.response)

	informations = list(filter(None, informations))

	for information in informations:
		print("> " + information)

	if negative_score < 10:
		if positive_score > 50:
			print("# This news is real.")
		elif positive_score < negative_score:
			print("# This news is cannot be verified properly. Please check another available sources.")
		else:
			print("# This news seems to be real, however you'd better to verify that.")
	else:
		if negative_score < 50 and positive_score > 30:
			print("# This news could be real, but there some negative results.")
		elif negative_score < 70:
			print("# This news is almost certainly fake.")
		else:
			print("# This news is fake.")
