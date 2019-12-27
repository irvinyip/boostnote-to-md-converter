import os
import re
import json

rootdir = '.\\notes'

# build folder dict
a = json.load(open('./boostnote.json'))
folders = a['folders']
folderDict = {}
for x in folders:
    print(x['key'])
    folderDict[x['key']] = x['name']


# Loop all files
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filePath = os.path.join(subdir, file)
        f = open(filePath)

        captureStart = False
        nextlineIsTitle = False
        for line in f:
            # Get folder value when line starts with 'folder'
            if line[:6] == 'folder':
                folderkey = line.split(' ')[1].split('"')[1]

            if nextlineIsTitle:
                # Remove leading space and # characters
                fileNameOutput = ' '.join(line.split('#')[-1].split(' ')[1:])
                fileNameOutput = fileNameOutput.split('\n')[0]
                fileNameOutput = re.sub(r'[^A-Za-z0-9 ]+', '', fileNameOutput)

                # Remove special characters for folder name
                folder = folderDict[folderkey]
                folder = re.sub(r'[^A-Za-z0-9 ]+', '', folder)
                
                # Append folder name as prefix of file name, which is used as title on import
                fileNameOutput = '[' + folder + '] ' + fileNameOutput
                print(fileNameOutput)
                outFilePath = os.path.join('.\\output', fileNameOutput) + '.md'
                outputFile = open(outFilePath,"w+")
                nextlineIsTitle = False

            # Detect ''' staring line as end of content block, exit for line loop
            if line[:3] == "'''":
                outputFile.close()
                break
            
            # Write to file within content block
            if captureStart:
                outputFile.write(line)

            # Detect content: ''' line as starting capture next line
            if line[:12] == "content: '''":
                captureStart = True
                nextlineIsTitle = True
        

