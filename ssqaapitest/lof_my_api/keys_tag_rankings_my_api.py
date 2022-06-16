class ValuesTagRangkins(object):

    def tag_rankings_db(self, tag_rankings_db):
        db_apmvid = [i['ApmvId'] for i in tag_rankings_db]
        db_rankingsid = [i['TagRankingsId'] for i in tag_rankings_db]
        db_alertid = [i['FK_AlertId'] for i in tag_rankings_db]
        db_tagreference = [i['FK_TagReference'] for i in tag_rankings_db]
        db_ConnectionId = [i['FK_ConnectionId'] for i in tag_rankings_db]
        db_SensorName = [i['SensorName'] for i in tag_rankings_db]
        db_SensorRole = [i['SensorRole'] for i in tag_rankings_db]
        db_SensorDescription = [i['SensorDescription'] for i in tag_rankings_db]
        db_ApmAlertId = [i['ApmvAlertId'] for i in tag_rankings_db]

        db_list = [db_apmvid, db_rankingsid, db_alertid, db_tagreference, db_ConnectionId, db_SensorName, db_SensorRole, db_SensorDescription,db_ApmAlertId]

        frozen_live_a_db = {(frozenset(item)) for item in db_list}

        return frozen_live_a_db

    def tag_rankings_api(self, tag_rankings_api):
        api_apmvId = [i['apmvId'] for i in tag_rankings_api]
        api_tagRankingsId = [i['tagRankingsId'] for i in tag_rankings_api]
        api_fkAlertId = [i['fkAlertId'] for i in tag_rankings_api]
        api_fkTagReferenceId = [i['fkTagReferenceId'] for i in tag_rankings_api]
        api_fkConnectionId = [i['fkConnectionId'] for i in tag_rankings_api]
        api_sensorName = [i['sensorName'] for i in tag_rankings_api]
        api_sensorRole = [i['sensorRole'] for i in tag_rankings_api]
        api_sensorDescription = [i['sensorDescription'] for i in tag_rankings_api]
        api_apmvAlertId = [i['apmvAlertId'] for i in tag_rankings_api]

        api_list = [api_apmvId, api_tagRankingsId, api_fkAlertId, api_fkTagReferenceId, api_fkConnectionId, api_sensorName, api_sensorRole, api_sensorDescription, api_apmvAlertId]
        frozen_live_a_api = {(frozenset(item)) for item in api_list}

        return frozen_live_a_api