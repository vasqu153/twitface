# twitface.py
#
# Author: Paul Vasquez
# Email: vasqu153@mail.chapman.edu
# Co-Author: Gabriela Ghermezi
# Email: gherm101@mail.chapman.edu
# Course: CPSC 353
# Version 1.3
# Date: November 11, 2018
#
# This program should prompt user to enter their twitter and facebook login
# information,and give the user an option to either post their own
# status update, or select from a generic list of options. The program will then
# display the status, and will verify that the user wants the program to post
# to twitter and facebook
#

# Connect to Twitter API and Facebok API

import twitter
import json
import urlparse
import oauth2 as oauth

consumer_key = 'P8qYXSmm4Xy77ru7hRm0r22zU'
consumer_secret = '80JAMe4FnhrtgrlFWeRthxe9cj9CxdG4PK3yvsVA1LOrL6cKFd'

request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
authorize_url = 'https://api.twitter.com/oauth/authorize'

consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)

# Getting request token

resp, content = client.request(request_token_url, "GET")
if resp['status'] != '200':
    raise Exception("Invalid response %s." % resp['status'])

request_token = dict(urlparse.parse_qsl(content))

print "Request Token:"
print "    - oauth_token        = %s" % request_token['oauth_token']
print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']
print

# Redirect to allow access

print "Go to the following link in your browser:"
print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])
print

# After the user has allowed access, the program continues with verification process
accepted = 'n'
while accepted.lower() == 'n':
    accepted = raw_input('Have you authorized me? (y/n) ')
oauth_verifier = raw_input('What is the PIN? ')

# Finishing up verification process
token = oauth.Token(request_token['oauth_token'],
    request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)
client = oauth.Client(consumer, token)

resp, content = client.request(access_token_url, "POST")
access_token = dict(urlparse.parse_qsl(content))

print "Access Token:"
print "    - oauth_token        = %s" % access_token['oauth_token']
print "    - oauth_token_secret = %s" % access_token['oauth_token_secret']
print
print "You may now access protected resources using the access tokens above."
print
print "---------------------------------------------------------------------"

# Connecting to Twitter API

print 'Connecting to Twitter'

twitter_api = twitter.Api(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token_key = access_token['oauth_token'], access_token_secret = access_token['oauth_token_secret'])

print "Test to check that connecction is successful"
print
print twitter_api
print

print "---------------------------------------------------------------------"
print ''
print "Welcome to TwitFace!"
print ''
print "---------------------------------------------------------------------"
print ''
print "Here you can either post to twitter with a status of your own, or you can choose from a collection we have provided."
print ''
choice = 0
status = ""

print ""
print "Enter 1 to create your own post, or 2 to select from a list"
print ""

choice = int(input("Choice: "))
print ""
if choice == 1:
    status = raw_input("Enter your status. When finished, press Enter: ")
elif choice == 2:
    choice_2 = 0
    while True:
        print "Choose your post to share: "
        print ''
        print "1: Happy Post"
        print "2: Sad Post"
        print "3: Angry Post"
        print "4: Good Luck Post"
        choice_2 = int(input())
        if choice_2 == 1:
            status = "Having a great day so far! #happy"
            break
        elif choice_2 == 2:
            status = "Wish I had a better day today #sad"
            break
        elif choice_2 == 3:
            status = "Studied all night and my test was postponed! #angry"
            break
        elif choice_2 == 4:
            status = "#GoodLuck on midterms everyone!"
            break
        else:
            print "Invalid Entry! Try Again!"

print ""
print "Are you sure you want to post this status?"
print ""

while True:
        # main program
        while True:
            answer = raw_input('(y/n): ')
            if answer in ('y'):
                twitter_api.PostUpdate(status = status)
                print ""
                print 'Your status has successfully been posted'
                print 'Thanks for using TwitFace!'
                print ""
            if answer == 'y':
                exit()
# loops back to beginning to reprompt user input
            if answer in ('n'):
                exit()

print "---------------------------------------------------------------------"
