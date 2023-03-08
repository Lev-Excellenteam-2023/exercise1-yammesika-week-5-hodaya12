logo_path="logo.jpg"

def get_file(filename,buffer_size=2**10*8):
    with open(filename,"rb") as f:
        x=''
        while chunk := f.read(buffer_size):
            i = 0
            while i<len(chunk):
                try:
                    if(chunk.decode(encoding="utf8", errors='ignore')[i]>='a' and chunk.decode(encoding="utf8", errors='ignore')[i]<='z'):
                        x=x+chunk.decode(encoding="utf8", errors='ignore')[i]
                    elif chunk.decode(encoding="utf8", errors='ignore')[i]=='!':
                        x = x + chunk.decode(encoding="utf8", errors='ignore')[i]
                        if(len(x))>=5:
                            yield x
                            x=''
                    else:x=''
                except:x=''
                i=i+1



for i in get_file(logo_path):
    print("message is:  "+i)