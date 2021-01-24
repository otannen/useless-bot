import requests


class Tweet(object):
    def __init__(self, city):
        self.city = city
        pass

    def get_weather(self):
        weather = (
            requests.get(
                "http://api.openweathermap.org/data/2.5/weather?q="
                + self.city
                + ""  ###add api key here
            )
        ).json()
        return 1.8 * (weather["main"]["temp_max"] - 273) + 32

    def get_gas_price(self):
        gas = (
            requests.get(
                "https://www.quandl.com/api/v3/datasets/FRED/GASREGCOVW.json?api_key=##add api key here"
            )
        ).json()
        return gas["dataset"]["data"][0][1]

    def get_wiki(self):
        wiki = (
            requests.get("https://en.wikipedia.org/api/rest_v1/page/random/summary")
        ).json()
        return wiki["content_urls"]["desktop"]["page"]

    def get_news(self):
        news = (
            requests.get(
                "http://newsapi.org/v2/top-headlines?"
                "country=us&"
                "apiKey=#add api key here"
            )
        ).json()
        news = news["articles"][0]["url"]
        return news