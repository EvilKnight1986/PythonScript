# 用python写的一个计算文件哈希值的脚本
import hashlib 
import os,sys 

def CalcValue(HashName, FilePath): 
    with open(FilePath,'rb') as f:
        t = eval("hashlib." + HashName)
        Hashobj = t() 
        Hashobj.update(f.read()) 
        HashValue = Hashobj.hexdigest()
        print "%6s Value: %s" %(HashName, HashValue)
        return HashValue
        
def PrintHelp():
    print sys.argv[0] + " [-sha1] [-sha224] [-sha256]  [-sha384] [-sha512] [-md5] <FilePath>"
    sys.exit(0)
          
if __name__ == "__main__": 
    FilePath = ""
    Len = len(sys.argv)
    HashName = ['-sha1', '-sha224', '-sha256', '-sha384', '-sha512', '-md5']
    
    if 1 == Len:
        PrintHelp()
    
    for i in range(1, Len):
        if os.path.exists(sys.argv[i]):
            FilePath = sys.argv[i]
            break ;
    
    if len(FilePath) == 0:
        print 'File Not Found'
        sys.exit(0)
        
    for i in range(1, Len):
        Str = sys.argv[i]
        Str.lower()
        for Hash in HashName:
            if -1 != sys.argv[i].find(Hash):
                CalcValue(Hash[1:],FilePath)