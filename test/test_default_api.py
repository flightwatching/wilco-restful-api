# coding: utf-8

"""
    WILCO API

    This  API allows you to pull and push data with your WILCO deployment [https://github.com/flightwatching/wilco-api](https://github.com/flightwatching/wilco-api) or on  [www.flightwatching.com](www.flightwatching.com).   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@flightwatching.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.default_api import DefaultApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_analysis(self):
        """Test case for create_analysis

        create an analysis from the event passed. should use insert message. see https://github.com/flightwatching/fleet-monitor/issues/55  # noqa: E501
        """
        pass

    def test_create_dashboard(self):
        """Test case for create_dashboard

        creates the dashboard  # noqa: E501
        """
        pass

    def test_create_dashboard_rule(self):
        """Test case for create_dashboard_rule

        creates a dashboard rule  # noqa: E501
        """
        pass

    def test_create_dashboard_svg(self):
        """Test case for create_dashboard_svg

        Returns the SVG for a dashboard  # noqa: E501
        """
        pass

    def test_create_dashboard_symbols(self):
        """Test case for create_dashboard_symbols

        Returns all the dashboard symbols  # noqa: E501
        """
        pass

    def test_create_event(self):
        """Test case for create_event

        creates an event  # noqa: E501
        """
        pass

    def test_create_event_samples(self):
        """Test case for create_event_samples

        Returns the samples of an event  # noqa: E501
        """
        pass

    def test_create_faultcode(self):
        """Test case for create_faultcode

        Creates a fault code from the body  # noqa: E501
        """
        pass

    def test_create_fwot(self):
        """Test case for create_fwot

        Returns all the fwots paginated. If the connected user has an airline, the list is filtered for this airline  # noqa: E501
        """
        pass

    def test_create_fwot_property(self):
        """Test case for create_fwot_property

        add a new property to the fwot. If null passed in the value arg, the prop is removed  # noqa: E501
        """
        pass

    def test_create_layout(self):
        """Test case for create_layout

        modifies a layout stored in WILCO  # noqa: E501
        """
        pass

    def test_create_layout_event(self):
        """Test case for create_layout_event

        Creates a layout from a message  # noqa: E501
        """
        pass

    def test_create_layouts(self):
        """Test case for create_layouts

        Returns list of layouts stored in WILCO  # noqa: E501
        """
        pass

    def test_create_parameters(self):
        """Test case for create_parameters

        Returns the parameters for the given search string  # noqa: E501
        """
        pass

    def test_create_simulate_push_pull(self):
        """Test case for create_simulate_push_pull

        Calls the URL service and simulates the call to the IFT with the returned content in the right variable. In the body you will need a json structure {formula:'<the formula>'}  # noqa: E501
        """
        pass

    def test_create_symbol(self):
        """Test case for create_symbol

        Returns/create/updates all the dashboard symbols. to delete a symbol function, empty its name  # noqa: E501
        """
        pass

    def test_create_symbol_svg_example(self):
        """Test case for create_symbol_svg_example

        Returns the SVG example for a symbol  # noqa: E501
        """
        pass

    def test_create_test_ift(self):
        """Test case for create_test_ift

        returns the logs for simulating the passed formula against past evtId. In the body you will need a json structure {formula:'<the formula>', msgId:3652, language:JS_NODEJS}  # noqa: E501
        """
        pass

    def test_create_toggle_event(self):
        """Test case for create_toggle_event

        Updates an event  # noqa: E501
        """
        pass

    def test_create_toggle_event1(self):
        """Test case for create_toggle_event1

        Updates an event  # noqa: E501
        """
        pass

    def test_create_trends(self):
        """Test case for create_trends

        Returns list of trends stored in WILCO  # noqa: E501
        """
        pass

    def test_create_uplink(self):
        """Test case for create_uplink

        uplink the with the layout  # noqa: E501
        """
        pass

    def test_create_uplink_same(self):
        """Test case for create_uplink_same

        uplink the fwot to get the same message as the event passed.uplinks only if the event has an uplinkable layout  # noqa: E501
        """
        pass

    def test_create_webhook(self):
        """Test case for create_webhook

        endpoint for push layouts webhooks  # noqa: E501
        """
        pass

    def test_delete_dashboard_rule(self):
        """Test case for delete_dashboard_rule

        deletes the dashboard rule  # noqa: E501
        """
        pass

    def test_delete_dashboard_symbols(self):
        """Test case for delete_dashboard_symbols

        Returns all the dashboard symbols  # noqa: E501
        """
        pass

    def test_delete_dashboards_dbid(self):
        """Test case for delete_dashboards_dbid

        trashes the dashboard  # noqa: E501
        """
        pass

    def test_delete_event(self):
        """Test case for delete_event

        Returns an event from the ID  # noqa: E501
        """
        pass

    def test_delete_layout(self):
        """Test case for delete_layout

        marks a layout as trashed  # noqa: E501
        """
        pass

    def test_delete_parameter(self):
        """Test case for delete_parameter

        returns a parameter. You can PUT or GET. DELETE not yet supported  # noqa: E501
        """
        pass

    def test_delete_symbol(self):
        """Test case for delete_symbol

        Returns/create/updates all the dashboard symbols. to delete a symbol function, empty its name  # noqa: E501
        """
        pass

    def test_delete_trend(self):
        """Test case for delete_trend

        get, update or delete a trend  # noqa: E501
        """
        pass

    def test_get_admin_links(self):
        """Test case for get_admin_links

        returns a list of links to admin features  # noqa: E501
        """
        pass

    def test_get_blocking_listen(self):
        """Test case for get_blocking_listen

        The method blocks until something happends in the message queue: creation, new message, fault, rule detected something, user did something (manual close, clear, recall warning...). no more than 100 messages from the after parameter  # noqa: E501
        """
        pass

    def test_get_bookmark(self):
        """Test case for get_bookmark

        Returns the bookmark image  # noqa: E501
        """
        pass

    def test_get_bookmarks(self):
        """Test case for get_bookmarks

        Returns list of bookmarks stored in WILCO  # noqa: E501
        """
        pass

    def test_get_categories(self):
        """Test case for get_categories

        Returns all the categories  # noqa: E501
        """
        pass

    def test_get_config(self):
        """Test case for get_config

        check the status of the server  # noqa: E501
        """
        pass

    def test_get_constants(self):
        """Test case for get_constants

        Returns all the constants  # noqa: E501
        """
        pass

    def test_get_dashboard(self):
        """Test case for get_dashboard

        Returns the dashboard  # noqa: E501
        """
        pass

    def test_get_dashboard_rule(self):
        """Test case for get_dashboard_rule

        Returns the dashboard rule  # noqa: E501
        """
        pass

    def test_get_dashboard_rule1(self):
        """Test case for get_dashboard_rule1

        Returns the dashboard rule  # noqa: E501
        """
        pass

    def test_get_dashboard_svg(self):
        """Test case for get_dashboard_svg

        Returns the SVG for a dashboard  # noqa: E501
        """
        pass

    def test_get_dashboard_symbols(self):
        """Test case for get_dashboard_symbols

        Returns all the dashboard symbols  # noqa: E501
        """
        pass

    def test_get_event(self):
        """Test case for get_event

        Returns an event from the ID  # noqa: E501
        """
        pass

    def test_get_event1(self):
        """Test case for get_event1

        Returns an event from the ID  # noqa: E501
        """
        pass

    def test_get_event_param(self):
        """Test case for get_event_param

        Returns param for this name, in this event  # noqa: E501
        """
        pass

    def test_get_event_param1(self):
        """Test case for get_event_param1

        Returns param for this name, in this event  # noqa: E501
        """
        pass

    def test_get_event_params(self):
        """Test case for get_event_params

        Returns the params involved in an event  # noqa: E501
        """
        pass

    def test_get_event_params1(self):
        """Test case for get_event_params1

        Returns the params involved in an event  # noqa: E501
        """
        pass

    def test_get_event_samples(self):
        """Test case for get_event_samples

        Returns the samples of an event  # noqa: E501
        """
        pass

    def test_get_event_samples1(self):
        """Test case for get_event_samples1

        Returns the samples of an event  # noqa: E501
        """
        pass

    def test_get_faultcodes(self):
        """Test case for get_faultcodes

        Returns the fault codes for the given fwot type  # noqa: E501
        """
        pass

    def test_get_fwot(self):
        """Test case for get_fwot

        Returns the fwot  # noqa: E501
        """
        pass

    def test_get_fwot_events(self):
        """Test case for get_fwot_events

        Returns some events of an fwot according to some filters  # noqa: E501
        """
        pass

    def test_get_fwot_events1(self):
        """Test case for get_fwot_events1

        Returns some events of an fwot according to some filters  # noqa: E501
        """
        pass

    def test_get_fwot_image(self):
        """Test case for get_fwot_image

        Returns the fwot image  # noqa: E501
        """
        pass

    def test_get_fwots(self):
        """Test case for get_fwots

        Returns all the fwots paginated. If the connected user has an airline, the list is filtered for this airline  # noqa: E501
        """
        pass

    def test_get_fwots1(self):
        """Test case for get_fwots1

        Returns all the fwots paginated. If the connected user has an airline, the list is filtered for this airline  # noqa: E501
        """
        pass

    def test_get_ift(self):
        """Test case for get_ift

        updates (PUT) and/or returns(GET) the ift  # noqa: E501
        """
        pass

    def test_get_ifts(self):
        """Test case for get_ifts

        Returns the ifts for faultcodes, layouts, parameters or robots  # noqa: E501
        """
        pass

    def test_get_ifts1(self):
        """Test case for get_ifts1

        Returns the ifts for faultcodes, layouts, parameters or robots  # noqa: E501
        """
        pass

    def test_get_last_event(self):
        """Test case for get_last_event

        all last events  # noqa: E501
        """
        pass

    def test_get_last_fwot_event(self):
        """Test case for get_last_fwot_event

        Returns the last event for a fwot  # noqa: E501
        """
        pass

    def test_get_layout(self):
        """Test case for get_layout

        Returns a layout stored in WILCO  # noqa: E501
        """
        pass

    def test_get_layouts(self):
        """Test case for get_layouts

        Returns list of layouts stored in WILCO  # noqa: E501
        """
        pass

    def test_get_layouts_layout_id_spider(self):
        """Test case for get_layouts_layout_id_spider

        Tunnels the layout EXT URL. If not an ExternalSourceLayout, returns a BAD REQUEST   # noqa: E501
        """
        pass

    def test_get_login(self):
        """Test case for get_login

        login to be authenticated  # noqa: E501
        """
        pass

    def test_get_logout(self):
        """Test case for get_logout

        log out from the current session  # noqa: E501
        """
        pass

    def test_get_next_event(self):
        """Test case for get_next_event

        Returns the next events type as the given one  # noqa: E501
        """
        pass

    def test_get_parameter(self):
        """Test case for get_parameter

        returns a parameter. You can PUT or GET. DELETE not yet supported  # noqa: E501
        """
        pass

    def test_get_parameter1(self):
        """Test case for get_parameter1

        Returns the parameter  # noqa: E501
        """
        pass

    def test_get_parameter2(self):
        """Test case for get_parameter2

        Returns the parameter  # noqa: E501
        """
        pass

    def test_get_parameters(self):
        """Test case for get_parameters

        Returns the parameters for the given search string  # noqa: E501
        """
        pass

    def test_get_parameters1(self):
        """Test case for get_parameters1

        Returns all parameters for an fwot type  # noqa: E501
        """
        pass

    def test_get_plural_category_reg_refresh(self):
        """Test case for get_plural_category_reg_refresh

        refresh the cache of the fwot  # noqa: E501
        """
        pass

    def test_get_previous_event(self):
        """Test case for get_previous_event

        Returns the previous events type as the given one  # noqa: E501
        """
        pass

    def test_get_raw(self):
        """Test case for get_raw

        returns the raw data for a message. empty string if not exists  # noqa: E501
        """
        pass

    def test_get_sample(self):
        """Test case for get_sample

        Returns a sample  # noqa: E501
        """
        pass

    def test_get_samples(self):
        """Test case for get_samples

        Returns list of samples stored in WILCO  # noqa: E501
        """
        pass

    def test_get_samples1(self):
        """Test case for get_samples1

        Returns a sample csv table as required in dygraphs for the fwot type. It can be filtered on filter parameter values.  # noqa: E501
        """
        pass

    def test_get_samples2(self):
        """Test case for get_samples2

        Returns list of samples stored in WILCO  # noqa: E501
        """
        pass

    def test_get_samples3(self):
        """Test case for get_samples3

        Returns list of samples stored in WILCO  # noqa: E501
        """
        pass

    def test_get_stats(self):
        """Test case for get_stats

        fetches some statistics on the running server  # noqa: E501
        """
        pass

    def test_get_status(self):
        """Test case for get_status

        check the status of the server  # noqa: E501
        """
        pass

    def test_get_symbol(self):
        """Test case for get_symbol

        Returns/create/updates all the dashboard symbols. to delete a symbol function, empty its name  # noqa: E501
        """
        pass

    def test_get_symbol_svg_example(self):
        """Test case for get_symbol_svg_example

        Returns the SVG example for a symbol  # noqa: E501
        """
        pass

    def test_get_terms_and_conditions(self):
        """Test case for get_terms_and_conditions

        returns the HTML for the terms and conditions  # noqa: E501
        """
        pass

    def test_get_trend(self):
        """Test case for get_trend

        get, update or delete a trend  # noqa: E501
        """
        pass

    def test_get_trends(self):
        """Test case for get_trends

        Returns list of trends stored in WILCO  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Returns profile of the current user  # noqa: E501
        """
        pass

    def test_get_users(self):
        """Test case for get_users

        fetches the list of users  # noqa: E501
        """
        pass

    def test_post_acars(self):
        """Test case for post_acars

        posts some raw data. if the decoder is not passed, then they are tried to find the first matching one  # noqa: E501
        """
        pass

    def test_post_acars_parser_name(self):
        """Test case for post_acars_parser_name

        posts some raw data. if the decoder is not passed, then they are tried to find the first matching one  # noqa: E501
        """
        pass

    def test_put_insert_message(self):
        """Test case for put_insert_message

        interface to update a message with the WILCO format. Deprecated. Use PUT:event  # noqa: E501
        """
        pass

    def test_update_batch_reprocess(self):
        """Test case for update_batch_reprocess

        allows to reprocess all the events with the same layout. It deletes and recreates the matching messages, samples and analysis. THIS CAN BE VEEERRY LONG and DANGEROUS. It processes the last week only taking the event date as ref date  # noqa: E501
        """
        pass

    def test_update_dashboard(self):
        """Test case for update_dashboard

        modifies the dashboard  # noqa: E501
        """
        pass

    def test_update_dashboard_rule(self):
        """Test case for update_dashboard_rule

        modifies the dashboard rule  # noqa: E501
        """
        pass

    def test_update_dashboard_symbols(self):
        """Test case for update_dashboard_symbols

        Returns all the dashboard symbols  # noqa: E501
        """
        pass

    def test_update_event(self):
        """Test case for update_event

        Returns an event from the ID  # noqa: E501
        """
        pass

    def test_update_fwot(self):
        """Test case for update_fwot

        Updates the fwot  # noqa: E501
        """
        pass

    def test_update_fwot_position(self):
        """Test case for update_fwot_position

        sets the fwot position  # noqa: E501
        """
        pass

    def test_update_ift(self):
        """Test case for update_ift

        updates (PUT) and/or returns(GET) the ift  # noqa: E501
        """
        pass

    def test_update_parameter(self):
        """Test case for update_parameter

        returns a parameter. You can PUT or GET. DELETE not yet supported  # noqa: E501
        """
        pass

    def test_update_reprocess(self):
        """Test case for update_reprocess

        allows to reprocess the event. It deletes the message, samples and analysis and recomputes it  # noqa: E501
        """
        pass

    def test_update_symbol(self):
        """Test case for update_symbol

        Returns/create/updates all the dashboard symbols. to delete a symbol function, empty its name  # noqa: E501
        """
        pass

    def test_update_tag(self):
        """Test case for update_tag

        tags an event  # noqa: E501
        """
        pass

    def test_update_trend(self):
        """Test case for update_trend

        get, update or delete a trend  # noqa: E501
        """
        pass

    def test_update_un_tag(self):
        """Test case for update_un_tag

        untags an event  # noqa: E501
        """
        pass

    def test_update_webhook(self):
        """Test case for update_webhook

        endpoint for push layouts webhooks  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
