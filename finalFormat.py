productIdStart=2
record=""
flag=0
recordend=""
recordHead=[]
recordEnd=[]
productSet=[]
formatedFile=file("finalReport.txt",'a')
for line in open("result.txt"):
    recordArry=line.strip().split(",")
    #recordHead=recordArry[0:2]
    #record=','.join(recordHead)
    #print recordHead
    recordEnd=recordArry[productIdStart:len(line)]
    #print recordEnd
    print len(recordArry)
    if len(recordEnd)<=0:
        print line
        formatedFile.write(line.strip())
        formatedFile.write(",1\n")
        
        
    productSet=set(recordEnd)
    for product in productSet:
        recordHead=recordArry[0:productIdStart]
        recordHead.append(product)
        recordHead.append(str(recordEnd.count(product)))
        record=','.join(recordHead)
        formatedFile.write(record)
        formatedFile.write("\n")

        #print recordHead
        #print record
        #print "next"
        recordHead=[]

            #record=record+","+product

            #print product
            #print recordEnd.count(product)
            #print record
    
        

    #print recordArry[0]
    #print recordHead
    #print recordEnd
    #print productSet
    #print line
   

#formatedFile=file("finalReport.txt",'a')
#formatedFile.write(record)
           
       

