import csv
from urllib.parse import urlparse
import numpy as np

class DomainDetector:
    def __init__(self, url):
        self.url = url
        self.domain = urlparse(url).netloc
        self.domain = str(np.char.strip(self.domain,'www.'))
        self.danger_ind = 0
        self.positive_ind = 0
        self.response = ""

    def check(self):
        domain_database = {}
        with open('resources/domain_database.csv', newline='') as csvfile:
            dbreader = csv.reader(csvfile, delimiter=',')
            for row in dbreader:
                domain = row[0]
                tags = row[1:]
                domain_database[domain.lower()] = ', '.join(list(filter(None, tags)))
        self.set_response(domain_database)


    def set_response(self, database):
        if self.domain in database:
            self.danger_ind = 100
            self.response = "The domain is blacklisted: " + database[self.domain] + "."
        else:
            self.positive_ind = 50