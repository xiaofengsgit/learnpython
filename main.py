#!/usr/bin/env python
# -*- coding: utf-8 -*-

import weiboLogin
import getWeiboPage
import urllib
import urllib2

username = '839309885@qq.com'
pwd = 'ZXF6850462-'

WBLogin = weiboLogin.weiboLogin()
WBLogin.login()

WBmsg = getWeiboPage.getWeiboPage()
url = 'http://weibo.com/1624087025?from=otherprofile&wvr=3.6&loc=tagweibo'

WBmsg.get_firstpage(url)
WBmsg.get_secondpage(url)
WBmsg.get_thirdpage(url)