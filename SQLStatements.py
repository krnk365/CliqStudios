from sqlalchemy import MetaData, create_engine
from Meta import SQLMeta

class InsertStmt:
    def contacts(dict_):
        Contacts = SQLMeta.contacts(meta=MetaData())
        stmt = Contacts.insert().values(
                                        id=dict_['id'],
                                        first_name=dict_['first_name'],
                                        last_name=dict_['last_name'],
                                        display_name=dict_['display_name'],
                                        avatar=dict_['avatar'],
                                        job_title=dict_['job_title'],
                                        city=dict_['city'],
                                        state=dict_['state'],
                                        zipcode=dict_['zipcode'],
                                        country=dict_['country'],
                                        email=dict_['email'],
                                        time_zone=dict_['time_zone'],
                                        work_number=dict_['work_number'],
                                        mobile_number=dict_['mobile_number'],
                                        address=dict_['address'],
                                        last_seen=dict_['last_seen'],
                                        lead_score=dict_['lead_score'],
                                        last_contacted=dict_['last_contacted'],
                                        open_deals_amount=dict_['open_deals_amount'],
                                        won_deals_amount=dict_['won_deals_amount'],
                                        last_contacted_sales_activity_mode=dict_['last_contacted_sales_activity_mode'],
                                        created_at=dict_['created_at'],
                                        updated_at=dict_['updated_at'],
                                        keyword=dict_['keyword'],
                                        medium=dict_['medium'],
                                        last_contacted_mode=dict_['last_contacted_mode'],
                                        recent_note=dict_['recent_note'],
                                        won_deals_count=dict_['won_deals_count'],
                                        last_contacted_via_sales_activity=dict_['last_contacted_via_sales_activity'],
                                        completed_sales_sequences=dict_['completed_sales_sequences'],
                                        active_sales_sequences=dict_['active_sales_sequences'],
                                        open_deals_count=dict_['open_deals_count'],
                                        last_assigned_at=dict_['last_assigned_at'],
                                        facebook=dict_['facebook'],
                                        twitter=dict_['twitter'],
                                        linkedin=dict_['linkedin'],
                                        is_deleted=dict_['is_deleted'],
                                        subscription_status=dict_['subscription_status'],
                                        unsubscription_reason=dict_['unsubscription_reason'],
                                        other_unsubscription_reason=dict_['other_unsubscription_reason'],
                                        customer_fit=dict_['customer_fit'],
                                        record_type_id=dict_['record_type_id'],
                                        last_seen_chat=dict_['last_seen_chat'],
                                        first_seen_chat=dict_['first_seen_chat'],
                                        locale=dict_['locale'],
                                        total_sessions=dict_['total_sessions'],
                                        first_campaign=dict_['first_campaign'],
                                        first_medium=dict_['first_medium'],
                                        first_source=dict_['first_source'],
                                        last_campaign=dict_['last_campaign'],
                                        last_medium=dict_['last_medium'],
                                        last_source=dict_['last_source'],
                                        latest_campaign=dict_['latest_campaign'],
                                        latest_medium=dict_['latest_medium'],
                                        latest_source=dict_['latest_source'],
                                        conversations=dict_['links']['conversations'],
                                        timeline_feeds=dict_['links']['timeline_feeds'],
                                        document_associations=dict_['links']['document_associations'],
                                        notes=dict_['links']['notes'],
                                        tasks=dict_['links']['tasks'],
                                        appointments=dict_['links']['appointments'],
                                        reminders=dict_['links']['reminders'],
                                        duplicates=dict_['links']['duplicates'],
                                        connections=dict_['links']['connections'],
                                        owner_id=dict_['owner_id'],
                                        creater_id=dict_['creater_id'],
                                        updater_id=dict_['updater_id'],
                                        lead_source_id=dict_['lead_source_id'],
                                        campaign_id=dict_['campaign_id'],
                                        territory_id=dict_['territory_id']
                                    )
        return stmt
    
    def contacts_cf(parent_dict,child_dict):
        Contacts_Cf = SQLMeta.contacts_cf(meta=MetaData())
        stmt = Contacts_Cf.insert().values(
                                            contactid=parent_dict['id'],
                                            cf_not_moving_forward_reason=child_dict['cf_not_moving_forward_reason'],
                                            cf_spouse_partner_name=child_dict['cf_spouse_partner_name'],
                                            cf_jde_number=child_dict['cf_jde_number'],
                                            cf_customer_tier=child_dict['cf_customer_tier'],
                                            cf_how_did_you_hear_about_us=child_dict['cf_how_did_you_hear_about_us'],
                                            cf_samples_ordered=child_dict['cf_samples_ordered'],
                                            cf_attachments=child_dict['cf_attachments'],
                                            cf_pro_program=child_dict['cf_pro_program'],
                                            cf_marketo_lead_score=child_dict['cf_marketo_lead_score'],
                                            cf_marketo_lead_updated_datetime=child_dict['cf_marketo_lead_updated_datetime'],
                                            cf_first_contacted_source=child_dict['cf_first_contacted_source'],
                                            cf_web_form_type=child_dict['cf_web_form_type'],
                                            cf_contact_result=child_dict['cf_contact_result'],
                                            cf_comments_single_line=child_dict['cf_comments_single_line'],
                                            cf_is_coming_back=child_dict['cf_is_coming_back'],
                                            cf_likely_pro_since_date=child_dict['cf_likely_pro_since_date'],
                                            cf_contractor_name=child_dict['cf_contractor_name'],
                                            cf_submitted_for_design=child_dict['cf_submitted_for_design'],
                                            cf_main_phone=child_dict['cf_main_phone'],
                                            cf_company_name=child_dict['cf_company_name'],
                                            cf_pro_website=child_dict['cf_pro_website'],
                                            cf_pro_business_type=child_dict['cf_pro_business_type'],
                                            cf_likely_pro=child_dict['cf_likely_pro'],
                                            cf_pro_since=child_dict['cf_pro_since'],
                                            cf_csmyaccountid=child_dict['cf_csmyaccountid'],
                                            cf_original_owner=child_dict['cf_original_owner'],
                                            cf_project_type=child_dict['cf_project_type'],
                                            cf_project_stage=child_dict['cf_project_stage'],
                                            cf_door_style=child_dict['cf_door_style'],
                                            cf_time_line=child_dict['cf_time_line'],
                                            cf_door_color=child_dict['cf_door_color'],
                                            cf_quickquote_estimate=child_dict['cf_quickquote_estimate'],
                                            cf_do_you_have_measurements=child_dict['cf_do_you_have_measurements'],
                                            cf_comments=child_dict['cf_comments'],
                                            cf_cliqstudios_stay_in_touch=child_dict['cf_cliqstudios_stay_in_touch'],
                                            cf_send_marketing_materials=child_dict['cf_send_marketing_materials'],
                                            cf_features=child_dict['cf_features'],
                                            cf_kitchen_style_preferences=child_dict['cf_kitchen_style_preferences'],
                                            cf_kitchen_layout=child_dict['cf_kitchen_layout'],
                                            cf_has_island=child_dict['cf_has_island'],
                                            cf_has_measurement=child_dict['cf_has_measurement'],
                                            cf_layout_measurement=child_dict['cf_layout_measurement'],
                                            cf_installation_service=child_dict['cf_installation_service'],
                                            cf_quick_question=child_dict['cf_quick_question'],
                                            cf_cabinet_budget=child_dict['cf_cabinet_budget'],
                                            cf_description=child_dict['cf_description'],
                                            cf_referral_date=child_dict['cf_referral_date'],
                                            cf_customer_design_referral=child_dict['cf_customer_design_referral'],
                                            cf_owner_title=child_dict['cf_owner_title'],
                                            cf_owner_name=child_dict['cf_owner_name'],
                                            cf_owner_email=child_dict['cf_owner_email'],
                                            cf_owner_phone=child_dict['cf_owner_phone'],
                                            cf_owner_photo=child_dict['cf_owner_photo'],
                                            cf_owner_page_link=child_dict['cf_owner_page_link'],
                                            cf_owner_setster_link=child_dict['cf_owner_setster_link'],
                                            cf_owner_signature_url=child_dict['cf_owner_signature_url'],
                                            cf_opportunity_stage=child_dict['cf_opportunity_stage'],
                                            cf_deal_stage=child_dict['cf_deal_stage'],
                                            cf_cliqstudios_enabled=child_dict['cf_cliqstudios_enabled'],
                                            cf_cliq_studios_user_name=child_dict['cf_cliq_studios_user_name'],
                                            cf_converting_campaign=child_dict['cf_converting_campaign'],
                                            cf_user_city=child_dict['cf_user_city'],
                                            cf_originating_channel=child_dict['cf_originating_channel'],
                                            cf_user_zip_code=child_dict['cf_user_zip_code'],
                                            cf_converting_date=child_dict['cf_converting_date'],
                                            cf_follow_up=child_dict['cf_follow_up'],
                                            cf_cliqstudios_id_create_date=child_dict['cf_cliqstudios_id_create_date'],
                                            cf_do_not_allow_mails=child_dict['cf_do_not_allow_mails'],
                                            cf_mobile_phone=child_dict['cf_mobile_phone'],
                                            cf_free_design=child_dict['cf_free_design'],
                                            cf_dynamic_owner=child_dict['cf_dynamic_owner'],
                                            cf_user_address_1=child_dict['cf_user_address_1'],
                                            cf_do_not_allow_bulk_emails=child_dict['cf_do_not_allow_bulk_emails'],
                                            cf_user_address_2=child_dict['cf_user_address_2'],
                                            cf_converting_channel=child_dict['cf_converting_channel'],
                                            cf_originating_campaign=child_dict['cf_originating_campaign'],
                                            cf_user_state=child_dict['cf_user_state'],
                                            cf_repeat_referral=child_dict['cf_repeat_referral'],
                                            cf_new_page_views_in_last_week=child_dict['cf_new_page_views_in_last_week'],
                                            cf_expiration_date=child_dict['cf_expiration_date'],
                                            cf_originating_date=child_dict['cf_originating_date'],
                                            cf_do_not_allow_faxes=child_dict['cf_do_not_allow_faxes'],
                                            cf_do_not_allow_emails=child_dict['cf_do_not_allow_emails'],
                                            cf_do_not_allow_phone_calls=child_dict['cf_do_not_allow_phone_calls'],
                                            cf_marketo_lead_id=child_dict['cf_marketo_lead_id'],
                                            cf_utm_campaign=child_dict['cf_utm_campaign'],
                                            cf_utm_source=child_dict['cf_utm_source'],
                                            cf_utm_medium=child_dict['cf_utm_medium'],
                                            cf_utm_term=child_dict['cf_utm_term'],
                                            cf_utm_content=child_dict['cf_utm_content'],
                                            cf_orig_utm_campaign=child_dict['cf_orig_utm_campaign'],
                                            cf_orig_utm_source=child_dict['cf_orig_utm_source'],
                                            cf_orig_utm_medium=child_dict['cf_orig_utm_medium'],
                                            cf_orig_utm_term=child_dict['cf_orig_utm_term'],
                                            cf_orig_utm_content=child_dict['cf_orig_utm_content'],
                                            cf_last_updated_case=child_dict['cf_last_updated_case'],
                                            cf_lead_stage=child_dict['cf_lead_stage'],
                                            cf_lead_date=child_dict['cf_lead_date'],
                                            cf_lead_opportunity_stage=child_dict['cf_lead_opportunity_stage'],
                                            cf_lead_quality_score=child_dict['cf_lead_quality_score'],
                                            cf_finish_type=child_dict['cf_finish_type'],
                                            cf_contact_created_by_quiz=child_dict['cf_contact_created_by_quiz'],
                                            cf_product_rec_1=child_dict['cf_product_rec_1'],
                                            cf_product_rec_2=child_dict['cf_product_rec_2'],
                                            cf_product_rec_3=child_dict['cf_product_rec_3'],
                                            cf_digioh_quiz_budget=child_dict['cf_digioh_quiz_budget'],
                                            cf_frameless_finish=child_dict['cf_frameless_finish'],
                                            cf_cabinet_style=child_dict['cf_cabinet_style'],
                                            cf_timeline=child_dict['cf_timeline'],
                                            cf_installation_interest=child_dict['cf_installation_interest'],
                                            cf_speciality_feature=child_dict['cf_speciality_feature'],
                                            cf_full_name=child_dict['cf_full_name'],
                                            cf_budget=child_dict['cf_budget'],
                                            cf_designer_referral=child_dict['cf_designer_referral'],
                                            cf_cs_owner=child_dict['cf_cs_owner']
                                            )
        return stmt
    
    def contacts_appointment_ids(contactid,appointmentid):
        Contacts_Appointment_Ids = SQLMeta.contacts_appointment_ids(meta=MetaData())
        stmt = Contacts_Appointment_Ids.insert().values(
                                                    id = None,
                                                    contactid = contactid,
                                                    appointment_ids = appointmentid
                                                    )
        return stmt

    def contacts_deal_ids(contactid,dealid):
        Contacts_Deal_Ids = SQLMeta.contacts_deal_ids(meta=MetaData())
        stmt = Contacts_Deal_Ids.insert().values(
                                                id = None,
                                                contactid = contactid,
                                                deal_ids = dealid
                                                )
        return stmt
    
    def contacts_emails(contactid,dict_):
        Contacts_Emails = SQLMeta.contacts_emails(meta=MetaData())
        stmt = Contacts_Emails.insert().values(
                                                id = dict_['id'],
                                                value = dict_['value'],
                                                is_primary = dict_['is_primary'],
                                                label = dict_['label'],
                                                _destroy = dict_['_destroy'],
                                                contactid = contactid
                                                )
        return stmt

    def contacts_note_ids(contactid,noteid):
        Contacts_Note_Ids = SQLMeta.contacts_note_ids(meta=MetaData())
        stmt = Contacts_Note_Ids.insert().values(
                                                id = None,
                                                contactid = contactid,
                                                note_ids = noteid
                                                )
        return stmt
    
    def contacts_phone_numbers(contactid,dict_):
        Contacts_Phone_Numbers = SQLMeta.contacts_phone_numbers(meta=MetaData())
        stmt = Contacts_Phone_Numbers.insert().values(
                                                    id = dict_['id'],
                                                    value = dict_['value'],
                                                    label = dict_['label'],
                                                    _destroy = dict_['_destroy'],
                                                    contactid = contactid
                                                    )
        return stmt
    
    def contacts_sales_accounts(contactid,salesaccountid):
        Contacts_Sales_Accounts = SQLMeta.contacts_sales_accounts(meta=MetaData())
        stmt = Contacts_Sales_Accounts.insert().values(
                                                        id = None,
                                                        contactid = contactid,
                                                        salesaccountid = salesaccountid
                                                    )
        return stmt

    def contacts_sales_activity_ids(contactid,salesactivityids):
        Contacts_Sales_Activity_Ids = SQLMeta.contacts_sales_activity_ids(meta=MetaData())
        stmt = Contacts_Sales_Activity_Ids.insert().values(
                                                            id = None,
                                                            contactid = contactid,
                                                            sales_activity_ids = salesactivityids
                                                        )
        return stmt
    
    def contacts_system_tags(contactid,systemtags):
        Contacts_System_Tags = SQLMeta.contacts_system_tags(meta=MetaData())
        stmt = Contacts_System_Tags.insert().values(
                                                    id = None,
                                                    contactid = contactid,
                                                    system_tags = systemtags
                                                    )
        return stmt
    
    def contacts_tags(contactid,tags):
        Contacts_Tags = SQLMeta.contacts_tags(meta=MetaData())
        stmt = Contacts_Tags.insert().values(
                                            id = None,
                                            contactid = contactid,
                                            tags = tags
                                            )
        return stmt
    
    def contacts_task_ids(contactid,taskid):
        Contacts_Task_Ids = SQLMeta.contacts_task_ids(meta=MetaData())
        stmt = Contacts_Task_Ids.insert().values(
                                            id = None,
                                            contactid = contactid,
                                            task_ids = taskid
                                            )
        return stmt
    
    def contacts_team_user_ids(contactid,teamuserid):
        Contacts_Team_User_Ids = SQLMeta.contacts_team_user_ids(meta=MetaData())
        stmt = Contacts_Team_User_Ids.insert().values(
                                            id = None,
                                            contactid = contactid,
                                            team_user_ids = teamuserid
                                            )
        return stmt
    
    def contacts_web_form_ids(contactid,webformid):
        Contacts_Web_Form_Ids = SQLMeta.contacts_web_form_ids(meta=MetaData())
        stmt = Contacts_Web_Form_Ids.insert().values(
                                            id = None,
                                            contactid = contactid,
                                            web_form_ids = webformid
                                            )
        return stmt

    def logs(page,module,starttime,endtime,executiontime):
        Logs = SQLMeta.logs(meta=MetaData())
        stmt = Logs.insert().values(id=None,page=page,module=module,starttime=starttime,endtime=endtime,executiontime=executiontime)
        return stmt
    
    def batch_logs(module,starttime,endtime,executiontime):
        Batch_Logs = SQLMeta.batch_logs(meta=MetaData())
        stmt = Batch_Logs.insert().values(id=None,module=module,starttime=starttime,endtime=endtime,executiontime=executiontime)
        return stmt
    
    def ApiLogs(jobname,endpoint,errorcode,datetime):
        ApiLogs = SQLMeta.ApiLogs(meta=MetaData())
        stmt = ApiLogs.insert().values(id=None,jobname=jobname,endpoint=endpoint,errorcode=errorcode,datetime=datetime)
        return stmt
    
    def deals(dict_):
        Deals = SQLMeta.deals(MetaData())
        stmt = Deals.insert().values(
                                id = dict_['id'],
                                name = dict_['name'],
                                amount = dict_['amount'],
                                base_currency_amount = dict_['base_currency_amount'],
                                expected_close = dict_['expected_close'],
                                closed_date = dict_['closed_date'],
                                stage_updated_time = dict_['stage_updated_time'],
                                probability = dict_['probability'],
                                updated_at = dict_['updated_at'],
                                created_at = dict_['created_at'],
                                deal_pipeline_id = dict_['deal_pipeline_id'],
                                deal_stage_id = dict_['deal_stage_id'],
                                age = dict_['age'],
                                links_conversations = dict_['links']['conversations'],
                                links_document_associations = dict_['links']['document_associations'],
                                links_notes = dict_['links']['notes'],
                                links_tasks = dict_['links']['tasks'],
                                links_appointments = dict_['links']['appointments'],
                                recent_note = dict_['recent_note'],
                                completed_sales_sequences = dict_['completed_sales_sequences'],
                                active_sales_sequences = dict_['active_sales_sequences'],
                                web_form_id = dict_['web_form_id'],
                                upcoming_activities_time = dict_['upcoming_activities_time'],
                                collaboration_id = dict_['collaboration']['id'],
                                collaboration_title = dict_['collaboration']['title'],
                                collaboration_convo_token = dict_['collaboration']['convo_token'],
                                last_assigned_at = dict_['last_assigned_at'],
                                last_contacted_sales_activity_mode = dict_['last_contacted_sales_activity_mode'],
                                last_contacted_via_sales_activity = dict_['last_contacted_via_sales_activity'],
                                expected_deal_value = dict_['expected_deal_value'],
                                team_user_ids = dict_['team_user_ids'],
                                avatar = dict_['avatar'],
                                fc_widget_collaboration_convo_token = dict_['fc_widget_collaboration']['convo_token'],
                                fc_widget_collaboration_auth_token = dict_['fc_widget_collaboration']['auth_token'],
                                fc_widget_collaboration_encoded_jwt_token = dict_['fc_widget_collaboration']['encoded_jwt_token'],
                                forecast_category = dict_['forecast_category'],
                                deal_prediction = dict_['deal_prediction'],
                                deal_prediction_last_updated_at = dict_['deal_prediction_last_updated_at'],
                                record_type_id = dict_['record_type_id'],
                                freddy_forecast_metrics = dict_['freddy_forecast_metrics'],
                                last_deal_prediction = dict_['last_deal_prediction'],
                                rotten_days = dict_['rotten_days'],
                                owner_id = dict_['owner_id'],
                                creater_id = dict_['creater_id'],
                                updater_id = dict_['updater_id'],
                                lead_source_id = dict_['lead_source_id'],
                                sales_account_id = dict_['sales_account_id'],
                                deal_type_id = dict_['deal_type_id'],
                                deal_reason_id = dict_['deal_reason_id'],
                                campaign_id = dict_['campaign_id'],
                                deal_payment_status_id = dict_['deal_payment_status_id'],
                                deal_product_id = dict_['deal_product_id'],
                                currency_id = dict_['currency_id'],
                                is_deleted = dict_['is_deleted']
                                )
        return stmt
    
    def deals_cf(parent_dict,child_dict):
        Deals_Cf = SQLMeta.deals_cf(MetaData())
        stmt = Deals_Cf.insert().values(
                                    dealid = parent_dict['id'],
                                    cf_opportunity_id = child_dict['cf_opportunity_id'],
                                    cf_contact_pro_program = child_dict['cf_contact_pro_program'],
                                    cf_samples_ordered = child_dict['cf_samples_ordered'],
                                    cf_next_follow_up_date = child_dict['cf_next_follow_up_date'],
                                    cf_follow_up_status = child_dict['cf_follow_up_status'],
                                    cf_revision_counter = child_dict['cf_revision_counter'],
                                    cf_budget_amount = child_dict['cf_budget_amount'],
                                    cf_description = child_dict['cf_description'],
                                    cf_dynamics_opportunity_id = child_dict['cf_dynamics_opportunity_id'],
                                    cf_installation_services_purchased = child_dict['cf_installation_services_purchased'],
                                    cf_contact_first_name = child_dict['cf_contact_first_name'],
                                    cf_contact_last_name = child_dict['cf_contact_last_name'],
                                    cf_contact_email = child_dict['cf_contact_email'],
                                    cf_designer_name = child_dict['cf_designer_name'],
                                    cf_designer_email = child_dict['cf_designer_email'],
                                    cf_workflow_trigger = child_dict['cf_workflow_trigger'],
                                    cf_how_did_you_hear_about_us = child_dict['cf_how_did_you_hear_about_us'],
                                    cf_followup_status = child_dict['cf_followup_status'],
                                    cf_color_1 = child_dict['cf_color_1'],
                                    cf_next_followup_date = child_dict['cf_next_followup_date'],
                                    cf_installer = child_dict['cf_installer'],
                                    cf_door_style_1 = child_dict['cf_door_style_1'],
                                    cf_ceiling_height = child_dict['cf_ceiling_height'],
                                    cf_color_2 = child_dict['cf_color_2'],
                                    cf_soffit = child_dict['cf_soffit'],
                                    cf_door_style_2 = child_dict['cf_door_style_2'],
                                    cf_wall_cabinet_height = child_dict['cf_wall_cabinet_height'],
                                    cf_measurements = child_dict['cf_measurements'],
                                    cf_sink = child_dict['cf_sink'],
                                    cf_refrigerator = child_dict['cf_refrigerator'],
                                    cf_farm_sink = child_dict['cf_farm_sink'],
                                    cf_dishwasher = child_dict['cf_dishwasher'],
                                    cf_range_cooktop = child_dict['cf_range_cooktop'],
                                    cf_other_appliances = child_dict['cf_other_appliances'],
                                    cf_wall_oven = child_dict['cf_wall_oven'],
                                    cf_microwave = child_dict['cf_microwave'],
                                    cf_crown_molding = child_dict['cf_crown_molding'],
                                    cf_hood = child_dict['cf_hood'],
                                    cf_light_rail = child_dict['cf_light_rail'],
                                    cf_design_type = child_dict['cf_design_type'],
                                    cf_actual_revenue = child_dict['cf_actual_revenue'],
                                    cf_competitor = child_dict['cf_competitor'],
                                    cf_revision_sent_date = child_dict['cf_revision_sent_date'],
                                    cf_initial_design_sent_date = child_dict['cf_initial_design_sent_date'],
                                    cf_deals_expected_close_date = child_dict['cf_deals_expected_close_date'],
                                    cf_final_packet_sent_date = child_dict['cf_final_packet_sent_date'],
                                    cf_final_packet_sent = child_dict['cf_final_packet_sent'],
                                    cf_initial_design_sent = child_dict['cf_initial_design_sent'],
                                    cf_estimated_close_date = child_dict['cf_estimated_close_date'],
                                    cf_cabinet_line = child_dict['cf_cabinet_line'],
                                    cf_initial_packet_sent = child_dict['cf_initial_packet_sent'],
                                    cf_timeline = child_dict['cf_timeline'],
                                    cf_status_reason = child_dict['cf_status_reason'],
                                    cf_status = child_dict['cf_status'],
                                    cf_wish_list = child_dict['cf_wish_list'],
                                    cf_contractor = child_dict['cf_contractor'],
                                    cf_referral_incentive = child_dict['cf_referral_incentive'],
                                    cf_referral_date = child_dict['cf_referral_date'],
                                    cf_repeat_referral = child_dict['cf_repeat_referral'],
                                    cf_initial_design_start = child_dict['cf_initial_design_start'],
                                    cf_follow_up_status_date_1 = child_dict['cf_follow_up_status_date_1'],
                                    cf_signup_date = child_dict['cf_signup_date'],
                                    cf_cabinet_budget = child_dict['cf_cabinet_budget'],
                                    cf_assigned_by = child_dict['cf_assigned_by'],
                                    cf_measure_received_y_n = child_dict['cf_measure_received_y_n'],
                                    cf_additional_door_and_color_details = child_dict['cf_additional_door_and_color_details'],
                                    cf_auto_activities_completed = child_dict['cf_auto_activities_completed'],
                                    cf_competitor_quotes = child_dict['cf_competitor_quotes'],
                                    cf_follow_up_status_date_2 = child_dict['cf_follow_up_status_date_2'],
                                    cf_est_revenue = child_dict['cf_est_revenue'],
                                    cf_designer_referral = child_dict['cf_designer_referral'],
                                    cf_dynamic_owner = child_dict['cf_dynamic_owner'],
                                    cf_order_tracking = child_dict['cf_order_tracking'],
                                    cf_lastorderupdatedstatus = child_dict['cf_lastorderupdatedstatus'],
                                    cf_mondaycom_boardid = child_dict['cf_mondaycom_boardid'],
                                    cf_mondaycom_itemid = child_dict['cf_mondaycom_itemid'],
                                    cf_last_updated_case = child_dict['cf_last_updated_case'],
                                    cf_power_bi_opportunity_stages = child_dict['cf_power_bi_opportunity_stages'],
                                    cf_power_bi_lost_reason = child_dict['cf_power_bi_lost_reason'],
                                    cf_actual_revenue_base = child_dict['cf_actual_revenue_base'],
                                    cf_budget_amount_base = child_dict['cf_budget_amount_base'],
                                    cf_owner = child_dict['cf_owner'],
                                    cf_budget = child_dict['cf_budget'],
                                    cf_total_tax = child_dict['cf_total_tax'],
                                    cf_total_detail_amount = child_dict['cf_total_detail_amount'],
                                    cf_total_pre_freight_amount = child_dict['cf_total_pre-freight_amount'],
                                    cf_opportunity_discount = child_dict['cf_opportunity_discount'],
                                    cf_opportunity_discount_amount = child_dict['cf_opportunity_discount_amount'],
                                    cf_freight_amount = child_dict['cf_freight_amount'],
                                    cf_pipeline_phase = child_dict['cf_pipeline_phase'],
                                    cf_exchange_rate = child_dict['cf_exchange_rate'],
                                    cf_total_discount_amount = child_dict['cf_total_discount_amount'],
                                    cf_total_line_item_discount_amount = child_dict['cf_total_line_item_discount_amount'],
                                    cf_est_revenue_revisions = child_dict['cf_est_revenue_revisions'],
                                    cf_est_revenue_initial = child_dict['cf_est_revenue_initial'],
                                    cf_est_revenue_final = child_dict['cf_est_revenue_final'],
                                    cf_interested_in_countertops = child_dict['cf_interested_in_countertops'],
                                    cf_measure_eligible_obsolete = child_dict['cf_measure_eligible_obsolete'],
                                    cf_opportunity_id_prefix = child_dict['cf_opportunity_id_prefix'],
                                    cf_opportunity_counter_number = child_dict['cf_opportunity_counter_number'],
                                    cf_total_amount = child_dict['cf_total_amount'],
                                    cf_full_name = child_dict['cf_full_name'],
                                    cf_ct_eligible = child_dict['cf_ct_eligible'],
                                    cf_ct_area_type = child_dict['cf_ct_area_type'],
                                    cf_counter_opportunity = child_dict['cf_counter_opportunity'],
                                    cf_ct_offered_date = child_dict['cf_ct_offered_date'],
                                    cf_pre_pipeline_phase = child_dict['cf_pre_pipeline_phase'],
                                    cf_laundry = child_dict['cf_laundry'],
                                    cf_kitchen = child_dict['cf_kitchen'],
                                    cf_family = child_dict['cf_family'],
                                    cf_entertainment = child_dict['cf_entertainment'],
                                    cf_bathroom = child_dict['cf_bathroom'],
                                    cf_storage = child_dict['cf_storage'],
                                    cf_other = child_dict['cf_other'],
                                    cf_farm_sink_old = child_dict['cf_farm_sink_old'],
                                    cf_measure_offered_date = child_dict['cf_measure_offered_date'],
                                    cf_price_list = child_dict['cf_price_list'],
                                    cf_temp_topic = child_dict['cf_temp_topic'],
                                    cf_forecast_category = child_dict['cf_forecast_category'],
                                    cf_revenue = child_dict['cf_revenue'],
                                    cf_assigned_date = child_dict['cf_assigned_date'],
                                    cf_desired_line_date = child_dict['cf_desired_line_date'],
                                    cf_selected_line_date = child_dict['cf_selected_line_date']
                                    )
        return stmt

    def deals_contactsIds(dealid,contactid):
        Deals_ContactsIds = SQLMeta.deals_contactsIds(MetaData())
        stmt = Deals_ContactsIds.insert().values(
                                            id = None,
                                            dealid = dealid,
                                            contactid = contactid
                                            )
        return stmt

    def deals_tags(dealid,tag):
        Deals_Tags = SQLMeta.deals_tags(MetaData())
        stmt = Deals_Tags.insert().values(
                                            id = None,
                                            dealid = dealid,
                                            tag = tag
                                            )
        return stmt
    
    def deals_sales_activity_ids(dealid,sales_activity_id):
        Deals_Sales_Activity_Ids = SQLMeta.deals_sales_activity_ids(MetaData())
        stmt = Deals_Sales_Activity_Ids.insert().values(
                                                    id = None,
                                                    dealid = dealid,
                                                    sales_activity_id = sales_activity_id
                                                    )
        return stmt

class DeleteStmt:
    def contacts(dict_):
        Contacts = SQLMeta.contacts(meta=MetaData())
        stmt = Contacts.delete().where(Contacts.c.id==dict_['id'])
        return stmt
    
    def contacts_cf(dict_):
        Contacts_Cf = SQLMeta.contacts_cf(meta=MetaData())
        stmt = Contacts_Cf.delete().where(Contacts_Cf.c.contactid==dict_['id'])
        return stmt
    
    def contacts_appointment_ids(contactid):
        Contacts_Appointment_Ids = SQLMeta.contacts_appointment_ids(meta=MetaData())
        stmt = Contacts_Appointment_Ids.delete().where(Contacts_Appointment_Ids.c.contactid==contactid)
        return stmt
    
    def contacts_deal_ids(contactid):
        Contacts_Deal_Ids = SQLMeta.contacts_deal_ids(meta=MetaData())
        stmt = Contacts_Deal_Ids.delete().where(Contacts_Deal_Ids.c.contactid==contactid)
        return stmt
    
    def contacts_emails(contactid):
        Contacts_Emails = SQLMeta.contacts_emails(meta=MetaData())
        stmt = Contacts_Emails.delete().where(Contacts_Emails.c.contactid==contactid)
        return stmt
    
    def contacts_note_ids(contactid):
        Contacts_Note_Ids = SQLMeta.contacts_note_ids(meta=MetaData())
        stmt = Contacts_Note_Ids.delete().where(Contacts_Note_Ids.c.contactid==contactid)
        return stmt
    
    def contacts_phone_numbers(contactid):
        Contacts_Phone_Numbers = SQLMeta.contacts_phone_numbers(meta=MetaData())
        stmt = Contacts_Phone_Numbers.delete().where(Contacts_Phone_Numbers.c.contactid==contactid)
        return stmt
    
    def contacts_sales_accounts(contactid):
        Contacts_Sales_Accounts = SQLMeta.contacts_sales_accounts(meta=MetaData())
        stmt = Contacts_Sales_Accounts.delete().where(Contacts_Sales_Accounts.c.contactid==contactid)
        return stmt
    
    def contacts_sales_activity_ids(contactid):
        Contacts_Sales_Activity_Ids = SQLMeta.contacts_sales_activity_ids(meta=MetaData())
        stmt = Contacts_Sales_Activity_Ids.delete().where(Contacts_Sales_Activity_Ids.c.contactid==contactid)
        return stmt
    
    def contacts_system_tags(contactid):
        Contacts_System_Tags = SQLMeta.contacts_system_tags(meta=MetaData())
        stmt = Contacts_System_Tags.delete().where(Contacts_System_Tags.c.contactid==contactid)
        return stmt
    
    def contacts_tags(contactid):
        Contacts_Tags = SQLMeta.contacts_tags(meta=MetaData())
        stmt = Contacts_Tags.delete().where(Contacts_Tags.c.contactid==contactid)
        return stmt
    
    def contacts_task_ids(contactid):
        Contacts_Task_Ids = SQLMeta.contacts_task_ids(meta=MetaData())
        stmt = Contacts_Task_Ids.delete().where(Contacts_Task_Ids.c.contactid==contactid)
        return stmt
    
    def contacts_team_user_ids(contactid):
        Contacts_Team_User_Ids = SQLMeta.contacts_team_user_ids(meta=MetaData())
        stmt = Contacts_Team_User_Ids.delete().where(Contacts_Team_User_Ids.c.contactid==contactid)
        return stmt
    
    def contacts_web_form_ids(contactid):
        Contacts_Web_Form_Ids = SQLMeta.contacts_web_form_ids(meta=MetaData())
        stmt = Contacts_Web_Form_Ids.delete().where(Contacts_Web_Form_Ids.c.contactid==contactid)
        return stmt
    
    def deals(dealid):
        Deals = SQLMeta.deals(MetaData())
        stmt = Deals.delete().where(Deals.c.id==dealid)
        return stmt
    
    def deals_cf(dealid):
        Deals_Cf = SQLMeta.deals_cf(MetaData())
        stmt = Deals_Cf.delete().where(Deals_Cf.c.dealid==dealid)
        return stmt
    
    def deals_contactsIds(dealid):
        Deals_ContactsIds = SQLMeta.deals_contactsIds(MetaData())
        stmt = Deals_ContactsIds.delete().where(Deals_ContactsIds.c.dealid==dealid)
        return stmt
    
    def deals_tags(dealid):
        Deals_Tags = SQLMeta.deals_tags(MetaData())
        stmt = Deals_Tags.delete().where(Deals_Tags.c.dealid==dealid)
        return stmt

    def deals_sales_activity_ids(dealid):
        Seals_Sales_Activity_Ids = SQLMeta.deals_sales_activity_ids(MetaData())
        stmt = Seals_Sales_Activity_Ids.delete().where(Seals_Sales_Activity_Ids.c.dealid==dealid)
        return stmt

    
class RecycleBin():
    def contacts(dict_):
        Contacts = SQLMeta.contacts(meta=MetaData())
        stmt = Contacts.update().where(Contacts.c.id==dict_['id']).values(is_deleted=True)
        return stmt
    
    def deals(dict_):
        Deals = SQLMeta.deals(MetaData())
        stmt = Deals.update().where(Deals.c.id==dict_['id']).values(is_deleted=True)
        return stmt