from get_note_links import *
from get_link_to_next_page import *


def download_notes(url,page_number,dir):
	links = get_links_of_pages(url,page_number)

	for page in links:
		#print article
		download_notes_from_note_page(links[page],dir)

	#return get_links_of_pages(url,page_number)


#print get_links_of_pages("http://www.douban.com/people/audreyang/",20)