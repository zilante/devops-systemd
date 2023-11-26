from __future__ import print_function
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import logging


logging.basicConfig(level=logging.DEBUG)


def run_client():
    while True:
        # create an instance of the API class
        configuration = None
        api_instance = swagger_client.ControllerApi(swagger_client.ApiClient(configuration))
        body = swagger_client.SockRequest(color="color", cotton_part="10", quantity="3") # SockRequest | 

        try:
            api_response = api_instance.add_socks(body)
            logging.info(api_response)
        except ApiException as e:
            api_instance.close()
            logging.info("Exception when calling ControllerApi->add_socks: %s\n" % e)

            raise e

        color = "color" # str | 
        operation = "lessThan" # str | 
        cotton_part = 56 # int | 

        try:
            api_response = api_instance.get_sock_quantity(color, operation, cotton_part)
            logging.info(api_response)
        except ApiException as e:
            api_instance.close()
            logging.info("Exception when calling ControllerApi->get_sock_quantity: %s\n" % e)

            raise e 

        try:
            api_response = api_instance.delete_socks(body)
            logging.info(api_response)
        except ApiException as e:
            api_instance.close()
            logging.info("Exception when calling ControllerApi->delete_socks: %s\n" % e)

            raise e 


if __name__ == "__main__":
    run_client()
