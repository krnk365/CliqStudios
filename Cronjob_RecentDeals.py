from job import Jobs
from logger import myLogger
import traceback

if __name__ == '__main__':
    try:
        Jobs.deals_cron(pagechunk=100,cronjob=True)
    except Exception as e:
        exception_ = traceback.format_exception_only(etype=type(e),value=e)
        traceback_list = traceback.extract_tb(tb=e.__traceback__)
        tb_str = ""
        for i in traceback_list:
            tb_str += f"\n{i}"
        myLogger(level='error',msg=f"JobType:Deals Cronjob\nJobLevel:Recent Deals\nMessage:{exception_}\nTraceback:{tb_str}")