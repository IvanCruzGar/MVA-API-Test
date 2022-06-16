class String_mapping(object):

    def string_mapping_db(self, mapping_db):
        id = [i['Id'] for i in mapping_db]
        widget = [i['Widget'] for i in mapping_db]
        key = [i['Key'] for i in mapping_db]
        value = [i['Value'] for i in mapping_db]

        db_list = [id, widget, key, value]

        frozen_live_a_db = {(frozenset(item)) for item in db_list}

        return frozen_live_a_db

    def string_mapping_api(self, mapping_api):
        id = [i['id'] for i in mapping_api]
        widget = [i['widget'] for i in mapping_api]
        key = [i['key'] for i in mapping_api]
        value = [i['value'] for i in mapping_api]

        db_list = [id, widget, key, value]

        frozen_live_a_db = {(frozenset(item)) for item in db_list}

        return frozen_live_a_db

