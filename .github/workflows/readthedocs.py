"""
Trigger ReadTheDocs documentation build and check response for confirmation
"""

import os
import time
import requests

URL = 'https://readthedocs.org/api/v3/projects/pyreportjasper'
TOKEN = os.getenv('READTHEDOCS_TOKEN')
HEADERS = {
    'Authorization': f'Token {TOKEN}',
    'Content-Length': '0',
    }


def build_status(build_id: str) -> str:
    """
    Use ReadTheDocs API to check build status until either failed or succeeds. The function checks the status in 30s
    intervals. Stop process after max. 3min.

    Response field state - code can have the following values: triggered, cloning, installing, building, finished and
    failed (check TBD)
    """

    max_min = 3
    status = 'triggered'

    i = 0
    while True:
        i += 1
        time.sleep(30)

        response = requests.get(f'{URL}/builds/{build_id}/', headers=HEADERS)
        response = response.json()

        if response['success'] is True:
            status = 'finished'
            break
        elif response['success'] is False:
            status = 'failed'
            break

        if i == 2*max_min:
            break

    return status


def main():
    response = requests.post(f'{URL}/versions/latest/builds/', headers=HEADERS)
    response = response.json()

    if response['triggered']:
        print('ReadTheDocs build successfully triggered.')
        print(f"Build id: {response['build']['id']}")
        print(f"Branch: {response['version']['identifier']}")
        print(f"Version: {response['build']['version']}")

        build_id = response['build']['id']
        status = build_status(build_id)

        if status == 'finished':
            print('ReadTheDocs build successfully finished.')
            return 0
        elif status == 'triggered':
            print('ReadTheDocs build still ongoing... Please check manually.')
            return 0
        elif status == 'failed':
            print('ReadTheDocs build failed.')
            return 1
    else:
        print('ReadTheDocs build triggering failed.')
        return 1


if __name__ == '__main__':
    main()