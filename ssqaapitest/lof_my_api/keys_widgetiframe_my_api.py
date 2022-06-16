class Values_widgetiframe(object):

    def get_widgetiframe_db(self, widget_db):
        db_widget = [i['Widget'] for i in widget_db]
        db_apiurl = [i['ApiUrl'] for i in widget_db]
        db_baseurl = [i['BaseUrl'] for i in widget_db]

        db_list = [db_widget, db_apiurl, db_baseurl]
        #frozen_workitem_db = {(frozenset(item)) for item in db_list}

        return db_list

    def get_widgetiframe_api(self, widget_api):
        api_widget = [i['widget'] for i in widget_api]
        api_baseUrl = [i['baseUrl'] for i in widget_api]
        api_apiUrl = [i['apiUrl'] for i in widget_api]

        api_list = [api_widget, api_apiUrl, api_baseUrl]
        #frozen_workitem_db = {(frozenset(item)) for item in db_list}

        return api_list