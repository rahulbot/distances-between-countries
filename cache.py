import hashlib, os, codecs

'''
Super basic file-based cache (utf-8 friendly).  Helpful if you're developing a 
webpage scraper and want to be a bit more polite to the server you're scraping 
while developing. The idea is that it caches content in files, each named by the 
key you pass in (use the md5_key helper to generate keys and make this super easy).
'''

DEFAULT_DIR = "cache"

dir = DEFAULT_DIR

def md5_key(string):
    '''
    Use this to generate filenae keys
    '''
    m = hashlib.md5()
    m.update(string)
    return m.hexdigest()

def set_dir(dir = DEFAULT_DIR):
    '''
    Don't need to call this, unless you want to override the default location
    '''
    if not os.path.exists(dir):
        os.makedirs(dir)

def contains(key):
    '''
    Returns true if a file named by key is in the cache dir
    '''
    return os.path.isfile(os.path.join(dir,key))

def get(key):
    '''
    Returns the contents of the file named by key from the cache dir.
    Returns None if file doesn't exist
    '''
    if os.path.isfile(os.path.join(dir,key)):
        with codecs.open(os.path.join(dir,key), mode="r",encoding='utf-8') as myfile:
            return myfile.read()
    return None

def put(key,content):
    '''
    Creates a file in the cache dir named by key, with the content in it
    '''
    text_file = codecs.open(os.path.join(dir,key), encoding='utf-8', mode="w")
    text_file.write(content.decode('utf-8'))
    text_file.close()
