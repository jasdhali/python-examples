import aspose.words as aw
#create the document object

doc = aw.Document()

#create document builder object

builder = aw.DocumentBuilder(doc)

#add text to the document

builder.write("Hello world!")

#save

doc.save("out.docx")