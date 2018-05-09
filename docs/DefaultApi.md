# swagger_client.DefaultApi

All URIs are relative to *https://demo.flightwatching.com/fleet*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_analysis**](DefaultApi.md#create_analysis) | **POST** /apiv3/events/{eventId}/createAnalysis | create an analysis from the event passed. should use insert message. see https://github.com/flightwatching/fleet-monitor/issues/55
[**create_dashboard**](DefaultApi.md#create_dashboard) | **POST** /apiv3/dashboards | creates the dashboard
[**create_dashboard_rule**](DefaultApi.md#create_dashboard_rule) | **POST** /apiv3/dashboards/{dbid}/rules | creates a dashboard rule
[**create_dashboard_svg**](DefaultApi.md#create_dashboard_svg) | **POST** /apiv3/dashboards/{dbid}/svg | Returns the SVG for a dashboard
[**create_dashboard_symbols**](DefaultApi.md#create_dashboard_symbols) | **POST** /apiv3/symbols | Returns all the dashboard symbols
[**create_event**](DefaultApi.md#create_event) | **POST** /apiv3/events | creates an event
[**create_event_samples**](DefaultApi.md#create_event_samples) | **POST** /apiv3/events/{eventId}/samples | Returns the samples of an event
[**create_faultcode**](DefaultApi.md#create_faultcode) | **POST** /apiv3/faultcodes | Creates a fault code from the body
[**create_fwot**](DefaultApi.md#create_fwot) | **POST** /apiv3/fwots | Returns all the fwots paginated. If the connected user has an airline, the list is filtered for this airline
[**create_fwot_property**](DefaultApi.md#create_fwot_property) | **POST** /apiv3/{pluralCategory}/{reg}/property | add a new property to the fwot. If null passed in the value arg, the prop is removed
[**create_layout**](DefaultApi.md#create_layout) | **POST** /apiv3/layouts/{layoutId} | modifies a layout stored in WILCO
[**create_layout_event**](DefaultApi.md#create_layout_event) | **POST** /apiv3/events/{eventId}/layout | Creates a layout from a message
[**create_layouts**](DefaultApi.md#create_layouts) | **POST** /apiv3/layouts | Returns list of layouts stored in WILCO
[**create_parameters**](DefaultApi.md#create_parameters) | **POST** /apiv3/parameters | Returns the parameters for the given search string
[**create_simulate_push_pull**](DefaultApi.md#create_simulate_push_pull) | **POST** /apiv3/layouts/{pullLayoutId}/test | Calls the URL service and simulates the call to the IFT with the returned content in the right variable. In the body you will need a json structure {formula:&#39;&lt;the formula&gt;&#39;}
[**create_symbol**](DefaultApi.md#create_symbol) | **POST** /apiv3/symbols/{symbolId} | Returns/create/updates all the dashboard symbols. to delete a symbol function, empty its name
[**create_symbol_svg_example**](DefaultApi.md#create_symbol_svg_example) | **POST** /apiv3/symbols/{symbolId}/svgExample | Returns the SVG example for a symbol
[**create_test_ift**](DefaultApi.md#create_test_ift) | **POST** /apiv3/ifts/test | returns the logs for simulating the passed formula against past evtId. In the body you will need a json structure {formula:&#39;&lt;the formula&gt;&#39;, msgId:3652, language:JS_NODEJS}
[**create_toggle_event**](DefaultApi.md#create_toggle_event) | **POST** /apiv3/events/{eventId}/toggle | Updates an event
[**create_toggle_event1**](DefaultApi.md#create_toggle_event1) | **POST** /apiv3/{pluralCategory}/{reg}/events/{eventId}/toggle | Updates an event
[**create_trends**](DefaultApi.md#create_trends) | **POST** /apiv3/trendbundles | Returns list of trends stored in WILCO
[**create_uplink**](DefaultApi.md#create_uplink) | **POST** /apiv3/layouts/{layoutId}/uplink | uplink the with the layout
[**create_uplink_same**](DefaultApi.md#create_uplink_same) | **POST** /apiv3/{pluralCategory}/{reg}/events/{eventId}/uplinkSame | uplink the fwot to get the same message as the event passed.uplinks only if the event has an uplinkable layout
[**create_webhook**](DefaultApi.md#create_webhook) | **POST** /apiv3/layouts/webhook/{webhookId} | endpoint for push layouts webhooks
[**delete_dashboard_rule**](DefaultApi.md#delete_dashboard_rule) | **DELETE** /apiv3/dashboards/{dbid}/rules/{id} | deletes the dashboard rule
[**delete_dashboard_symbols**](DefaultApi.md#delete_dashboard_symbols) | **DELETE** /apiv3/symbols | Returns all the dashboard symbols
[**delete_dashboards_dbid**](DefaultApi.md#delete_dashboards_dbid) | **DELETE** /apiv3/dashboards/{dbid} | trashes the dashboard
[**delete_event**](DefaultApi.md#delete_event) | **DELETE** /apiv3/events/{eventId} | Returns an event from the ID
[**delete_layout**](DefaultApi.md#delete_layout) | **DELETE** /apiv3/layouts/{layoutId} | marks a layout as trashed
[**delete_parameter**](DefaultApi.md#delete_parameter) | **DELETE** /apiv3/parameters/{id} | returns a parameter. You can PUT or GET. DELETE not yet supported
[**delete_symbol**](DefaultApi.md#delete_symbol) | **DELETE** /apiv3/symbols/{symbolId} | Returns/create/updates all the dashboard symbols. to delete a symbol function, empty its name
[**delete_trend**](DefaultApi.md#delete_trend) | **DELETE** /apiv3/trendbundles/{bundleId} | get, update or delete a trend
[**get_admin_links**](DefaultApi.md#get_admin_links) | **GET** /apiv3/adminLinks | returns a list of links to admin features
[**get_blocking_listen**](DefaultApi.md#get_blocking_listen) | **GET** /apiv3/events/listenNewMessages | The method blocks until something happends in the message queue: creation, new message, fault, rule detected something, user did something (manual close, clear, recall warning...). no more than 100 messages from the after parameter
[**get_bookmark**](DefaultApi.md#get_bookmark) | **GET** /apiv3/bookmarks/{bookmark}/photo | Returns the bookmark image
[**get_bookmarks**](DefaultApi.md#get_bookmarks) | **GET** /apiv3/bookmarks | Returns list of bookmarks stored in WILCO
[**get_categories**](DefaultApi.md#get_categories) | **GET** /apiv3/categories | Returns all the categories
[**get_config**](DefaultApi.md#get_config) | **GET** /apiv3/config | check the status of the server
[**get_constants**](DefaultApi.md#get_constants) | **GET** /apiv3/constants | Returns all the constants
[**get_dashboard**](DefaultApi.md#get_dashboard) | **GET** /apiv3/dashboards/{id} | Returns the dashboard
[**get_dashboard_rule**](DefaultApi.md#get_dashboard_rule) | **GET** /apiv3/dashboards/rules/{id} | Returns the dashboard rule
[**get_dashboard_rule1**](DefaultApi.md#get_dashboard_rule1) | **GET** /apiv3/dashboards/{dbid}/rules/{id} | Returns the dashboard rule
[**get_dashboard_svg**](DefaultApi.md#get_dashboard_svg) | **GET** /apiv3/dashboards/{dbid}/svg | Returns the SVG for a dashboard
[**get_dashboard_symbols**](DefaultApi.md#get_dashboard_symbols) | **GET** /apiv3/symbols | Returns all the dashboard symbols
[**get_event**](DefaultApi.md#get_event) | **GET** /apiv3/events/{eventId} | Returns an event from the ID
[**get_event1**](DefaultApi.md#get_event1) | **GET** /apiv3/{pluralCategory}/{reg}/events/{eventId} | Returns an event from the ID
[**get_event_param**](DefaultApi.md#get_event_param) | **GET** /apiv3/events/{eventId}/parameters/{name} | Returns param for this name, in this event
[**get_event_param1**](DefaultApi.md#get_event_param1) | **GET** /apiv3/{pluralCategory}/{reg}/events/{eventId}/parameters/{name} | Returns param for this name, in this event
[**get_event_params**](DefaultApi.md#get_event_params) | **GET** /apiv3/events/{eventId}/parameters | Returns the params involved in an event
[**get_event_params1**](DefaultApi.md#get_event_params1) | **GET** /apiv3/{pluralCategory}/{reg}/events/{eventId}/parameters | Returns the params involved in an event
[**get_event_samples**](DefaultApi.md#get_event_samples) | **GET** /apiv3/events/{eventId}/samples | Returns the samples of an event
[**get_event_samples1**](DefaultApi.md#get_event_samples1) | **GET** /apiv3/{pluralCategory}/{reg}/events/{eventId}/samples | Returns the samples of an event
[**get_faultcodes**](DefaultApi.md#get_faultcodes) | **GET** /apiv3/faultcodes | Returns the fault codes for the given fwot type
[**get_fwot**](DefaultApi.md#get_fwot) | **GET** /apiv3/{pluralCategory}/{reg} | Returns the fwot
[**get_fwot_events**](DefaultApi.md#get_fwot_events) | **GET** /apiv3/events | Returns some events of an fwot according to some filters
[**get_fwot_events1**](DefaultApi.md#get_fwot_events1) | **GET** /apiv3/{pluralCategory}/{reg}/events | Returns some events of an fwot according to some filters
[**get_fwot_image**](DefaultApi.md#get_fwot_image) | **GET** /apiv3/{pluralCategory}/{reg}/photo | Returns the fwot image
[**get_fwots**](DefaultApi.md#get_fwots) | **GET** /apiv3/{pluralCategory} | Returns all the fwots paginated. If the connected user has an airline, the list is filtered for this airline
[**get_fwots1**](DefaultApi.md#get_fwots1) | **GET** /apiv3/fwots | Returns all the fwots paginated. If the connected user has an airline, the list is filtered for this airline
[**get_ift**](DefaultApi.md#get_ift) | **GET** /apiv3/ifts/{id} | updates (PUT) and/or returns(GET) the ift
[**get_ifts**](DefaultApi.md#get_ifts) | **GET** /apiv3/ifts | Returns the ifts for faultcodes, layouts, parameters or robots
[**get_ifts1**](DefaultApi.md#get_ifts1) | **GET** /apiv3/ifts/{category} | Returns the ifts for faultcodes, layouts, parameters or robots
[**get_last_event**](DefaultApi.md#get_last_event) | **GET** /apiv3/events/last/{count} | all last events
[**get_last_fwot_event**](DefaultApi.md#get_last_fwot_event) | **GET** /apiv3/{pluralCategory}/{reg}/events/last | Returns the last event for a fwot
[**get_layout**](DefaultApi.md#get_layout) | **GET** /apiv3/layouts/{layoutId} | Returns a layout stored in WILCO
[**get_layouts**](DefaultApi.md#get_layouts) | **GET** /apiv3/layouts | Returns list of layouts stored in WILCO
[**get_layouts_layout_id_spider**](DefaultApi.md#get_layouts_layout_id_spider) | **GET** /apiv3/layouts/{layoutId}/spider | Tunnels the layout EXT URL. If not an ExternalSourceLayout, returns a BAD REQUEST 
[**get_login**](DefaultApi.md#get_login) | **GET** /apiv3/login | login to be authenticated
[**get_logout**](DefaultApi.md#get_logout) | **GET** /apiv3/logout | log out from the current session
[**get_next_event**](DefaultApi.md#get_next_event) | **GET** /apiv3/{pluralCategory}/{reg}/events/{eventId}/next | Returns the next events type as the given one
[**get_parameter**](DefaultApi.md#get_parameter) | **GET** /apiv3/parameters/{id} | returns a parameter. You can PUT or GET. DELETE not yet supported
[**get_parameter1**](DefaultApi.md#get_parameter1) | **GET** /apiv3/parameters/{actype}/{name} | Returns the parameter
[**get_parameter2**](DefaultApi.md#get_parameter2) | **GET** /apiv3/{pluralCategory}/{reg}/parameters/{name} | Returns the parameter
[**get_parameters**](DefaultApi.md#get_parameters) | **GET** /apiv3/parameters | Returns the parameters for the given search string
[**get_parameters1**](DefaultApi.md#get_parameters1) | **GET** /apiv3/parameters/{actype} | Returns all parameters for an fwot type
[**get_plural_category_reg_refresh**](DefaultApi.md#get_plural_category_reg_refresh) | **GET** /apiv3/{pluralCategory}/{reg}/refresh | refresh the cache of the fwot
[**get_previous_event**](DefaultApi.md#get_previous_event) | **GET** /apiv3/{pluralCategory}/{reg}/events/{eventId}/prev | Returns the previous events type as the given one
[**get_raw**](DefaultApi.md#get_raw) | **GET** /apiv3/{pluralCategory}/{reg}/events/{eventId}/raw | returns the raw data for a message. empty string if not exists
[**get_sample**](DefaultApi.md#get_sample) | **GET** /apiv3/samples/{sampleId} | Returns a sample
[**get_samples**](DefaultApi.md#get_samples) | **GET** /apiv3/samples | Returns list of samples stored in WILCO
[**get_samples1**](DefaultApi.md#get_samples1) | **GET** /apiv3/parameters/{actype}/{name}/samples | Returns a sample csv table as required in dygraphs for the fwot type. It can be filtered on filter parameter values.
[**get_samples2**](DefaultApi.md#get_samples2) | **GET** /apiv3/{pluralCategory}/{reg}/samples/{name} | Returns list of samples stored in WILCO
[**get_samples3**](DefaultApi.md#get_samples3) | **GET** /apiv3/{pluralCategory}/{reg}/samples | Returns list of samples stored in WILCO
[**get_stats**](DefaultApi.md#get_stats) | **GET** /apiv3/stats | fetches some statistics on the running server
[**get_status**](DefaultApi.md#get_status) | **GET** /apiv3/status | check the status of the server
[**get_symbol**](DefaultApi.md#get_symbol) | **GET** /apiv3/symbols/{symbolId} | Returns/create/updates all the dashboard symbols. to delete a symbol function, empty its name
[**get_symbol_svg_example**](DefaultApi.md#get_symbol_svg_example) | **GET** /apiv3/symbols/{symbolId}/svgExample | Returns the SVG example for a symbol
[**get_terms_and_conditions**](DefaultApi.md#get_terms_and_conditions) | **GET** /apiv3/TnCs.html | returns the HTML for the terms and conditions
[**get_trend**](DefaultApi.md#get_trend) | **GET** /apiv3/trendbundles/{bundleId} | get, update or delete a trend
[**get_trends**](DefaultApi.md#get_trends) | **GET** /apiv3/trendbundles | Returns list of trends stored in WILCO
[**get_user**](DefaultApi.md#get_user) | **GET** /apiv3/profile | Returns profile of the current user
[**get_users**](DefaultApi.md#get_users) | **GET** /apiv3/users | fetches the list of users
[**post_acars**](DefaultApi.md#post_acars) | **POST** /apiv3/acars | posts some raw data. if the decoder is not passed, then they are tried to find the first matching one
[**post_acars_parser_name**](DefaultApi.md#post_acars_parser_name) | **POST** /apiv3/acars/{parserName} | posts some raw data. if the decoder is not passed, then they are tried to find the first matching one
[**put_insert_message**](DefaultApi.md#put_insert_message) | **PUT** /apiv3/insertMessage | interface to update a message with the WILCO format. Deprecated. Use PUT:event
[**update_batch_reprocess**](DefaultApi.md#update_batch_reprocess) | **PUT** /apiv3/events/{eventId}/reprocess/batch | allows to reprocess all the events with the same layout. It deletes and recreates the matching messages, samples and analysis. THIS CAN BE VEEERRY LONG and DANGEROUS. It processes the last week only taking the event date as ref date
[**update_dashboard**](DefaultApi.md#update_dashboard) | **PUT** /apiv3/dashboards/{id} | modifies the dashboard
[**update_dashboard_rule**](DefaultApi.md#update_dashboard_rule) | **PUT** /apiv3/dashboards/{dbid}/rules/{id} | modifies the dashboard rule
[**update_dashboard_symbols**](DefaultApi.md#update_dashboard_symbols) | **PUT** /apiv3/symbols | Returns all the dashboard symbols
[**update_event**](DefaultApi.md#update_event) | **PUT** /apiv3/events/{eventId} | Returns an event from the ID
[**update_fwot**](DefaultApi.md#update_fwot) | **PUT** /apiv3/{pluralCategory}/{reg} | Updates the fwot
[**update_fwot_position**](DefaultApi.md#update_fwot_position) | **PUT** /apiv3/{pluralCategory}/{reg}/location | sets the fwot position
[**update_ift**](DefaultApi.md#update_ift) | **PUT** /apiv3/ifts/{id} | updates (PUT) and/or returns(GET) the ift
[**update_parameter**](DefaultApi.md#update_parameter) | **PUT** /apiv3/parameters/{id} | returns a parameter. You can PUT or GET. DELETE not yet supported
[**update_reprocess**](DefaultApi.md#update_reprocess) | **PUT** /apiv3/events/{eventId}/reprocess | allows to reprocess the event. It deletes the message, samples and analysis and recomputes it
[**update_symbol**](DefaultApi.md#update_symbol) | **PUT** /apiv3/symbols/{symbolId} | Returns/create/updates all the dashboard symbols. to delete a symbol function, empty its name
[**update_tag**](DefaultApi.md#update_tag) | **PUT** /apiv3/events/{eventId}/tag | tags an event
[**update_trend**](DefaultApi.md#update_trend) | **PUT** /apiv3/trendbundles/{bundleId} | get, update or delete a trend
[**update_un_tag**](DefaultApi.md#update_un_tag) | **PUT** /apiv3/events/{eventId}/untag | untags an event
[**update_webhook**](DefaultApi.md#update_webhook) | **PUT** /apiv3/layouts/webhook/{webhookId} | endpoint for push layouts webhooks


# **create_analysis**
> create_analysis(event_id, content=content, rule_id=rule_id, fault_code=fault_code, d=d, severity=severity, flight_phase=flight_phase)

create an analysis from the event passed. should use insert message. see https://github.com/flightwatching/fleet-monitor/issues/55

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
event_id = 789 # int | the id of the event
content = 'content_example' # str | the sumUp (optional)
rule_id = 789 # int | the id of the rule that has trigged the creation (optional)
fault_code = 'fault_code_example' # str | the fault code if the analysis is linked to a fault code (optional)
d = '2013-10-20T19:20:30+01:00' # datetime | the date where the analysis has to locate. if not set, the event computed date is used (optional)
severity = 'severity_example' # str | the severity of the analysis (optional)
flight_phase = 'flight_phase_example' # str |  (optional)

try:
    # create an analysis from the event passed. should use insert message. see https://github.com/flightwatching/fleet-monitor/issues/55
    api_instance.create_analysis(event_id, content=content, rule_id=rule_id, fault_code=fault_code, d=d, severity=severity, flight_phase=flight_phase)
except ApiException as e:
    print("Exception when calling DefaultApi->create_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| the id of the event | 
 **content** | **str**| the sumUp | [optional] 
 **rule_id** | **int**| the id of the rule that has trigged the creation | [optional] 
 **fault_code** | **str**| the fault code if the analysis is linked to a fault code | [optional] 
 **d** | **datetime**| the date where the analysis has to locate. if not set, the event computed date is used | [optional] 
 **severity** | **str**| the severity of the analysis | [optional] 
 **flight_phase** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dashboard**
> DashboardV3IO create_dashboard()

creates the dashboard

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # creates the dashboard
    api_response = api_instance.create_dashboard()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_dashboard: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DashboardV3IO**](DashboardV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dashboard_rule**
> RuleV3IO create_dashboard_rule(dbid)

creates a dashboard rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
dbid = 789 # int | the id of the dashboard

try:
    # creates a dashboard rule
    api_response = api_instance.create_dashboard_rule(dbid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_dashboard_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbid** | **int**| the id of the dashboard | 

### Return type

[**RuleV3IO**](RuleV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dashboard_svg**
> str create_dashboard_svg(dbid)

Returns the SVG for a dashboard

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
dbid = 789 # int | the id of the symbol

try:
    # Returns the SVG for a dashboard
    api_response = api_instance.create_dashboard_svg(dbid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_dashboard_svg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbid** | **int**| the id of the symbol | 

### Return type

**str**

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dashboard_symbols**
> DashboardSymbolV3IO create_dashboard_symbols()

Returns all the dashboard symbols

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Returns all the dashboard symbols
    api_response = api_instance.create_dashboard_symbols()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_dashboard_symbols: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DashboardSymbolV3IO**](DashboardSymbolV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_event**
> EventV3IO create_event()

creates an event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # creates an event
    api_response = api_instance.create_event()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_event: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EventV3IO**](EventV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_event_samples**
> SampleV3IO create_event_samples(event_id, category=category, reg=reg, format=format, _from=_from, to=to)

Returns the samples of an event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
event_id = 789 # int | the id of the event
category = 'category_example' # str | the category of the fwot (optional)
reg = 'reg_example' # str | the registration of the fwot (optional)
format = 'format_example' # str |   or json. default is json (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | the min date for the sample (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | the max date for the sample (optional)

try:
    # Returns the samples of an event
    api_response = api_instance.create_event_samples(event_id, category=category, reg=reg, format=format, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_event_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| the id of the event | 
 **category** | **str**| the category of the fwot | [optional] 
 **reg** | **str**| the registration of the fwot | [optional] 
 **format** | **str**|   or json. default is json | [optional] 
 **_from** | **datetime**| the min date for the sample | [optional] 
 **to** | **datetime**| the max date for the sample | [optional] 

### Return type

[**SampleV3IO**](SampleV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_faultcode**
> IftV3IO create_faultcode()

Creates a fault code from the body

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Creates a fault code from the body
    api_response = api_instance.create_faultcode()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_faultcode: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IftV3IO**](IftV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fwot**
> FwotV3IO create_fwot()

Returns all the fwots paginated. If the connected user has an airline, the list is filtered for this airline

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Returns all the fwots paginated. If the connected user has an airline, the list is filtered for this airline
    api_response = api_instance.create_fwot()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_fwot: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FwotV3IO**](FwotV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fwot_property**
> create_fwot_property(plural_category, reg, name, value=value)

add a new property to the fwot. If null passed in the value arg, the prop is removed

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
reg = 'reg_example' # str | the registration of the fwot
name = 'name_example' # str | the name of the property
value = 'value_example' # str | the value of the property. if null, the prop is removed (optional)

try:
    # add a new property to the fwot. If null passed in the value arg, the prop is removed
    api_instance.create_fwot_property(plural_category, reg, name, value=value)
except ApiException as e:
    print("Exception when calling DefaultApi->create_fwot_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **reg** | **str**| the registration of the fwot | 
 **name** | **str**| the name of the property | 
 **value** | **str**| the value of the property. if null, the prop is removed | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_layout**
> LayoutV3IO create_layout(layout_id)

modifies a layout stored in WILCO

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
layout_id = 789 # int | the id of the layout

try:
    # modifies a layout stored in WILCO
    api_response = api_instance.create_layout(layout_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layout_id** | **int**| the id of the layout | 

### Return type

[**LayoutV3IO**](LayoutV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_layout_event**
> LayoutV3IO create_layout_event(event_id)

Creates a layout from a message

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
event_id = 789 # int | the id of the event from which we create the layout

try:
    # Creates a layout from a message
    api_response = api_instance.create_layout_event(event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_layout_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| the id of the event from which we create the layout | 

### Return type

[**LayoutV3IO**](LayoutV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_layouts**
> LayoutV3IO create_layouts(page=page, count=count, contains=contains)

Returns list of layouts stored in WILCO

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
page = 56 # int | the page. starts #1 (optional)
count = 56 # int | the max count of parameter (optional)
contains = 'contains_example' # str | the layout name part to filter on (optional)

try:
    # Returns list of layouts stored in WILCO
    api_response = api_instance.create_layouts(page=page, count=count, contains=contains)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_layouts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| the page. starts #1 | [optional] 
 **count** | **int**| the max count of parameter | [optional] 
 **contains** | **str**| the layout name part to filter on | [optional] 

### Return type

[**LayoutV3IO**](LayoutV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_parameters**
> ParameterV3IO create_parameters(contains=contains, detailled=detailled, page=page, count=count)

Returns the parameters for the given search string

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
contains = 'contains_example' # str | the parameter name part to filter on (optional)
detailled = true # bool | Do we return the head (false&default) or the complete description? (optional)
page = 56 # int | the page. starts #1 (optional)
count = 56 # int | the max count of parameter (optional)

try:
    # Returns the parameters for the given search string
    api_response = api_instance.create_parameters(contains=contains, detailled=detailled, page=page, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contains** | **str**| the parameter name part to filter on | [optional] 
 **detailled** | **bool**| Do we return the head (false&amp;default) or the complete description? | [optional] 
 **page** | **int**| the page. starts #1 | [optional] 
 **count** | **int**| the max count of parameter | [optional] 

### Return type

[**ParameterV3IO**](ParameterV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_simulate_push_pull**
> create_simulate_push_pull(pull_layout_id)

Calls the URL service and simulates the call to the IFT with the returned content in the right variable. In the body you will need a json structure {formula:'<the formula>'}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
pull_layout_id = 789 # int | the id of the pull layout

try:
    # Calls the URL service and simulates the call to the IFT with the returned content in the right variable. In the body you will need a json structure {formula:'<the formula>'}
    api_instance.create_simulate_push_pull(pull_layout_id)
except ApiException as e:
    print("Exception when calling DefaultApi->create_simulate_push_pull: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pull_layout_id** | **int**| the id of the pull layout | 

### Return type

void (empty response body)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_symbol**
> DashboardSymbolV3IO create_symbol(symbol_id)

Returns/create/updates all the dashboard symbols. to delete a symbol function, empty its name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
symbol_id = 789 # int | the id of the symbol

try:
    # Returns/create/updates all the dashboard symbols. to delete a symbol function, empty its name
    api_response = api_instance.create_symbol(symbol_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_symbol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol_id** | **int**| the id of the symbol | 

### Return type

[**DashboardSymbolV3IO**](DashboardSymbolV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_symbol_svg_example**
> str create_symbol_svg_example(symbol_id)

Returns the SVG example for a symbol

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
symbol_id = 789 # int | the id of the symbol

try:
    # Returns the SVG example for a symbol
    api_response = api_instance.create_symbol_svg_example(symbol_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_symbol_svg_example: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol_id** | **int**| the id of the symbol | 

### Return type

**str**

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_test_ift**
> IftV3IO create_test_ift()

returns the logs for simulating the passed formula against past evtId. In the body you will need a json structure {formula:'<the formula>', msgId:3652, language:JS_NODEJS}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # returns the logs for simulating the passed formula against past evtId. In the body you will need a json structure {formula:'<the formula>', msgId:3652, language:JS_NODEJS}
    api_response = api_instance.create_test_ift()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_test_ift: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IftV3IO**](IftV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_toggle_event**
> EventV3IO create_toggle_event(event_id, category=category, reg=reg)

Updates an event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
event_id = 789 # int | the id of the event
category = 'category_example' # str | the category of the fwot (optional)
reg = 'reg_example' # str | the registration of the fwot (optional)

try:
    # Updates an event
    api_response = api_instance.create_toggle_event(event_id, category=category, reg=reg)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_toggle_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| the id of the event | 
 **category** | **str**| the category of the fwot | [optional] 
 **reg** | **str**| the registration of the fwot | [optional] 

### Return type

[**EventV3IO**](EventV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_toggle_event1**
> EventV3IO create_toggle_event1(plural_category, reg, event_id)

Updates an event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
reg = 'reg_example' # str | the registration of the fwot
event_id = 789 # int | the id of the event

try:
    # Updates an event
    api_response = api_instance.create_toggle_event1(plural_category, reg, event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_toggle_event1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **reg** | **str**| the registration of the fwot | 
 **event_id** | **int**| the id of the event | 

### Return type

[**EventV3IO**](EventV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_trends**
> TrendBundleV3IO create_trends()

Returns list of trends stored in WILCO

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Returns list of trends stored in WILCO
    api_response = api_instance.create_trends()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_trends: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TrendBundleV3IO**](TrendBundleV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_uplink**
> create_uplink(reg, layout_id, delay=delay, rule_id=rule_id)

uplink the with the layout

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
reg = 'reg_example' # str | the registration of the fwot
layout_id = 789 # int | the ID of the layout to uplink
delay = 56 # int | delay in seconds before the actual uplink (optional)
rule_id = 789 # int | the id of the rule that trigged the uplink. if null, the user is considered (optional)

try:
    # uplink the with the layout
    api_instance.create_uplink(reg, layout_id, delay=delay, rule_id=rule_id)
except ApiException as e:
    print("Exception when calling DefaultApi->create_uplink: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reg** | **str**| the registration of the fwot | 
 **layout_id** | **int**| the ID of the layout to uplink | 
 **delay** | **int**| delay in seconds before the actual uplink | [optional] 
 **rule_id** | **int**| the id of the rule that trigged the uplink. if null, the user is considered | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_uplink_same**
> create_uplink_same(plural_category, reg, event_id)

uplink the fwot to get the same message as the event passed.uplinks only if the event has an uplinkable layout

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
reg = 'reg_example' # str | the registration of the fwot
event_id = 789 # int | the id of the event

try:
    # uplink the fwot to get the same message as the event passed.uplinks only if the event has an uplinkable layout
    api_instance.create_uplink_same(plural_category, reg, event_id)
except ApiException as e:
    print("Exception when calling DefaultApi->create_uplink_same: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **reg** | **str**| the registration of the fwot | 
 **event_id** | **int**| the id of the event | 

### Return type

void (empty response body)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_webhook**
> LayoutV3IO create_webhook(webhook_id)

endpoint for push layouts webhooks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
webhook_id = 'webhook_id_example' # str | the uuid of the hook

try:
    # endpoint for push layouts webhooks
    api_response = api_instance.create_webhook(webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| the uuid of the hook | 

### Return type

[**LayoutV3IO**](LayoutV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard_rule**
> RuleV3IO delete_dashboard_rule(dbid, id)

deletes the dashboard rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
dbid = 789 # int | the id of the dashboard
id = 789 # int | the id of the dashboard rule

try:
    # deletes the dashboard rule
    api_response = api_instance.delete_dashboard_rule(dbid, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_dashboard_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbid** | **int**| the id of the dashboard | 
 **id** | **int**| the id of the dashboard rule | 

### Return type

[**RuleV3IO**](RuleV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard_symbols**
> DashboardSymbolV3IO delete_dashboard_symbols()

Returns all the dashboard symbols

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Returns all the dashboard symbols
    api_response = api_instance.delete_dashboard_symbols()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_dashboard_symbols: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DashboardSymbolV3IO**](DashboardSymbolV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboards_dbid**
> RuleV3IO delete_dashboards_dbid(dbid)

trashes the dashboard

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
dbid = 789 # int | the id of the dashboard

try:
    # trashes the dashboard
    api_response = api_instance.delete_dashboards_dbid(dbid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_dashboards_dbid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbid** | **int**| the id of the dashboard | 

### Return type

[**RuleV3IO**](RuleV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event**
> EventV3IO delete_event(event_id, category=category, reg=reg, nested=nested)

Returns an event from the ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
event_id = 789 # int | the id of the event
category = 'category_example' # str | the category of the fwot (optional)
reg = 'reg_example' # str | the registration of the fwot (optional)
nested = true # bool | do we create a nested JSON (samples+A/C+...) (optional)

try:
    # Returns an event from the ID
    api_response = api_instance.delete_event(event_id, category=category, reg=reg, nested=nested)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| the id of the event | 
 **category** | **str**| the category of the fwot | [optional] 
 **reg** | **str**| the registration of the fwot | [optional] 
 **nested** | **bool**| do we create a nested JSON (samples+A/C+...) | [optional] 

### Return type

[**EventV3IO**](EventV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_layout**
> LayoutV3IO delete_layout(layout_id)

marks a layout as trashed

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
layout_id = 789 # int | the id of the layout

try:
    # marks a layout as trashed
    api_response = api_instance.delete_layout(layout_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layout_id** | **int**| the id of the layout | 

### Return type

[**LayoutV3IO**](LayoutV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_parameter**
> ParameterV3IO delete_parameter(id)

returns a parameter. You can PUT or GET. DELETE not yet supported

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 789 # int | the id of the parameters to filter on.

try:
    # returns a parameter. You can PUT or GET. DELETE not yet supported
    api_response = api_instance.delete_parameter(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| the id of the parameters to filter on. | 

### Return type

[**ParameterV3IO**](ParameterV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_symbol**
> DashboardSymbolV3IO delete_symbol(symbol_id)

Returns/create/updates all the dashboard symbols. to delete a symbol function, empty its name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
symbol_id = 789 # int | the id of the symbol

try:
    # Returns/create/updates all the dashboard symbols. to delete a symbol function, empty its name
    api_response = api_instance.delete_symbol(symbol_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_symbol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol_id** | **int**| the id of the symbol | 

### Return type

[**DashboardSymbolV3IO**](DashboardSymbolV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_trend**
> TrendBundleV3IO delete_trend(bundle_id)

get, update or delete a trend

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
bundle_id = 789 # int | the id of the bundle

try:
    # get, update or delete a trend
    api_response = api_instance.delete_trend(bundle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_trend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **int**| the id of the bundle | 

### Return type

[**TrendBundleV3IO**](TrendBundleV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_links**
> get_admin_links()

returns a list of links to admin features

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # returns a list of links to admin features
    api_instance.get_admin_links()
except ApiException as e:
    print("Exception when calling DefaultApi->get_admin_links: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blocking_listen**
> EventV3IO get_blocking_listen(after=after, block_duration=block_duration)

The method blocks until something happends in the message queue: creation, new message, fault, rule detected something, user did something (manual close, clear, recall warning...). no more than 100 messages from the after parameter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
after = 789 # int | the timestamp after which we want the elements. if no value, use current time (optional)
block_duration = 789 # int | how many seconds this method blocks before releasing if no event. if no value, blocks 10s (optional)

try:
    # The method blocks until something happends in the message queue: creation, new message, fault, rule detected something, user did something (manual close, clear, recall warning...). no more than 100 messages from the after parameter
    api_response = api_instance.get_blocking_listen(after=after, block_duration=block_duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_blocking_listen: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **int**| the timestamp after which we want the elements. if no value, use current time | [optional] 
 **block_duration** | **int**| how many seconds this method blocks before releasing if no event. if no value, blocks 10s | [optional] 

### Return type

[**EventV3IO**](EventV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bookmark**
> get_bookmark(bookmark)

Returns the bookmark image

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
bookmark = 789 # int | the id of the bookmark

try:
    # Returns the bookmark image
    api_instance.get_bookmark(bookmark)
except ApiException as e:
    print("Exception when calling DefaultApi->get_bookmark: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bookmark** | **int**| the id of the bookmark | 

### Return type

void (empty response body)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bookmarks**
> BookmarkV3IO get_bookmarks()

Returns list of bookmarks stored in WILCO

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Returns list of bookmarks stored in WILCO
    api_response = api_instance.get_bookmarks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_bookmarks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BookmarkV3IO**](BookmarkV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories**
> str get_categories()

Returns all the categories

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Returns all the categories
    api_response = api_instance.get_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config**
> get_config()

check the status of the server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # check the status of the server
    api_instance.get_config()
except ApiException as e:
    print("Exception when calling DefaultApi->get_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_constants**
> ConstantV3IO get_constants()

Returns all the constants

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Returns all the constants
    api_response = api_instance.get_constants()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_constants: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConstantV3IO**](ConstantV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard**
> DashboardV3IO get_dashboard(id)

Returns the dashboard

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 789 # int | the id of the dashboard

try:
    # Returns the dashboard
    api_response = api_instance.get_dashboard(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| the id of the dashboard | 

### Return type

[**DashboardV3IO**](DashboardV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_rule**
> RuleV3IO get_dashboard_rule(id, dbid=dbid)

Returns the dashboard rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 789 # int | the id of the dashboard rule
dbid = 789 # int | the id of the dashboard (optional)

try:
    # Returns the dashboard rule
    api_response = api_instance.get_dashboard_rule(id, dbid=dbid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_dashboard_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| the id of the dashboard rule | 
 **dbid** | **int**| the id of the dashboard | [optional] 

### Return type

[**RuleV3IO**](RuleV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_rule1**
> RuleV3IO get_dashboard_rule1(dbid, id)

Returns the dashboard rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
dbid = 789 # int | the id of the dashboard
id = 789 # int | the id of the dashboard rule

try:
    # Returns the dashboard rule
    api_response = api_instance.get_dashboard_rule1(dbid, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_dashboard_rule1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbid** | **int**| the id of the dashboard | 
 **id** | **int**| the id of the dashboard rule | 

### Return type

[**RuleV3IO**](RuleV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_svg**
> str get_dashboard_svg(dbid)

Returns the SVG for a dashboard

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
dbid = 789 # int | the id of the symbol

try:
    # Returns the SVG for a dashboard
    api_response = api_instance.get_dashboard_svg(dbid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_dashboard_svg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbid** | **int**| the id of the symbol | 

### Return type

**str**

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_symbols**
> DashboardSymbolV3IO get_dashboard_symbols()

Returns all the dashboard symbols

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Returns all the dashboard symbols
    api_response = api_instance.get_dashboard_symbols()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_dashboard_symbols: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DashboardSymbolV3IO**](DashboardSymbolV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event**
> EventV3IO get_event(event_id, category=category, reg=reg, nested=nested)

Returns an event from the ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
event_id = 789 # int | the id of the event
category = 'category_example' # str | the category of the fwot (optional)
reg = 'reg_example' # str | the registration of the fwot (optional)
nested = true # bool | do we create a nested JSON (samples+A/C+...) (optional)

try:
    # Returns an event from the ID
    api_response = api_instance.get_event(event_id, category=category, reg=reg, nested=nested)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| the id of the event | 
 **category** | **str**| the category of the fwot | [optional] 
 **reg** | **str**| the registration of the fwot | [optional] 
 **nested** | **bool**| do we create a nested JSON (samples+A/C+...) | [optional] 

### Return type

[**EventV3IO**](EventV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event1**
> EventV3IO get_event1(plural_category, reg, event_id, nested=nested)

Returns an event from the ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
reg = 'reg_example' # str | the registration of the fwot
event_id = 789 # int | the id of the event
nested = true # bool | do we create a nested JSON (samples+A/C+...) (optional)

try:
    # Returns an event from the ID
    api_response = api_instance.get_event1(plural_category, reg, event_id, nested=nested)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_event1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **reg** | **str**| the registration of the fwot | 
 **event_id** | **int**| the id of the event | 
 **nested** | **bool**| do we create a nested JSON (samples+A/C+...) | [optional] 

### Return type

[**EventV3IO**](EventV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_param**
> ParameterV3IO get_event_param(event_id, name, category=category, reg=reg)

Returns param for this name, in this event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
event_id = 789 # int | the id of the event
name = 'name_example' # str | the name of the param
category = 'category_example' # str | the category of the fwot (optional)
reg = 'reg_example' # str | the registration of the fwot (optional)

try:
    # Returns param for this name, in this event
    api_response = api_instance.get_event_param(event_id, name, category=category, reg=reg)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_event_param: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| the id of the event | 
 **name** | **str**| the name of the param | 
 **category** | **str**| the category of the fwot | [optional] 
 **reg** | **str**| the registration of the fwot | [optional] 

### Return type

[**ParameterV3IO**](ParameterV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_param1**
> ParameterV3IO get_event_param1(plural_category, reg, event_id, name)

Returns param for this name, in this event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
reg = 'reg_example' # str | the registration of the fwot
event_id = 789 # int | the id of the event
name = 'name_example' # str | the name of the param

try:
    # Returns param for this name, in this event
    api_response = api_instance.get_event_param1(plural_category, reg, event_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_event_param1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **reg** | **str**| the registration of the fwot | 
 **event_id** | **int**| the id of the event | 
 **name** | **str**| the name of the param | 

### Return type

[**ParameterV3IO**](ParameterV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_params**
> ParameterV3IO get_event_params(event_id, category=category, reg=reg, name=name)

Returns the params involved in an event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
event_id = 789 # int | the id of the event
category = 'category_example' # str | the category of the fwot (optional)
reg = 'reg_example' # str | the registration of the fwot (optional)
name = 'name_example' # str | the name of the param (optional)

try:
    # Returns the params involved in an event
    api_response = api_instance.get_event_params(event_id, category=category, reg=reg, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_event_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| the id of the event | 
 **category** | **str**| the category of the fwot | [optional] 
 **reg** | **str**| the registration of the fwot | [optional] 
 **name** | **str**| the name of the param | [optional] 

### Return type

[**ParameterV3IO**](ParameterV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_params1**
> ParameterV3IO get_event_params1(plural_category, reg, event_id, name=name)

Returns the params involved in an event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
reg = 'reg_example' # str | the registration of the fwot
event_id = 789 # int | the id of the event
name = 'name_example' # str | the name of the param (optional)

try:
    # Returns the params involved in an event
    api_response = api_instance.get_event_params1(plural_category, reg, event_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_event_params1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **reg** | **str**| the registration of the fwot | 
 **event_id** | **int**| the id of the event | 
 **name** | **str**| the name of the param | [optional] 

### Return type

[**ParameterV3IO**](ParameterV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_samples**
> SampleV3IO get_event_samples(event_id, category=category, reg=reg, format=format, _from=_from, to=to)

Returns the samples of an event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
event_id = 789 # int | the id of the event
category = 'category_example' # str | the category of the fwot (optional)
reg = 'reg_example' # str | the registration of the fwot (optional)
format = 'format_example' # str |   or json. default is json (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | the min date for the sample (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | the max date for the sample (optional)

try:
    # Returns the samples of an event
    api_response = api_instance.get_event_samples(event_id, category=category, reg=reg, format=format, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_event_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| the id of the event | 
 **category** | **str**| the category of the fwot | [optional] 
 **reg** | **str**| the registration of the fwot | [optional] 
 **format** | **str**|   or json. default is json | [optional] 
 **_from** | **datetime**| the min date for the sample | [optional] 
 **to** | **datetime**| the max date for the sample | [optional] 

### Return type

[**SampleV3IO**](SampleV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_samples1**
> SampleV3IO get_event_samples1(plural_category, reg, event_id, format=format, _from=_from, to=to)

Returns the samples of an event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
reg = 'reg_example' # str | the registration of the fwot
event_id = 789 # int | the id of the event
format = 'format_example' # str |   or json. default is json (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | the min date for the sample (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | the max date for the sample (optional)

try:
    # Returns the samples of an event
    api_response = api_instance.get_event_samples1(plural_category, reg, event_id, format=format, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_event_samples1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **reg** | **str**| the registration of the fwot | 
 **event_id** | **int**| the id of the event | 
 **format** | **str**|   or json. default is json | [optional] 
 **_from** | **datetime**| the min date for the sample | [optional] 
 **to** | **datetime**| the max date for the sample | [optional] 

### Return type

[**SampleV3IO**](SampleV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_faultcodes**
> IftV3IO get_faultcodes(actype=actype, prefix=prefix, page=page, count=count)

Returns the fault codes for the given fwot type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
actype = 'actype_example' # str | the fwot type (optional)
prefix = 'prefix_example' # str | the faultcode prefix (eg ATA) (optional)
page = 56 # int | the page. starts #1 (optional)
count = 56 # int | the max count of faultcodes (optional)

try:
    # Returns the fault codes for the given fwot type
    api_response = api_instance.get_faultcodes(actype=actype, prefix=prefix, page=page, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_faultcodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actype** | **str**| the fwot type | [optional] 
 **prefix** | **str**| the faultcode prefix (eg ATA) | [optional] 
 **page** | **int**| the page. starts #1 | [optional] 
 **count** | **int**| the max count of faultcodes | [optional] 

### Return type

[**IftV3IO**](IftV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fwot**
> FwotV3IO get_fwot(plural_category, reg)

Returns the fwot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
reg = 'reg_example' # str | the registration of the fwot

try:
    # Returns the fwot
    api_response = api_instance.get_fwot(plural_category, reg)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_fwot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **reg** | **str**| the registration of the fwot | 

### Return type

[**FwotV3IO**](FwotV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fwot_events**
> EventV3IO get_fwot_events(category=category, reg=reg, _from=_from, to=to, with_dismissed=with_dismissed, show_hidden=show_hidden, important=important, sev=sev, tag=tag, count=count, after=after)

Returns some events of an fwot according to some filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
category = 'category_example' # str | the category of the fwot (optional)
reg = 'reg_example' # str | the registration of the fwot (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | the date from which we want to get the events (strict gt -> does not include exact same date (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | the date to which we want to get the events (strict lt -> does not include exact same date (optional)
with_dismissed = true # bool | show the dismissed events (optional)
show_hidden = true # bool | show the non visible events (optional)
important = true # bool | only important events (optional)
sev = 'sev_example' # str | only important events (optional)
tag = 'tag_example' # str | only events matching the given tag. Can have several tags in the request (optional)
count = 56 # int | the max count of messages (optional)
after = 789 # int | the timestamp after which we want the elements (optional)

try:
    # Returns some events of an fwot according to some filters
    api_response = api_instance.get_fwot_events(category=category, reg=reg, _from=_from, to=to, with_dismissed=with_dismissed, show_hidden=show_hidden, important=important, sev=sev, tag=tag, count=count, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_fwot_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| the category of the fwot | [optional] 
 **reg** | **str**| the registration of the fwot | [optional] 
 **_from** | **datetime**| the date from which we want to get the events (strict gt -&gt; does not include exact same date | [optional] 
 **to** | **datetime**| the date to which we want to get the events (strict lt -&gt; does not include exact same date | [optional] 
 **with_dismissed** | **bool**| show the dismissed events | [optional] 
 **show_hidden** | **bool**| show the non visible events | [optional] 
 **important** | **bool**| only important events | [optional] 
 **sev** | **str**| only important events | [optional] 
 **tag** | **str**| only events matching the given tag. Can have several tags in the request | [optional] 
 **count** | **int**| the max count of messages | [optional] 
 **after** | **int**| the timestamp after which we want the elements | [optional] 

### Return type

[**EventV3IO**](EventV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fwot_events1**
> EventV3IO get_fwot_events1(plural_category, reg, _from=_from, to=to, with_dismissed=with_dismissed, show_hidden=show_hidden, important=important, sev=sev, tag=tag, count=count, after=after)

Returns some events of an fwot according to some filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
reg = 'reg_example' # str | the registration of the fwot
_from = '2013-10-20T19:20:30+01:00' # datetime | the date from which we want to get the events (strict gt -> does not include exact same date (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | the date to which we want to get the events (strict lt -> does not include exact same date (optional)
with_dismissed = true # bool | show the dismissed events (optional)
show_hidden = true # bool | show the non visible events (optional)
important = true # bool | only important events (optional)
sev = 'sev_example' # str | only important events (optional)
tag = 'tag_example' # str | only events matching the given tag. Can have several tags in the request (optional)
count = 56 # int | the max count of messages (optional)
after = 789 # int | the timestamp after which we want the elements (optional)

try:
    # Returns some events of an fwot according to some filters
    api_response = api_instance.get_fwot_events1(plural_category, reg, _from=_from, to=to, with_dismissed=with_dismissed, show_hidden=show_hidden, important=important, sev=sev, tag=tag, count=count, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_fwot_events1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **reg** | **str**| the registration of the fwot | 
 **_from** | **datetime**| the date from which we want to get the events (strict gt -&gt; does not include exact same date | [optional] 
 **to** | **datetime**| the date to which we want to get the events (strict lt -&gt; does not include exact same date | [optional] 
 **with_dismissed** | **bool**| show the dismissed events | [optional] 
 **show_hidden** | **bool**| show the non visible events | [optional] 
 **important** | **bool**| only important events | [optional] 
 **sev** | **str**| only important events | [optional] 
 **tag** | **str**| only events matching the given tag. Can have several tags in the request | [optional] 
 **count** | **int**| the max count of messages | [optional] 
 **after** | **int**| the timestamp after which we want the elements | [optional] 

### Return type

[**EventV3IO**](EventV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fwot_image**
> get_fwot_image(plural_category, reg)

Returns the fwot image

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
reg = 'reg_example' # str | the registration of the fwot

try:
    # Returns the fwot image
    api_instance.get_fwot_image(plural_category, reg)
except ApiException as e:
    print("Exception when calling DefaultApi->get_fwot_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **reg** | **str**| the registration of the fwot | 

### Return type

void (empty response body)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fwots**
> FwotV3IO get_fwots(plural_category, page=page, count=count)

Returns all the fwots paginated. If the connected user has an airline, the list is filtered for this airline

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
page = 56 # int | the page. starts #1 (optional)
count = 56 # int | the max count of messages (optional)

try:
    # Returns all the fwots paginated. If the connected user has an airline, the list is filtered for this airline
    api_response = api_instance.get_fwots(plural_category, page=page, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_fwots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **page** | **int**| the page. starts #1 | [optional] 
 **count** | **int**| the max count of messages | [optional] 

### Return type

[**FwotV3IO**](FwotV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fwots1**
> FwotV3IO get_fwots1(category, page=page, count=count)

Returns all the fwots paginated. If the connected user has an airline, the list is filtered for this airline

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
category = 'category_example' # str | the category of the fwot
page = 56 # int | the page. starts #1 (optional)
count = 56 # int | the max count of messages (optional)

try:
    # Returns all the fwots paginated. If the connected user has an airline, the list is filtered for this airline
    api_response = api_instance.get_fwots1(category, page=page, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_fwots1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| the category of the fwot | 
 **page** | **int**| the page. starts #1 | [optional] 
 **count** | **int**| the max count of messages | [optional] 

### Return type

[**FwotV3IO**](FwotV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ift**
> IftV3IO get_ift(id)

updates (PUT) and/or returns(GET) the ift

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 789 # int | the ift ID

try:
    # updates (PUT) and/or returns(GET) the ift
    api_response = api_instance.get_ift(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_ift: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| the ift ID | 

### Return type

[**IftV3IO**](IftV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifts**
> IftV3IO get_ifts(category=category, contains=contains, page=page, count=count)

Returns the ifts for faultcodes, layouts, parameters or robots

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
category = 'category_example' # str | category of the IFT: faultcodes, layouts, parameters, robots (optional)
contains = 'contains_example' # str | a string contained by the formula (optional)
page = 56 # int | the page. starts #1 (optional)
count = 56 # int | the max count of faultcodes (optional)

try:
    # Returns the ifts for faultcodes, layouts, parameters or robots
    api_response = api_instance.get_ifts(category=category, contains=contains, page=page, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_ifts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| category of the IFT: faultcodes, layouts, parameters, robots | [optional] 
 **contains** | **str**| a string contained by the formula | [optional] 
 **page** | **int**| the page. starts #1 | [optional] 
 **count** | **int**| the max count of faultcodes | [optional] 

### Return type

[**IftV3IO**](IftV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifts1**
> IftV3IO get_ifts1(category, contains=contains, page=page, count=count)

Returns the ifts for faultcodes, layouts, parameters or robots

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
category = 'category_example' # str | category of the IFT: faultcodes, layouts, parameters, robots
contains = 'contains_example' # str | a string contained by the formula (optional)
page = 56 # int | the page. starts #1 (optional)
count = 56 # int | the max count of faultcodes (optional)

try:
    # Returns the ifts for faultcodes, layouts, parameters or robots
    api_response = api_instance.get_ifts1(category, contains=contains, page=page, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_ifts1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| category of the IFT: faultcodes, layouts, parameters, robots | 
 **contains** | **str**| a string contained by the formula | [optional] 
 **page** | **int**| the page. starts #1 | [optional] 
 **count** | **int**| the max count of faultcodes | [optional] 

### Return type

[**IftV3IO**](IftV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_event**
> EventV3IO get_last_event(count, tags=tags, sev=sev, dismissed=dismissed)

all last events

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
count = 56 # int | the max count of messages
tags = 'tags_example' # str | the list of filtering tags (optional)
sev = 'sev_example' # str | the list of filtering severity (optional)
dismissed = true # bool | filter if dismissed or not dismissed or no filter if not set (optional)

try:
    # all last events
    api_response = api_instance.get_last_event(count, tags=tags, sev=sev, dismissed=dismissed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_last_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| the max count of messages | 
 **tags** | **str**| the list of filtering tags | [optional] 
 **sev** | **str**| the list of filtering severity | [optional] 
 **dismissed** | **bool**| filter if dismissed or not dismissed or no filter if not set | [optional] 

### Return type

[**EventV3IO**](EventV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_fwot_event**
> EventV3IO get_last_fwot_event(plural_category, reg)

Returns the last event for a fwot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
reg = 'reg_example' # str | the registration of the fwot

try:
    # Returns the last event for a fwot
    api_response = api_instance.get_last_fwot_event(plural_category, reg)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_last_fwot_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **reg** | **str**| the registration of the fwot | 

### Return type

[**EventV3IO**](EventV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_layout**
> LayoutV3IO get_layout(layout_id)

Returns a layout stored in WILCO

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
layout_id = 789 # int | the id of the layout

try:
    # Returns a layout stored in WILCO
    api_response = api_instance.get_layout(layout_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layout_id** | **int**| the id of the layout | 

### Return type

[**LayoutV3IO**](LayoutV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_layouts**
> LayoutV3IO get_layouts(page=page, count=count, contains=contains)

Returns list of layouts stored in WILCO

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
page = 56 # int | the page. starts #1 (optional)
count = 56 # int | the max count of parameter (optional)
contains = 'contains_example' # str | the layout name part to filter on (optional)

try:
    # Returns list of layouts stored in WILCO
    api_response = api_instance.get_layouts(page=page, count=count, contains=contains)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_layouts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| the page. starts #1 | [optional] 
 **count** | **int**| the max count of parameter | [optional] 
 **contains** | **str**| the layout name part to filter on | [optional] 

### Return type

[**LayoutV3IO**](LayoutV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_layouts_layout_id_spider**
> LayoutV3IO get_layouts_layout_id_spider(layout_id)

Tunnels the layout EXT URL. If not an ExternalSourceLayout, returns a BAD REQUEST 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
layout_id = 789 # int | the id of the layout

try:
    # Tunnels the layout EXT URL. If not an ExternalSourceLayout, returns a BAD REQUEST 
    api_response = api_instance.get_layouts_layout_id_spider(layout_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_layouts_layout_id_spider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layout_id** | **int**| the id of the layout | 

### Return type

[**LayoutV3IO**](LayoutV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_login**
> UserV3IO get_login(username, tnc, password=password, remember=remember)

login to be authenticated

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
username = 'username_example' # str | the login to connect with. Is an email address
tnc = true # bool | I do accept the terms and conditions
password = 'password_example' # str | the password to connect with (optional)
remember = true # bool | remember the connection information for 30 days (optional)

try:
    # login to be authenticated
    api_response = api_instance.get_login(username, tnc, password=password, remember=remember)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the login to connect with. Is an email address | 
 **tnc** | **bool**| I do accept the terms and conditions | 
 **password** | **str**| the password to connect with | [optional] 
 **remember** | **bool**| remember the connection information for 30 days | [optional] 

### Return type

[**UserV3IO**](UserV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logout**
> ErrorDao get_logout()

log out from the current session

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # log out from the current session
    api_response = api_instance.get_logout()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ErrorDao**](ErrorDao.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_next_event**
> EventV3IO get_next_event(plural_category, reg, event_id, count=count)

Returns the next events type as the given one

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
reg = 'reg_example' # str | the registration of the fwot
event_id = 789 # int | the id of the event
count = 56 # int | the count of returned messages (optional)

try:
    # Returns the next events type as the given one
    api_response = api_instance.get_next_event(plural_category, reg, event_id, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_next_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **reg** | **str**| the registration of the fwot | 
 **event_id** | **int**| the id of the event | 
 **count** | **int**| the count of returned messages | [optional] 

### Return type

[**EventV3IO**](EventV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter**
> ParameterV3IO get_parameter(id)

returns a parameter. You can PUT or GET. DELETE not yet supported

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 789 # int | the id of the parameters to filter on.

try:
    # returns a parameter. You can PUT or GET. DELETE not yet supported
    api_response = api_instance.get_parameter(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| the id of the parameters to filter on. | 

### Return type

[**ParameterV3IO**](ParameterV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter1**
> ParameterV3IO get_parameter1(actype, name, category=category, reg=reg)

Returns the parameter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
actype = 'actype_example' # str | the fwot type. You will need either a actype or a reg for this request
name = 'name_example' # str | the name of the parameter
category = 'category_example' # str | the category of the fwot (optional)
reg = 'reg_example' # str | the fwot reg. You will need either a actype or a reg for this request (optional)

try:
    # Returns the parameter
    api_response = api_instance.get_parameter1(actype, name, category=category, reg=reg)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_parameter1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actype** | **str**| the fwot type. You will need either a actype or a reg for this request | 
 **name** | **str**| the name of the parameter | 
 **category** | **str**| the category of the fwot | [optional] 
 **reg** | **str**| the fwot reg. You will need either a actype or a reg for this request | [optional] 

### Return type

[**ParameterV3IO**](ParameterV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter2**
> ParameterV3IO get_parameter2(plural_category, reg, name, actype=actype)

Returns the parameter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
reg = 'reg_example' # str | the fwot reg. You will need either a actype or a reg for this request
name = 'name_example' # str | the name of the parameter
actype = 'actype_example' # str | the fwot type. You will need either a actype or a reg for this request (optional)

try:
    # Returns the parameter
    api_response = api_instance.get_parameter2(plural_category, reg, name, actype=actype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_parameter2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **reg** | **str**| the fwot reg. You will need either a actype or a reg for this request | 
 **name** | **str**| the name of the parameter | 
 **actype** | **str**| the fwot type. You will need either a actype or a reg for this request | [optional] 

### Return type

[**ParameterV3IO**](ParameterV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameters**
> ParameterV3IO get_parameters(contains=contains, detailled=detailled, page=page, count=count)

Returns the parameters for the given search string

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
contains = 'contains_example' # str | the parameter name part to filter on (optional)
detailled = true # bool | Do we return the head (false&default) or the complete description? (optional)
page = 56 # int | the page. starts #1 (optional)
count = 56 # int | the max count of parameter (optional)

try:
    # Returns the parameters for the given search string
    api_response = api_instance.get_parameters(contains=contains, detailled=detailled, page=page, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contains** | **str**| the parameter name part to filter on | [optional] 
 **detailled** | **bool**| Do we return the head (false&amp;default) or the complete description? | [optional] 
 **page** | **int**| the page. starts #1 | [optional] 
 **count** | **int**| the max count of parameter | [optional] 

### Return type

[**ParameterV3IO**](ParameterV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameters1**
> ParameterV3IO get_parameters1(actype, name=name)

Returns all parameters for an fwot type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
actype = 'actype_example' # str | the fwot type
name = 'name_example' # str | the parameter names to filter on. May be null (optional)

try:
    # Returns all parameters for an fwot type
    api_response = api_instance.get_parameters1(actype, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_parameters1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actype** | **str**| the fwot type | 
 **name** | **str**| the parameter names to filter on. May be null | [optional] 

### Return type

[**ParameterV3IO**](ParameterV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plural_category_reg_refresh**
> FwotV3IO get_plural_category_reg_refresh(plural_category, reg)

refresh the cache of the fwot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
reg = 'reg_example' # str | the registration of the fwot

try:
    # refresh the cache of the fwot
    api_response = api_instance.get_plural_category_reg_refresh(plural_category, reg)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_plural_category_reg_refresh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **reg** | **str**| the registration of the fwot | 

### Return type

[**FwotV3IO**](FwotV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_previous_event**
> EventV3IO get_previous_event(plural_category, reg, event_id, count=count)

Returns the previous events type as the given one

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
reg = 'reg_example' # str | the registration of the fwot
event_id = 789 # int | the id of the event
count = 56 # int | the count of returned messages (optional)

try:
    # Returns the previous events type as the given one
    api_response = api_instance.get_previous_event(plural_category, reg, event_id, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_previous_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **reg** | **str**| the registration of the fwot | 
 **event_id** | **int**| the id of the event | 
 **count** | **int**| the count of returned messages | [optional] 

### Return type

[**EventV3IO**](EventV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw**
> str get_raw(plural_category, reg, event_id)

returns the raw data for a message. empty string if not exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
reg = 'reg_example' # str | the registration of the fwot
event_id = 789 # int | the id of the event

try:
    # returns the raw data for a message. empty string if not exists
    api_response = api_instance.get_raw(plural_category, reg, event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **reg** | **str**| the registration of the fwot | 
 **event_id** | **int**| the id of the event | 

### Return type

**str**

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sample**
> SampleV3IO get_sample(sample_id)

Returns a sample

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
sample_id = 789 # int | the id of the sample

try:
    # Returns a sample
    api_response = api_instance.get_sample(sample_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_sample: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **int**| the id of the sample | 

### Return type

[**SampleV3IO**](SampleV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_samples**
> SampleV3IO get_samples(category=category, reg=reg, actype=actype, name=name, _from=_from, to=to, page=page, count=count, with_invalid=with_invalid, format=format, chronological=chronological)

Returns list of samples stored in WILCO

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
category = 'category_example' # str | the category of the fwot (optional)
reg = 'reg_example' # str | if reg is null or empty, will be all the fwots (optional)
actype = 'actype_example' # str | fwot type (optional)
name = 'name_example' # str | the parameter name. May be several (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | the date from which we want to get the samples (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | the date to which we want to get the samples (optional)
page = 56 # int | the page. starts #1 (optional)
count = 56 # int | the max count of messages (optional)
with_invalid = true # bool | default/false: include not VALID state samples. true -> include them (optional)
format = 'format_example' # str | json or csv or tsv (optional)
chronological = true # bool | if false: from newest to oldest (optional)

try:
    # Returns list of samples stored in WILCO
    api_response = api_instance.get_samples(category=category, reg=reg, actype=actype, name=name, _from=_from, to=to, page=page, count=count, with_invalid=with_invalid, format=format, chronological=chronological)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| the category of the fwot | [optional] 
 **reg** | **str**| if reg is null or empty, will be all the fwots | [optional] 
 **actype** | **str**| fwot type | [optional] 
 **name** | **str**| the parameter name. May be several | [optional] 
 **_from** | **datetime**| the date from which we want to get the samples | [optional] 
 **to** | **datetime**| the date to which we want to get the samples | [optional] 
 **page** | **int**| the page. starts #1 | [optional] 
 **count** | **int**| the max count of messages | [optional] 
 **with_invalid** | **bool**| default/false: include not VALID state samples. true -&gt; include them | [optional] 
 **format** | **str**| json or csv or tsv | [optional] 
 **chronological** | **bool**| if false: from newest to oldest | [optional] 

### Return type

[**SampleV3IO**](SampleV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_samples1**
> SampleV3IO get_samples1(actype, name, filter_name=filter_name, filter_value=filter_value, format=format, _from=_from, to=to, with_invalid=with_invalid, count=count)

Returns a sample csv table as required in dygraphs for the fwot type. It can be filtered on filter parameter values.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
actype = 'actype_example' # str | the type of fwot
name = 'name_example' # str | the parameter name
filter_name = 'filter_name_example' # str | the parameter name used to filter (optional)
filter_value = 'filter_value_example' # str | the parameter name used to filter (optional)
format = 'format_example' # str | json or csv or tsv (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | the date from which we want to get the samples (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | the date to which we want to get the samples (optional)
with_invalid = true # bool | default/false: include not VALID state samples. true -> include them (optional)
count = 56 # int | the max count of messages (optional)

try:
    # Returns a sample csv table as required in dygraphs for the fwot type. It can be filtered on filter parameter values.
    api_response = api_instance.get_samples1(actype, name, filter_name=filter_name, filter_value=filter_value, format=format, _from=_from, to=to, with_invalid=with_invalid, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_samples1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actype** | **str**| the type of fwot | 
 **name** | **str**| the parameter name | 
 **filter_name** | **str**| the parameter name used to filter | [optional] 
 **filter_value** | **str**| the parameter name used to filter | [optional] 
 **format** | **str**| json or csv or tsv | [optional] 
 **_from** | **datetime**| the date from which we want to get the samples | [optional] 
 **to** | **datetime**| the date to which we want to get the samples | [optional] 
 **with_invalid** | **bool**| default/false: include not VALID state samples. true -&gt; include them | [optional] 
 **count** | **int**| the max count of messages | [optional] 

### Return type

[**SampleV3IO**](SampleV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_samples2**
> SampleV3IO get_samples2(plural_category, reg, name, actype=actype, _from=_from, to=to, page=page, count=count, with_invalid=with_invalid, format=format, chronological=chronological)

Returns list of samples stored in WILCO

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
reg = 'reg_example' # str | if reg is null or empty, will be all the fwots
name = 'name_example' # str | the parameter name. May be several
actype = 'actype_example' # str | fwot type (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | the date from which we want to get the samples (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | the date to which we want to get the samples (optional)
page = 56 # int | the page. starts #1 (optional)
count = 56 # int | the max count of messages (optional)
with_invalid = true # bool | default/false: include not VALID state samples. true -> include them (optional)
format = 'format_example' # str | json or csv or tsv (optional)
chronological = true # bool | if false: from newest to oldest (optional)

try:
    # Returns list of samples stored in WILCO
    api_response = api_instance.get_samples2(plural_category, reg, name, actype=actype, _from=_from, to=to, page=page, count=count, with_invalid=with_invalid, format=format, chronological=chronological)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_samples2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **reg** | **str**| if reg is null or empty, will be all the fwots | 
 **name** | **str**| the parameter name. May be several | 
 **actype** | **str**| fwot type | [optional] 
 **_from** | **datetime**| the date from which we want to get the samples | [optional] 
 **to** | **datetime**| the date to which we want to get the samples | [optional] 
 **page** | **int**| the page. starts #1 | [optional] 
 **count** | **int**| the max count of messages | [optional] 
 **with_invalid** | **bool**| default/false: include not VALID state samples. true -&gt; include them | [optional] 
 **format** | **str**| json or csv or tsv | [optional] 
 **chronological** | **bool**| if false: from newest to oldest | [optional] 

### Return type

[**SampleV3IO**](SampleV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_samples3**
> SampleV3IO get_samples3(plural_category, reg, actype=actype, name=name, _from=_from, to=to, page=page, count=count, with_invalid=with_invalid, format=format, chronological=chronological)

Returns list of samples stored in WILCO

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
reg = 'reg_example' # str | if reg is null or empty, will be all the fwots
actype = 'actype_example' # str | fwot type (optional)
name = 'name_example' # str | the parameter name. May be several (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | the date from which we want to get the samples (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | the date to which we want to get the samples (optional)
page = 56 # int | the page. starts #1 (optional)
count = 56 # int | the max count of messages (optional)
with_invalid = true # bool | default/false: include not VALID state samples. true -> include them (optional)
format = 'format_example' # str | json or csv or tsv (optional)
chronological = true # bool | if false: from newest to oldest (optional)

try:
    # Returns list of samples stored in WILCO
    api_response = api_instance.get_samples3(plural_category, reg, actype=actype, name=name, _from=_from, to=to, page=page, count=count, with_invalid=with_invalid, format=format, chronological=chronological)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_samples3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **reg** | **str**| if reg is null or empty, will be all the fwots | 
 **actype** | **str**| fwot type | [optional] 
 **name** | **str**| the parameter name. May be several | [optional] 
 **_from** | **datetime**| the date from which we want to get the samples | [optional] 
 **to** | **datetime**| the date to which we want to get the samples | [optional] 
 **page** | **int**| the page. starts #1 | [optional] 
 **count** | **int**| the max count of messages | [optional] 
 **with_invalid** | **bool**| default/false: include not VALID state samples. true -&gt; include them | [optional] 
 **format** | **str**| json or csv or tsv | [optional] 
 **chronological** | **bool**| if false: from newest to oldest | [optional] 

### Return type

[**SampleV3IO**](SampleV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats**
> StatsV3IO get_stats(_from=_from, to=to)

fetches some statistics on the running server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
_from = '2013-10-20T19:20:30+01:00' # datetime | the computed date from which we want to get the events (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | the computed date to which we want to get the events (optional)

try:
    # fetches some statistics on the running server
    api_response = api_instance.get_stats(_from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| the computed date from which we want to get the events | [optional] 
 **to** | **datetime**| the computed date to which we want to get the events | [optional] 

### Return type

[**StatsV3IO**](StatsV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> get_status()

check the status of the server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # check the status of the server
    api_instance.get_status()
except ApiException as e:
    print("Exception when calling DefaultApi->get_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_symbol**
> DashboardSymbolV3IO get_symbol(symbol_id)

Returns/create/updates all the dashboard symbols. to delete a symbol function, empty its name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
symbol_id = 789 # int | the id of the symbol

try:
    # Returns/create/updates all the dashboard symbols. to delete a symbol function, empty its name
    api_response = api_instance.get_symbol(symbol_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_symbol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol_id** | **int**| the id of the symbol | 

### Return type

[**DashboardSymbolV3IO**](DashboardSymbolV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_symbol_svg_example**
> str get_symbol_svg_example(symbol_id)

Returns the SVG example for a symbol

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
symbol_id = 789 # int | the id of the symbol

try:
    # Returns the SVG example for a symbol
    api_response = api_instance.get_symbol_svg_example(symbol_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_symbol_svg_example: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol_id** | **int**| the id of the symbol | 

### Return type

**str**

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_terms_and_conditions**
> get_terms_and_conditions()

returns the HTML for the terms and conditions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # returns the HTML for the terms and conditions
    api_instance.get_terms_and_conditions()
except ApiException as e:
    print("Exception when calling DefaultApi->get_terms_and_conditions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trend**
> TrendBundleV3IO get_trend(bundle_id)

get, update or delete a trend

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
bundle_id = 789 # int | the id of the bundle

try:
    # get, update or delete a trend
    api_response = api_instance.get_trend(bundle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_trend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **int**| the id of the bundle | 

### Return type

[**TrendBundleV3IO**](TrendBundleV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trends**
> TrendBundleV3IO get_trends()

Returns list of trends stored in WILCO

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Returns list of trends stored in WILCO
    api_response = api_instance.get_trends()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_trends: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TrendBundleV3IO**](TrendBundleV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserV3IO get_user()

Returns profile of the current user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Returns profile of the current user
    api_response = api_instance.get_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserV3IO**](UserV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> UserV3IO get_users()

fetches the list of users

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # fetches the list of users
    api_response = api_instance.get_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserV3IO**](UserV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_acars**
> EventV3IO post_acars(parser_name=parser_name, webhook=webhook)

posts some raw data. if the decoder is not passed, then they are tried to find the first matching one

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
parser_name = 'parser_name_example' # str | the name of the parser (optional)
webhook = 'webhook_example' # str | if defined, the query returns immediately and calls the webhook when finished with the event as JSON (optional)

try:
    # posts some raw data. if the decoder is not passed, then they are tried to find the first matching one
    api_response = api_instance.post_acars(parser_name=parser_name, webhook=webhook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_acars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parser_name** | **str**| the name of the parser | [optional] 
 **webhook** | **str**| if defined, the query returns immediately and calls the webhook when finished with the event as JSON | [optional] 

### Return type

[**EventV3IO**](EventV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_acars_parser_name**
> EventV3IO post_acars_parser_name(parser_name, webhook=webhook)

posts some raw data. if the decoder is not passed, then they are tried to find the first matching one

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
parser_name = 'parser_name_example' # str | the name of the parser
webhook = 'webhook_example' # str | if defined, the query returns immediately and calls the webhook when finished with the event as JSON (optional)

try:
    # posts some raw data. if the decoder is not passed, then they are tried to find the first matching one
    api_response = api_instance.post_acars_parser_name(parser_name, webhook=webhook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_acars_parser_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parser_name** | **str**| the name of the parser | 
 **webhook** | **str**| if defined, the query returns immediately and calls the webhook when finished with the event as JSON | [optional] 

### Return type

[**EventV3IO**](EventV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_insert_message**
> put_insert_message()

interface to update a message with the WILCO format. Deprecated. Use PUT:event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # interface to update a message with the WILCO format. Deprecated. Use PUT:event
    api_instance.put_insert_message()
except ApiException as e:
    print("Exception when calling DefaultApi->put_insert_message: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_batch_reprocess**
> update_batch_reprocess(event_id)

allows to reprocess all the events with the same layout. It deletes and recreates the matching messages, samples and analysis. THIS CAN BE VEEERRY LONG and DANGEROUS. It processes the last week only taking the event date as ref date

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
event_id = 789 # int | the id of the event

try:
    # allows to reprocess all the events with the same layout. It deletes and recreates the matching messages, samples and analysis. THIS CAN BE VEEERRY LONG and DANGEROUS. It processes the last week only taking the event date as ref date
    api_instance.update_batch_reprocess(event_id)
except ApiException as e:
    print("Exception when calling DefaultApi->update_batch_reprocess: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| the id of the event | 

### Return type

void (empty response body)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard**
> DashboardV3IO update_dashboard(id, skip_symbols)

modifies the dashboard

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 789 # int | the id of the dashboard
skip_symbols = true # bool | do not update symbols

try:
    # modifies the dashboard
    api_response = api_instance.update_dashboard(id, skip_symbols)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| the id of the dashboard | 
 **skip_symbols** | **bool**| do not update symbols | 

### Return type

[**DashboardV3IO**](DashboardV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard_rule**
> RuleV3IO update_dashboard_rule(dbid, id)

modifies the dashboard rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
dbid = 789 # int | the id of the dashboard
id = 789 # int | the id of the dashboard rule

try:
    # modifies the dashboard rule
    api_response = api_instance.update_dashboard_rule(dbid, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_dashboard_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbid** | **int**| the id of the dashboard | 
 **id** | **int**| the id of the dashboard rule | 

### Return type

[**RuleV3IO**](RuleV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard_symbols**
> DashboardSymbolV3IO update_dashboard_symbols()

Returns all the dashboard symbols

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Returns all the dashboard symbols
    api_response = api_instance.update_dashboard_symbols()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_dashboard_symbols: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DashboardSymbolV3IO**](DashboardSymbolV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event**
> EventV3IO update_event(event_id, category=category, reg=reg, nested=nested)

Returns an event from the ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
event_id = 789 # int | the id of the event
category = 'category_example' # str | the category of the fwot (optional)
reg = 'reg_example' # str | the registration of the fwot (optional)
nested = true # bool | do we create a nested JSON (samples+A/C+...) (optional)

try:
    # Returns an event from the ID
    api_response = api_instance.update_event(event_id, category=category, reg=reg, nested=nested)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| the id of the event | 
 **category** | **str**| the category of the fwot | [optional] 
 **reg** | **str**| the registration of the fwot | [optional] 
 **nested** | **bool**| do we create a nested JSON (samples+A/C+...) | [optional] 

### Return type

[**EventV3IO**](EventV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fwot**
> FwotV3IO update_fwot(plural_category, reg)

Updates the fwot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
reg = 'reg_example' # str | the registration of the fwot

try:
    # Updates the fwot
    api_response = api_instance.update_fwot(plural_category, reg)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_fwot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **reg** | **str**| the registration of the fwot | 

### Return type

[**FwotV3IO**](FwotV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fwot_position**
> FwotV3IO update_fwot_position(plural_category, reg, reg_log=reg_log, lat=lat, lon=lon, alt=alt, date=date)

sets the fwot position

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
plural_category = 'plural_category_example' # str | the category of the fwot
reg = 'reg_example' # str | the registration of the fwot
reg_log = 'reg_log_example' # str | the reg of a fwot that has lat/lon (optional)
lat = 3.4 # float | the lat of the fwot (optional)
lon = 3.4 # float | the lon of the fwot (optional)
alt = 3.4 # float | the alt of the fwot (optional)
date = '2013-10-20T19:20:30+01:00' # datetime | the pos date of the fwot (optional)

try:
    # sets the fwot position
    api_response = api_instance.update_fwot_position(plural_category, reg, reg_log=reg_log, lat=lat, lon=lon, alt=alt, date=date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_fwot_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plural_category** | **str**| the category of the fwot | 
 **reg** | **str**| the registration of the fwot | 
 **reg_log** | **str**| the reg of a fwot that has lat/lon | [optional] 
 **lat** | **float**| the lat of the fwot | [optional] 
 **lon** | **float**| the lon of the fwot | [optional] 
 **alt** | **float**| the alt of the fwot | [optional] 
 **date** | **datetime**| the pos date of the fwot | [optional] 

### Return type

[**FwotV3IO**](FwotV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ift**
> IftV3IO update_ift(id)

updates (PUT) and/or returns(GET) the ift

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 789 # int | the ift ID

try:
    # updates (PUT) and/or returns(GET) the ift
    api_response = api_instance.update_ift(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_ift: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| the ift ID | 

### Return type

[**IftV3IO**](IftV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_parameter**
> ParameterV3IO update_parameter(id)

returns a parameter. You can PUT or GET. DELETE not yet supported

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 789 # int | the id of the parameters to filter on.

try:
    # returns a parameter. You can PUT or GET. DELETE not yet supported
    api_response = api_instance.update_parameter(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| the id of the parameters to filter on. | 

### Return type

[**ParameterV3IO**](ParameterV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reprocess**
> update_reprocess(event_id)

allows to reprocess the event. It deletes the message, samples and analysis and recomputes it

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
event_id = 789 # int | the id of the event

try:
    # allows to reprocess the event. It deletes the message, samples and analysis and recomputes it
    api_instance.update_reprocess(event_id)
except ApiException as e:
    print("Exception when calling DefaultApi->update_reprocess: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| the id of the event | 

### Return type

void (empty response body)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_symbol**
> DashboardSymbolV3IO update_symbol(symbol_id)

Returns/create/updates all the dashboard symbols. to delete a symbol function, empty its name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
symbol_id = 789 # int | the id of the symbol

try:
    # Returns/create/updates all the dashboard symbols. to delete a symbol function, empty its name
    api_response = api_instance.update_symbol(symbol_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_symbol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol_id** | **int**| the id of the symbol | 

### Return type

[**DashboardSymbolV3IO**](DashboardSymbolV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag**
> EventV3IO update_tag(event_id, tag)

tags an event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
event_id = 789 # int | the id of the event
tag = 'tag_example' # str | the tag to set

try:
    # tags an event
    api_response = api_instance.update_tag(event_id, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| the id of the event | 
 **tag** | **str**| the tag to set | 

### Return type

[**EventV3IO**](EventV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_trend**
> TrendBundleV3IO update_trend(bundle_id)

get, update or delete a trend

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
bundle_id = 789 # int | the id of the bundle

try:
    # get, update or delete a trend
    api_response = api_instance.update_trend(bundle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_trend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **int**| the id of the bundle | 

### Return type

[**TrendBundleV3IO**](TrendBundleV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_un_tag**
> EventV3IO update_un_tag(event_id, tag)

untags an event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
event_id = 789 # int | the id of the event
tag = 'tag_example' # str | the tag to remove

try:
    # untags an event
    api_response = api_instance.update_un_tag(event_id, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_un_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| the id of the event | 
 **tag** | **str**| the tag to remove | 

### Return type

[**EventV3IO**](EventV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> LayoutV3IO update_webhook(webhook_id)

endpoint for push layouts webhooks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key_header
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: api_key_param
configuration = swagger_client.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
webhook_id = 'webhook_id_example' # str | the uuid of the hook

try:
    # endpoint for push layouts webhooks
    api_response = api_instance.update_webhook(webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| the uuid of the hook | 

### Return type

[**LayoutV3IO**](LayoutV3IO.md)

### Authorization

[api_key_header](../README.md#api_key_header), [api_key_param](../README.md#api_key_param)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

