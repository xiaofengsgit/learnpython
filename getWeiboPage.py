#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')

class getWeiboPage:
	body = {
		'__rnd':'',
		'_k':'',
		'_t':'0',
		'count':'50',
		'end_id':'',
		'max_id':'',
		'page':1,
		'pagebar':'',
		'pre_page':'0',
		'uid':''
	}
	uid_list = []
	charset = 'utf8'

	def get_msg(self,uid):
		getWeiboPage.body['uid'] = uid
		url = self.get_url(uid)
		self.get_firstpage(url)
		self.get_secondpage(url)
		self.get_thirdpage(url)
	def get_firstpage(self,url):
		getWeiboPage.body['pre_page'] = getWeiboPage.body['page']-1
		url = url +urllib.urlencode(getWeiboPage.body)
		req = urllib2.Request(url)
		result = urllib2.urlopen(req)
		text = result.read()
		self.writefile('./output/text1',text)		
		self.writefile('./output/result1',eval("u'''"+text+"'''"))
		
	def get_secondpage(self,url):
		getWeiboPage.body['count'] = '15'
	#	getWeiboPage.body['end_id'] = '3490160379905732'
	#	getWeiboPage.body['max_id'] = '3487344294660278'
		getWeiboPage.body['pagebar'] = '0'
		getWeiboPage.body['pre_page'] = getWeiboPage.body['page']

		url = url +urllib.urlencode(getWeiboPage.body)
		req = urllib2.Request(url)
		result = urllib2.urlopen(req)
		text = result.read()
		self.writefile('./output/text2',text)		
		self.writefile('./output/result2',eval("u'''"+text+"'''"))
	def get_thirdpage(self,url):
		getWeiboPage.body['count'] = '15'
		getWeiboPage.body['pagebar'] = '1'
		getWeiboPage.body['pre_page'] = getWeiboPage.body['page']

		url = url +urllib.urlencode(getWeiboPage.body)
		req = urllib2.Request(url)
		result = urllib2.urlopen(req)
		text = result.read()
		self.writefile('./output/text3',text)		
		self.writefile('./output/result3',eval("u'''"+text+"'''"))
	def get_url(self,uid):
		url = 'http://weibo.com/' + uid + '?from=otherprofile&wvr=3.6&loc=tagweibo'
		return url
	def get_uid(self,filename):
		fread = file(filename)
		for line in fread:
			getWeiboPage.uid_list.append(line)
			print line
			time.sleep(1)
	def writefile(self,filename,content):
		fw = file(filename,'w')
		fw.write(content)
		fw.close()