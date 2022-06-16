class Values_fmecitems(object):

    def fmecitems_db(self, fmecitems_db):
        itemid = [i['ItemId'] for i in fmecitems_db]
        group_id = [i['GroupId'] for i in fmecitems_db]
        description = [i['Description'] for i in fmecitems_db]
        itemcode = [i['ItemCode'] for i in fmecitems_db]

        db_list = [itemid, group_id, description, itemcode]

        frozen_live_a_db = {(frozenset(item)) for item in db_list}

        return frozen_live_a_db

    def fmecitems_api(self, mapping_api):
        itemid = [i['id'] for i in mapping_api]
        group_id = [i['groupId'] for i in mapping_api]
        description = [i['description'] for i in mapping_api]
        itemcode = [i['itemCode'] for i in mapping_api]

        db_list = [itemid, group_id, description, itemcode]

        frozen_live_a_db = {(frozenset(item)) for item in db_list}

        return frozen_live_a_db

    def fmecagroupsitems(self):
        list_fmecagroupsitems = [
            "Aspen Mtell ISO Codes",
            "USER DEFINED",
            "User Defined Codes"
        ]

        return list_fmecagroupsitems
