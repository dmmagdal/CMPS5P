#  Web.py

from urllib.request import urlopen

def get_page(url):
   """
   Retrieve the contents of a web page, convert it to a string, then return
   the string.
   """
   socket = urlopen(url)     # open a connection to url
   data = socket.read()      # read everything as a stream of bytes
   socket.close()            # close connection
   s = str(data, 'utf-8')    # convert bytes to string using utf-8 encoding
   return s                  # return string
# end get_page()


#-- main ----------------------------------------------------------------------

text = get_page('https://classes.soe.ucsc.edu/cmps005p/Spring17/')
print()
print(text)
print()