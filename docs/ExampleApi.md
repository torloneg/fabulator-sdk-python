# swagger_client.ExampleApi

All URIs are relative to *http://localhost:8003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_example_v1_iddomain_id**](ExampleApi.md#delete_example_v1_iddomain_id) | **DELETE** /example/v1/{iddomain}/{id} | 
[**get_example_v1_info_iddomain_id**](ExampleApi.md#get_example_v1_info_iddomain_id) | **GET** /example/v1/info/{iddomain}/{id} | 
[**patch_example_v1_update_iddomain_id_field_value**](ExampleApi.md#patch_example_v1_update_iddomain_id_field_value) | **PATCH** /example/v1/update/{iddomain}/{id}/{field}/{value} | 
[**post_example_v1_add_iddomain**](ExampleApi.md#post_example_v1_add_iddomain) | **POST** /example/v1/add/{iddomain} | 
[**post_example_v1_query_iddomain_skip_limit**](ExampleApi.md#post_example_v1_query_iddomain_skip_limit) | **POST** /example/v1/query/{iddomain}/{skip}/{limit} | 
[**put_example_v1_update_iddomain_id**](ExampleApi.md#put_example_v1_update_iddomain_id) | **PUT** /example/v1/update/{iddomain}/{id} | 
[**put_example_v1_update_json_iddomain_id**](ExampleApi.md#put_example_v1_update_json_iddomain_id) | **PUT** /example/v1/update_json/{iddomain}/{id} | 


# **delete_example_v1_iddomain_id**
> str delete_example_v1_iddomain_id(iddomain, id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExampleApi()
iddomain = 'iddomain_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.delete_example_v1_iddomain_id(iddomain, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExampleApi->delete_example_v1_iddomain_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iddomain** | **str**|  | 
 **id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_example_v1_info_iddomain_id**
> str get_example_v1_info_iddomain_id(iddomain, id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExampleApi()
iddomain = 'iddomain_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.get_example_v1_info_iddomain_id(iddomain, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExampleApi->get_example_v1_info_iddomain_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iddomain** | **str**|  | 
 **id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_example_v1_update_iddomain_id_field_value**
> str patch_example_v1_update_iddomain_id_field_value(iddomain, id, field, value)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExampleApi()
iddomain = 'iddomain_example' # str | 
id = 'id_example' # str | 
field = 'field_example' # str | 
value = 'value_example' # str | 

try:
    api_response = api_instance.patch_example_v1_update_iddomain_id_field_value(iddomain, id, field, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExampleApi->patch_example_v1_update_iddomain_id_field_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iddomain** | **str**|  | 
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

# **post_example_v1_add_iddomain**
> str post_example_v1_add_iddomain(iddomain, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExampleApi()
iddomain = 'iddomain_example' # str | 
body = swagger_client.Model4() # Model4 |  (optional)

try:
    api_response = api_instance.post_example_v1_add_iddomain(iddomain, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExampleApi->post_example_v1_add_iddomain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iddomain** | **str**|  | 
 **body** | [**Model4**](Model4.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_example_v1_query_iddomain_skip_limit**
> str post_example_v1_query_iddomain_skip_limit(iddomain, skip, limit, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExampleApi()
iddomain = 'iddomain_example' # str | 
skip = 8.14 # float | 
limit = 8.14 # float | 
body = swagger_client.Model9() # Model9 |  (optional)

try:
    api_response = api_instance.post_example_v1_query_iddomain_skip_limit(iddomain, skip, limit, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExampleApi->post_example_v1_query_iddomain_skip_limit: %s\n" % e)
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

# **put_example_v1_update_iddomain_id**
> str put_example_v1_update_iddomain_id(iddomain, id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExampleApi()
iddomain = 'iddomain_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.put_example_v1_update_iddomain_id(iddomain, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExampleApi->put_example_v1_update_iddomain_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iddomain** | **str**|  | 
 **id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_example_v1_update_json_iddomain_id**
> str put_example_v1_update_json_iddomain_id(iddomain, id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExampleApi()
iddomain = 'iddomain_example' # str | 
id = 'id_example' # str | 
body = swagger_client.Model14() # Model14 |  (optional)

try:
    api_response = api_instance.put_example_v1_update_json_iddomain_id(iddomain, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExampleApi->put_example_v1_update_json_iddomain_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iddomain** | **str**|  | 
 **id** | **str**|  | 
 **body** | [**Model14**](Model14.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

