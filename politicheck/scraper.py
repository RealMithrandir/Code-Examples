from selenium import webdriver
#import urllib2
from bs4 import BeautifulSoup
import pickle, os, time, sys, random

path = os.getcwd()
f_scraped = os.path.join(path,'scraper_output_{}.pickle'.format(int(time.time())))

statements = []
browser = webdriver.Firefox()
browser.set_page_load_timeout(10)
npages = 51
for num in xrange(1,npages):
    print "Scraping page {} of {}".format(num,npages)
    browser.get('http://www.politifact.com/truth-o-meter/statements/?page={}'.format(num))
    #elem = browser.find_element_by_xpath("//*")
    #source_code = elem.get_attribute("outerHTML")
    source_code = browser.page_source
    soup = BeautifulSoup(source_code,'html.parser')
    checks = soup.find_all(class_='statement')
    for c in checks:
        meter = unicode(c.find('img')['alt']).strip()
        reason = unicode(c.find(class_='quote').string).strip()
        source = unicode(c.find(class_='statement__source').string).strip()
        body = unicode(c.find(class_='link').string).strip()
        statements.append(tuple([meter,reason,source,body]))
    time.sleep(random.random()*2.0)
browser.quit()
#print '\n'
print len(statements)

f = open(f_scraped,'wb')
pickle.dump(statements, f, -1)
f.close()
