import os
import re
#ip = subprocess.Popen(['ifconfig','ppp0'],stdout=subprocess.PIPE)
pp = os.popen('ifconfig ppp0')
for i in pp:
    #print i
    ipa = re.compile(r'\sxxx.xxx.xxx.\d+') #xxx 部分是你的vpn地址前三段
    matchs = ipa.findall(i)

localIP= matchs[0]
route_add="route add xxx.xxx.xxx.x %s"%localIP   #xxx部分为添加的被路由地址
route_add1="route add xxx.xxx.xxx.x %s"%localIP
routeadd=[route_add,route_add1]
print localIP
gon=raw_input("input y continue:").strip()
if gon is 'y':
    for i in routeadd:
        os.system(i)
    if os.system(i) == 0:
        print "route add successful"
    else:
       print "sorry,try again"
else:
     print "sorry an error occurred"