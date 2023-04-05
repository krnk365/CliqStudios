import requests
import json
from config import api_credentials, endpoints
from SQLOps import DataImport
from logger import myLogger

headers = {
            'content-type': 'application/json',
            'accept' : 'application/json',
            'Authorization' : f"Token token={api_credentials['key']}"
            }

class GetApi:
    def contacts(page,pagechunk,sortBy='created_at',sortType='asc'):
        url = f"{api_credentials['base_url']}{endpoints['All_contacts']}?page={page}&per_page={pagechunk}&sort={sortBy}&sort_type={sortType}&include=sales_activities,owner,creater,updater,source,campaign,tasks,appointments,notes,deals,sales_accounts,territory"
        req = requests.get(url=url,headers=headers)
        data = json.loads(req.content)
        All_contacts = data['contacts']
        return All_contacts
    
    def deals(page,pagechunk,sortBy='created_at',sortType='asc'):
        url = f"{api_credentials['base_url']}{endpoints['All_deals']}?page={page}&per_page={pagechunk}&sort={sortBy}&sort_type={sortType}&include=sales_activities,owner,creater,updater,source,contacts,sales_account,deal_stage,deal_type,deal_reason,campaign,deal_payment_status,deal_product,currency,probability"
        req = requests.get(url=url,headers=headers)
        if req.status_code == 200:
            data = json.loads(req.content)
            All_contacts = data['deals']
            return All_contacts
        else:
            myLogger(level='error',msg=f"Deals Response Status Code is {req.status_code}")

    def contacts_pendingPages(page,pagechunk):
        url = f"{api_credentials['base_url']}{endpoints['All_contacts']}?page={page}&per_page={pagechunk}&sort=created_at&sort_type=asc"
        req = requests.get(url=url,headers=headers)
        data = json.loads(req.content)
        All_contacts = data['contacts']
        return All_contacts
    
    def contacts_test(pages,pagechunk):
        page_list = range(1,pages+1)

        All_contacts = []

        for i in page_list:
            url = f"{api_credentials['base_url']}{endpoints['All_contacts']}?page={i}&per_page={pagechunk}&sort=created_at&sort_type=asc&include=sales_activities,owner,creater,updater,source,campaign,tasks,appointments,notes,deals,sales_accounts,territory"
            req = requests.get(url=url,headers=headers)
            data1 = json.loads(req.content)
            list_ = data1['contacts']
            for i in list_:
                All_contacts.append(i)
        return All_contacts
    
    def contact_recyclebin_lastpage():
        test_url = f"{api_credentials['base_url']}{endpoints['contacts_recyclebin']}?page=10000000&per_page=100&sort=updated_at&sort_type=desc"
        req = requests.get(url=test_url,headers=headers)
        test_data = json.loads(req.content)
        lastPage = test_data['meta']['total_pages']
        return lastPage
    
    def contact_recyclebin():
        lastPage = GetApi.contact_recyclebin_lastpage()
        All_recycleBin_contacts = []
        pages = range(1,lastPage+1)
        for page in pages:
            url = f"{api_credentials['base_url']}{endpoints['contacts_recyclebin']}?page={page}&per_page=100&sort=updated_at&sort_type=desc"
            req = requests.get(url=url,headers=headers)
            if req.status_code == 200:
                data1 = json.loads(req.content)
                recycleBinContacts = data1['contacts']
                for i in recycleBinContacts:
                    All_recycleBin_contacts.append(i)
            else:
                myLogger(level='error',msg=f"JobType:Contacts_Recyclebin Error:{req.status_code}")
        return All_recycleBin_contacts
    
    def deals_recyclebin_lastpage():
        test_url = f"{api_credentials['base_url']}{endpoints['deals_recyclebin']}?page=10000000&per_page=100&sort=updated_at&sort_type=desc"
        req = requests.get(url=test_url,headers=headers)
        test_data = json.loads(req.content)
        lastPage = test_data['meta']['total_pages']
        return lastPage
    
    def deals_recyclebin():
        lastPage = GetApi.deals_recyclebin_lastpage()
        All_recycleBin_deals = []
        pages = range(1,lastPage+1)
        for page in pages:
            url = f"{api_credentials['base_url']}{endpoints['deals_recyclebin']}?page={page}&per_page=100&sort=updated_at&sort_type=desc"
            req = requests.get(url=url,headers=headers)
            if req.status_code == 200:
                data1 = json.loads(req.content)
                recycleBinDeals = data1['deals']
                for i in recycleBinDeals:
                    All_recycleBin_deals.append(i)
            else:
                myLogger(level='error',msg=f"Deals Response Status Code is {req.status_code}")
        return All_recycleBin_deals
    
    def contact_singleRecord(contactId):
        url = f"https://cliqstudios.freshsales.io/api/contacts/{contactId}?include=sales_activities,owner,creater,updater,source,campaign,tasks,appointments,notes,deals,sales_accounts,territory"
        req = requests.get(url=url,headers=headers)
        data = json.loads(req.content)
        record = data['contact']
        return record
    
    def cronjob_newContacts(pagechunk):
        new_contacts_get_pageCount_url = f"{api_credentials['base_url']}{endpoints['new_contacts']}?include=sales_activities,owner,creater,updater,source,campaign,tasks,appointments,notes,deals,sales_accounts,territory&page=1200000&per_page={pagechunk}&sort=created_at&sort_type=asc"
        getCount_req = requests.get(url=new_contacts_get_pageCount_url,headers=headers)
        res = json.loads(getCount_req.content)
        pageCount = res['meta']['total_pages']
        if pageCount <= 1:
            url = f"{api_credentials['base_url']}{endpoints['new_contacts']}?include=sales_activities,owner,creater,updater,source,campaign,tasks,appointments,notes,deals,sales_accounts,territory&page=1&per_page={pagechunk}&sort=created_at&sort_type=asc"
            req = requests.get(url=url,headers=headers)
            data = json.loads(req.content)
            records = data['contacts']
            return records
        elif pageCount > 1:
            pageRange = range(1,pageCount+1)
            new_contacts = []
            for page in pageRange:
                url = f"{api_credentials['base_url']}{endpoints['new_contacts']}?include=sales_activities,owner,creater,updater,source,campaign,tasks,appointments,notes,deals,sales_accounts,territory&page={page}&per_page={pagechunk}&sort=created_at&sort_type=asc"
                req = requests.get(url=url,headers=headers)
                if req.status_code == 200:
                    data = json.loads(req.content)
                    records = data['contacts']
                    for record in records:
                        new_contacts.append(record)
                else:
                    myLogger(level='error',msg=f"JobType:cronjob_newContacts Error:{req.status_code}")
            return new_contacts
        
    def cronjob_recentlyModified(pagechunk):
        recentModified_get_pageCount_url = f"{api_credentials['base_url']}{endpoints['contacts_recently_modified']}?include=sales_activities,owner,creater,updater,source,campaign,tasks,appointments,notes,deals,sales_accounts,territory&page=1200000&per_page={pagechunk}&sort=updated_at&sort_type=desc"
        getCount_req = requests.get(url=recentModified_get_pageCount_url,headers=headers)
        res = json.loads(getCount_req.content)
        pageCount = res['meta']['total_pages']
        if pageCount <= 1:
            url = f"{api_credentials['base_url']}{endpoints['contacts_recently_modified']}?include=sales_activities,owner,creater,updater,source,campaign,tasks,appointments,notes,deals,sales_accounts,territory&page=1&per_page={pagechunk}&sort=updated_at&sort_type=desc"
            req = requests.get(url=url,headers=headers)
            data = json.loads(req.content)
            records = data['contacts']
            return records
        elif pageCount > 1:
            pageRange = range(1,pageCount+1)
            recentModified_contacts = []
            for page in pageRange:
                url = f"{api_credentials['base_url']}{endpoints['contacts_recently_modified']}?include=sales_activities,owner,creater,updater,source,campaign,tasks,appointments,notes,deals,sales_accounts,territory&page={page}&per_page={pagechunk}&sort=updated_at&sort_type=desc"
                req = requests.get(url=url,headers=headers)
                if req.status_code == 200:
                    data = json.loads(req.content)
                    records = data['contacts']
                    for record in records:
                        recentModified_contacts.append(record)
                    print(f"Page {page} Done | Total Pages : {pageCount}")
                else:
                    myLogger(level='error',msg=f"JobType:cronjob_recentlyModified Error:{req.status_code}")
            return recentModified_contacts
        
    def cronjob_newDeals(pagechunk):
        recentModified_get_pageCount_url = f"{api_credentials['base_url']}{endpoints['recent_deals']}?&page=1200000&per_page={pagechunk}&sort=updated_at&sort_type=desc"
        getCount_req = requests.get(url=recentModified_get_pageCount_url,headers=headers)
        res = json.loads(getCount_req.content)
        pageCount = res['meta']['total_pages']
        if pageCount <= 1:
            url = f"{api_credentials['base_url']}{endpoints['recent_deals']}?page=1&per_page={pagechunk}&include=sales_activities,owner,creater,updater,source,contacts,sales_account,deal_stage,deal_type,deal_reason,campaign,deal_payment_status,deal_product,currency,probability&sort=updated_at&sort_type=desc"
            req = requests.get(url=url,headers=headers)
            data = json.loads(req.content)
            records = data['deals']
            return records
        elif pageCount > 1:
            pageRange = range(1,pageCount+1)
            recentModified_deals = []
            for page in pageRange:
                url = f"{api_credentials['base_url']}{endpoints['recent_deals']}?page={page}&per_page={pagechunk}&include=sales_activities,owner,creater,updater,source,contacts,sales_account,deal_stage,deal_type,deal_reason,campaign,deal_payment_status,deal_product,currency,probability&sort=updated_at&sort_type=desc"
                req = requests.get(url=url,headers=headers)
                if req.status_code == 200:
                    data = json.loads(req.content)
                    records = data['deals']
                    for record in records:
                        recentModified_deals.append(record)
                    print(f"Page {page} Done | Total Pages : {pageCount}")
                else:
                    myLogger(level='error',msg=f"JobType:Recent Deals PageNo:{page} Error:{req.status_code}")
            return recentModified_deals