class Values_tag(object):

    def tag_rankings_db(self, tag_rankings_db):
        db_fk_tag = [i['FK_TagReferenceId'] for i in tag_rankings_db]
        db_sensor_name = [i['SensorName'] for i in tag_rankings_db]
        db_sensor_role = [i['SensorRole'] for i in tag_rankings_db]
        db_sensor_desc = [i['SensorDescription'] for i in tag_rankings_db]

        db_list = [db_fk_tag, db_sensor_name, db_sensor_role, db_sensor_desc]

        frozen_objects_db = {(frozenset(item)) for item in db_list}

        return frozen_objects_db

    def tag_rankings_api(self, tag_rankings_api):
        api_fk_tag = [i['FK_TagReferenceId'] for i in tag_rankings_api]
        api_sensor_name = [i['SensorName'] for i in tag_rankings_api]
        api_sensor_role = [i['SensorRole'] for i in tag_rankings_api]
        api_sensor_desc = [i['SensorDescription'] for i in tag_rankings_api]

        db_list = [api_fk_tag, api_sensor_name, api_sensor_role, api_sensor_desc]

        frozen_objects_db = {(frozenset(item)) for item in db_list}

        return frozen_objects_db
