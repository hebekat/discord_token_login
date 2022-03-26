#!/usr/local/bin/python3
from selenium import webdriver
from selenium.webdriver import Firefox
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests

tokens = [
'OTMxODI5Njk5NDY5MDA4OTA2.YeKIkQ.XDMa04Ux-qB8WNxERS3wv7BoDtE',
'OTMxODI5ODg5MzI4MzY5NzA1.YeKI5g._m7t50cb2bCtO_g1WUmBm2SnYY8',
'OTMxODI5NzI2NjAxOTUzMzAy.YeKIqw.SlQG0GAFLJSVmR_oiB2XbgMIuJI',
'OTMxODI5ODk1NjgyNzQ0MzIx.YeKI3g.HLotYHoFXINwSoQgEc6VXLU3Rmc',
'OTMxODMwMTA1MjE3NTg1MTg0.YeKJDA.vyo64dAMqxpcNXmycBcD1Uqx7oI',
'OTMxODI5ODg3MDU5MjYzNTE4.YeKI4A.FjZaoNoMYTxecUCbtkts4Hnv428',
'OTMxODI5NzA3NzkwNDg3NTgy.YeKIzQ.eqXJIqbPWgrQBS4i6TqFGjU3ym0',
'OTMxODMwMTIxNzEzNzk1MTEz.YeKJHg.E-8Mqlqn2NIAeirKEZ9vyInBaFk',
'OTMxODI1NDQzMjAyNTY0MTI2.YeKEsQ.4xrDrKX56aM2lATH5LnTE60b930',
'OTMxODMwMDk4MzgwODczNzM4.YeKJAA.Pg5hzxvFlB_UhUQ--wHYTMTQwkY',
'OTMxODMwMDk2MTkxNDMwNjc2.YeKJBg.0f3Q5xlNQN3pPnw5nr09hlHobWQ',
'OTMxODMwMTA4MTA3NDY0NzI0.YeKJBQ.YonVrtoM6ShQygPLiJ_EpiaYSxY',
'OTMxODMwNjAyNjI0Mjg2NzYw.YeKJaw.Glmw8nNiwu4srw0J45y65b9YJfk',
'OTMxODMwNTczMTkyODcxOTU4.YeKJdQ.R0c5_9PZ8rTr_ZlxIq9Zz8aTMLc',
'OTMxODMwMTA3MjM1MDI5MDEy.YeKJGA.0pFUQjE0HGTBJ02DHofCjA2ILSM',
'OTMxODMxMjI5NTY3ODY4OTY4.YeKKHw.EC8SDVgNIzjog3qs8bJCIBtA_zU',
'OTMxODMwMDgyNTA5NjIzMzA4.YeKJEQ.XAKsVrp-6ipDzYU3H3ASVEQ94hU',
'OTMxODMxMjM5MzYxNTkzMzc2.YeKKFQ.gxNTCkniDW2z3iUHiM8gPKXc_kY',
'OTMxODMxMjA0NjI0MzY3NjY3.YeKKIA.Wtr8pGXB3_8MPMijeYRUC47mcKk',
'OTMxODMxMjM3ODY4MzkyNDg4.YeKKIQ.QL8uO91IWQMDKHn6Mxb8uB0hlPc',
'OTMxODMwMTI2MDMzOTAzNjQ3.YeKJDw.VSBB95ANZ6XvSdncyx6r7rMCTf0',
'OTMxODMwNTgzNzk2MDY0MjU2.YeKJgw.0JYmul0GpI8J5PpaHq9RLVgFI-o',
'OTMxODMxMjU0ODIxNzgxNTY0.YeKKIw.jry688VRoTCPuDe8fBaXXdd46og',
'OTMxODMxMjMwNTQ1MTU0MDU4.YeKKJA.fxs8XpSAy4RYL0j7PWE4c2E8zDw',
'OTMxODMxMzA1OTA4NDIwNjc4.YeKKKw.45zpQETVoRr6xHJUEgVPUZ9qA-s',
'OTMxODMxMjEyNzA2Nzg3MzM4.YeKKHw.sgSMpUHumFRUBsgzvpr9CujplyY',
'OTMxODMxMzA4MTE4ODE4ODQ2.YeKKMA.5WXdn1a2Bu9VWZyxJbSfqKGSsDM',
'OTMxODMxMjA5NzM3MjIwMTA3.YeKKKA.yICK5_8jtwy-gFPzpN2wZuTDeLk',
'OTMxODM3MTAxMjI0Mzg2NTcw.YeKPqA.7I5Lr1R2XBXOniIvwWuKoX1sXpk',
'OTMxODMxNTU3MzIzMzc4Njk4.YeKKWw.QuiT7GoKlX1sGehUG8DpO2GbNcU',
'OTMxODMxNTQ1MzE5MjY4Mzgz.YeKKag.3SWre_Z4ZkVf9-jBd8fUzojZbYw',
'OTMxODMxNTcwMTI0Mzc0MDU3.YeKKUA.4v71KnVMOsbY2zcGRGkaxE6vr-8'
];

def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

def join(token, server_invite):
    header = {"authorization": token}
    r = requests.post("https://discord.com/api/v9/invites/hPMPCGxU", headers=header)
    print(r)
    
profile_path = r'/Volumes/Storage/cache/tohebeka/Library/Application Support/Firefox/Profiles/08eoij8h.default'
options=Options()
options.set_preference('profile', profile_path)
options.set_preference("browser.privatebrowsing.autostart", True)

script = open("./tokens.js").read()

for x in range(25, 30):
    driver = Firefox(options=options)
    driver.get("https://discord.com/login")
    script = replace_str_index(script, len(script) - 4, x)
    driver.execute_script(script)
    # time.sleep(10)
    # join(tokens[x], "https://discord.com/invite/hPMPCGxU")

    # driver.get("https://discord.com/invite/hPMPCGxU")
    # time.sleep(3)
    # driver.find_elements(By.XPATH, '//button')[0].click();


