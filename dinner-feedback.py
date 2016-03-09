#!/usr/bin/env python

#import time to use and put a time stamp at the start
import datetime
print datetime.datetime.now()

#just trying to make a simple script - this will ask the question about dinner
print ( "hey there, what did you have for dinner?" )

#this will get the input from the user
dinner_answer = raw_input()

#this will output the answer and ask if it was good
print ( "oh really, you had " + dinner_answer + ", was it good?" )

#and now we should get an answer again into another var
like_answer = raw_input()

#do an if statement
if like_answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
	print ( "glad you liked it" )
else:
	print ( "sorry you didn't like it" )

#now that we have that out of the way - I want to get a list of s3 buckets
#so I need to import the awscli
#import awscli
#aws s3 ls

#import boto.ec2

#did that work?
print ( "did that work?" )

#sleep - I can only do this because I imported the date time thing - but this is sleep for 15 seconds
time.sleep(15)

#also use time stamp at the end
print datetime.datetime.now()
