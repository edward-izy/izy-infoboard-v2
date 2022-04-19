from datetime import datetime


def message(status, message):
    response_object = {"status": status, "message": message}
    return response_object


def validation_error(status, errors):
    response_object = {"status": status, "errors": errors}

    return response_object


def err_resp(msg, reason, code):
    err = message(False, msg)
    err["error_reason"] = reason
    return err, code


def internal_err_resp():
    err = message(False, "Something went wrong during the process!")
    err["error_reason"] = "server_error"
    return err, 500


def success(message="No message"):
    return {"status": 'Success', "reason": message}, 200


def input_validation_error(reason="Unknown", code=400):
    return {'status': 'Input Validation Failed', 'reason': reason}, code


def error_response(reason="Unknown", code=400):
    return {'status': 'Error', 'reason': reason}, code


def internal_error_response(reason="Unknown"):
    return {'status': 'Internal Error', 'reason': reason}, 500


def duplicate_error_response(reason="Unknown"):
    return {'status': 'Unique Violation Error', 'reason': reason}, 400


def timestamp_program(timestamp_string):
    return datetime.strptime(timestamp_string, '%Y-%m-%d %H:%M:%S.%f')


def timestamp_format(timestamp_object):
    return datetime.strftime(timestamp_object, '%Y-%m-%d %H:%M:%S.%f')
