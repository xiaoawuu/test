def print_color(color_name, color):
	start_line = '\033[1;' + color + 'm '
	end_line = '\033[0m'
	print(start_line + color_name + ' ' + end_line)


# if __name__ == '__main__':
# 	import threading
#
# 	colors_names_list = ["我是白色/黑色（取决于当前输出栏的背景颜色）", "我是红色", "我是绿色", "我是黄色", "我是蓝色", "我是紫色", "我是深绿色",
# 						 "我是白色/灰色（取决于当前输出栏的背景颜色）"]
# 	threads_list = []
# 	colors_list = ['30', '31', '32', '33', '34', '35', '36', '100']
# 	loop_flag = 0
# 	for color_name in colors_names_list:
# 		t = threading.Thread(target=print_color, args=(color_name, colors_list[loop_flag]))
# 		t.start()
# 		threads_list.append(t)
# 		loop_flag += 1
# 	for t in threads_list:
# 		t.join()
#

import re

"""
爬虫，需非常理解正则表达式

"""
# 从头开始
# print(re.match("^[a-zA-Z]", '' or ''))
# print(re.match(r"^[a-z]|[A-Z]|_", "zhang123san456"))
# print(re.match(r"^zhang\d+", "zhang123san456"))
# print(re.match(r"^zhang\d+", "zhangsan456"))
# print(re.match(".^s.n$", "zhangsan456"))
"""
开始：match
所有：search
所有：(返回多个)findall
"""
a = 'L_-47jjj--_adsgfssdfgdsgjhjj7'

# print(re.match(r"^[a-z]|[A-Z]|_", a))
# print(len(re.findall(r"[a-z]|[A-Z]|_|-|[0-9]", a)))

print(re.match(r"(^[a-zA-Z_])([a-zA-Z0-9_-]{5,19})+$", a))

# print(len(a))


# print(re.search(r'^a~z|A-Z|_\d+','_123'))
# print(re.match(r'a-z|A-Z|_\d+','a123'))
# print(re.search(r'^a-z|A-Z|_','A123'))
# print(re.search("s.+n","zhangsan456"))
# print(re.search("s.+n","zhangsan456"))
# print(re.search("[0-9]{3}","12zhang568san"))
# print(re.search("[0-9]{1,3}","1zhang56san"))
# print(re.findall("[0-9]{1,3}","1zhang5678san"))
# #或者匹配
# print(re.search("abc|ABC","ABCabc123aa"))
# print(re.search("abc|ABC","ABCabc123aa"))
# print(re.findall("[a-z]|[1-9]|\\/","ABCabc/123/aa"))
# 匹配abcc
# print(re.search("abc{2}","ABCabc123aabcc"))
# print(re.search("(abc){2}","ABCabc123aabcc"))
# #匹配abcabc
# print(re.search("(abc){2}","ABCabc123abcabcabc"))
# #匹配管道符
# print(re.search("(abc){2}|\|","ABCabc123abcabcabcc|"))
# print(re.search("\||(abc){2}","|ABCabc123abcabcabcc|"))
# print(re.search("\||(abc){2}","|ABCabc123|abcabcabcc|"))
# # #分组匹配
# print(re.search("(abc){}v(123|456)z","abcabcv456zasfd"))
# print(re.search("(abc){2}v(123|456)z","abczabcv456zasfd"))
# print(re.search("(abc|abb){2}.+(123|456)z","abcabczx456zasfd"))
# #\A跟^一样
# print(re.search("\A[0-9]","abcabczx456zasfd"))
# print(re.search("\A[0-9][a-z]\Z","2a"))
# #\d匹配数字1-9；\D匹配非数字
# print(re.search("\A\d\D\Z","2a"))
#
# print(re.search("\A[0-9][a-z]\Z","2a"))
# print(re.search("\A[0-9].+[a-z]\Z","2abcabczx456zasfd"))
# #\w匹配[A-Za-z0-9]  \W匹配非[A-Za-z0-9]
#
# print(re.search("\w+","2abcabczx456za&sfd"))
# print(re.findall("\W+","2abc@#abc$zx456za&sfd"))
#
# #\s匹配空字符、\t、\n、\r,
# print(re.search("\s+","2abc\nab\tczx456za&sfd"))
# print(re.search("\s+","2abc\n\t     czx456za&sfd"))
# print(re.findall("\s","2a\nbc@\t#abc$zx456za&sfd"))
# #分组匹配
# print(re.search("(?P<id>[0-9]+)","abcs12345%15").groupdict())
# print(re.search("(?P<id>[0-9]+)","abcs12345%15").group())
# print(re.search("(?P<id>[0-9]+)","abcs12345%15").group)
# print(re.search("(?P<name>[a-z]+)(?P<age>[0-9])","abcs12345%15").groupdict())
# print(re.search("(?P<name>[a-z]+)(?P<age>[0-9])","abcs12345%15").group("name"))

# 正则地址及身份证号
# splita
# splitall
# 使用数字分割
# print(re.split("[0-9]+","abc 12de3f45h68"))
# #sub替换:count=2替换多少次
# print(re.sub("[0-9]+","**","12sad1654asdf143e5r4g3a5e4g35",count=2))
# print(re.search(r"\\",r"sd1321\\\65465asdf"))
# print(re.sub(r"\\",r"\\",r"sd1321\\65465asdf",count=1))
# #忽略大小写
# print(re.findall("[a-z]+","sd1321\\65465Aasdf",flags=re.I))
#
# #
# print(re.search("^a","\nabc\n123"))
# print(re.search("^a+","\nabc\na123",flags=re.M))
# print(re.search(".+\\d+","\nabc\na123",flags=re.M))
# print(re.search(".+","\nabc\na123",flags=re.S))
# print(re.search(".+\D+","\nabc\na123"))


# 没匹配到返回None
# >>><re.Match object; span=(0, 5), match='zhang'>


"""
1.来发一个简单的python计算机
2.实现加减乘除及括号优先级解析
    用户输入1-2*((60-30+(-40/50)*(9-285/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
    等类似公式后，必须自己解析里面的(),+,-,*,/符号和公式（不能调用eval等类似功能偷懒实现）
    运行得出结果必须正确
"""

a = '''SELECT SUM
	( money ) sum_money,
	COUNT ( money ) [order],
	(
	SELECT COUNT
		( * ) + (
		SELECT COUNT
			( * ) 
		FROM
			biz_wallet_record 
		WHERE
			pay_time >= ( SELECT CONVERT ( VARCHAR, GETDATE( ), 23 ) + ' 00:00:00' ) 
			AND buy_type = 11 
		) 
	FROM
		biz_order 
	WHERE
		create_time >= ( SELECT CONVERT ( VARCHAR, GETDATE( ), 23 ) + ' 00:00:00' ) 
		AND status = 1 
		AND currency = 0 
	) vip,
	(
	SELECT COUNT
		( sex ) 
	FROM
		biz_user 
	WHERE
		create_time >= ( SELECT CONVERT ( VARCHAR, GETDATE( ), 23 ) + ' 00:00:00' ) 
		AND status = 4 
	) count_user 
FROM
	biz_order 
WHERE
	create_time >= ( SELECT CONVERT ( VARCHAR, GETDATE( ), 23 ) + ' 00:00:00' ) 
	AND status = 1;'''

from test_server.data.sql import sql_select

a = sql_select(a)

data = {'money':a[0][0],'order':a[0][1],'vip':a[0][2],'user':a[0][3]}
print(data)
