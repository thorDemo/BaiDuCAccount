# -*-coding:utf-8-*-
from mylib.baidu_add_site import add_random_site
from mylib.baidu_delete_site import delete_all_site
import time

cookie_file = open('config/cookies.txt')
cookie = ''
for line in cookie_file:
    cookie = line
cookie = 'PSTM=1570088456; BIDUPSID=D4E03B64E01845115409BD57959D67A1; BAIDUID=45E9A9042C9C71369DD39A9E2E13699B:FG=1; __cas__st__=NLI; __cas__id__=0; Hm_lvt_6f6d5bc386878a651cb8c9e1b4a3379a=1570088299,1570425031,1570872925; lastIdentity=PassUserIdentity; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=7; pgv_pvi=7044786176; pgv_si=s88735744; H_PS_PSSID=1445_21121_20697_29567_29221_26350; BDUSS=lhmVkFROTRyR01Xa0otakt0cDJzRnZRTzRNeWVISDkwajRtOG1nNGhwMjR1c3RkRUFBQUFBJCQAAAAAAAAAAAEAAAB-nCSeAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALgtpF24LaRdT; SITEMAPSESSID=5048qs4vb6vcph9k31at0593k5; Hm_lpvt_6f6d5bc386878a651cb8c9e1b4a3379a=1571040880'
for x in range(1000, 3700, 10):
    while True:
        result = add_random_site('www.aienao.com', x, cookie)
        if result:
            print('添加成功')
            break
        # print(result)
        time.sleep(6)
# print('=')
# result = delete_all_site('www.aienao.com', cookie)
# print(result)