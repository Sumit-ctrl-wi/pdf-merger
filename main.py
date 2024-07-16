import PyPDF2
pdffiles=["Harsh-Resume[2].pdf","Harsh-Resume[20].pdf","Harsh-Resume[22].pdf"]
merger=PyPDF2.PdfMerger()
for filename in pdffiles:
    pdffiles=open(filename,'rb')
    pdfreader=PyPDF2.PdfReader(pdffiles)
    merger.append(pdfreader)
pdffiles.close()
merger.write('merger.pdf')