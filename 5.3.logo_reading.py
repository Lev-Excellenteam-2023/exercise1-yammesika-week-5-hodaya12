logo_path="logo.jpg"

def get_file(filename):
    with open(filename, "rb") as f:
        x=''
        while chunk := f.read():
            i = 0
            while i<len(chunk):
                if(str(chunk)[i]>='a' and str(chunk)[i]<='z'):
                    x=x+str(chunk)[i]
                elif str(chunk)[i]=='!':
                    x = x + str(chunk)[i]
                    if(len(x))>=5:
                        yield x
                        x=''
                else:x=''
                i=i+1



for i in get_file(logo_path):
    print("message is:  "+i)