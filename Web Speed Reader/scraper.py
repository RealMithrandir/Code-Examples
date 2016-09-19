import os, sys, newspaper, subprocess
from newspaper import Article

url = 'http://en.wikipedia.org/wiki/HMS_Zubian'

page = Article(url)
page.download()
page.parse()

path = os.getcwd()
f_name = 'test_file.txt'
f = open(os.path.join(path, f_name),'w')
#Write headers for text file
base = '##########'
h = base+'URL\n'
f.write(h)
f.write(url+'\n')

h = base+'BODY\n'
f.write(h)

out = page.text
f.write(out.encode('ascii','ignore'))
f.close()

rate = 800

f_p = os.path.join(path, 'fast_print.py')

command = ["gnome-terminal","--command=python "+f_p+" "+str(rate)+" "+os.path.join(path, f_name)]

pid = subprocess.Popen(args=command).pid
print pid
