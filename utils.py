import re
import google
import urllib2
import bs4

def parse_raw(raw):
    """Parses raw input for a keyword and Google search query.
    
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
    """Searches the query using Google and then gets the answer based on keyword.
    
    Args:
        keyword: Who?
        
        query: A string.
    """
    page_list = []
    for
