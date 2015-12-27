#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-11-04 09:21:31
# author: 郑集文
# Description:
import re


def pipei(inp_list):
	'''
	字符串截取方法实现
	先匹配最后一个左括号，在匹配离它最近的右括号。
	他俩之间的字符串 你懂得！
	'''
	equation=inp_list[0]
	count_l=equation.find('(')
	if count_l == -1:
		final = compute(inp_list[0])
		inp_list[0] = final
		return inp_list
	else:
		match=count_l
		match_l=count_l
		while True:
			match=equation.find('(',int(match)+1)
			if match == -1:
				break
			else:
				match_l=match
		match_r=equation.find(')',int(match_l))
		bracket=equation[int(match_l):int(match_r)+1]
		bracket=bracket[1:-1]
		before=equation[:int(match_l)]
		after=equation[int(match_r)+1:]
		ret=compute(bracket)
		inp_list[0] = "%s%s%s" %(before, ret, after)
	pipei(inp_list)
		

def compute(expression):
	inp = [expression,0]
	compute_mul_div(inp)
	compute_add_sub(inp)
	if divmod(inp[1],2)[1] == 1:
		result = float(inp[0])
		result = result * -1
	else:
		result = float(inp[0])
	return result




def exec_bracket(inp_list):
    if not re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', inp_list[0]):
        final = compute(inp_list[0])
        inp_list[0] = final
        return inp_list
    content = re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', inp_list[0]).group()
    before, nothing, after = re.split('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', inp_list[0], 1)
    content = content[2:len(content)-1]
    ret = compute(content)
    inp_list[0] = "%s%s%s" %(before, ret, after)
    exec_bracket(inp_list)


def compute_add_sub(arg):
    arg[0] = arg[0].replace('+-','-')
    arg[0] = arg[0].replace('++','+')
    arg[0] = arg[0].replace('-+','-')
    arg[0] = arg[0].replace('--','+')
    if arg[0].startswith('-'):
        arg[1] += 1
        arg[0] = arg[0].replace('-','&')
        arg[0] = arg[0].replace('+','-')
        arg[0] = arg[0].replace('&','+')
        arg[0] = arg[0][1:]
    val = arg[0]
    mch = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', val)
    if not mch:
        return
    content = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', val).group()
    if len(content.split('+'))>1:
        n1, n2 = content.split('+')
        value = float(n1) + float(n2)
    else:
        n1, n2 = content.split('-')
        value = float(n1) - float(n2)
    before, after = re.split('\d+\.*\d*[\+\-]{1}\d+\.*\d*', val, 1)
    new_str = "%s%s%s" % (before,value,after)
    arg[0] = new_str
    compute_add_sub(arg)



def compute_mul_div(arg):
    val = arg[0]
    mch = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', val)
    if not mch:
        return
    content = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', val).group()

    if len(content.split('*'))>1:
        n1, n2 = content.split('*')
        value = float(n1) * float(n2)
    else:
        n1, n2 = content.split('/')
        value = float(n1) / float(n2)
    before, after = re.split('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', val, 1)
    new_str = "%s%s%s" % (before,value,after)
    arg[0] = new_str
    compute_mul_div(arg)





if __name__ == "__main__":
	inpp = '1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 *	 568/14 )) - (-4*3)/ (16-3*2) ) '
	inpp = re.sub('\s*','',inpp)
	inp_list = [inpp,]
	pipei(inp_list)
	final = inp_list[0]
	print "本月工资结算：%s元"%final
