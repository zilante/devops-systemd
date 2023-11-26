# swagger_client.ControllerApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_socks**](ControllerApi.md#add_socks) | **POST** /api/socks/income | 
[**delete_socks**](ControllerApi.md#delete_socks) | **POST** /api/socks/outcome | 
[**get_sock_quantity**](ControllerApi.md#get_sock_quantity) | **GET** /api/socks | 

# **add_socks**
> str add_socks(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ControllerApi()
body = swagger_client.SockRequest() # SockRequest | 

try:
    api_response = api_instance.add_socks(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControllerApi->add_socks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SockRequest**](SockRequest.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_socks**
> str delete_socks(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ControllerApi()
body = swagger_client.SockRequest() # SockRequest | 

try:
    api_response = api_instance.delete_socks(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControllerApi->delete_socks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SockRequest**](SockRequest.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sock_quantity**
> str get_sock_quantity(color, operation, cotton_part)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ControllerApi()
color = 'color_example' # str | 
operation = 'operation_example' # str | 
cotton_part = 56 # int | 

try:
    api_response = api_instance.get_sock_quantity(color, operation, cotton_part)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControllerApi->get_sock_quantity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **color** | **str**|  | 
 **operation** | **str**|  | 
 **cotton_part** | **int**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

