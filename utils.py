import re
import google
import urllib2
import bs4

def parse_raw(raw):
    """ Parses raw input for a keyword and Google search query.
    
    Args:
        raw: The input directly from the web form.
    
    Returns:
        A list with two elements, the keyword and a Google search query.
        For example:
        
        ['who', 'who played spiderman']
    """
    words = raw.strip().split()
    keyword = words[0]
    return [keyword, raw]

def search(keyword, query):
    """ Searches the query using Google and then gets the answer based on keyword.
        
        Pulls only the top 10 results.
        
    Args:
        keyword: e.g., "who"
        
        query: A string.
    
    Returns:
        A list with three answers in order of decreasing "correctness".
        Answers default to empty strings.
    """
    pages = google.search(query, num=10, start=0, stop=10)
    page_list = []
    for p in pages:
        page_list.append(p)
    
    for i in range(1):
        url = urllib2.urlopen(page_list[i])
        page = url.read().decode('utf-8')
        
        soup = bs4.BeautifulSoup(page, 'html.parser')
        raw = soup.get_text(page)
        pattern = re.compile('[\t\n ]')
        text = pattern.sub(' ', raw)
        print text[:120]

if __name__ == "__main__":
    query = '   who is fred'
    keyword = parse_raw(query)
    search(keyword, query)
