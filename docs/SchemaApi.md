# swagger_client.SchemaApi

All URIs are relative to *http://localhost:8003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_schema_v1_info_id**](SchemaApi.md#get_schema_v1_info_id) | **GET** /schema/v1/info/{id} | 
[**post_schema_v1_group_type**](SchemaApi.md#post_schema_v1_group_type) | **POST** /schema/v1/group/{type} | 
[**post_schema_v1_query_skip_limit**](SchemaApi.md#post_schema_v1_query_skip_limit) | **POST** /schema/v1/query/{skip}/{limit} | 


# **get_schema_v1_info_id**
> str get_schema_v1_info_id(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SchemaApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.get_schema_v1_info_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->get_schema_v1_info_id: %s\n" % e)
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

# **post_schema_v1_group_type**
> str post_schema_v1_group_type(type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SchemaApi()
type = 'type_example' # str | 

try:
    api_response = api_instance.post_schema_v1_group_type(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->post_schema_v1_group_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_schema_v1_query_skip_limit**
> str post_schema_v1_query_skip_limit(skip, limit, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SchemaApi()
skip = 8.14 # float | 
limit = 8.14 # float | 
body = swagger_client.Model11() # Model11 |  (optional)

try:
    api_response = api_instance.post_schema_v1_query_skip_limit(skip, limit, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->post_schema_v1_query_skip_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **float**|  | 
 **limit** | **float**|  | 
 **body** | [**Model11**](Model11.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

