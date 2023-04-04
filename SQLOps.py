import json
from Meta import SQLMeta
from sqlalchemy import MetaData, create_engine, text
from SQLStatements import InsertStmt, DeleteStmt, RecycleBin
from config import sqlData

class DataImport:        
    def contacts(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            deleteStmt = DeleteStmt.contacts(i)
            insertStmt = InsertStmt.contacts(i)
            with engine.begin() as connx:
                connx.execute(deleteStmt)
                connx.execute(insertStmt)

    def contacts_cf(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            cf_dict = i['custom_field']
            deleteStmt = DeleteStmt.contacts_cf(i)
            insertStmt = InsertStmt.contacts_cf(parent_dict=i,child_dict=cf_dict)
            with engine.begin() as connx:
                connx.execute(deleteStmt)
                connx.execute(insertStmt)
    
    def contacts_appointment_ids(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            deleteStmt = DeleteStmt.contacts_appointment_ids(contactid=i['id'])
            with engine.begin() as connx:
                connx.execute(deleteStmt)
            appointment_ids_list = i['appointment_ids']
            for j in appointment_ids_list:
                insertStmt = InsertStmt.contacts_appointment_ids(contactid=i['id'],appointmentid=j)
                with engine.begin() as connx:
                    connx.execute(insertStmt)

    def contacts_deal_ids(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            deleteStmt = DeleteStmt.contacts_deal_ids(contactid=i['id'])
            with engine.begin() as connx:
                connx.execute(deleteStmt)
            contacts_deal_ids_list = i['deal_ids']
            for j in contacts_deal_ids_list:
                insertStmt = InsertStmt.contacts_deal_ids(contactid=i['id'],dealid=j)
                with engine.begin() as connx:
                    connx.execute(insertStmt)

    def contacts_emails(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            deleteStmt = DeleteStmt.contacts_emails(contactid=i['id'])
            with engine.begin() as connx:
                connx.execute(deleteStmt)
            contacts_emails_list = i['emails']
            for j in contacts_emails_list:
                insertStmt = InsertStmt.contacts_emails(contactid=i['id'],dict_=j)
                with engine.begin() as connx:
                    connx.execute(insertStmt)

    def contacts_note_ids(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            deleteStmt = DeleteStmt.contacts_note_ids(contactid=i['id'])
            with engine.begin() as connx:
                connx.execute(deleteStmt)
            contacts_note_ids_list = i['note_ids']
            for j in contacts_note_ids_list:
                insertStmt = InsertStmt.contacts_note_ids(contactid=i['id'],noteid=j)
                with engine.begin() as connx:
                    connx.execute(insertStmt)

    def contacts_phone_numbers(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            deleteStmt = DeleteStmt.contacts_phone_numbers(contactid=i['id'])
            with engine.begin() as connx:
                connx.execute(deleteStmt)
            contacts_phone_numbers_list = i['phone_numbers']
            for j in contacts_phone_numbers_list:
                insertStmt = InsertStmt.contacts_phone_numbers(contactid=i['id'],dict_=j)
                with engine.begin() as connx:
                    connx.execute(insertStmt)

    def contacts_sales_accounts(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            deleteStmt = DeleteStmt.contacts_sales_accounts(contactid=i['id'])
            with engine.begin() as connx:
                connx.execute(deleteStmt)
            contacts_sales_accounts_list = i['sales_accounts']
            for j in contacts_sales_accounts_list:
                insertStmt = InsertStmt.contacts_sales_accounts(contactid=i['id'],salesaccountid=j['id'])
                with engine.begin() as connx:
                    connx.execute(insertStmt)

    def contacts_sales_activity_ids(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            deleteStmt = DeleteStmt.contacts_sales_activity_ids(contactid=i['id'])
            with engine.begin() as connx:
                connx.execute(deleteStmt)
            contacts_sales_activity_ids_list = i['sales_activity_ids']
            for j in contacts_sales_activity_ids_list:
                insertStmt = InsertStmt.contacts_sales_activity_ids(contactid=i['id'],salesactivityids=j)
                with engine.begin() as connx:
                    connx.execute(insertStmt)

    def contacts_system_tags(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            deleteStmt = DeleteStmt.contacts_system_tags(contactid=i['id'])
            with engine.begin() as connx:
                connx.execute(deleteStmt)
            contacts_system_tags_list = i['system_tags']
            for j in contacts_system_tags_list:
                insertStmt = InsertStmt.contacts_system_tags(contactid=i['id'],systemtags=j)
                with engine.begin() as connx:
                    connx.execute(insertStmt)
    
    def contacts_tags(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            deleteStmt = DeleteStmt.contacts_tags(contactid=i['id'])
            with engine.begin() as connx:
                connx.execute(deleteStmt)
            contacts_tags_list = i['tags']
            for j in contacts_tags_list:
                insertStmt = InsertStmt.contacts_tags(contactid=i['id'],tags=j)
                with engine.begin() as connx:
                    connx.execute(insertStmt)

    def contacts_task_ids(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            deleteStmt = DeleteStmt.contacts_task_ids(contactid=i['id'])
            with engine.begin() as connx:
                connx.execute(deleteStmt)
            contacts_task_ids_list = i['task_ids']
            for j in contacts_task_ids_list:
                insertStmt = InsertStmt.contacts_task_ids(contactid=i['id'],taskid=j)
                with engine.begin() as connx:
                    connx.execute(insertStmt)
    
    def contacts_team_user_ids(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            deleteStmt = DeleteStmt.contacts_team_user_ids(contactid=i['id'])
            with engine.begin() as connx:
                connx.execute(deleteStmt)
            contacts_team_user_ids_list = i['team_user_ids']
            if contacts_team_user_ids_list is not None:
                for j in contacts_team_user_ids_list:
                    insertStmt = InsertStmt.contacts_team_user_ids(contactid=i['id'],teamuserid=j)
                    with engine.begin() as connx:
                        connx.execute(insertStmt)

    def contacts_web_form_ids(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            deleteStmt = DeleteStmt.contacts_web_form_ids(contactid=i['id'])
            with engine.begin() as connx:
                connx.execute(deleteStmt)
            contacts_web_form_ids_list = i['web_form_ids']
            if contacts_web_form_ids_list is not None:
                for j in contacts_web_form_ids_list:
                    insertStmt = InsertStmt.contacts_web_form_ids(contactid=i['id'],webformid=j)
                    with engine.begin() as connx:
                        connx.execute(insertStmt)


    def logs(page,module,starttime,endtime,executiontime):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        insertStmt = InsertStmt.logs(page=page,module=module,starttime=starttime,endtime=endtime,executiontime=executiontime)
        with engine.begin() as connx:
            connx.execute(insertStmt)

    def logs_truncate():
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        truncateStmt = text(f"""TRUNCATE `{sqlData['db']}`.`logs`""")
        with engine.begin() as connx:
            connx.execute(truncateStmt)

    def batch_logs(module,starttime,endtime,executiontime):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        insertStmt = InsertStmt.batch_logs(module=module,starttime=starttime,endtime=endtime,executiontime=executiontime)
        with engine.begin() as connx:
            connx.execute(insertStmt)

    def contacts_recycleBin(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            recycleBinStmt = RecycleBin.contacts(dict_=i)
            with engine.begin() as connx:
                connx.execute(recycleBinStmt)

    def ApiLogs(jobname,endpoint,errorcode,datetime):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        insertStmt = InsertStmt.ApiLogs(jobname=jobname,endpoint=endpoint,errorcode=errorcode,datetime=datetime)
        with engine.begin() as connx:
            connx.execute(insertStmt)

    def deals(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            deleteStmt = DeleteStmt.deals(dealid=i['id'])
            insertStmt = InsertStmt.deals(dict_=i)
            with engine.begin() as connx:
                connx.execute(deleteStmt)
                connx.execute(insertStmt)

    def deals_cf(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            cf_dict = i['custom_field']
            deleteStmt = DeleteStmt.deals_cf(dealid=i['id'])
            insertStmt = InsertStmt.deals_cf(parent_dict=i,child_dict=cf_dict)
            with engine.begin() as connx:
                connx.execute(deleteStmt)
                connx.execute(insertStmt)

    def deals_contactsIds(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            deleteStmt = DeleteStmt.deals_contactsIds(dealid=i['id'])
            with engine.begin() as connx:
                connx.execute(deleteStmt)
            for contact in i['contact_ids']:
                insertStmt = InsertStmt.deals_contactsIds(dealid=i['id'],contactid=contact)
                with engine.begin() as connx:
                    connx.execute(insertStmt)

    def deals_tags(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            deleteStmt = DeleteStmt.deals_tags(dealid=i['id'])
            with engine.begin() as connx:
                connx.execute(deleteStmt)
            for tag in i['tags']:
                insertStmt = InsertStmt.deals_tags(dealid=i['id'],tag=tag)
                with engine.begin() as connx:
                    connx.execute(insertStmt)

    def deals_sales_activity_ids(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            deleteStmt = DeleteStmt.deals_sales_activity_ids(dealid=i['id'])
            with engine.begin() as connx:
                connx.execute(deleteStmt)
            if i['sales_activity_ids'] is not None:
                for sales_activity_id in i['sales_activity_ids']:
                    insertStmt = InsertStmt.deals_sales_activity_ids(dealid=i['id'],sales_activity_id=sales_activity_id)
                    with engine.begin() as connx:
                        connx.execute(insertStmt)

    def deals_recycleBin(list_):
        engine = create_engine(f"mysql+pymysql://{sqlData['user']}:{sqlData['pass']}@{sqlData['host']}/{sqlData['db']}")
        for i in list_:
            recycleBinStmt = RecycleBin.deals(dict_=i)
            with engine.begin() as connx:
                connx.execute(recycleBinStmt)