import sys, os, time, newspaper
from newspaper import Article

class colors:
    """Uses ANSI codes to manipulate terminal printing colors.  Use by inserting colors.COLORNAME into a printed string to change following colors"""
    CSI = '\033'
    
    black   = CSI+'[30m'
    red = CSI+'[31m'
    green   = CSI+'[32m'
    yellow  = CSI+'[33m'
    blue    = CSI+'[34m'
    magenta = CSI+'[35m'
    cyan    = CSI+'[36m'
    white   = CSI+'[37m'
    off     = CSI+'[39m'
    
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

def Import_Data(url):
    """Using Newspaper.py, fetches body text from the given URL, returning said text, as well as the article object"""
    a = Article(url)
    a.download()
    a.parse()
    return a.text, a

def Display_Text(text, rate, length):
    print colors.bg_white
    ptime = 0 #used to track delay between displaying words

    for word in text.split(): #plit the body of text into a list whever there is whitespace, then iterate through each element of the resulting list
        waiting = True
        while waiting: #wait until DELAY seconds have passed, then move on to the next word
            if time.time()-ptime>delay:
                w = word.strip() #remove leading/following whitespaces from word.  Now unessecary
                if w != '': #ignore empty strings, shouldn't happen ever anymore.  Now unessecary
                    print Prep_String(w,length,[colors.black, colors.red])
                ptime = time.time()
                waiting = False
            time.sleep(delay/5.0) # loop approximatly 5 times, checking delay each time
    print colors.bg_off
    print colors.off

# Sample text, for testing printing w/o scraping
sample = 'This is a simple test message, meant to demo a clone of various speed-reading tools.  It prints a stream of text to the terminal at a specified \
rate, aligning the centermost vowel of each word to be in a column'

if __name__ == '__main__':
    rate = 500 #in WPM
##    if len(sys.argv) > 1: #get command line arguments
##       rate = int(sys.argv[1])
##        url = sys.argv[2]
##        text = Import_Data(url)
##   else: #prompt user for url, rate
    rate = int(input("Desired reading rate (in words per minute): "))
    url = raw_input("Source url: ")
    text, art = Import_Data(url)
    #convert text to ascii, may want to improve in the future (py3?)
    text = text.encode('ascii','ignore')
    print "Fetching & Parsing Article"
    delay = 60.0/rate #get delay, in seconds, between each word's appeareance

    length = 30 #length of each output line in terminal-can make as long as terminal width, used for alignment padding
    
    Display_Text(text, rate, length)
    
    mode = 1
## Add interactivity for repeating, scoring, here
    while mode == 1: #lazy approach to a proper state machine, will have to change in future
        print "Article completed"
        mode = 0
        print "Type 1 and press enter to repeate text, type 2 and press enter to score and save article,  press enter to quit"
        mode = input(':')
        if mode == 1:
            Display_Text(text, rate, length)
        if mode == 2:
            print "Enter a string of numbers, describing the story in the following manner: 1 = Informative, 2 = Funny, 3 = Bad, 4 = Good, 5 = Relevant"
            score = raw_input(':')
            f_p = os.getcwd() #Get current working directory, as location to write file to
            f_n = str(time.time())+'_'+'_'.join(url.split('/'))+'.txt' #file name, as funtion of time and url--NEED BETTER ENCODING FOR URL (base 36?)
            f = open(os.path.join(f_p, f_n), 'w')
            f.write(score+'\n')
            f.write('##########\n')
            f.write(text)
            f.close()
    
    print "Closing program"
    time.sleep(1)
