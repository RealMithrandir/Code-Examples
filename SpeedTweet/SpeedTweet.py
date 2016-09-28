from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 'YOUR CONSUMER KEY'
csecret = 'YOUR SECRET KEY'
atoken = 'YOUR ACCESS TOKEN'
asecret = 'YOUR SECRET TOKEN'

#def extract_urls():

class colors:
    """Uses ANSI codes to manipulate terminal printing colors.  Use by inserting colors.COLORNAME into a printed string to change following colors"""
    CSI = '\033'
    
    black   = ""
    red = ""
    green   = ""
    yellow  = ""
    blue    = ""
    magenta = ""
    cyan    = ""
    white   = ""
    off     = ""
    
    #change background colors
    bg_black= CSI+'[40m'
    bg_red  = CSI+'[41m'
    bg_green= CSI+'[42m'
    bg_yellow=CSI+'[43m'
    bg_blue = CSI+'[44m'
    bg_magenta=CSI+'[45m'
    bg_cyan = CSI+'[46m'
    bg_white= CSI+'[47m'
    bg_off  = CSI+'[49m'

def Display_Text(text, rate, length):
        ptime = 0 #used to track delay between displaying words
        for word in text.split(): #split the body of text into a list whever there is whitespace, then iterate through each element of the resulting list
            waiting = True
            while waiting: #wait until DELAY seconds have passed, then move on to the next word
                if time.time()-ptime>delay:
                    w = word.strip() #remove leading/following whitespaces from word.  Now unessecary
                    if w != '': #ignore empty strings, shouldn't happen ever anymore.  Now unessecary
                        print Prep_String(w,length,[colors.black, colors.red])
                    ptime = time.time()
                    waiting = False
                time.sleep(delay/5.0) # loop approximatly 5 times, checking delay each time

def Word_Point(word):
    """Find the "center" point of the word, to align and color"""
    if len(word) == 0:
        return None
    vowels = 'aeiouyAEIOUY'
    center = len(word)/2
    pattern = []
    i = 0
    while i<center:
        pattern = [i, -i]+pattern
        i+=1
    #print pattern
    for i in pattern:
        if word[i] in vowels:
            i_abs = i%len(word)
            return i_abs
    return center

def Prep_String(word,length,pallet):
    #print word
    if len(word) != 0:
        c = Word_Point(word)
        #print c
        front_padding = (length/2)-c
        back_padding = length-front_padding-len(word)
        s = ' '*front_padding+pallet[0]+word[:c]+pallet[1]+word[c]+pallet[0]+word[c+1:]+' '*back_padding
        return s            

class listener (StreamListener):
    def on_data (self, data):
        try:
            #print data, type(data)
            i1 = data.find("text")
            if i1 != -1: #if tweet text is found in the data string
                i_start = data[i1:].find(':')+i1+1 #shifting indecies around
                i_end = data[i1:].find(',')+i1
                tweettext = data[i_start:i_end]
                Display_Text (tweettext, 200, 20)
            #extract_urls(data)
            #saveFile = open ('twitDB1.csv','a')
            #saveFile.write (data)
            #saveFile.write('\n')
            #saveFile.close ()
            return True
        except BaseException, e:
            print 'failed ondata,',str (e)
            time.sleep (5)

if __name__ == '__main__':
    rate = 500 #in WPM
##    if len(sys.argv) > 1: #get command line arguments
##       rate = int(sys.argv[1])
##        url = sys.argv[2]
##        text = Import_Data(url)
##   else: #prompt user for url, rate
    rate = int(input("Desired reading rate (in words per minute): "))
    s = raw_input("Enter keywords seoarated by a space: ")
    s = s.split()
    #convert text to ascii, may want to improve in the future (py3?)
    print "Collecting tweets"
    delay = 60.0/rate #get delay, in seconds, between each word's appeareance

    length = 30 #length of each output line in terminal-can make as long as terminal width, used for alignment padding
    
    def on_error (self, status):
        print status

auth = OAuthHandler (ckey, csecret)
auth.set_access_token (atoken, asecret)
twitterStream = Stream (auth, listener ())
twitterStream.filter (track = s)
