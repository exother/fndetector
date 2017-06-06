import requests

class ClickBaitDetector:
    def __init__(self, title):
        self.title = title
        self.clickbaitiness = 0.0
        self.danger_ind = 0
        self.positive_ind = 0
        self.response = ""

    def check(self):
        request = requests.get('https://clickbait-detector.herokuapp.com/detect?headline=' + self.title)
        response = request.json()
        self.clickbaitiness = float(response['clickbaitiness'])
        self.set_response()

    def set_response(self):
        if self.clickbaitiness > 90:
            self.danger_ind = 70
            self.response = "The title is a clickbait!"
        elif self.clickbaitiness > 65:
            self.danger_ind = 30
            self.response = "The title is supposed to be a clickbait."
        elif self.clickbaitiness > 25:
            self.danger_ind = 10
            self.response = "The title might be a clickbait."
        else:
            self.positive_ind = 10