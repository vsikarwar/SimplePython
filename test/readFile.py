file = open("result.txt","r")
totalRunTime = 0
totalRec = 0

skippedAvg = 0
skippedTotal = 0
insertAvg = 0
insertTotal = 0
updateAvg = 0
updateTotal = 0
processingAvg = 0
processingTotal = 0
deleteAvg = 0
deleteTotal = 0
detailingAvg = 0
detailingTotal= 0
publishingAvg = 0
publishingTotal = 0
errorsAvg = 0
errorsTotal = 0

isTotalTime = 0
for line in file:
    l = line.split(' ')

    if "Total run time:" in line:
        isTotalTime= 1
        continue
    
    if isTotalTime == 1:
        time = l[0]
        isTotalTime = 0
        if(totalRunTime < int(time)):
            totalRunTime = int(time)
            totalRec = totalRec+ 1;
    
    if l[0] == "Skipped":
        skippedAvg = skippedAvg + float(l[5])
        skippedTotal = skippedTotal + 1;
        
    if l[0] == "Updated":
        updateAvg = updateAvg + float(l[5])
        updateTotal = updateTotal + 1
        
    if l[0] == "Inserted":
        insertAvg = insertAvg + float(l[5])
        insertTotal = insertTotal + 1
    
    if l[0] == "Deletes:":
        deleteAvg = deleteAvg + float(l[5])
        deleteTotal = deleteTotal +1
    
    if l[0] == "Detailing:":
        detailingAvg = detailingAvg + float(l[4])
        detailingTotal = detailingTotal + 1
    
    if l[0] == "Publishing:":
        publishingAvg = publishingAvg + float(l[4])
        publishingTotal = publishingTotal + 1
    
    if l[0] == "Errors:":
        errorsAvg = errorsAvg + float(l[4])
        errorsTotal = errorsTotal + 1
        
    if l[0] == "Processing:":
        processingAvg = processingAvg + float(l[4])
        processingTotal = processingTotal + 1

print("Max Run Time : " + str(totalRunTime))
print("Total Skipped Record Average Time : " + str(skippedAvg/skippedTotal))
print("Total Update Record Average Time : " + str(updateAvg/updateTotal))
print("Total Inserted Record Average Time : " + str(insertAvg/insertTotal))
print("Total Deletes Record Average Time : " + str(deleteAvg/deleteTotal))
print("Total Detailing Record Average Time : " + str(detailingAvg/detailingTotal))
print("Total Publishing Record Average Time : " + str(publishingAvg/publishingTotal))
print("Total Errors Record Average Time : " + str(errorsAvg/errorsTotal))
print("Total Processing Record Average Time : " + str(processingAvg/processingTotal))