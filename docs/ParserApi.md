# swagger_client.ParserApi

All URIs are relative to *http://localhost:8003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_parser_v1_rule_idrule**](ParserApi.md#post_parser_v1_rule_idrule) | **POST** /parser/v1/rule/{idrule} | 


# **post_parser_v1_rule_idrule**
> str post_parser_v1_rule_idrule()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ParserApi()

try:
    api_response = api_instance.post_parser_v1_rule_idrule()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParserApi->post_parser_v1_rule_idrule: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

