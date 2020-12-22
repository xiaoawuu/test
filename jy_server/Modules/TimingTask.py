import time

import requests
from test_server.data.sql import sql_select
from test_server.utils.responseJSON import responseJSON_1, responseJSON_0, responseJSON


def timingTask(time_sleep):
    url = "http://app.juyuanpark.com//api/user.ashx"
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
              AND LEN(invite_code) =16  AND id > {} ORDER BY id DESC;
        '''.format(getMaxId)
        new_invite_code = sql_select(sql)
        if not new_invite_code:
            print('没有新的用户进入！')
            continue
        invite_code = '7D32EFAA378F96A3'
        user_id = new_invite_code[0][1]
        sex = new_invite_code[0][2]
        token = new_invite_code[0][3]

        print('用户invite_code', invite_code)
        print('用户user_id', user_id)
        print('用户sex', sex)
        print('用户token', token)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        if sex == 1:  # 男用户
            print('男性用户注册！')
            is_recharge_record = sql_select('SELECT * FROM biz_order WHERE user_id = {} and status=1;'.format(user_id))
            if not is_recharge_record:
                print('已充值')
                continue
            payload = 'target=invite_code&user_id={}&invite_code={}&token={}'.format(user_id, invite_code, token)
            print(payload)
            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)
            getMaxId = user_id
        elif sex == 2:  # 女性用户
            print('女性用户注册！')
            is_true = sql_select('SELECT * FROM biz_user WHERE is_true = 1 and id = {};'.format(user_id))
            if not is_true:
                print('未认证')
                continue
            url = "http://app.juyuanpark.com//api/invitecode.ashx"
            payload = 'target=modify_invite_code&user_id={}&invite_code={}&token={}'.format(user_id, invite_code, token)
            print(payload)
            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)
            getMaxId = user_id
if __name__ == '__main__':
    timingTask(10)
