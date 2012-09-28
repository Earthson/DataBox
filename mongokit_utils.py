from mongokit import Connection

'''
Extension for Mongokit support

1. Auto Connection support
2. easy way to use Document Class

@with_conn
class BlogPost(Document):
    pass

You do not have to use conn.BlogPost(), just use BlogPost() to do this.

~~~~~~~~~~~~~
Inheritance:
class Comment(BlogPost.__clsobj__):
    pass
'''

conn = Connection()

def with_conn(cls):
    '''auto_register and replace cls with conn'''
    #print cls_obj.__name__
    conn.register([cls])
    cls.__clsobj__ = cls 
    #save cls self to cls.__clsobj__, may be useful when Inheritance
    return getattr(conn, cls.__name__)
