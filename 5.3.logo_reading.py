logo_path="logo.jpg"

def get_file(filename,buffer_size=2**10*8):
    with open(filename,"rb") as f:
        x=''
        while chunk := f.read(buffer_size):
            i = 0
            while i<len(chunk):
                try:
                    it1=chunk.decode(encoding="utf8", errors='ignore')[i]
                    if(it1>='a' and it1<='z'):
                        x=x+it1
                    elif it1=='!':
                        x = x + it1
                        if(len(x))>=5:
                            yield x
                            x=''
                    else:x=''
                except:x=''
                i=i+1



for i in get_file(logo_path):
    print("message is:  "+i)