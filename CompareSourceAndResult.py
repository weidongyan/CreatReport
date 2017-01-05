ProductIdCounter = 0
TicketIdCounter = 0
UserIdCounter = 0
CompareLog = file("CompareLog.txt",'a')
for item in open("sourcefile.txt"):
    print len(item.strip())
    if len(item.strip()) ==12:
        ProductIdCounter = ProductIdCounter +1
    elif len(item.strip()) > 12:
        TicketIdCounter = TicketIdCounter +1
    elif len(item.strip()) < 12:
        UserIdCounter = UserIdCounter +1
    else:
        print item
        #CompareLog.write("Error Find in Sourcefile \n")
        #CompareLog.write(item)
print "ProductIdCounter is " + str(ProductIdCounter)
print "TicketIdCounter is " +str(TicketIdCounter)
print "UserIdCounter is " +str(UserIdCounter)
CompareLog.write("Product Total in sourcefile is: " + str(ProductIdCounter) +"\n")
CompareLog.write("Tickect Total in sourcefile is: " + str(TicketIdCounter) +"\n")
ProductIdArray = []
ProductIdSet = []
ProductionIdInResult = 0
for line in open("finalReport.txt"):
    RecordArray = line.strip().split(",")
    try:
        if not RecordArray[3]:
            CompareLog.write("Error find in finalReport: try \n")
            CompareLog.write(line)
    except:
        CompareLog.write(line)
    ProductIdArray.append(RecordArray[0])
    ProductIdSet = set(ProductIdArray)
    #print len(RecordArray)
    if len(RecordArray) ==4:
        #ProductIdArray.append(RecordArray[0])
        #ProductIdSet = set(ProductIdArray)
        #print RecordArray[3].strip()
        temp=RecordArray[3].strip()
        if temp.isdigit():
            #print "temp"
            #print temp
            ProductionIdInResult = ProductionIdInResult + int(temp)
    else:
        #print line
        CompareLog.write("Error find in finalReport:" + line +"\n")

#print len(ProductIdArray)
#print ProductIdSet
#print ProductionIdInResult
#print "Production Total in finalReport is: " +str(ProductionIdInResult)
CompareLog.write("Product Total in finalReport is: " + str(ProductionIdInResult) + '\n')
CompareLog.write("Tickect Total in finalReport is: " + str(len(ProductIdSet)) +'\n')
CompareLog.close()


