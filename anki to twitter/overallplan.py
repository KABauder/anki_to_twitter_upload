# -*- coding: utf-8 -*-

#1. Take the anki_export.txt file, and read it.
# =+-*/_ #

import os

import imp
import time
import random
#markovbot = imp.load_source('markovbot', '/Users/kylebauder/Desktop/TweetBot/markovbot/markovbot/markovbot27.py')

#from markovbot import MarkovBot

import TwitterAPI

file = open("anki_export.txt","r")

#Currently have a list of all the lines.

#I want to just get the german noun or verb...
#Want to make sure that it is readable, so it should include

filelist = file.readlines()

import time

count = 0

def split_into_list(filelist,n):
    temp = ""
    listo = []
    for char in filelist[n]:

        if char == "<":
            if temp != "":
                listo.append(str(temp))
                temp = ""
                temp += char
        elif char == ">":
            temp += char
            listo.append(str(temp))
            temp = ""
        else:
            temp += char

    listo.append(str(temp))
    temp = ""

    return listo

def list_split(listo):

    list2 = []
    count = 0

    for string in listo:

        string = string.replace("\t","")
        string = string.replace("\n","")
        string = string.replace('\\',"")

        if count != len(listo)-1:
            string = string.replace("/","")

        string = string.replace('&nbsp',"")
        string = string.replace('"',"")
        string = string.replace('>',"")
        string = string.replace('<',"")

        string = string.replace("img src=","")
        string = string.replace("<div>","")
        string = string.replace("div>","")

        #umlauts
        string = string.replace("\xc3\xbc","ü")
        string = string.replace("\xc3\xa4","ä")

        try:
            if string[-1] == " ":
                string = string[:-1]
        except:
            string = string.replace("\xc3\xa4","ä")

        #for the english translation
        if count == len(listo)-1:

            string = " " + string
            string = string.replace(";"," /")

        #for the german section
        if count == 0:
            string = string.replace(";","")

        if string != "" and string != "div":

            list2.append(string)


        count += 1

    return list2

def properformatting(list2):

    #if it has more than one screenshot, remove:

    count = 0
    listofnums = []
    for i in range(0,len(list2)):
        if i > 0:
            if "Screen Shot" in list2[i]:
                if count < 1:
                    listofnums.append(list2[i])
                count += 1
            else:
                listofnums.append(list2[i])
        else:
            listofnums.append(list2[i])

    if count > 0:
        return listofnums


biglist = []
for i in range(112,150):
    biglist.append(split_into_list(filelist,i))

biglist2 = []
for index in biglist:
    biglist2.append(list_split(index))

biglist3 = []
for index in biglist2:
    newlist = properformatting(index)
    if newlist != None:
        biglist3.append(newlist)

def sendtotwitter(list2):
    filename = "/Users/kylebauder/Documents/Anki/User 1/collection.media/"+str(list2[1])

    # ALL YOUR SECRET STUFF!
    # Consumer Key (API Key)
    cons_key = 'Y7dzXbP9Jx7HPnLyscaAcuzHD'
    # Consumer Secret (API Secret)
    cons_secret = 'OE9tDUnQLzJGZ6LcwliVt5OJ3M3u8Xdx21ETSJMQtaRT0qe9qA'
    # Access Token
    access_token = '953403732384886784-A4eYTNV8nfb8meOEoN0zbQvvchi0Agr'
    # Access Token Secret
    access_token_secret = 'jfm2s1wkORCc1HgGyCV28c7pRnMuGAzU4TvLgz0QOpTDR'

    api = TwitterAPI.TwitterAPI(cons_key, cons_secret, access_token, access_token_secret)
    file = open(filename, 'rb')
    data = file.read()
    hashtag = randomizer()
    stringtoadd = list2[0]+" >>> "+list2[2] + hashtag
    r = api.request('statuses/update_with_media', {'status':stringtoadd}, {'media[]':data})

def randomizer():

    string2 = ""
    rando = random.randint(0,3)

    if rando == 0:
        string2 = " #learngerman"
    elif rando == 1:
        string2 = " #deutsch"
    elif rando == 2:
        string2 = " #videospielen"

    return string2

bigcount = 100

for index in biglist3:
    bigcount += 1
    sendtotwitter(index)
    time.sleep(30)
    print(bigcount)
