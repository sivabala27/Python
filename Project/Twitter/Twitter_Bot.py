import tweepy
import config
import weather
import matplotlib.pyplot as plt

#Method Create Twitter API Object using keay and token genated in https://developer.twitter.com/en/apps
def connetTwitter():
    try:
        api_key = config.api_key
        api_secret_key = config.api_secret_key
        access_token = config.access_token
        access_token_secret = config.access_token_secret
        auth = tweepy.OAuthHandler(api_key, api_secret_key)
        auth.set_access_token(access_token,access_token_secret)
        api=tweepy.API(auth)
        return api
    except Exception:
        print(Exception)
        return

#Print tweets available in home for the user count in default is limited to 5
def home(cnt=5):
    home = api.home_timeline(count=cnt)
    for i in home:
        print(f'[{i.created_at}] {i.user.location}\n{i.user.name} : {i.text}\nRetweet : {i.retweet_count}\t Fav: {i.favorite_count} \n')

#Prit tweets of a user ,when user ID is passed / API user tweets are listed
def getTweets(userid=None,cnt=5):
    for i in api.user_timeline(id=userid, count=cnt):
        print(f'[{i.created_at}] {i.user.location}\n{i.user.name} : {i.text}\nRetweet : {i.retweet_count}\t Fav: {i.favorite_count} \n')

#Retruns weather info based on city name and yahoo's woeid
def getWeatherInfo(loc,location):
    a = weather.Weather(weather.Unit.CELSIUS)
    result = ''
    for i in loc:
        if i['country'].upper() == "INDIA" and i['name'].upper() == location.upper():
            try:
                climate = a.lookup(i['woeid'])
                result='☁ '+result+i['name']+ ' : '+climate.condition.text+'\n'
            except Exception:
                pass
    return result

#Update status to profile  - updates weather of given location
def updateStatus(location):
    loc = api.trends_available()
    result=getWeatherInfo(loc,location)
    try:
        api.update_status(result)
        print("tweet posted Successfully")
    except Exception as e:
        print(e)

#Print the latest trend of the given location and print the chart
def get_trends(loc='Chennai'):
    trend_list = api.trends_available()
    locid = [s['woeid'] for s in trend_list if loc.upper() in s['name'].upper()]
    treands=api.trends_place(locid[0])[0]['trends']
    trend_item=[]
    trend_volume=[]
    for trend in treands:
        if trend['tweet_volume'] is not None:
            print(trend['name'],trend['tweet_volume'])
            trend_item.append(trend['name'])
            trend_volume.append(trend['tweet_volume'])
        pass
    plt.bar(trend_item[:5],trend_volume[:5])
    plt.show()


api=connetTwitter()                                         #App For Twitter Bot
home(1)                                                     #Get Tweet of home time line : pass count as parameter [optionl]
getTweets('thisisysr')                                      #Pass the user id and get the latest tweets
updateStatus('Chennai')                                     #Post a tweet on timeline
get_trends('Chennai')                                       #Get trend of a Location
