from docx import Document
from docx.shared import Pt, RGBColor
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH
import re


def AddTitle(resultDocument, text, isCenter=True):
    title = resultDocument.add_paragraph()
    if isCenter:
        title.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title.add_run(text).font.bold = True
    if isCenter:
        resultDocument.add_paragraph()


def AddChoice(resultDocument, paragraphs, number):
    global index
    AddTitle(resultDocument, paragraphs[index].text, False)
    index += 1
    for i in range(number):
        answers = list(re.findall("[A-Z]", str(paragraphs[index].text)))
        resultDocument.add_paragraph(paragraphs[index].text)
        index += 1
        tempIndex = index
        selections = ""
        thisLine = str(paragraphs[index].text)
        while len(thisLine) and thisLine[0] != "【":
            selections += thisLine
            tempIndex += 1
            thisLine = str(paragraphs[tempIndex].text)
        for j in range(tempIndex - index):
            index += 1
        selections = list(re.findall("[A-Z][^A-Z]+", selections))
        for j in range(len(selections)):
            tempIndex = selections[j].strip()
            newParagraph = resultDocument.add_paragraph()
            if tempIndex[0] in answers:
                newRun = newParagraph.add_run(tempIndex)
                newRun.font.bold = True
                newRun.font.color.rgb = RGBColor(255, 0, 0)
            else:
                newParagraph.add_run(tempIndex)
    resultDocument.add_paragraph()
    index += 1


def AddJudge(resultDocument, paragraphs, number):
    global index
    AddTitle(resultDocument, paragraphs[index].text, False)
    index += 1
    for i in range(number):
        resultDocument.add_paragraph(paragraphs[index].text)
        index += 1


sourceDocument = Document("Docx Auto Bold\Source Document.docx")
resultDocument = Document()
resultDocument.styles["Normal"].font.name = u"宋体"
resultDocument.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
resultDocument.styles["Normal"].font.size = Pt(12)
resultDocument.styles["Normal"].font.name = "Times New Roman"
paragraphs = list(sourceDocument.paragraphs)
index = 0
AddTitle(resultDocument, paragraphs[index].text)
index += 2
AddChoice(resultDocument, paragraphs, 248)
AddChoice(resultDocument, paragraphs, 208)
AddJudge(resultDocument, paragraphs, 152)
resultDocument.save("Docx Auto Bold\Result Document.docx")