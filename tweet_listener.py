#author: Adriano Henrique Cantao
#creationDate: 15/Sept/2017
#publicationDate: 27/Oct/2017
#email: adriano.cantao@gmail.com
#email2: cantao@usp.br

#Open the output file in notepad++ or others (try to avoid notepad)
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import codecs

#tokens
consumerkey="InsertYourKeyHere"
consumersecret="InsertYourConsumerSecretHere"
accesstoken="insertYOurAcessTokenHere"
accesstokensecret="insertYourAccessTokenSecretHere"

class StdOutListener(StreamListener):
    def on_status(self, status):
        #opens the file
        fileName = "FileNameHere" #without the file extension
        fp = codecs.open(fileName + ".txt", "a", "utf-8")
        #the code bellow write the data to the file
        fp.write("\ntweet ID: " + str(status.id))
        fp.write("\nuser name: " + str(status.user.name))
        fp.write("\nuser acc name: " + str(status.user.screen_name))
        fp.write("\nuser ID: " + str(status.user.id))
        fp.write("\nUser Location: " + str(status.user.location))
#        fp.write("\nTwitter Location: ", status.place.full_name) #location of the tweet, only use if coordinates filtering is active
        fp.write("\nTweet: " + str(status.text))
        fp.write("\n--------------------------------------------")
        fp.write("\n--------------------------------------------")
        fp.close()
		
		#the code bellow print the same data written - just to have a visual aspect of whats going on
		#can be commented or deleted if its necessary
        print ("tweet ID: ",status.id)
        print ("user name: ",status.user.name)
        print ("user acc name: ",status.user.screen_name)
        print ("user ID: ",status.user.id)
        print ("User Location: ", status.user.location)
#       print ("Twitter Location: ", status.place.full_name) #location of the tweet, only use if coordinates filtering is active
        print ("Message: ",status.text)
        print ("--------------------------------------------")
        print ("--------------------------------------------")
        return True

    def on_error(self, status):
        print ("Error, something bad has just happened...")
        print (status)

    def on_timeout(self):
        print ("TimeOut...")
        return False #return True #to avoid stopping the script

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumerkey, consumersecret)
    auth.set_access_token(accesstoken, accesstokensecret)
    stream = Stream(auth, l)
    api = tweepy.API(auth)

#applying filters
#choose any words to track in tweets - use at least one...
stream.filter(track=["today", "happy"])

#to filter by the location, imagine a square on the map and get only the left bottom coordinates and the right top coordinates
#and uncomment the code bellow:

#leftBotLong = insertValueHere
#leftBotlat = insertValueHere
#rightToplong = insertValueHere
#rightToplat = insertValueHere
#stream.filter(locations=[leftBotLong,leftBotlat,rightToplong,rightToplat], async=False)