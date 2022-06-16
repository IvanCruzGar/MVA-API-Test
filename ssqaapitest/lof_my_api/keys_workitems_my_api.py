import pdb


class Values_workitem(object):

    def get_work_items_db(self, work_items_db):
        db_work_item = [i['ApmvId'] for i in work_items_db]
        db_work_item_id = [i['WorkItemId'] for i in work_items_db]
        db_fk_objectUid = [i['FK_ObjectUid'] for i in work_items_db]
        db_fk_connectionId = [i['FK_ConnectionId'] for i in work_items_db]
        db_work_item_title = [i['WorkItemTitle'] for i in work_items_db]
        db_work_description = [i['WorkItemDescription'] for i in work_items_db]
        db_CActions = [i['CorrectiveActions'] for i in work_items_db]
        db_work_StrId = [i['WorkItemStrId'] for i in work_items_db]
        db_work_AssetId = [i['AssetId'] for i in work_items_db]
        db_work_SiteId = [i['SiteId'] for i in work_items_db]
        db_fk_ApmvobjectId = [i['FK_ApmvObjectId'] for i in work_items_db]

        db_list = [db_work_item, db_work_item_id, db_fk_objectUid, db_fk_connectionId, db_work_item_title, db_work_description,
                   db_CActions, db_work_StrId, db_work_AssetId, db_work_SiteId, db_fk_ApmvobjectId]
        #frozen_workitem_db = {(frozenset(item)) for item in db_list}

        return db_list

    def get_work_items_api(self, work_items_api):
        api_work_item = [i['apmvId'] for i in work_items_api]
        api_work_item_id = [i['workItemUid'] for i in work_items_api]
        api_fk_objectUid = [i['fkObjectUid'] for i in work_items_api]
        api_fk_connectionId = [i['fkConnectionId'] for i in work_items_api]
        api_work_item_title = [i['workItemTitle'] for i in work_items_api]
        api_work_description = [i['workItemDescription'] for i in work_items_api]
        api_CActions = [i['correctiveActions'] for i in work_items_api]
        api_work_StrId = [i['workItemStrId'] for i in work_items_api]
        api_work_AssetId = [i['assetId'] for i in work_items_api]
        api_work_SiteId = [i['siteId'] for i in work_items_api]
        api_fk_ApmvobjectId = [i['apmvObjectId'] for i in work_items_api]

        api_list = [api_work_item, api_work_item_id, api_fk_objectUid, api_fk_connectionId, api_work_item_title,
                   api_work_description, api_CActions, api_work_StrId, api_work_AssetId, api_work_SiteId,
                    api_fk_ApmvobjectId]

        #frozen_workitem_api = {(frozenset(item)) for item in api_list}

        return api_list

    def get_workitems_byid_db(self, work_items_db):
        #db_work_item = [i['ApmvId'] for i in work_items_db]
        db_work_item_id = [i['WorkItemId'] for i in work_items_db]
        db_work_StrId = [i['WorkItemStrId'] for i in work_items_db]
        db_work_AssetId = [i['AssetId'] for i in work_items_db]
        db_work_SiteId = [i['SiteId'] for i in work_items_db]
        db_work_item_title = [i['WorkItemTitle'] for i in work_items_db]
        db_work_description = [i['WorkItemDescription'] for i in work_items_db]
        db_FailureCode = [i['FailureCode'] for i in work_items_db]
        db_CauseCode = [i['CauseCode'] for i in work_items_db]
        db_RemedyCode = [i['RemedyCode'] for i in work_items_db]
        db_ProblemCode = [i['ProblemCode'] for i in work_items_db]
        db_correctiveActions = [i['CorrectiveActions'] for i in work_items_db]

        db_list = [db_work_item_id, db_work_StrId, db_work_AssetId, db_work_SiteId, db_work_item_title, db_work_description, db_FailureCode,
                   db_CauseCode, db_RemedyCode, db_ProblemCode, db_correctiveActions]
        #frozen_workitem_db = {(frozenset(item)) for item in db_list}

        return db_list

    def get_workitems_byid_api(self, work_items_api):
        #api_work_item = [i['apmvId'] for i in work_items_api]
        api_work_item_id = [i['workItemUid'] for i in work_items_api]
        api_work_StrId = [i['workItemStrId'] for i in work_items_api]
        api_work_AssetId = [i['assetStrId'] for i in work_items_api]
        api_work_SiteId = [i['siteStrId'] for i in work_items_api]
        api_work_item_title = [i['Title'] for i in work_items_api]
        api_work_description = [i['description'] for i in work_items_api]
        api_failureCode = [i['failureCode'] for i in work_items_api]
        api_causeCode = [i['causeCode'] for i in work_items_api]
        api_remedyCode = [i['remedyCode'] for i in work_items_api]
        api_problemCode = [i['problemCode'] for i in work_items_api]
        api_CActions = [i['correctiveActions'] for i in work_items_api]

        api_list = [api_work_item_id, api_work_StrId,api_work_AssetId, api_work_SiteId, api_work_item_title,
                    api_work_description, api_failureCode, api_causeCode, api_remedyCode, api_problemCode, api_CActions]

        #frozen_workitem_api = {(frozenset(item)) for item in api_list}
        return api_list

    def get_workitems_by_id_api_dic_list(self, work_items_api):
        api_work_StrId = [work_items_api['workItemStrId']]
        api_work_AssetId = [work_items_api['assetStrId']]
        api_work_SiteId = [i['siteStrId'] for i in work_items_api]
        api_work_item_title = [i['Title'] for i in work_items_api]
        api_work_description = [i['description'] for i in work_items_api]
        api_failureCode = [i['failureCode'] for i in work_items_api]
        api_causeCode = [i['causeCode'] for i in work_items_api]
        api_remedyCode = [i['remedyCode'] for i in work_items_api]
        api_problemCode = [i['problemCode'] for i in work_items_api]
        api_CActions = [i['correctiveActions'] for i in work_items_api]

        api_list = [api_work_item_id, api_work_StrId,api_work_AssetId, api_work_SiteId, api_work_item_title, api_work_description,
                    api_failureCode, api_causeCode, api_remedyCode, api_problemCode, api_CActions]

        #frozen_workitem_api = {(frozenset(item)) for item in api_list}
        return api_list



