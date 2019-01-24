# swagger_client.DomainApi

All URIs are relative to *http://localhost:8003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_domain_v1_id**](DomainApi.md#delete_domain_v1_id) | **DELETE** /domain/v1/{id} | 
[**get_domain_v1_info_id**](DomainApi.md#get_domain_v1_info_id) | **GET** /domain/v1/info/{id} | 
[**patch_domain_v1_update_id_field_value**](DomainApi.md#patch_domain_v1_update_id_field_value) | **PATCH** /domain/v1/update/{id}/{field}/{value} | 
[**post_domain_v1_add**](DomainApi.md#post_domain_v1_add) | **POST** /domain/v1/add | 
[**post_domain_v1_query_skip_limit**](DomainApi.md#post_domain_v1_query_skip_limit) | **POST** /domain/v1/query/{skip}/{limit} | 
[**put_domain_v1_update_id**](DomainApi.md#put_domain_v1_update_id) | **PUT** /domain/v1/update/{id} | 


# **delete_domain_v1_id**
> str delete_domain_v1_id(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.delete_domain_v1_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->delete_domain_v1_id: %s\n" % e)
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

# **get_domain_v1_info_id**
> str get_domain_v1_info_id(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.get_domain_v1_info_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->get_domain_v1_info_id: %s\n" % e)
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

# **patch_domain_v1_update_id_field_value**
> str patch_domain_v1_update_id_field_value(id, field, value)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainApi()
id = 'id_example' # str | 
field = 'field_example' # str | 
value = 'value_example' # str | 

try:
    api_response = api_instance.patch_domain_v1_update_id_field_value(id, field, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->patch_domain_v1_update_id_field_value: %s\n" % e)
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

# **post_domain_v1_add**
> str post_domain_v1_add(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainApi()
body = swagger_client.Model1() # Model1 |  (optional)

try:
    api_response = api_instance.post_domain_v1_add(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->post_domain_v1_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Model1**](Model1.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_domain_v1_query_skip_limit**
> str post_domain_v1_query_skip_limit(skip, limit, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainApi()
skip = 8.14 # float | 
limit = 8.14 # float | 
body = swagger_client.Model9() # Model9 |  (optional)

try:
    api_response = api_instance.post_domain_v1_query_skip_limit(skip, limit, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->post_domain_v1_query_skip_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **put_domain_v1_update_id**
> str put_domain_v1_update_id(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainApi()
id = 'id_example' # str | 
body = swagger_client.Model1() # Model1 |  (optional)

try:
    api_response = api_instance.put_domain_v1_update_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->put_domain_v1_update_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Model1**](Model1.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

