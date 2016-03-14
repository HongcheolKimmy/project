from openpyxl import load_workbook
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class QCscanner:
    def __init__(self, filename):
        self.excelsheet = filename
        self.excelsheet = load_workbook(filename=self.excelsheet)

    def excel_tabtest(self, tabname):
        encoded = self.excelsheet.get_sheet_names()
        for i in encoded:
            if tabname in i:
                print unicode(i)
            else:
                pass

    def excel_datatest(self,worksheet, text):
        encoded = self.excelsheet.get_sheet_names()
        for i in encoded:
            if worksheet in i:
                sheet_name = i
            else:
                pass
        data = self.excelsheet.get_sheet_by_name(sheet_name)
        cell = data.rows
        for i in cell:
            for l in i:
                datavalue = str(l.value)
                if text in datavalue:
                    print datavalue + "\t" +  str(l)
                else:
                    pass
        print "------Parsing complete----"





test = QCscanner('test.xlsx')
# test.excel_tabtest("")
test.excel_datatest("FLEX - Income Statement-ARD","S3862")
