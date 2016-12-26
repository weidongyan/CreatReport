record=""
flag=0
recordend=""
for line in open("sourcefile.txt"):
    #record +=line.strip('\n')
    #record=record +","
    #print len(line)
    recordend=","
    if len(line)>=15:
        flag=flag+1
        if flag==2:
            #print record + "\n"
            #print flag
            #print line
            #record=""
            recordend="\n"
            #record=
            flag=1
        else:
            recordend=","
    record=record+recordend+line.strip('\n')
print record

formatedFile=file("result.txt",'a')
formatedFile.write(record)
           
       

