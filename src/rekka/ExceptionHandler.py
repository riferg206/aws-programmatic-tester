import json


def raise_error(error_type, message, aws_request_id):
    response = {
        'errorType': error_type,
        'message': message,
        'awsRequestId': aws_request_id
    }
    raise Exception(json.dumps(response))
