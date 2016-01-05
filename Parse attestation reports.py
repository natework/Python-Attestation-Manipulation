# Import Needed Modules
import PyPDF2, re

pdfFileObj = open('Sub-Set 20 Page Test.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
pageObj.extractText()

# Create Regex object to find Provider Name
providerNameRegex = re.compile(r'[^/]+')

# Split Output
matchSplit = providerNameRegex.findall(pageObj.extractText())
print(matchSplit[1])

#providerNameRegex = re.compile(r'*[^/]+').split(pageObj.extractText())
#print(providerNameRegex)

pageObj.getContents()
print(pageObj)
