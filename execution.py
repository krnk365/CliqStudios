from job import Jobs, TrackEvent
from Api import GetApi
from SQLOps import DataImport
import time
from logger import myLogger
import traceback

class BulkImport:
    def contacts(pageStart,pageEnd,pagechunk,step=None,sleep=None):
        batch_startTime = TrackEvent.currentTime()
        DataImport.logs_truncate()
        page_list = range(pageStart,pageEnd+1)
        page_count = 1
        for page in page_list:
            page_startTime = TrackEvent.currentTime()
            if step is not None:
                if page_count < step:
                    Jobs.contacts(page,pagechunk=pagechunk)
                    page_count += 1
                    page_endTime = TrackEvent.currentTime()
                    page_duration = TrackEvent.duration(startTime=page_startTime,endTime=page_endTime)
                    DataImport.logs(page=page,module='contacts',starttime=page_startTime,endtime=page_endTime,executiontime=page_duration)
                elif page_count >= step:
                    Jobs.contacts(page,pagechunk=pagechunk)
                    sleepstr = str(sleep)
                    hours = int(sleepstr[0:2])
                    minutes = int(sleepstr[3:5])
                    seconds = int(sleepstr[6:-1])
                    sleepTime = TrackEvent.sleep(hours=hours,minutes=minutes,seconds=seconds)
                    time.sleep(sleepTime)
                    page_count = 1
                    page_endTime = TrackEvent.currentTime()
                    page_duration = TrackEvent.duration(startTime=page_startTime,endTime=page_endTime)
                    DataImport.logs(page=page,module='contacts',starttime=page_startTime,endtime=page_endTime,executiontime=page_duration)
            else:
                Jobs.contacts(page,pagechunk=pagechunk)
                page_endTime = TrackEvent.currentTime()
                page_duration = TrackEvent.duration(startTime=page_startTime,endTime=page_endTime)
                DataImport.logs(page=page,module='contacts',starttime=page_startTime,endtime=page_endTime,executiontime=page_duration)
        recycleBin_contacts = GetApi.contact_recyclebin()
        DataImport.contacts_recycleBin(list_=recycleBin_contacts)
        batch_endTime = TrackEvent.currentTime()
        batch_duration = TrackEvent.duration(startTime=batch_startTime,endTime=batch_endTime)
        DataImport.batch_logs(module='contacts',starttime=batch_startTime,endtime=batch_endTime,executiontime=batch_duration)

    def deals(pageStart,pageEnd,pagechunk,step=None,sleep=None):
        try:
            page_list = range(pageStart,pageEnd+1)
            page_count = 1
            for page in page_list:
                if step is not None:
                    if page_count < step:
                        Jobs.deals(page,pagechunk=pagechunk)
                        page_count += 1
                    elif page_count >= step:
                        Jobs.deals(page,pagechunk=pagechunk)
                        sleepstr = str(sleep)
                        hours = int(sleepstr[0:2])
                        minutes = int(sleepstr[3:5])
                        seconds = int(sleepstr[6:-1])
                        sleepTime = TrackEvent.sleep(hours=hours,minutes=minutes,seconds=seconds)
                        time.sleep(sleepTime)
                        page_count = 1
                else:
                    Jobs.deals(page,pagechunk=pagechunk)
            recycleBin_deals = GetApi.deals_recyclebin()
            DataImport.deals_recycleBin(list_=recycleBin_deals)
            myLogger(level='info',msg=f"Entity:Deals Status:Success")
        except Exception as e:
            exception_ = traceback.format_exception_only(etype=type(e),value=e)
            traceback_list = traceback.extract_tb(tb=e.__traceback__)
            tb_str = ""
            for i in traceback_list:
                tb_str += f"\n{i}"
            myLogger(level='error',msg=f"Entity:Deals\nMessage:{exception_}\nTraceback:{tb_str}")

class GetData:
    def contacts(pageStart,pageEnd,pagechunk):
        ContactList = []
        batch_startTime = TrackEvent.currentTime()
        page_list = range(pageStart,pageEnd+1)
        for page in page_list:
            page_startTime = TrackEvent.currentTime()
            res = GetApi.contacts(page=page,pagechunk=pagechunk)
            for i in res:
                ContactList.append(res)
            print(f"Page: {page} , Time : {TrackEvent.currentTime()}")
            page_endTime = TrackEvent.currentTime()
            page_duration = TrackEvent.duration(startTime=page_startTime,endTime=page_endTime)
            DataImport.logs(page=page,module='contacts',starttime=page_startTime,endtime=page_endTime,executiontime=page_duration)
        batch_endTime = TrackEvent.currentTime()
        batch_duration = TrackEvent.duration(startTime=batch_startTime,endTime=batch_endTime)
        DataImport.batch_logs(page=page,module='contacts',starttime=batch_startTime,endtime=batch_endTime,executiontime=batch_duration)
        return ContactList