from wxpy import *

# 初始化机器人，扫码登陆
bot = Bot()

# 获取所有好友
my_friends = bot.friends()
print(type(my_friends))