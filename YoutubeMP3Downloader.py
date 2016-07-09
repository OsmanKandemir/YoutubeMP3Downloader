#! usr/bin/env/python
#! -*- coding : utf-8 -*-



from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import urllib2

print """

             Coded OsmanKandemir
            Youtube Mp3Downloader


      """

def fonk():

    iste = raw_input("Please Enter a Video Link : ")
    print "Please wait the video Converting"

    display = Display(visible=0, size=(400, 300))
    display.start()

    browser = webdriver.Firefox()
    browser.get("http://www.youtube-mp3.org/tr")

    videolink = browser.find_element_by_id("youtube-url")
    browser.find_element_by_id('youtube-url').clear()
    videolink.send_keys(iste)

    browser.find_element_by_css_selector('#submit').click()

    time.sleep(1)

    #browser.find_element_by_link_text('Download').click()

    code = browser.page_source

   
   	
    if 'id="progress_info" class="error"' in code:
    	print "ERROR -- Twenty(20) Minutes a long video is not supported"
    
	if "</b><br />%s</div>" %iste in code:
	    print "ERROR2 -- Invalid URL"
    	
    a1 =  re.search('><b>Download</b></a><a href=".+"><b>Download</b></a><a style="',code).group(0).replace('><b>Download</b></a><a href="',"http://www.youtube-mp3.org").replace('"><b>Download</b></a><a style="','').replace("amp;","").replace('href="/get?video_id=',"").replace("&h=-1&r=-1.1","")
    a2 = re.search('k:</b>.+</div>',code).group().replace("k:</b>","").replace("</div>","")
    




    if a1:
        if a2:
            
            b1 = a1.split('"')[0]
            ab = urllib2.urlopen(b1)
            ab2 = ab.read()
            d = open('%s.mp3'%a2,'w')
            d.write(ab2)
            d.close()

    browser.close()
    display.stop()
    print "MP3 conversion is completed."

    



try:
	
	fonk()
except AttributeError:
	print "Please re-enter Link"
	fonk()