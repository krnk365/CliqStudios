from config import sqlData
from sqlalchemy import create_engine, MetaData, Table, Column, String, Date, DateTime, BigInteger, DECIMAL, Integer, text, Boolean, Time, Text
import datetime as dt 

def timer(days):
    end_date = dt.datetime.today()
    start_date = end_date-dt.timedelta(days=days)
    end_datetime = end_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    start_datetime = start_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    timer = {
        "start" : start_datetime,
        "end" : end_datetime
    }
    return timer

class SQLMeta:
    def contacts(meta=None):
        Contacts = Table('contacts',meta,
                    Column('id',BigInteger,primary_key=True),
                    Column('first_name',Text),
                    Column('last_name',Text),
                    Column('display_name',Text),
                    Column('avatar',Text),
                    Column('job_title',Text),
                    Column('city',Text),
                    Column('state',Text),
                    Column('zipcode',Text),
                    Column('country',Text),
                    Column('email',Text),
                    Column('time_zone',Text),
                    Column('work_number',Text),
                    Column('mobile_number',Text),
                    Column('address',Text),
                    Column('last_seen',DateTime),
                    Column('lead_score',Integer),
                    Column('last_contacted',DateTime),
                    Column('open_deals_amount',DECIMAL(20,0)),
                    Column('won_deals_amount',DECIMAL(20,0)),
                    Column('last_contacted_sales_activity_mode',Text),
                    Column('created_at',DateTime),
                    Column('updated_at',DateTime),
                    Column('keyword',Text),
                    Column('medium',Text),
                    Column('last_contacted_mode',Text),
                    Column('recent_note',Text),
                    Column('won_deals_count',Integer),
                    Column('last_contacted_via_sales_activity',DateTime),
                    Column('completed_sales_sequences',Text),
                    Column('active_sales_sequences',Text),
                    Column('open_deals_count',Integer),
                    Column('last_assigned_at',DateTime),
                    Column('facebook',Text),
                    Column('twitter',Text),
                    Column('linkedin',Text),
                    Column('is_deleted',Boolean),
                    Column('subscription_status',Text),
                    Column('unsubscription_reason',Text),
                    Column('other_unsubscription_reason',Text),
                    Column('customer_fit',Integer),
                    Column('record_type_id',Text),
                    Column('last_seen_chat',Text),
                    Column('first_seen_chat',Text),
                    Column('locale',Text),
                    Column('total_sessions',Text),
                    Column('first_campaign',Text),
                    Column('first_medium',Text),
                    Column('first_source',Text),
                    Column('last_campaign',Text),
                    Column('last_medium',Text),
                    Column('last_source',Text),
                    Column('latest_campaign',Text),
                    Column('latest_medium',Text),
                    Column('latest_source',Text),
                    Column('conversations',Text),
                    Column('timeline_feeds',Text),
                    Column('document_associations',Text),
                    Column('notes',Text),
                    Column('tasks',Text),
                    Column('appointments',Text),
                    Column('reminders',Text),
                    Column('duplicates',Text),
                    Column('connections',Text),
                    Column('owner_id',BigInteger),
                    Column('creater_id',BigInteger),
                    Column('updater_id',BigInteger),
                    Column('lead_source_id',BigInteger),
                    Column('campaign_id',BigInteger),
                    Column('territory_id',BigInteger)
                    )
        return Contacts

    def contacts_cf(meta=None):
        Contacts_Cf = Table('contacts_cf',meta,
                        Column('contactid',BigInteger),
                        Column('cf_not_moving_forward_reason',Text),
                        Column('cf_spouse_partner_name',Text),
                        Column('cf_jde_number',Text),
                        Column('cf_customer_tier',Text),
                        Column('cf_how_did_you_hear_about_us',Text),
                        Column('cf_samples_ordered',Text),
                        Column('cf_attachments',Text),
                        Column('cf_pro_program',Text),
                        Column('cf_marketo_lead_score',Text),
                        Column('cf_marketo_lead_updated_datetime',DateTime),
                        Column('cf_first_contacted_source',Text),
                        Column('cf_web_form_type',Text),
                        Column('cf_contact_result',Text),
                        Column('cf_comments_single_line',Text),
                        Column('cf_is_coming_back',Text),
                        Column('cf_likely_pro_since_date',DateTime),
                        Column('cf_contractor_name',Text),
                        Column('cf_submitted_for_design',Text),
                        Column('cf_main_phone',Text),
                        Column('cf_company_name',Text),
                        Column('cf_pro_website',Text),
                        Column('cf_pro_business_type',Text),
                        Column('cf_likely_pro',Text),
                        Column('cf_pro_since',DateTime),
                        Column('cf_csmyaccountid',Text),
                        Column('cf_original_owner',Text),
                        Column('cf_project_type',Text),
                        Column('cf_project_stage',Text),
                        Column('cf_door_style',Text),
                        Column('cf_time_line',Text),
                        Column('cf_door_color',Text),
                        Column('cf_quickquote_estimate',Text),
                        Column('cf_do_you_have_measurements',Text),
                        Column('cf_comments',Text),
                        Column('cf_cliqstudios_stay_in_touch',Text),
                        Column('cf_send_marketing_materials',Text),
                        Column('cf_features',Text),
                        Column('cf_kitchen_style_preferences',Text),
                        Column('cf_kitchen_layout',Text),
                        Column('cf_has_island',Text),
                        Column('cf_has_measurement',Text),
                        Column('cf_layout_measurement',Text),
                        Column('cf_installation_service',Text),
                        Column('cf_quick_question',Text),
                        Column('cf_cabinet_budget',Text),
                        Column('cf_description',Text),
                        Column('cf_referral_date',DateTime),
                        Column('cf_customer_design_referral',Text),
                        Column('cf_owner_title',Text),
                        Column('cf_owner_name',Text),
                        Column('cf_owner_email',Text),
                        Column('cf_owner_phone',Text),
                        Column('cf_owner_photo',Text),
                        Column('cf_owner_page_link',Text),
                        Column('cf_owner_setster_link',Text),
                        Column('cf_owner_signature_url',Text),
                        Column('cf_opportunity_stage',Text),
                        Column('cf_deal_stage',Text),
                        Column('cf_cliqstudios_enabled',Text),
                        Column('cf_cliq_studios_user_name',Text),
                        Column('cf_converting_campaign',Text),
                        Column('cf_user_city',Text),
                        Column('cf_originating_channel',Text),
                        Column('cf_user_zip_code',Text),
                        Column('cf_converting_date',DateTime),
                        Column('cf_follow_up',DateTime),
                        Column('cf_cliqstudios_id_create_date',DateTime),
                        Column('cf_do_not_allow_mails',Text),
                        Column('cf_mobile_phone',Text),
                        Column('cf_free_design',Text),
                        Column('cf_dynamic_owner',Text),
                        Column('cf_user_address_1',Text),
                        Column('cf_do_not_allow_bulk_emails',Text),
                        Column('cf_user_address_2',Text),
                        Column('cf_converting_channel',Text),
                        Column('cf_originating_campaign',Text),
                        Column('cf_user_state',Text),
                        Column('cf_repeat_referral',Text),
                        Column('cf_new_page_views_in_last_week',Text),
                        Column('cf_expiration_date',DateTime),
                        Column('cf_originating_date',DateTime),
                        Column('cf_do_not_allow_faxes',Text),
                        Column('cf_do_not_allow_emails',Text),
                        Column('cf_do_not_allow_phone_calls',Text),
                        Column('cf_marketo_lead_id',Text),
                        Column('cf_utm_campaign',Text),
                        Column('cf_utm_source',Text),
                        Column('cf_utm_medium',Text),
                        Column('cf_utm_term',Text),
                        Column('cf_utm_content',Text),
                        Column('cf_orig_utm_campaign',Text),
                        Column('cf_orig_utm_source',Text),
                        Column('cf_orig_utm_medium',Text),
                        Column('cf_orig_utm_term',Text),
                        Column('cf_orig_utm_content',Text),
                        Column('cf_last_updated_case',Text),
                        Column('cf_lead_stage',Text),
                        Column('cf_lead_date',DateTime),
                        Column('cf_lead_opportunity_stage',Text),
                        Column('cf_lead_quality_score',Text),
                        Column('cf_finish_type',Text),
                        Column('cf_contact_created_by_quiz',Text),
                        Column('cf_product_rec_1',Text),
                        Column('cf_product_rec_2',Text),
                        Column('cf_product_rec_3',Text),
                        Column('cf_digioh_quiz_budget',Text),
                        Column('cf_frameless_finish',Text),
                        Column('cf_cabinet_style',Text),
                        Column('cf_timeline',Text),
                        Column('cf_installation_interest',Text),
                        Column('cf_speciality_feature',Text),
                        Column('cf_full_name',Text),
                        Column('cf_budget',Text),
                        Column('cf_designer_referral',Text),
                        Column('cf_cs_owner',Text)
                        )
        return Contacts_Cf
    
    def logs(meta=None):
        Logs = Table('logs',meta,
                    Column('id',BigInteger,primary_key=True),
                    Column('page',Integer),
                    Column('module',Text),
                    Column('starttime',DateTime),
                    Column('endtime',DateTime),
                    Column('executiontime',Time)
                    )
        return Logs
    
    def batch_logs(meta=None):
        Batch_Logs = Table('batch_logs',meta,
                           Column('id',BigInteger,primary_key=True),
                           Column('module',Text),
                           Column('starttime',DateTime),
                           Column('endtime',DateTime),
                           Column('executiontime',Time)
                           )
        return Batch_Logs
    
    def contacts_appointment_ids(meta=None):
        Contacts_Appointment_Ids = Table('contacts_appointment_ids',meta,
                                         Column('id',BigInteger,primary_key=True),
                                         Column('contactid',BigInteger),
                                         Column('appointment_ids',BigInteger)
                                         )
        return Contacts_Appointment_Ids
    
    def contacts_deal_ids(meta=None):
        Contacts_Deal_Ids = Table('contacts_deal_ids',meta,
                                         Column('id',BigInteger,primary_key=True),
                                         Column('contactid',BigInteger),
                                         Column('deal_ids',BigInteger)
                                         )
        return Contacts_Deal_Ids
    
    def contacts_emails(meta=None):
        Contacts_Emails = Table('contacts_emails',meta,
                                Column('id',BigInteger,primary_key=True),
                                Column('value',Text),
                                Column('is_primary',Boolean),
                                Column('label',Text),
                                Column('_destroy',Boolean),
                                Column('contactid',BigInteger)
                                )
        return Contacts_Emails
    
    def contacts_note_ids(meta=None):
        Contacts_Note_Ids = Table('contacts_note_ids',meta,
                                         Column('id',BigInteger,primary_key=True),
                                         Column('contactid',BigInteger),
                                         Column('note_ids',BigInteger)
                                         )
        return Contacts_Note_Ids
    
    def contacts_phone_numbers(meta=None):
        Contacts_Phone_Numbers = Table('contacts_phone_numbers',meta,
                                       Column('id',BigInteger,primary_key=True),
                                       Column('value',Text),
                                       Column('label',Text),
                                       Column('_destroy',Boolean),
                                       Column('contactid',BigInteger)
                                       )
        return Contacts_Phone_Numbers
    
    def contacts_sales_accounts(meta=None):
        Contacts_Sales_Accounts = Table('contacts_sales_accounts',meta,
                                         Column('id',BigInteger,primary_key=True),
                                         Column('contactid',BigInteger),
                                         Column('salesaccountid',BigInteger)
                                         )
        return Contacts_Sales_Accounts
    
    def contacts_system_tags(meta=None):
        Contacts_System_Tags = Table('contacts_system_tags',meta,
                                         Column('id',BigInteger,primary_key=True),
                                         Column('contactid',BigInteger),
                                         Column('system_tags',Text)
                                         )
        return Contacts_System_Tags
    
    def contacts_sales_activity_ids(meta=None):
        Contacts_Sales_Activity_Ids = Table('contacts_sales_activity_ids',meta,
                                         Column('id',BigInteger,primary_key=True),
                                         Column('contactid',BigInteger),
                                         Column('sales_activity_ids',BigInteger)
                                         )
        return Contacts_Sales_Activity_Ids
    
    def contacts_tags(meta=None):
        Contacts_Tags = Table('contacts_tags',meta,
                                    Column('id',BigInteger,primary_key=True),
                                    Column('contactid',BigInteger),
                                    Column('tags',Text)
                                    )
        return Contacts_Tags
    
    def contacts_task_ids(meta=None):
        Contacts_Task_Ids = Table('contacts_task_ids',meta,
                                         Column('id',BigInteger,primary_key=True),
                                         Column('contactid',BigInteger),
                                         Column('task_ids',BigInteger)
                                         )
        return Contacts_Task_Ids
    
    def contacts_team_user_ids(meta=None):
        Contacts_Team_User_Ids = Table('contacts_team_user_ids',meta,
                                         Column('id',BigInteger,primary_key=True),
                                         Column('contactid',BigInteger),
                                         Column('team_user_ids',BigInteger)
                                         )
        return Contacts_Team_User_Ids
    
    def contacts_web_form_ids(meta=None):
        Contacts_Web_Form_Ids = Table('contacts_web_form_ids',meta,
                                         Column('id',BigInteger,primary_key=True),
                                         Column('contactid',BigInteger),
                                         Column('web_form_ids',BigInteger)
                                         )
        return Contacts_Web_Form_Ids
    
    def ApiLogs(meta=None):
        ApiLogs = Table('ApiLogs',meta,
                        Column('id',BigInteger,primary_key=True),
                        Column('jobname',Text),
                        Column('endpoint',Text),
                        Column('errorcode',Integer),
                        Column('datetime',DateTime)
                        )
        return ApiLogs
    
    def deals(meta=None):
        Deals = Table('deals',meta,
                                Column('id',BigInteger,primary_key=True),
                                Column('name',Text),
                                Column('amount',DECIMAL(20,0)),
                                Column('base_currency_amount',DECIMAL(20,0)),
                                Column('expected_close',DateTime),
                                Column('closed_date',DateTime),
                                Column('stage_updated_time',DateTime),
                                Column('probability',Integer),
                                Column('updated_at',DateTime),
                                Column('created_at',DateTime),
                                Column('deal_pipeline_id',BigInteger),
                                Column('deal_stage_id',BigInteger),
                                Column('age',BigInteger),
                                Column('links_conversations',Text),
                                Column('links_document_associations',Text),
                                Column('links_notes',Text),
                                Column('links_tasks',Text),
                                Column('links_appointments',Text),
                                Column('recent_note',Text),
                                Column('completed_sales_sequences',Text),
                                Column('active_sales_sequences',Text),
                                Column('web_form_id',BigInteger),
                                Column('upcoming_activities_time',DateTime),
                                Column('collaboration_id',BigInteger),
                                Column('collaboration_title',Text),
                                Column('collaboration_convo_token',Text),
                                Column('last_assigned_at',DateTime),
                                Column('last_contacted_sales_activity_mode',Text),
                                Column('last_contacted_via_sales_activity',Text),
                                Column('expected_deal_value',DECIMAL(20,0)),
                                Column('team_user_ids',BigInteger),
                                Column('avatar',Text),
                                Column('fc_widget_collaboration_convo_token',Text),
                                Column('fc_widget_collaboration_auth_token',Text),
                                Column('fc_widget_collaboration_encoded_jwt_token',Text),
                                Column('forecast_category',Integer),
                                Column('deal_prediction',Integer),
                                Column('deal_prediction_last_updated_at',DateTime),
                                Column('record_type_id',BigInteger),
                                Column('freddy_forecast_metrics',Text),
                                Column('last_deal_prediction',Text),
                                Column('rotten_days',BigInteger),
                                Column('owner_id',BigInteger),
                                Column('creater_id',BigInteger),
                                Column('updater_id',BigInteger),
                                Column('lead_source_id',BigInteger),
                                Column('sales_account_id',BigInteger),
                                Column('deal_type_id',BigInteger),
                                Column('deal_reason_id',BigInteger),
                                Column('campaign_id',BigInteger),
                                Column('deal_payment_status_id',BigInteger),
                                Column('deal_product_id',BigInteger),
                                Column('currency_id',BigInteger),
                                Column('is_deleted',Text)
                                )
        return Deals

    def deals_cf(meta=None):
        Deals_Cf = Table('deals_cf',meta,
                                Column('dealid',BigInteger,primary_key=True),
                                Column('cf_opportunity_id',BigInteger),
                                Column('cf_contact_pro_program',Text),
                                Column('cf_samples_ordered',Text),
                                Column('cf_next_follow_up_date',DateTime),
                                Column('cf_follow_up_status',Text),
                                Column('cf_revision_counter',BigInteger),
                                Column('cf_budget_amount',DECIMAL(20,0)),
                                Column('cf_description',Text),
                                Column('cf_dynamics_opportunity_id',BigInteger),
                                Column('cf_installation_services_purchased',Text),
                                Column('cf_contact_first_name',Text),
                                Column('cf_contact_last_name',Text),
                                Column('cf_contact_email',Text),
                                Column('cf_designer_name',Text),
                                Column('cf_designer_email',Text),
                                Column('cf_workflow_trigger',Boolean),
                                Column('cf_how_did_you_hear_about_us',Text),
                                Column('cf_followup_status',Text),
                                Column('cf_color_1',Text),
                                Column('cf_next_followup_date',DateTime),
                                Column('cf_installer',Text),
                                Column('cf_door_style_1',Text),
                                Column('cf_ceiling_height',Text),
                                Column('cf_color_2',Text),
                                Column('cf_soffit',Text),
                                Column('cf_door_style_2',Text),
                                Column('cf_wall_cabinet_height',Text),
                                Column('cf_measurements',Text),
                                Column('cf_sink',Text),
                                Column('cf_refrigerator',Text),
                                Column('cf_farm_sink',Text),
                                Column('cf_dishwasher',Text),
                                Column('cf_range_cooktop',Text),
                                Column('cf_other_appliances',Text),
                                Column('cf_wall_oven',Text),
                                Column('cf_microwave',Text),
                                Column('cf_crown_molding',Text),
                                Column('cf_hood',Text),
                                Column('cf_light_rail',Text),
                                Column('cf_design_type',Text),
                                Column('cf_actual_revenue',Text),
                                Column('cf_competitor',Text),
                                Column('cf_revision_sent_date',DateTime),
                                Column('cf_initial_design_sent_date',DateTime),
                                Column('cf_deals_expected_close_date',DateTime),
                                Column('cf_final_packet_sent_date',DateTime),
                                Column('cf_final_packet_sent',Text),
                                Column('cf_initial_design_sent',Text),
                                Column('cf_estimated_close_date',DateTime),
                                Column('cf_cabinet_line',Text),
                                Column('cf_initial_packet_sent',Text),
                                Column('cf_timeline',Text),
                                Column('cf_status_reason',Text),
                                Column('cf_status',Text),
                                Column('cf_wish_list',Text),
                                Column('cf_contractor',Text),
                                Column('cf_referral_incentive',Text),
                                Column('cf_referral_date',DateTime),
                                Column('cf_repeat_referral',Text),
                                Column('cf_initial_design_start',Text),
                                Column('cf_follow_up_status_date_1',DateTime),
                                Column('cf_signup_date',DateTime),
                                Column('cf_cabinet_budget',Text),
                                Column('cf_assigned_by',Text),
                                Column('cf_measure_received_y_n',Text),
                                Column('cf_additional_door_and_color_details',Text),
                                Column('cf_auto_activities_completed',Text),
                                Column('cf_competitor_quotes',Text),
                                Column('cf_follow_up_status_date_2',DateTime),
                                Column('cf_est_revenue',DECIMAL(20,0)),
                                Column('cf_designer_referral',Text),
                                Column('cf_dynamic_owner',Text),
                                Column('cf_order_tracking',Text),
                                Column('cf_lastorderupdatedstatus',Text),
                                Column('cf_mondaycom_boardid',BigInteger),
                                Column('cf_mondaycom_itemid',BigInteger),
                                Column('cf_last_updated_case',Text),
                                Column('cf_power_bi_opportunity_stages',Text),
                                Column('cf_power_bi_lost_reason',Text),
                                Column('cf_actual_revenue_base',Text),
                                Column('cf_budget_amount_base',Text),
                                Column('cf_owner',Text),
                                Column('cf_budget',Text),
                                Column('cf_total_tax',Text),
                                Column('cf_total_detail_amount',DECIMAL(20,0)),
                                Column('cf_total_pre_freight_amount',DECIMAL(20,0)),
                                Column('cf_opportunity_discount',Text),
                                Column('cf_opportunity_discount_amount',DECIMAL(20,0)),
                                Column('cf_freight_amount',DECIMAL(20,0)),
                                Column('cf_pipeline_phase',Text),
                                Column('cf_exchange_rate',Integer),
                                Column('cf_total_discount_amount',DECIMAL(20,0)),
                                Column('cf_total_line_item_discount_amount',DECIMAL(20,0)),
                                Column('cf_est_revenue_revisions',DECIMAL(20,2)),
                                Column('cf_est_revenue_initial',DECIMAL(20,2)),
                                Column('cf_est_revenue_final',DECIMAL(20,2)),
                                Column('cf_interested_in_countertops',Text),
                                Column('cf_measure_eligible_obsolete',Text),
                                Column('cf_opportunity_id_prefix',BigInteger),
                                Column('cf_opportunity_counter_number',BigInteger),
                                Column('cf_total_amount',DECIMAL(20,0)),
                                Column('cf_full_name',Text),
                                Column('cf_ct_eligible',Text),
                                Column('cf_ct_area_type',Text),
                                Column('cf_counter_opportunity',Text),
                                Column('cf_ct_offered_date',DateTime),
                                Column('cf_pre_pipeline_phase',Text),
                                Column('cf_laundry',Text),
                                Column('cf_kitchen',Text),
                                Column('cf_family',Text),
                                Column('cf_entertainment',Text),
                                Column('cf_bathroom',Text),
                                Column('cf_storage',Text),
                                Column('cf_other',Text),
                                Column('cf_farm_sink_old',Text),
                                Column('cf_measure_offered_date',DateTime),
                                Column('cf_price_list',Text),
                                Column('cf_temp_topic',Text),
                                Column('cf_forecast_category',Text),
                                Column('cf_revenue',Text),
                                Column('cf_assigned_date',DateTime),
                                Column('cf_desired_line_date',DateTime),
                                Column('cf_selected_line_date',DateTime)
        )
        return Deals_Cf
    
    def deals_contactsIds(meta=None):
        Deals_ContactID = Table('deals_contactsIds',meta,
                                Column('id',BigInteger,primary_key=True),
                                Column('dealid',BigInteger),
                                Column('contactid',BigInteger)      
                                )
        return Deals_ContactID
    
    def deals_tags(meta=None):
        Deals_Tags = Table('deals_tags',meta,
                           Column('id',BigInteger,primary_key=True),
                           Column('dealid',BigInteger),
                           Column('tag',Text)
                           )
        return Deals_Tags
    
    def deals_sales_activity_ids(meta=None):
        Deals_Sales_Activity_Ids = Table('deals_sales_activity_ids',meta,
                                        Column('id',BigInteger,primary_key=True),
                                        Column('dealid',BigInteger),
                                        Column('sales_activity_id',BigInteger)
                                        )
        return Deals_Sales_Activity_Ids