from selenium import webdriver

setdirc = set()
dotset = set()

browser = webdriver.Firefox()

browser.get('https://goatlantalocal.com')

elem = browser.find_element('link text', 'SEARCH LOCAL BUSINESSES')

elem.click()

elems = browser.find_elements('tag name', 'a')

#For each anchor tag found, filter out the links with href
#and save them to the variable links
for elem in elems:
    links = elem.get_attribute('href')
    
    #Filters the links we really want to access and saves them to a unordered set
    if 'businesses/atlanta' in links:
        setdirc.add(links)

#Go through each set element, and open each companies page
for i in setdirc:
    browser.get(i)
    webs = browser.find_elements('tag name', 'a')

    #Look for the href attribute on each companies page
    #If the link is between 30 and 37 characters, add it to a set and print the set
    for web in webs:
        dotcom = web.get_attribute('href')
        if dotcom == None:
            continue
        if len(dotcom) in range(30, 37):
            dotset.add(dotcom)
print(dotset)

#Open up each companies website
for j in dotset:
    browser.get(j)
 

    
