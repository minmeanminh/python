
import requests
import getpass
import time

# Login
print('Enter Email or Username: ')
EmailOrUsername = input()
Password = getpass.getpass()


# Get cookies

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryJU1r05JWt0UVc5oj',
    'Origin': 'https://login.matbao.net',
    'Referer': 'https://login.matbao.net/Users/Login?ReturnUrl=%2f',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Microsoft Edge";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

params = {
    'ReturnUrl': 'https://id.matbao.net/',
}

data = '------WebKitFormBoundaryJU1r05JWt0UVc5oj\r\nContent-Disposition: form-data; name="__RequestVerificationToken"\r\n\r\nk3Ilnwy5JvfsDJpHXV-E5tO-gbfej7wvuLL6IOma0OxaqZtp6367HIomMjzr_pZSaIXNeuPNRdXAgXrrjm5W-kvQ3j-qlFye3WOcaq7GQ-o1\r\n------WebKitFormBoundaryJU1r05JWt0UVc5oj\r\nContent-Disposition: form-data; name="EmailOrUsername"\r\n\r\n'+EmailOrUsername+'\r\n------WebKitFormBoundaryJU1r05JWt0UVc5oj\r\nContent-Disposition: form-data; name="Password"\r\n\r\n'+Password+'\r\n------WebKitFormBoundaryJU1r05JWt0UVc5oj\r\nContent-Disposition: form-data; name="__RequestVerificationToken"\r\n\r\nVO5rLlnWZIF5EcLAFySLi8X9EmYWY3eodv2TqtkEvwyD707kXp9YJ02qw6S8PPJux-QyQmM91BjMJR_Yj__f_gXttiHmb-LjIhXg4d5Mnlc1\r\n------WebKitFormBoundaryJU1r05JWt0UVc5oj--\r\n'


session_cookies = requests.Session()
session_cookies.post('https://login.matbao.net/users/login', params=params, headers=headers, data=data)
session_cookies = session_cookies.cookies
session_cookies_dict = session_cookies.get_dict() 
#print(session_cookies_dict)

Cookie_ASP = session_cookies_dict['ASP.NET_SessionId']
Cookie_SubPortal = session_cookies_dict['MBIDSubPortalCookieManage']
Cookie_SingleLoginOn = session_cookies_dict['SingleLoginOn']
Cookie_CodePortal = session_cookies_dict['MBIDCodePortalCookieManage']

print()
print('GET COOKIES!')
print()
print('ASP.NET_SessionId:', Cookie_ASP)
print('MBIDSubPortalCookieManage:', Cookie_SubPortal)
print('SingleLoginOn:', Cookie_SingleLoginOn)
print('MBIDCodePortalCookieManage:', Cookie_CodePortal)

update_cookies = {
    'ASP.NET_SessionId': Cookie_ASP,
    'ShowLetTip': '1',
    'SL_G_WPT_TO': 'en',
    'SL_GWPT_Show_Hide_tmp': '1',
    'SL_wptGlobTipTmp': '1',
    'MBIDSubPortalCookieManage': Cookie_SubPortal,
    'SingleLoginOn': Cookie_SingleLoginOn,
    'MBIDCodePortalCookieManage': Cookie_CodePortal,
}

print()
print('COOKIES UPDATED!')
print()
print(update_cookies)
print()


update_headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'ASP.NET_SessionId=pbx0xo5hhrp3iqk2n2wpl5h1; ShowLetTip=1; SL_G_WPT_TO=en; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; MBIDSubPortalCookieManage=yifqXnisDXrabKFQ4SstmdstlcwHoBKgxBNN2S8R6TanV4oCftiVjKCsOU09J0cmEkhB3e8Er7Ri/i8wMrVNUrqmEWtLZprOrivdRmen3k2/Jpa1LbCqIpNBFJxmh7j3; SingleLoginOn=5F64ED30BC0998FD358C6A7373C0FF54C2F79F97BC67A7825059D18DE489A95837AC80F5B43A2C03F6EF0FB661C840F0B59BFAB846A9353AF801ABB2D963241EE336E3229C23EC168455CC49F7EA53F17B29A7ADABE4B073B8287EC940A53581; MBIDCodePortalCookieManage=Zz+AiWZPpYCJyYjOOqc45l3R/q2phreXjskEEclIzMu/pLCArZJrgV+vIdBmphTV/7TcePT3JPn29/eo8zafgCxOr3nzPGXqabJcJPJN4xCC6JDj4CUR1knEkZzP5FZG',
    'Origin': 'https://manage.matbao.net',
    'Referer': 'https://manage.matbao.net/domains/.vn0066896/detail',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Microsoft Edge";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

# import CSV file. File format: dns_records.csv

import pandas as pd
dns_records = pd.read_csv (r'.\dns_records.csv')
Record_Quantity = len(dns_records)
print('DNS RECORD(S) NEED TO BE UPDATED:',Record_Quantity)
print()

# Update DNS Records
i = 0
while i < Record_Quantity:
    Host = dns_records['Host'][i]
    Type = dns_records['Type'][i]
    Data = dns_records['Data'][i]
    TTL = dns_records['TTL'][i]

    update_data = {
        'actionform': '0',
        'typeupdate': 'REPLACE',
        'domainname': 'alpaca.vn',
        'iddomain': '.vn0066896',
        'name': Host,
        'type': Type,
        'ttl': TTL,
        'ip[]': Data,
        'X-Requested-With': 'XMLHttpRequest',
    }

# def Record_List(n):
#     lst = []
#     for i in range(n+1):
#         lst.append(i)
#     return(lst)

# for i in Record_List(Record_Quantity):
#     print(dns_records['Host'][i])
#     if i == Record_Quantity:
#         break

    update_dns_response = requests.post('https://manage.matbao.net/domains/update-dns/', cookies=update_cookies, headers=update_headers, data=update_data)
    print('DNS RECORD #',i,Host,Data,'UPDATE STATUS: ', update_dns_response, update_dns_response.text)
    print()
    i += 1
else:
    print('ALL DONE!')



time.sleep(10)
