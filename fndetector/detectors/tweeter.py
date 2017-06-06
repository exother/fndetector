import twitter
import urllib

class TwitterDetector:
    def __init__(self, url):
        self.url = url
        self.danger_ind = 0
        self.positive_ind = 0
        self.response = ""

    def check(self):
        api = twitter.Api(consumer_key='5a5MOkXLvbpPKnKB0vl6v4WWr', 
            consumer_secret='oS7aSXKLqN15VOrcK2fGhlHtb7iIf7d2X1GjcmSCK9ZsL85S4Z', 
            access_token_key='16377524-cYcirEx0BY0S0TyVTCBEe5nCtc0MG3bNnSoxpfuUz', 
            access_token_secret='DMfm6ONFuUNW2WFPN5DEHtnrnlnswh4x5ZTMWuh4PSsQH')
        results = api.GetSearch( raw_query="q=" + urllib.parse.quote_plus(self.url) )
        
        self.set_response(results)


    def set_response(self, results):
        retweets = 0
        favorites = 0

        for result in results:
            retweets += result.retweet_count
            favorites += result.favorite_count

        self.positive_ind = retweets / 100 + favorites / 100
