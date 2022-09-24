from PyPDF2 import PdfMerger

n = int(input('how many pdf you want to merge: '))
pdfs=[]
while n!=0:
    pdfinp= str(input('name/path of pdf file: '))
    pdfs.append(pdfinp+'.pdf')
    n-=1
merger = PdfMerger()
print(pdfs)
for pdf in pdfs:
    merger.append(pdf)
    
merger.write('result.pdf')
merger.close()