# swagger_client.RuleApi

All URIs are relative to *http://localhost:8003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_rule_v1_id**](RuleApi.md#delete_rule_v1_id) | **DELETE** /rule/v1/{id} | 
[**get_rule_v1_info_id**](RuleApi.md#get_rule_v1_info_id) | **GET** /rule/v1/info/{id} | 
[**patch_rule_v1_update_id_field_value**](RuleApi.md#patch_rule_v1_update_id_field_value) | **PATCH** /rule/v1/update/{id}/{field}/{value} | 
[**post_rule_v1_add_iddomain**](RuleApi.md#post_rule_v1_add_iddomain) | **POST** /rule/v1/add/{iddomain} | 
[**post_rule_v1_query_iddomain_skip_limit**](RuleApi.md#post_rule_v1_query_iddomain_skip_limit) | **POST** /rule/v1/query/{iddomain}/{skip}/{limit} | 
[**put_rule_v1_update_iddomain_id**](RuleApi.md#put_rule_v1_update_iddomain_id) | **PUT** /rule/v1/update/{iddomain}/{id} | 


# **delete_rule_v1_id**
> str delete_rule_v1_id(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RuleApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.delete_rule_v1_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleApi->delete_rule_v1_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_v1_info_id**
> str get_rule_v1_info_id(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RuleApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.get_rule_v1_info_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleApi->get_rule_v1_info_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_rule_v1_update_id_field_value**
> str patch_rule_v1_update_id_field_value(id, field, value)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RuleApi()
id = 'id_example' # str | 
field = 'field_example' # str | 
value = 'value_example' # str | 

try:
    api_response = api_instance.patch_rule_v1_update_id_field_value(id, field, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleApi->patch_rule_v1_update_id_field_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **field** | **str**|  | 
 **value** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_rule_v1_add_iddomain**
> str post_rule_v1_add_iddomain(iddomain, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RuleApi()
iddomain = 'iddomain_example' # str | 
body = swagger_client.Model6() # Model6 |  (optional)

try:
    api_response = api_instance.post_rule_v1_add_iddomain(iddomain, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleApi->post_rule_v1_add_iddomain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iddomain** | **str**|  | 
 **body** | [**Model6**](Model6.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_rule_v1_query_iddomain_skip_limit**
> str post_rule_v1_query_iddomain_skip_limit(iddomain, skip, limit, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RuleApi()
iddomain = 'iddomain_example' # str | 
skip = 8.14 # float | 
limit = 8.14 # float | 
body = swagger_client.Model9() # Model9 |  (optional)

try:
    api_response = api_instance.post_rule_v1_query_iddomain_skip_limit(iddomain, skip, limit, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleApi->post_rule_v1_query_iddomain_skip_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iddomain** | **str**|  | 
 **skip** | **float**|  | 
 **limit** | **float**|  | 
 **body** | [**Model9**](Model9.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_rule_v1_update_iddomain_id**
> str put_rule_v1_update_iddomain_id(id, iddomain, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RuleApi()
id = 'id_example' # str | 
iddomain = 'iddomain_example' # str | 
body = swagger_client.Model6() # Model6 |  (optional)

try:
    api_response = api_instance.put_rule_v1_update_iddomain_id(id, iddomain, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleApi->put_rule_v1_update_iddomain_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **iddomain** | **str**|  | 
 **body** | [**Model6**](Model6.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

