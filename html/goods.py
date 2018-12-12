# -*- coding:utf-8 -*-
# 作业任务：购物车程序
# 实现功能：
# 		1、启动程序后，输入用户名密码后，用户匹配后读取用户信息，如果用户可用余额为0，提醒用户充值，然后打印商品列表
#		2、允许用户根据商品编号购买商品
#		3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
#		4、可随时退出，退出时，打印已购买商品和余额
#		5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示
#		6、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
#		7、允许查询之前的消费记录
# 作业人：张云辉
# 完成日期：2018-10-31

# 定义文本颜色
import ctypes,sys,os,time,getpass,json

  
def input_handle(s):
    if str.isdigit(s):                                                     ###对输入是否是数字进行判断###
        s = int(s)                                                         ###如果输出的是个数字，则转化为整数类型###
    return s

out_handle=ctypes.windll.kernel32.GetStdHandle(-12)
 
def set_text_color(color, handle=out_handle):
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)

def resetColor():
    set_text_color(0x07)
 
def cprint(mess,color):
    if color=='darkblue':
        set_text_color(0x01)
    elif color=='darkgreen':
        set_text_color(0x02)
    elif color=='darkskyblue':
        set_text_color(0x03)
    elif color=='darkred':
        set_text_color(0x04)
    elif color=='darkpink':
        set_text_color(0x05)
    elif color=='darkyellow':
        set_text_color(0x06)
    elif color=='darkwhite':
        set_text_color(0x07)
    elif color=='darkgray':
        set_text_color(0x08)
    elif color=='blue':
        set_text_color(0x09)
    elif color=='green':
        set_text_color(0x0a)
    elif color=='skyblue':
        set_text_color(0x0b)
    elif color=='red':
        set_text_color(0x0c)
    elif color=='pink':
        set_text_color(0x0d)
    elif color=='yellow':
        set_text_color(0x0e)
    elif color=='white':
        set_text_color(0x0f)
    print(mess)
    resetColor()


# 函数名称：用户登录函数        
# 实现功能：校验用户身份，校验成功返回:true,否则返回:false
# 输入参数：username:登录名称,字符型；
# 			password:用户密码,字符型；
# 返回参数：result:布尔型：true:登录成功，false登录失败


#获取文件信息，返回用户数组
def get_file_data(file_name):
	file_data = ""
	with open(file_name,"r",encoding="utf-8") as f:
		file_data = f.readlines()
	return file_data

def dict_to_str(dict_name):
	str_data = ""
	for k in dict_name:
		v = dict_name[k]
		user_line = v['loginname']+'\t'+v['username']+'\t'+v['password']+'\t'+v['status']+'\t'+str(v['balance'])+'\t\n'
		str_data += user_line
	return str_data


#将文件信息写入文件
def write_file_data(file_name,u_data):
	file_data = dict_to_str(u_data)
	with open(file_name,"w",encoding="utf-8") as f:
		f.write(file_data)

def get_user_dict(file_data):
	user_dict = {}
	for line_num,user in enumerate(file_data):
		loginname = user.strip().split("\t")[0]
		username = user.strip().split("\t")[1]
		password = user.strip().split("\t")[2]
		status = user.strip().split("\t")[3]
		balance = user.strip().split("\t")[4]
		user_dict[line_num] = {'loginname':loginname,'username':username,'password':password,'status':status,'balance':balance}
	return user_dict

def alter_user_info(user_dict,user_name,firled,value):
	for k in user_dict:
		v = user_dict[k]
		if v['loginname'] == user_name:
			if firled == 'status':
				v['status'] = value
			elif firled == 'balance':
				v['balance'] = value
	return user_dict



#修改用户信息（目前只对用户状态和余额信息做修改）
#def alter_user_info(user_dict,user_name,filed,vlue):
#	m_user_data = ""
#	for line_num,user in enumerate(user_dict):
#		loginname = user.strip().split("\t")[0]
#		username = user.strip().split("\t")[1]
#		password = user.strip().split("\t")[2]
#		status = user.strip().split("\t")[3]
#		balance = user.strip().split("\t")[4]
#		if loginname == user_name:
#			if filed == 'status':
#				user = loginname+"\t"+username+"\t"+password+"\t"+vlue+"\t"+balance+"\n"
#			elif filed == 'balance':
#				user = loginname+"\t"+username+"\t"+password+"\t"+status+"\t"+str(vlue)+"\n"
#		m_user_data += user
#	return m_user_data

def pstr(chars,n):
	if n > 0:
		result = (chars * (n // len(chars)+1))[:n]
		return result
	else:
		return None	

def login(u_dict,username,password):
	for k in u_dict:
		user = u_dict[k]
		if username == user['loginname']:
			if user['status'] == 'locked':
				cprint("该账户被锁定！请联系管理员。",'red')
				break
			else:
				if password == user['password']:
					return [k,user['username'],user['balance']]
					break
				else:
					cprint("密码错误，请重新输入！",'red')
					for count in range(0,2):
						cprint('您还有%d次重试机会，超过错误次数限制后，账户将被锁定！'%(2-count),'red')
						count = count + 1
						password = getpass.getpass("请输入密码：")
						if password == user['password']:
							return [k,user['username'],user['balance']]
							break
						else:
							continue
					u_dict = alter_user_info(u_dict,username,'status','locked')
					write_file_data('account_file.txt',u_dict)
					cprint("重试次数用尽，账户已被锁定，请与管理员联系！",'red')
					return None
				break
		else:
			continue
	if username != user['loginname']:
		cprint("您输入的用户不存在。",'red')		
		return None

# 功能名称：初始化商品列表
# 实现功能：遍历商品信息文件，列出商品清单，商品数量为0的商品

def init_goods_list(goods_dict):
	local_dict = {}                                                        
	cprint("商品列表".center(72,' '),'yellow')
	cprint(pstr('=',76),'yellow')
	cprint('| %-2s | %-26s | %-2s | %-5s | %-5s |' % ('编号','商品名称','单位','商品单价(元)','可购买数量'),'yellow')
	cprint('| %-3s + %-26s + %-2s + %-3s + %-5s |' % (pstr('-',4),pstr('-',30),pstr('-',4),pstr('-',12),pstr('-',10)),'yellow')
	for i,v in enumerate(goods_dict):
		if int(v['number']) == 0:
			cprint('| %-4d | %-28s | %-3s | %-12d | %-10d |' % (i,v['name'],v['unit'],v['price'],v['number']),'darkgray')
		else:
			cprint('| %-4d | %-28s | %-3s | %-12d | %-10d |' % (i,v['name'],v['unit'],v['price'],v['number']),'yellow')
		local_dict[i] = [v['name'],v['unit'],v['price'],v['number']]               ###将商品列表赋值到local_dict###
	cprint(pstr('=',76),'yellow')

	return local_dict     ###返回格式化后的字典###

##############显示购物车信息###############################
def car_list(show_dict):
	prive_sum = 0
	buy_num = 0
	cprint("购物车".center(79,'='),'skyblue')
	cprint('%-3s  %-18s  %-2s  %-10s  %-10s  %-10s' % ('编号','商品名称','单位','商品单价(元)','购买数量','购买金额(元)'),'skyblue')	
	for k in show_dict:
		v = show_dict[k]
		cprint('%-6d  %-18s  %-2s  %-10d  %-10d  %-10d' % (k,v[0],v[1],v[2],v[3],v[4]),'skyblue')
		cprint(pstr('=',82),'skyblue')
		prive_sum += v[4]
		buy_num += 1
	return(prive_sum,buy_num)

def car_goods_modify(modify_dict,modify_goods_dict):

	a_flag = 1
	while a_flag:
		index = input('请输入商品编号 | 完成修改(q) : ')
		if len(index) != 0:
			index = input_handle(index)
		if index == 'q':
			break
		elif index in modify_dict:
			b_flag = 1
			name = modify_dict[index][0]                                  
			while b_flag:
				num = input('请输入新的商品数量(最大值为%d) |  完成修改(q) : ' % modify_dict[index][3] )
				if len(num) != 0:
					num = input_handle(num)
				if num == 'q':
					break
				elif num == 0:
					modify_goods_dict[index]['number'] = modify_dict[index][3]
					del modify_dict[index]
					b_flag = 0
				elif num > 0 and num <= modify_dict[index][3]:
					m_num = modify_dict[index][3] - num
					modify_dict[index][3] = num
					modify_dict[index][4] = modify_dict[index][2] * num
					modify_goods_dict[index]['number'] = modify_goods_dict[index]['number'] + m_num
					b_flag = 0
				else:
					pass
		else:
			pass
	return (modify_dict,modify_goods_dict) 	

def user_billing(u_dict,my_cart,billing_balance):

    cprint('欢迎来到结算菜单'.center(74,'-'),'skyblue')
    if my_cart:                                                             
        car_list(my_cart)
        billing_flag = input('请确认是否商品结算（y | n）：')
        if billing_flag == 'y':                                            
            cprint('结帐成功，你当前余额 ：%d'.center(72,' ') % billing_balance,'green')
            write_file_data('account_file.txt',u_dict)
            sys.exit(0)
        else:
            cprint('退出结算菜单，继续购物'.center(72,' '),'green')
            time.sleep(2)
    else:
        cprint('当前您的购物车为空，无需结算'.center(72,' '),'green')
        time.sleep(2)

def shopping_car_show(my_car,my_goods_dict):

	goods_all_sum = 0
	goods_all_num = 0

	if my_car:
		(goods_all_sum,goods_all_num) = car_list(my_car)

		choice = input('请进行如下操作：修改记录(m) | 继续购物(c)')
		if choice == 'm':
			(my_shop_car,my_goods_dict) = car_goods_modify(my_car,my_goods_dict)
			(goods_all_sum,goods_all_num) = car_list(my_car)
		else:
			pass
	else:		
		cprint('当前您的购物车为空'.center(76,' '),'skyblue')
	time.sleep(2)
	return(goods_all_sum,goods_all_num,my_goods_dict)


#主程序
#
#
goods_dict = [{"name":"电脑","unit":"台","price":1999,"number":20},
		 {"name":"鼠标","unit":"个","price":10,"number":100},
		 {"name":"游艇","unit":"艘","price":2999,"number":0},
		 {"name":"美女","unit":"位","price":8999,"number":2}]

if __name__=='__main__':
	login_name = input("请输入用户名：").strip()
	password = getpass.getpass("请输入密码:").strip()
	file_data = get_file_data('account_file.txt')
	user_dict = get_user_dict(file_data) 
	userinfo = login(user_dict,login_name,password)
	print(userinfo)
	if userinfo == None :
		sys.exit()
	else:
		username = userinfo[1]
		init_money = int(userinfo[2])
		if init_money == 0:
			init_money = int(input("您的可用余额为0，请充入用于剁手的锒两数："))
		usable_money = init_money
		user_shopping_car = {}
		user_buy_count = 0
		user_info = """
****************************************************************************
*                                                                          *
*                     欢迎光临么么哒购物商城                               *
*                                                                          *
****************************************************************************
会员：%s\t金额：%d\t余额：%d\t购物车：%d
					  """
		flage_one = 1
		while flage_one:
			os.system('cls') 
			cprint(user_info%(username,int(init_money),usable_money,user_buy_count),'pink')
			goods_output_dict=init_goods_list(goods_dict)
			goods_index = input('请选择菜单：输入商品编号 | 购物车（c）| 结账（b) | 退出（q):')
			if len(goods_index) != 0:
				goods_index = input_handle(goods_index)

			if goods_index == 'q':
				sys.exit(0)
			elif goods_index == 'b':
				user_dict[userinfo[0]]['balance'] = usable_money
				user_billing(user_dict,user_shopping_car,usable_money)
				
			elif goods_index == 'c':
				(my_goods_sum,user_buy_count,goods_dict) = shopping_car_show(user_shopping_car,goods_dict)
				usable_money = init_money - my_goods_sum
				if usable_money <= 0:
					cprint("您的剁手余额不足，请充值或重新选择，谢谢！",'red')
					time.sleep(5)
			elif goods_index in goods_output_dict:
				goods_name = goods_output_dict[goods_index][0]
				goods_unit = goods_output_dict[goods_index][1]
				goods_price = goods_output_dict[goods_index][2]
				goods_num = goods_output_dict[goods_index][3]

				print("【编号：%-2s  名称：%-10s  价格：%-5d (元)  数量：%-5d（个）】" % (goods_index,goods_name,goods_price,goods_num))
				flage_two = 1
				while flage_two:
					buy_num = input('请输入购买商品个数（最大值为%d） | 返回（b） | 退出 （q）:'% goods_num)
					if len(buy_num) != 0 :
						buy_num = input_handle(buy_num)
					if buy_num == 'q':
						sys.exit(0)
					elif buy_num == 'b':
						break
					elif type(buy_num) is int and buy_num > 0 and buy_num <= goods_num:
						my_goods_sum = goods_price * buy_num
						if my_goods_sum <= usable_money:
							cprint('购买商品 %s %d %s 总价格为：%d'%(goods_name,buy_num,goods_unit,my_goods_sum),'green')
							add_flag = input('请确认是否加入购物车（y | n）:')
							if add_flag == 'y':
								if goods_index not in user_shopping_car:
									user_buy_count += 1
									user_shopping_car[goods_index] = [goods_name,goods_unit,goods_price,buy_num,my_goods_sum]
								else:
									user_shopping_car[goods_index][3] += buy_num
									user_shopping_car[goods_index][4] += my_goods_sum
								usable_money -= my_goods_sum
								print(type(goods_dict[goods_index]['number']))
								goods_dict[goods_index]['number'] -= buy_num
								flage_two = 0
							else:
								break
						else:
							cprint("您的剁手余额不足，请充值或重新选择，谢谢！",'red')
							time.sleep(5)
					else:
						pass
			else:
				pass













