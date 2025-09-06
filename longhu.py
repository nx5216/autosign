"""
小程序龙湖天街
https://gw2c-hw-open.longfor.com 获取请求头 token 的值注：lmToken跟X-LF-UserToken都行
环境变量 lhtj="phone#lmToken"
cron: 0 5 * * *
"""
#import notify
import requests, json, re, os, sys, time, random, datetime


token = "6f052f64b1854135bedd93e32256af4d"
session = requests.session()
#---------------------主代码区块---------------------

def info(token):
    header = {
        "Accept": "*/*",
        "Content-Type": "application/json",
        "lmToken": token,
        "X-Gaia-Api-Key": "98717e7a-a039-46af-8143-be7558a089c0",
        "X-LF-Api-Version": "v1_11_0",
        "X-LF-Bucode": "C20400",
        "X-LF-Channel": "C2",
        "xweb_xhr": "1",
        "Host": "gw2c-hw-open.longfor.com",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    try:
        url = 'https://gw2c-hw-open.longfor.com/supera/member/api/bff/pages/v1_11_0/v1/user-info'
        response = session.get(url=url, headers=header).json()
        if response['code'] == "0000":
            level = response['data']['level']
            growthValue = response['data']['growthValue']
            nextLevelGrowthValue = response['data']['nextLevelGrowthValue']
            url = 'https://gw2c-hw-open.longfor.com/supera/member/api/bff/pages/v1_11_0/v2/user-lz-balance'
            response = session.get(url=url, headers=header).json()
            #print(response['data'])
            balance = response['data']['balance']
            expiringLz = response['data']['expiringLz']
            print(f"账户：{balance}珑珠")
            print(f"v{level}成长值：{growthValue}点")
        else:
            print(response)
    except Exception as e:
        print(e)

def sign(token):
    header = {
        "token": token,
        "X-LF-UserToken": token,
        "Host": "gw2c-hw-open.longfor.com",
        "Connection": "keep-alive",
        "X-LF-Bu-Code": "C20400",
        "X-GAIA-API-KEY": "c06753f1-3e68-437d-b592-b94656ea5517",
        "X-LF-DXRisk-Source": "5",
        "X-LF-DXRisk-Captcha-Token": "undefined",
        "X-LF-DXRisk-Token": "1",
        "X-LF-Channel": "C2",
        "Origin": "https://longzhu.longfor.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b13)XWEB/11581",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    try:
        url = 'https://gw2c-hw-open.longfor.com/lmarketing-task-api-mvc-prod/openapi/task/v1/signature/clock'
        response = session.post(url=url, headers=header, json={"activity_no":"11111111111686241863606037740000"}).json()
        if response['code'] == "0000":
            if response['data']['is_popup'] == 1:
                for i in response['data']['reward_info']:
                    print(i)
            elif response['data']['is_popup'] == 0:
                print(f"签到：已签到")
        elif "火爆" in response['message']:
            print(f"签到火爆")
            return
        elif "未登录" in response['message']:
            print(f"token过期了")
            return
    except Exception as e:
        print(e)

def lotterysign(token):
    header = {
        "Host": "gw2c-hw-open.longfor.com",
        "Connection": "keep-alive",
        "X-GAIA-API-KEY": "2f9e3889-91d9-4684-8ff5-24d881438eaf",
        "authtoken": token,
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "X-LF-DXRisk-Source": "5",
        "bucode": "C20400",
        "channel": "C2",
        "X-LF-DXRisk-Token": "1",
        "Origin": "https://llt.longfor.com",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    try:
        url = 'https://gw2c-hw-open.longfor.com/llt-gateway-prod/api/v1/activity/auth/lottery/sign'
        component_no = "CK09N57J55N28XF0"
        activity_no = "AP25W011M67ROK5Z"
        response = session.post(url=url, headers=header, json={"component_no":component_no,"activity_no":activity_no}).json()
        # print(response)
        if response['code'] == "0000":
            print(f"抽奖任务：完成")
        elif "已签到" in response['message']:
            print(f"抽奖任务：完成")
        elif "火爆" in response['message']:
            print(f"抽奖火爆")
            return
        url = f'https://gw2c-hw-open.longfor.com/llt-gateway-prod/api/v1/activity/auth/lottery/chance?component_no={component_no}&activity_no={activity_no}'
        response = session.get(url=url, headers=header,).json()
        if response['code'] == "0000":
            chance = response['data']["chance"]
            print(f"抽奖次数：{chance}次")
            if chance > 0:
                url = 'https://gw2c-hw-open.longfor.com/llt-gateway-prod/api/v1/activity/auth/lottery/click'
                response = session.post(url=url, headers=header,json={"component_no":component_no,"activity_no":activity_no,"batch_no":""}).json()
                if response['code'] == "0000":
                    print(f"抽奖获得：{response['data']}")
                    reward_num = response["data"]["reward_num"]
                    prize_name = response["data"]["prize_name"]

    except Exception as e:
        print(e)

def main():
    try:
        sign(token)
        lotterysign(token)
        info(token)
        time.sleep(random.randint(1, 2))
    except Exception as e:
        print(e)
    print(f'\n-----------执 行  结 束-----------')

if __name__ == '__main__':
    main()