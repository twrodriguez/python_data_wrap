# Import this to be able to load parent directory modules
from initSubdir import checkSubdirPath; checkSubdirPath(__name__)

import tableloader
import hashlib
import csv
import unittest
from os.path import dirname

def compareToCSV(filename, array):
    master = csv.reader(open(filename,"r"))
 
    for i, line in enumerate(master):
        for j, word in enumerate(line):
            if(word != array[i][j]):
                try: # Check if same number (0.00 vs 0)
                    # XLS & XLSX modules add extra digits for calculated cells.
                    if round(float(word),8) != round(float(array[i][j]),8):  
                        #print "Row:",i,"Column:",j,"Master:",word,"Test:",array[i][j],"END"
                        return False
                except:
                    return False
   
    return True

class FileConverterTest(unittest.TestCase):
    def setUp(self):
        self.csv_test = dirname(__file__)+'/tableLoadData/raw/csv_test.csv'
        self.csv_master = dirname(__file__)+'/tableLoadData/master/csv_master.csv'
        
        self.xls_test = dirname(__file__)+'/tableLoadData/raw/xls_test.xls'
        self.xlsx_test = dirname(__file__)+'/tableLoadData/raw/xlsx_test.xlsx'
        
        self.xls_formula_test = dirname(__file__)+'/tableLoadData/raw/formulas_xls.xls'
        self.xlsx_formula_test = dirname(__file__)+'/tableLoadData/raw/formulas_xlsx.xlsx'
        
        self.formula_master = dirname(__file__)+'/tableLoadData/master/formulas_master.csv'
        self.excel_master1 = dirname(__file__)+'/tableLoadData/master/excel_sheet1_master.csv'
        self.excel_master2 = dirname(__file__)+'/tableLoadData/master/excel_sheet2_master.csv'
        self.excel_master3 = dirname(__file__)+'/tableLoadData/master/excel_sheet3_master.csv'
    
    def testCSV(self):
        data = tableloader.read(self.csv_test)
        self.assertTrue(compareToCSV(self.csv_master,data[0]))
    
       
    def testXLS(self):
        data = tableloader.read(self.xls_test)      
        self.assertTrue(compareToCSV(self.excel_master1,data[0]))
        self.assertTrue(compareToCSV(self.excel_master2,data[1]))
        self.assertTrue(compareToCSV(self.excel_master3,data[2]))
        
    def testXLSX(self):
        data = tableloader.read(self.xlsx_test) 
        self.assertTrue(compareToCSV(self.excel_master1,data[0]))
        self.assertTrue(compareToCSV(self.excel_master2,data[1]))
        self.assertTrue(compareToCSV(self.excel_master3,data[2]))
        
    def testFunctionsXLS(self):
        data = tableloader.read(self.xls_formula_test)
        self.assertTrue(compareToCSV(self.formula_master,data[0]))
       
    def testFunctionsXLSX(self):
        data = tableloader.read(self.xlsx_formula_test)
        self.assertTrue(compareToCSV(self.formula_master,data[0]))

if __name__ == '__main__': 
    unittest.main()