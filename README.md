# rideshare_auto
driver.implicitly_wait(10)

screenSize = driver.get_window_size()
screenW = screenSize['width']
screenH = screenSize['height']
x =  screenW/2
y1 = int(screenH*0.8)
y2 = int(screenH*0.4)
avlst=[]
navlst=[]
for i in range(100):
    els4= driver.find_elements(by=AppiumBy.CLASS_NAME,value="android.view.View")
    for ele in els4:
        name=ele.id
        title=ele.text
        if name in avlst:
            continue
        avlst.append(title)
        if title == '<font color=&apos;#999999&apos;>以下服务商附近无车<font/>':
            break
    if title == '<font color=&apos;#999999&apos;>以下服务商附近无车<font/>':
        break
    driver.swipe(start_x=x, start_y=y1, end_x=x, end_y=y2, duration=800)

#还缺很多
companylist = ['聚的出租车','聚的新出租','鞍马出行','优e出行','安安用车','搭顺出行','风韵出行','携华出行','乐拼用车','及时用车','365约车','聚优出租',
'悦行出行','优e出租','T3特选','平凉出租','斑马快跑','62580约车','欧亚出行','雷利出行','团子出行','金张掖出租','首汽约车','呼我出行','牦牛出租','T3出行','鑫钜专车','快来车','捎点宝出行','腾飞出行','喜行约车','妥妥E行','汇迪出租车','曹操出行','小牛快跑','任行专车','放心出行','吉汽约车','陕水务出行','仟嘉出租','全在用车','众车出行','Uto悠途','900出行','招招出行','老兵约车','麦田商旅','五福出租','阳光出行','陇南出租','逸乘出行','江南出行','牦牛约车','易至出行','顺道出行','江西出租','小巷约车','全民GO','及时出行','车马上到','罗伦士出行','小马出行','蓉橙出行','叮叮出行','幸福专车','动力出行','大象出行','橄榄绿出行','神州专车','飞嘀打车','旅程约车','途途行','飞马出行','兰州出租','享道出行特惠','麦巴出行','犇犇出行','蔷薇出行','速的出行','创业者出行','天府行','云南出行','AA出行','铁航专车','燕都出行','犇犇约车','中交出行','迪尔出行','e族出行','玖玖约车','哈喽优行','天津出行','快客出行','旅程出租','J刻出行','易约出行','蛋卷出租','5U出行','博度出行','巴运出行','株洲出租车','来了出行','易通出行','星徽出行','鞍山出租','甘薯出行','易达出行','妥妥出租','好久来''添猫出行','漳州出租','日初出行','闽东出租','三秦出行','国民初行','普惠约车','博约出行','元翔专车','帮邦行','中军出行','腾飞出租','南京出租车','湘潭出租','享约车','有滴旅程','民途出行','北方出行','云能行','昆明打车','新月出租','渔阳出行','北汽出租','北京的士','金银建出行','旅程易到','大雁出行','纳溪出租','泸州出租','大国出行','温州出租','海厚出租','大众约车','环旅出行','大众出租','众行特惠','方舟行','悦道出行','桔子出行','鹰明出行','申程出行','徐州全顺','客多多出行','绍兴出租','飞豹出行','K9用车','开心出行','如一出行','双创打车','海后出租','金宇出租','黄金出行','三合e行','众至用车','天津出租','首邀出行','惠州出租','连云港出租','淮安出行','有鹏出行','深圳出租','如祺出行','合易接送','百靓出行','中山出租车''如嘀出行','任行出租','国泰出租','新动出行','及客出行','吉唐出租','国泰出行','幸福千万家','重庆出租','易达专车','富安出行','智体行','优讯快车','星城出租','和行约车','和行神州','摩登出行','免佣联盟精选司机','青岛出租','万行出租','惠普约车','麒麟优车','吉刻上车','沈城出租','快马嘟嘟','吉林出租','旗妙出行','众迪出租','联友出行','三合出行','普惠出行','神骅飞鹏','江西出行','果橙打车','云途出行','安易出行','美程出行','成都出租','深驾出行']

a=0
longlist=[]    #longlist包括经济型中的所有元素
for i in range(len(avlst)):
    if avlst[i]=='全选经济':
        a+=1
    if a==2:
        longlist.append(avlst[i])
    if avlst[i]=='<font color=&apos;#999999&apos;>以下服务商附近无车<font/>':
        b=i
        break
#前面能输出经济型框框里所有内容
zidian={}
for i in range(len(longlist)):
    if longlist[i] in companylist:
        c=longlist[i:]
        for j in range(len(c)):
            if c[j] ==' 元':
                zidian[c[0]]=c[1:1+j]
                break
print( zidian )

    
    
    
#点击查看服务商
driver.implicitly_wait(10)
xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.View'
element = driver.find_element(by=AppiumBy.XPATH, value=xpath)
actions.move_to_element(element)
actions.click()
actions.perform()

    
    
for i in range(4):
    els5= driver.find_elements(by=AppiumBy.CLASS_NAME,value="android.view.View") #classname不对
    for ele in els5:
       name=ele.id
       title=ele.text
       if name in navlst:
           continue
       navlst.append(title)
    driver.swipe(start_x=x, start_y=y1, end_x=x, end_y=y2, duration=800)

a=0
shortlist=[]
for i in range(len(navlst)):
    if navlst[i]=='以下服务商附近车辆较少，同时呼叫应答概率低':
        a+=1
    if  a==1:
        for j in range(len(navlst[i:])):
            shortlist.append(navlst[i+j])
            if navlst[i+j]=='现在':
                break
        break
    
zidian={}
for i in range(len(shortlist)):
    if shortlist[i] in companylist:
        d=shortlist[i:]
        for j in range(len(d)):
            if d[j] ==' 元':
                zidian[d[0]]=d[1:j+1]
                break
        continue
print(zidian)
