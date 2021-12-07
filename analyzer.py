import os
from openpyxl import Workbook
from datetime import datetime

user_input = input("Enter the path of your file: ")
     
assert os.path.exists(user_input), "I did not find the file at "+str(user_input)
f = open(user_input,'r')
print("Log File found, beginning analysis...")
f.close()

ProposerBlockMined = 'ProposerBlockMined'
ValidProposerBlockDownloaded = 'ValidProposerBlockDownloaded'
ProposerBlockConfirmed = 'ProposerBlockConfirmed'
ProposerBlockRolledBack = 'ProposerBlockRolledBack'
epoch = datetime.utcfromtimestamp(0)

def getTimestamp(timestr):
    dateTimeObj = datetime.strptime(dateTimeString, '%Y-%m-%d %H:%M:%S,%f')
    delta = dateTimeObj - epoch
    return delta.total_seconds()*1000

hashToNumber = {}
hashToCreationTimestamp = {}
hashToCreationEvent = {}
hashToConfirmationTimestamp = {}
hashToRollbackTimestamp = {}
with open(user_input, 'r') as f:
    for line in f:
        if "BENCHMARKING:" not in line:
            continue
        print(line)
        benchmarkSubstrings = line[line.find("BENCHMARKING"):-1].split(':')
        dateTimeString = line.split('[')[0][:-1]
        timestamp = getTimestamp(dateTimeString)
        event = benchmarkSubstrings[1]
        blockNumber = benchmarkSubstrings[3]
        blockHash = benchmarkSubstrings[-1][1:-1]
        hashToNumber[blockHash] = blockNumber
        if event == ProposerBlockMined or event == ValidProposerBlockDownloaded:
            hashToCreationEvent[blockHash] = event
            hashToCreationTimestamp[blockHash] = timestamp
        if event == ProposerBlockConfirmed:
            hashToConfirmationTimestamp[blockHash] = timestamp
        if event == ProposerBlockRolledBack:
            hashToRollbackTimestamp[blockHash] = timestamp

f.close()

wb = Workbook()
ws = wb.active
ws.title = 'Data'
ws.append(['Block Number','Block Hash','Timestamp - Creation','Event','Timestamp - Confirmation','Timestamp - Rollback'])

for key in hashToNumber.keys():
    ws.append([hashToNumber.get(key,''),
    key,
    hashToCreationTimestamp.get(key,''),
    hashToCreationEvent.get(key,''),
    hashToConfirmationTimestamp.get(key,''),
    hashToRollbackTimestamp.get(key,'')])

wb.save('analyzed_data.xlsx')