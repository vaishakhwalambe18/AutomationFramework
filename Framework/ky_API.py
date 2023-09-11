class kyAPI:
    # >> > import requests
    # >> > r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    # >> > r.status_code
    # 200
    # >> > r.headers['content-type']
    # 'application/json; charset=utf8'
    # >> > r.encoding
    # 'utf-8'
    # >> > r.text
    # '{"authenticated": true, ...'
    # >> > r.json()
    # {'authenticated': True, ...}
    @staticmethod
    def get_API(endpoint, authType, username, password, specificHeaderData, expectedResponseCode):
        if (authType.lower() == 'basic'):
            auth = HTTPBasicAuth(username, password)

        # if (specificHeaderData.len > 0):
        #     print('update_some_thing')

        response = requests.get(endpoint)
        print(response)
        act_response_code = response.status_code
        assert int(act_response_code) == int(expectedResponseCode)
        pass

        return response
