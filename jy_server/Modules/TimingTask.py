import time

import requests
from test_server.data.sql import sql_select
from test_server.utils.responseJSON import responseJSON_1, responseJSON_0, responseJSON


def timingTask(time_sleep):
    my_invite_code = '7D32EFAA378F96A3'
    url = "http://app.juyuanpark.com/api/user.ashx"
    getMaxId = sql_select('SELECT MAX(id) FROM biz_user')[0][0]
    while True:
        time.sleep(time_sleep)
        sql = '''
            SELECT
             TOP 1 invite_code ,id ,sex,token 
            FROM
             [dbo].[biz_user] 
            WHERE
             ( SELECT PATINDEX( '%[^0-9]%', invite_code ) ) = '0'
              AND LEN(invite_code) =16  AND id > {} and  ORDER BY id DESC;
        '''.format(getMaxId)
        new_invite_code = sql_select(sql)
        if new_invite_code == []:
            print('没有新的用户进入！')
            continue
        invite_code = new_invite_code[0][0]
        user_id = new_invite_code[0][1]
        sex = new_invite_code[0][2]
        token = new_invite_code[0][3]
        getMaxId = user_id
        print('用户invite_code', invite_code)
        print('用户user_id', user_id)
        print('用户sex', sex)
        print('用户token', token)
        payload = 'target=invite_code&user_id={}&invite_code={}&token={}'.format(user_id, my_invite_code, token)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        print(payload)
        # response = requests.request("POST", url, headers=headers, table_s=payload)
        # return response

# if __name__ == '__main__':
#     timingTask(10)
payload = 'target=invite_code&user_id=140088&invite_code=7D32EFAA378F96A3&token=98cec39350b74504a6bba30799e0dac5'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
print(payload)
url = "http://app.juyuanpark.com//api/user.ashx"
response = requests.request("POST", url, headers=headers, data=payload)
print(response)