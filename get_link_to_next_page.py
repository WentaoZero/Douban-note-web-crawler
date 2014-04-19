import urllib2
def get_page(url):
    return urllib2.urlopen(url).read()

def get_link_to_next_from_page(page):
	start_point = page.find('<span class="next">')
	end_point   = page.find('</span>',start_point+1)
	page_useful = page[start_point:end_point]

	key_href    = 'href="'
	start_point = page_useful.find(key_href)
	if start_point == -1:
		return None
	end_point   = page_useful.find('"/>',start_point)
	
	return page_useful[start_point+len(key_href):end_point]


def get_link_to_next_page(url):
	page = get_page(url)
	link = get_link_to_next_from_page(page)

	return link
def get_note_page_from_home(url):
	page        = get_page(url)
	start_point = page.find('<div class="info">')
	end_point   = page.find('<div class="clear"></div>',start_point+1)
	#page_useful = page[start_point:end_point]

	key_note   = "notes"
	start_note = page.find('photos',start_point)
	end_note   = page.find(key_note,start_note)

	#page_useful = page[start_note:end_note+7]

	key_href   = 'href="'
	start_link = page.find(key_href,start_note)
	end_link   = end_note

	link_of_note = page[start_link+len(key_href):end_link+len(key_note)]

	return link_of_note

def get_links_of_pages(url,number):
	
	url_note = get_note_page_from_home(url)
	count    = 0
	links    = {}

	while True:
		if url_note == None:
			break

		elif count >= number:
			break
		
		else:
			url_note = get_link_to_next_page(url_note)
			if url_note != None:
				links['page_' + str(count)] = url_note
			count += 1 
	
	return links


#print get_links_of_pages("http://www.douban.com/people/audreyang/notes",6)
