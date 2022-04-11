import easyargs

import json
import sys

import requests
from exitstatus import ExitStatus

global nb_total_tests
global nb_test_ran, nb_test_passed, nb_test_failed, nb_test_skipped
global test_final_status
global status_passed, status_failed, status_skipped

status_passed = "🟢"
status_skipped = "🟡"
status_failed = "🔴"


def get_nb_tests(url, header, endpoints, specific_endpoints):
    nb_total_tests = 0
    for path, details  in endpoints['paths'].items():
        if specific_endpoints:
            if path in specific_endpoints:
                nb_total_tests += get_nb_models(url, path, header)
        else:
            nb_total_tests += get_nb_models(url, path, header)

    return nb_total_tests

def get_nb_models(url, path, header):
    response = requests.get(f'{url}{path}', headers=header)
    models = response.json()
    return len(models)

def perform_test(details, url, header, path, skip_when_failed):
    global nb_test_ran, nb_test_passed, nb_test_failed, nb_test_skipped
    global test_final_status
    global status_passed, status_failed, status_skipped
    global nb_total_tests

    tag = details['get']['tags'][0]
    
    response = requests.get(f'{url}{path}', headers=header)
    models = response.json()
    
    for model in models:
        input, output, task = details['post']['tags'][0].split('.')
        status = ""

        if input == 'image':
            params = (
                ('model', model),
            )
            files = {
                'image': ('test.jpg', open('test.jpg', 'rb')),
            }

            response = requests.post(f'{url}{path}',  headers=header, params=params, files=files)
            
            
            if response.status_code == 200:
                nb_test_passed += 1
                status = status_passed
                
            else:
                nb_test_failed += 1
                status = status_failed
                test_final_status = ExitStatus.failure
                
        elif input == 'text':
            params = [
                ('model', model),
            ]

            for parameter in details['post']['parameters']:
                if parameter['schema']['title'] != 'Model':
                    params.append((parameter['schema']['title'], parameter['schema']['default']))

            params = tuple(params)
            response = requests.post(f'{url}{path}',  headers=header, params=params)

            if response.status_code == 200:
                status = status_passed
                nb_test_passed += 1
                
            else:
                status = status_failed
                nb_test_failed += 1
                test_final_status = ExitStatus.failure
                
        nb_test_ran += 1
        
        progress = round((nb_test_ran / nb_total_tests)*100, 2)
        print(f"|  |__ {status} {model} ({progress}%)  <{response.status_code}>")
        if skip_when_failed:
            if status == status_failed:
                sys.exit(status_failed)
    print("|")


@easyargs
def main(url, bearer_token='', specific_endpoints=None, skip_when_failed=True, after_endpoint=""):
    if specific_endpoints:
        specific_endpoints = specific_endpoints.split(',')
    else:
        specific_endpoints = []
    
    header = {'Authorization': 'Bearer ' + bearer_token}
    response = requests.get(f'{url}/openapi.json', headers=header)
    endpoints = response.json()

    print()
    print(f"Testing endpoints")
    print()

    global nb_total_tests, nb_test_ran, nb_test_passed, nb_test_failed, nb_test_skipped
    global test_final_status
    
    nb_test_skipped = 0
    nb_test_passed = 0
    nb_test_failed = 0
    nb_test_ran = 0
    nb_total_tests = get_nb_tests(url, header, endpoints, specific_endpoints)

    after_endpoint_continue = False
    test_final_status = ExitStatus.success
    for path, details  in endpoints['paths'].items():
        print(f"|__ {path}")
        if specific_endpoints:
            if path in specific_endpoints:
                perform_test(details, url, header, path, skip_when_failed)
                nb_test_ran += 1

            elif after_endpoint != "":
                if path in after_endpoint:
                    after_endpoint_continue = True
                    
                if after_endpoint_continue:
                    perform_test(details, url, header, path, skip_when_failed)
                    nb_test_ran += 1
                else:
                    print(f"|  |__ {status_skipped}  <Skipped>")
                    print(f"|")
                    nb_test_skipped += 1

            else:
                print(f"|  |__ {status_skipped}  <Skipped>")
                print(f"|")
                nb_test_skipped += 1

        elif after_endpoint != "":
            if path in after_endpoint:
                 after_endpoint_continue = True
                    
            if after_endpoint_continue:
                perform_test(details, url, header, path, skip_when_failed)
                nb_test_ran += 1
            else:
                print(f"|  |__ {status_skipped}  <Skipped>")
                print(f"|")
                nb_test_skipped += 1
        else:
            perform_test(details, url, header, path, skip_when_failed)
            nb_test_ran += 1

    if test_final_status == ExitStatus.success:
        str_final_status = "Success"
    else:
        str_final_status = "Failure"
    print(f"""
    Final status: {str_final_status}
    Test Passed: {nb_test_passed}/{nb_total_tests} ({round((nb_test_passed / nb_total_tests)*100, 2)}%)
    Test Failed: {nb_test_failed}/{nb_total_tests}  ({round((nb_test_failed / nb_total_tests)*100, 2)}%)
    Test Skipped: {nb_test_skipped}
    """)
    sys.exit(test_final_status)

if __name__ == '__main__':
    main()
