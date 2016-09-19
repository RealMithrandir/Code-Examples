import sys, os, time

class colors:
    
    CSI = '\033'
    
    black   = CSI+'[30m'
    red = CSI+'[31m'
    green   = CSI+'[32m'
    yellow  = CSI+'[33m'
    blue    = CSI+'[34m'
    magenta = CSI+'[35m'
    cyan    = CSI+'[36m'
    white   = CSI+'[37m'
    
    bg_black= CSI+'[40m'
    bg_red  = CSI+'[41m'
    bg_green= CSI+'[42m'
    bg_yellow=CSI+'[43m'
    bg_blue = CSI+'[44m'
    bg_magenta=CSI+'[45m'
    bg_cyan = CSI+'[46m'
    bg_white= CSI+'[47m'

def Word_Point(word):
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

def Import_Data(location):
    """opens the data file in the specified location, returning the headers in one block and raw content in another"""
    f = open(location,'r')
    t = f.read()
    h = '##########BODY\n'
    i = t.find(h)
    i_x = i+len(h)
    #print i, i_x
    return t[i_x:]

sample = 'This is a simple test message, meant to demo a clone of various speed-reading tools.  It prints a stream of text to the terminal at a specified \
rate, aligning the centermost vowel of each word to be in a column'

if __name__ == '__main__':
    rate = 700 #in WPM
    if len(sys.argv) > 1:
        rate = int(sys.argv[1])
        f_path = sys.argv[2]
        sample = Import_Data(f_path)
    rps = rate/60.0
    delay = 1.0/rps
    #print delay
    #print time.time()

    length = 30

    print colors.bg_white
    ptime = 0

    for word in sample.split():
        waiting = True
        while waiting:
            if time.time()-ptime>delay:
                w = word.strip()
                if w != '':
                    print Prep_String(w,length,[colors.black, colors.red])
                #print word
                #print Word_Point(word)
                ptime = time.time()
                waiting = False
            time.sleep(delay/5.0)
    
#    for arg in sys.argv:
#        print arg
