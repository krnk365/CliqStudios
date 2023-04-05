from Api import GetApi
from SQLOps import DataImport, RecycleBin
import datetime as dt
from pytz import timezone
from config import timezones
from logger import myLogger

class TrackEvent:
    def sleep(hours,minutes,seconds):
        hours_to_seconds = hours*60*60
        minutes_to_seconds = minutes*60
        total_seconds = hours_to_seconds+minutes_to_seconds+seconds
        return total_seconds
    
    def currentTime():
        return dt.datetime.now(timezone(timezones['timezone_log']))
    
    def duration(startTime,endTime):
        difference = endTime-startTime
        duration_in_seconds = round(difference.total_seconds())
        seconds = duration_in_seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return "%02d:%02d:%02d" % (hour, minutes, seconds)
        
class Jobs:
    def contacts(page,pagechunk):
        res = GetApi.contacts(page=page,pagechunk=pagechunk)
        DataImport.contacts(list_=res)
        DataImport.contacts_cf(list_=res)
        DataImport.contacts_appointment_ids(list_=res)
        DataImport.contacts_deal_ids(list_=res)
        DataImport.contacts_emails(list_=res)
        DataImport.contacts_note_ids(list_=res)
        DataImport.contacts_phone_numbers(list_=res)
        DataImport.contacts_sales_accounts(list_=res)
        DataImport.contacts_sales_activity_ids(list_=res)
        DataImport.contacts_system_tags(list_=res)
        DataImport.contacts_tags(list_=res)
        DataImport.contacts_task_ids(list_=res)
        DataImport.contacts_team_user_ids(list_=res)
        DataImport.contacts_web_form_ids(list_=res)

    def contactsByBatch(jsonFile):
        DataImport.contacts(list_=jsonFile)
        DataImport.contacts_cf(list_=jsonFile)
        DataImport.contacts_appointment_ids(list_=jsonFile)
        DataImport.contacts_deal_ids(list_=jsonFile)
        DataImport.contacts_emails(list_=jsonFile)
        DataImport.contacts_note_ids(list_=jsonFile)
        DataImport.contacts_phone_numbers(list_=jsonFile)
        DataImport.contacts_sales_accounts(list_=jsonFile)
        DataImport.contacts_sales_activity_ids(list_=jsonFile)
        DataImport.contacts_system_tags(list_=jsonFile)
        DataImport.contacts_tags(list_=jsonFile)
        DataImport.contacts_task_ids(list_=jsonFile)
        DataImport.contacts_team_user_ids(list_=jsonFile)
        DataImport.contacts_web_form_ids(list_=jsonFile)

    def deals(page,pagechunk):
        res = GetApi.deals(page=page,pagechunk=pagechunk)
        DataImport.deals(res)
        DataImport.deals_cf(res)
        DataImport.deals_contactsIds(res)
        DataImport.deals_tags(res)
        DataImport.deals_sales_activity_ids(res)

    def deals_cron(pagechunk,cronjob=None,recycleBin=None):
        if cronjob is True:
            res = GetApi.cronjob_newDeals(pagechunk=pagechunk)
            DataImport.deals(res)
            DataImport.deals_cf(res)
            DataImport.deals_contactsIds(res)
            DataImport.deals_tags(res)
            DataImport.deals_sales_activity_ids(res)
        elif recycleBin is True:
            res = GetApi.deals_recyclebin()
            DataImport.deals_recycleBin(res)