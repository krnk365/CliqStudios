from execution import BulkImport
from logger import myLogger
import traceback

if __name__ == '__main__':
    BulkImport.deals(pageStart=1,pageEnd=1955,pagechunk=100)