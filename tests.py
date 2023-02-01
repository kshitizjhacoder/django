# import openpyxl
# wb = openpyxl.load_workbook('friutsome.xlsx')
# print(wb.get_sheet_names())
# print(wb.get_active_sheet())
# sheet1 = wb.get_sheet_by_name('sheet1')
# sheet1.title = 'Special Sheet'
# sheet3 = wb.get_sheet_by_name('sheet3')
# print(sheet3['A1'].value)
# import openpyxl
# wb = openpyxl.Workbook()
# wb.create_sheet(index=0, title='firstsheet')
# wb.create_sheet(index=1, title='2ndsheet')
# some = wb.get_active_sheet()
# some['firstsheet'] = 200
# some['2ndsheet'] = 300
# sum = '=SUM(firstsheet:2ndsheet)'
# wb.save('somefile.wlsx')
# some['firstsheet'].height = 70
# some['firstsheet'].width = 20
# some.merge_cells('firstsheet:lastsheet')
# import PyPDF2
# pdffileobj = open('adp.pdf', 'r+')
# pdfreader = PyPDF2.PdfFileReader(pdffileobj)
# pdfreader.numPages
# pageobj = pdfreader.getPage(0)
# pageobj.extract_text()
# pdfreader = PyPDF2.PdfFileReader(open('adp.pdf', 'r+'))
# pdfreader.isEncrypted  # true
# pdfreader.decrypt('codetoconquer')
# import docx
# doc = docx.Document('demo.docx')
# doc.paragraph[0].text
# doc.paragraph[1].text
# doc.paragraph[2].text
# doc.add_picture('zombie.png', width=docx.shared.Inches(1),
#                 height=docx.shared.Cm(1))
