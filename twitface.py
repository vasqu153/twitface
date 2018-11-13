# twitface.py
#
# Author: Paul Vasquez
# Email: vasqu153@mail.chapman.edu
# Co-Author: Gabriela Ghermezi
# Email: gherm101@mail.chapman.edu
# Course: CPSC 353
# Version 1.2
# Date: November 11, 2018
#
# This program should prompt user to enter their twitter and facebook login
# information,and give the user an option to either post their own
# status update, or select from a generic list of options. The program will then
# display the status, and will verify that the user wants the program to post
# to twitter and facebook
#

# Connect to Twitter API and Facebok API

# import twitter #hidden until needed for code
# import json #hidden until needed

print "---------------------------------------------------------------------"
print ''
print "Welcome to TwitFace!"
print ''
#print"Please enter your login credentials for Twitter: "
#print
#print "Username: "
#print "Password: "
#print
#print "Login successful"

print "---------------------------------------------------------------------"
print ''
print "Here you can either post to twitter with a status of your own, or you can choose from a collection we have provided."
print ''
choice = 0
status = ""
print "Enter 1 to create your own post, or 2 to select from a list"
print ''

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
            status = ""
            break
        elif choice_2 == 2:
            status = ""
            break
        elif choice_2 == 3:
            status = ""
            break
        elif choice_2 == 4:
            status = ""
            break
        else:
            print "Invalid Entry! Try Again!"

print ""
print "Here's your status update"
print ""
print(status)

print "---------------------------------------------------------------------"

# Connecting to Twitter API

#print 'Connecting to Twitter'

# access keys from previous Twitter API access
# hidden until needed

#CONSUMER_KEY = ''
#CONSUMER_SECRET = ''
#OAUTH_TOKEN = ''
#OAUTH_TOKEN_SECRET = ''
#auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           #CONSUMER_KEY, CONSUMER_SECRET)

#twitter_api = twitter.Twitter(auth=auth)

#print "Test to check that connecction is successful"
#print
#print twitter_api
#print

print "---------------------------------------------------------------------"
