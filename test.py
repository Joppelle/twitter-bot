import tweepy


access_token = "ENTER YOUR ACCESS TOKEN"
access_token_secret = "ENTER YOUR ACCESS TOKEN SECRET"
consumer_key = "ENTER YOUR API KEY"
consumer_secret = "ENTER YOUR API SECRET"

if __name__ == '__main__':

    user = api.get_user('BillGates')
        
    bills_friends=[]

    for friend in user.friends(count=10,):
        print(api.user_timeline(screen_name=friend.screen_name, count=5, page=5))

