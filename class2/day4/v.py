def fileWrite():
    fp = open("test.txt","w") #w r a  t b
    fp.write("hello\nhi\npython")
    fp.close()

def fileRead():
    fp = open("test.txt","r") #w r a  t b
    for rd in fp: #라인단위로 읽어들인다
        print(rd)
    # rd = fp.read()
    # print(rd)
    fp.close()

fileWrite()
fileRead()
