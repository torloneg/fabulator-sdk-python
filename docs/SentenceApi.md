# swagger_client.SentenceApi

All URIs are relative to *http://localhost:8003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sentence_v1_idrule_id**](SentenceApi.md#delete_sentence_v1_idrule_id) | **DELETE** /sentence/v1/{idrule}/{id} | 
[**get_sentence_v1_info_idrule_id**](SentenceApi.md#get_sentence_v1_info_idrule_id) | **GET** /sentence/v1/info/{idrule}/{id} | 
[**post_sentence_v1_add_idrule**](SentenceApi.md#post_sentence_v1_add_idrule) | **POST** /sentence/v1/add/{idrule} | 
[**put_sentence_v1_update_idrule_id**](SentenceApi.md#put_sentence_v1_update_idrule_id) | **PUT** /sentence/v1/update/{idrule}/{id} | 


# **delete_sentence_v1_idrule_id**
> str delete_sentence_v1_idrule_id(idrule, id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SentenceApi()
idrule = 'idrule_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.delete_sentence_v1_idrule_id(idrule, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SentenceApi->delete_sentence_v1_idrule_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idrule** | **str**|  | 
 **id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sentence_v1_info_idrule_id**
> str get_sentence_v1_info_idrule_id(idrule, id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SentenceApi()
idrule = 'idrule_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.get_sentence_v1_info_idrule_id(idrule, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SentenceApi->get_sentence_v1_info_idrule_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idrule** | **str**|  | 
 **id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sentence_v1_add_idrule**
> str post_sentence_v1_add_idrule(idrule, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SentenceApi()
idrule = 'idrule_example' # str | 
body = swagger_client.Model7() # Model7 |  (optional)

try:
    api_response = api_instance.post_sentence_v1_add_idrule(idrule, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SentenceApi->post_sentence_v1_add_idrule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idrule** | **str**|  | 
 **body** | [**Model7**](Model7.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sentence_v1_update_idrule_id**
> str put_sentence_v1_update_idrule_id(idrule, id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SentenceApi()
idrule = 'idrule_example' # str | 
id = 'id_example' # str | 
body = swagger_client.Model15() # Model15 |  (optional)

try:
    api_response = api_instance.put_sentence_v1_update_idrule_id(idrule, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SentenceApi->put_sentence_v1_update_idrule_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idrule** | **str**|  | 
 **id** | **str**|  | 
 **body** | [**Model15**](Model15.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

