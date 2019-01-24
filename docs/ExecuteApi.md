# swagger_client.ExecuteApi

All URIs are relative to *http://localhost:8003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_execute_v1_local_domain_key**](ExecuteApi.md#post_execute_v1_local_domain_key) | **POST** /execute/v1/local/{domain}/{key} | 
[**post_execute_v1_rule_idrule**](ExecuteApi.md#post_execute_v1_rule_idrule) | **POST** /execute/v1/rule/{idrule} | 
[**post_execute_v1_rule_idrule_example_idexample**](ExecuteApi.md#post_execute_v1_rule_idrule_example_idexample) | **POST** /execute/v1/rule/{idrule}/example/{idexample} | 


# **post_execute_v1_local_domain_key**
> str post_execute_v1_local_domain_key(domain, key, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExecuteApi()
domain = 'domain_example' # str | 
key = 'key_example' # str | 
body = swagger_client.Model5() # Model5 |  (optional)

try:
    api_response = api_instance.post_execute_v1_local_domain_key(domain, key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExecuteApi->post_execute_v1_local_domain_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | 
 **key** | **str**|  | 
 **body** | [**Model5**](Model5.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_execute_v1_rule_idrule**
> str post_execute_v1_rule_idrule(idrule, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExecuteApi()
idrule = 'idrule_example' # str | 
body = swagger_client.Model5() # Model5 |  (optional)

try:
    api_response = api_instance.post_execute_v1_rule_idrule(idrule, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExecuteApi->post_execute_v1_rule_idrule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idrule** | **str**|  | 
 **body** | [**Model5**](Model5.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_execute_v1_rule_idrule_example_idexample**
> str post_execute_v1_rule_idrule_example_idexample(idrule, idexample, idsentence=idsentence)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExecuteApi()
idrule = 'idrule_example' # str | 
idexample = 'idexample_example' # str | 
idsentence = 'idsentence_example' # str |  (optional)

try:
    api_response = api_instance.post_execute_v1_rule_idrule_example_idexample(idrule, idexample, idsentence=idsentence)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExecuteApi->post_execute_v1_rule_idrule_example_idexample: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idrule** | **str**|  | 
 **idexample** | **str**|  | 
 **idsentence** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

