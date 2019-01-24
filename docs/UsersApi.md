# swagger_client.UsersApi

All URIs are relative to *http://localhost:8003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_users_v1_id**](UsersApi.md#delete_users_v1_id) | **DELETE** /users/v1/{id} | 
[**get_users_v1_info_id**](UsersApi.md#get_users_v1_info_id) | **GET** /users/v1/info/{id} | 
[**patch_users_v1_update_id_field_value**](UsersApi.md#patch_users_v1_update_id_field_value) | **PATCH** /users/v1/update/{id}/{field}/{value} | 
[**post_users_v1_add**](UsersApi.md#post_users_v1_add) | **POST** /users/v1/add | 
[**post_users_v1_login**](UsersApi.md#post_users_v1_login) | **POST** /users/v1/login | 
[**post_users_v1_query_skip_limit**](UsersApi.md#post_users_v1_query_skip_limit) | **POST** /users/v1/query/{skip}/{limit} | 
[**post_users_v1_reset_password_token**](UsersApi.md#post_users_v1_reset_password_token) | **POST** /users/v1/reset_password/{token} | 
[**post_users_v1_send_password_reminder_email**](UsersApi.md#post_users_v1_send_password_reminder_email) | **POST** /users/v1/send_password_reminder/{email} | 
[**put_users_v1_update_id**](UsersApi.md#put_users_v1_update_id) | **PUT** /users/v1/update/{id} | 


# **delete_users_v1_id**
> str delete_users_v1_id(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.delete_users_v1_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_users_v1_id: %s\n" % e)
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

# **get_users_v1_info_id**
> str get_users_v1_info_id(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.get_users_v1_info_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_v1_info_id: %s\n" % e)
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

# **patch_users_v1_update_id_field_value**
> str patch_users_v1_update_id_field_value(id, field, value)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | 
field = 'field_example' # str | 
value = 'value_example' # str | 

try:
    api_response = api_instance.patch_users_v1_update_id_field_value(id, field, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->patch_users_v1_update_id_field_value: %s\n" % e)
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

# **post_users_v1_add**
> str post_users_v1_add(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.Model2() # Model2 |  (optional)

try:
    api_response = api_instance.post_users_v1_add(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_users_v1_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Model2**](Model2.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_v1_login**
> str post_users_v1_login(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.Model3() # Model3 |  (optional)

try:
    api_response = api_instance.post_users_v1_login(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_users_v1_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Model3**](Model3.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_v1_query_skip_limit**
> str post_users_v1_query_skip_limit(skip, limit, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
skip = 8.14 # float | 
limit = 8.14 # float | 
body = swagger_client.Model12() # Model12 |  (optional)

try:
    api_response = api_instance.post_users_v1_query_skip_limit(skip, limit, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_users_v1_query_skip_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **float**|  | 
 **limit** | **float**|  | 
 **body** | [**Model12**](Model12.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_v1_reset_password_token**
> str post_users_v1_reset_password_token(token, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
token = 'token_example' # str | 
body = swagger_client.Model8() # Model8 |  (optional)

try:
    api_response = api_instance.post_users_v1_reset_password_token(token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_users_v1_reset_password_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **body** | [**Model8**](Model8.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_v1_send_password_reminder_email**
> str post_users_v1_send_password_reminder_email(email)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
email = 'email_example' # str | 

try:
    api_response = api_instance.post_users_v1_send_password_reminder_email(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_users_v1_send_password_reminder_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_users_v1_update_id**
> str put_users_v1_update_id(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | 
body = swagger_client.Model13() # Model13 |  (optional)

try:
    api_response = api_instance.put_users_v1_update_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->put_users_v1_update_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Model13**](Model13.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

