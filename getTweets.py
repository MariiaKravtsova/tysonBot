import time
import json
from api import getAPI

REQUEST_DELAY = 7
MAX_REQUESTS = 7

def main():
    try:
        # setup
        user = '@neiltyson'
        api = getAPI()
        tweetResults = []

        # getting last tweets based on the API delays and requests restrictions
        tweetIndex = api.user_timeline(screen_name=user, count=1)[0].id
        time.sleep(REQUEST_DELAY)
        for request in range(MAX_REQUESTS):
            tweets = api.user_timeline(screen_name=user, include_retweets=False, max_id=tweetIndex)
            for tweet in tweets:
                tweetResults.append(tweet.text)
                tweetIndex = tweet.id
            time.sleep(REQUEST_DELAY)

    except IndexError:
        print("Missing Twitter Handle")
    except Exception as e:
        print(e)
    finally:
        # saving tweets
        with open('tweets', 'w') as saveFile:
            json.dump(tweetResults, saveFile)

if __name__ == '__main__':
    main()
