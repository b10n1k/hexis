class hexis:

    def convert_hex(self,hchar):
        return hchar.decode('hex')

    def convert_char(self,char):
        if len(char)==1:
            return char.encode('hex')
        else:
            hex_str = ["".join(s.encode('hex')) for s in char]
            r=""
            for x in hex_str:
                r=r+x
                r=r+" "
            return r
    
    def hex_to_str(hextxt):
        pass

    def str_to_hex(txt):
        pass

    def asc_table(self):
        fd=open("asc_table.txt",'r')
        #while fd:
        lns = fd.readlines()
        for ln in lns:
            print(ln)
        fd.close()
    
if __name__=="__main__":
    print "Hexis"
    print "Choose Operation:"
    print "1 > convert to char"
    print "2 > convert to hex"
    print "3 > print ascii table"
    choise = input("..")
    #try:
    if choise in (1,2,3):
        print "choise "+str(choise)
        if int(choise) == 1:
            tx = raw_input("hex: ")
            val = hexis().convert_hex(tx)
            print(tx+" >> "+repr(val))
        elif int(choise) == 2:
            tx = raw_input("char: ")
            val = hexis().convert_char(tx)
            print(tx+" >> "+str(val))
        elif int(choise) == 3:
            hexis().asc_table()
        
    #catch ValidInput:
    else:    
        print "This is not an Option"
