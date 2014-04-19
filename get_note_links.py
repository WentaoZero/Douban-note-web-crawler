import urllib2
import os
def get_page(url):
    return urllib2.urlopen(url).read()

def get_next_link_of_note(content):
    start_point = content.find('<a title=')
    if start_point == -1:
        return None,None, 0

    #exract all useful content
    start_note = content.find('"', start_point)
    end_note   = content.find('</a>', start_note + 1)
    note       = content[start_note + 1:end_note]
    
    #exract title
    start_title = content.find('"', start_point)
    end_title   = content.find('"', start_title+1)
    title       = content[start_title+1:end_title]
    
    #exract link
    key_href   = 'href="'
    start_link = note.find(key_href)
    end_link   = note.find('">',start_link)
    link       = note[start_link+len(key_href):end_link]

    return title,link, end_note



def get_links_of_notes(page):
    link_list = {}

    while True:
        title,link,endpos = get_next_link_of_note(page)
        if link:
            link_list[title] = link
            page             = page[endpos:]
        else:
            break
    return link_list


def download_notes_from_note_page(url,dir):
    page      = get_page(url)
    link_list = get_links_of_notes(page)


    if not os.path.exists(dir):
        os.mkdir(dir)
    for article in link_list:
        print 'Downloading ' + '[ ' + article + ' ]'
        file_object = open(dir + '/' + article.replace('/','|') + '.html', 'w')
        # '/' is not allowed to use in a filename under HFS+(OS X)
        file_object.write(get_page(link_list[article]))
        file_object.close()
        print '100%'
    print '\n'
    print 'Articles saved in directory [' + dir + ']'
    print str(len(link_list)) + ' in total'
    print '\n'

#download_notes_from_note_page('http://www.douban.com/people/audreyang/notes','dir')
