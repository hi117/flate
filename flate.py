import zlib
def inflate(f, o):
    '''
    inflate(f, o)
    Inflates a file f and outputs the result to o.
    '''
    fd = open(f, 'rb')
    od = open(o, 'wb')
    od.write(zlib.decompress(fd.read()))
    fd.close()
    od.close()

def deflate(f, o):
    '''
    deflate(f, o)
    Deflates a file f and outputs the result to o.
    '''
    fd = open(f, 'rb')
    od = open(o, 'wb')
    od.write(zlib.compress(fd.read()))
    fd.close()
    od.close()
