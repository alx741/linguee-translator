#! /usr/bin/env python3

import sys
import os
from http import client
##variables for the search query
knownWord = ''
knownLanguage = ''
translatingLanguage = ''

if len(sys.argv) is not 4:
    print('Usage: ' + os.path.basename(__file__) + ' word SOURCE TARGET')
    print('\nSOURCE\n  Original Language')
    print('\nTARGET\n  Target Language')
    sys.exit(1)
else:
 conn = client.HTTPConnection("www.linguee.com") #connect to their server
 conn.request("GET", "/"+str(sys.argv[2])+"-"+str(sys.argv[3])+"/search?query="+str(sys.argv[1])) #linguee is done entirely through the web with results based on the client's browser
 r1 = conn.getresponse() #get the response(raw html)
 stringData = str(r1.read()) #turn the response into a string for analysis
 tagIndex = 0 #loop control variable
 while tagIndex < len(stringData): #search through the entire file
  tagIndex = stringData.find('dictLink featured', tagIndex) #dictLink featured is the tag right before the translated term. In case they change their website this argument will have to be changed. Luckily it only appears once
  if tagIndex == -1: #end of file, get out
   break
  SpecificTagCloseIndex = stringData.find('>', tagIndex)+1 #find the closing tag after dickLink featured, this ends the entire tag and is where the translation begins
  TagAfterSpecificTagOpenIndex = stringData.find('<', SpecificTagCloseIndex) #find the opening tag of the next element, this is where the translation ends
  print(stringData[SpecificTagCloseIndex:TagAfterSpecificTagOpenIndex]) #print out what's between the tags, the translation
  tagIndex += 2 #iterate so we don't have an infinite loop
