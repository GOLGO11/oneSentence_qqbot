# oneSentence_qqbot
使用python和qqbot创建一个优美的QQ机器人


## 第一步
  安装qqbot：pip install qqbot
  
  qqbot使用教程：https://github.com/GOLGO11/qqbot （只需要看前四点）

## 第二步

 编写机器人:
 
  1.打开命令行1
  
  1.进入 ~/.qqbot-tmp/plugins/ 目录，在该目录下创建sample.py
  
  1.调用一言网站（hotokoto）的公开API获取数据，https://hitokoto.cn/api
  
  2.将获得的数据存进一个变量str
  
  3.根据qqbot的使用规则，需要在sample.py中编写onQQMessage函数，将content判断条件改为‘一言’，并将变量str放进qqbot的onQQMessage函数中
  
  4.保存sample.py
 
 启动机器人
 
  1.打开命令行2
  
  1.在命令行2输入qqbot，启动qqbot服务，登录机器人账号
  
  2.在命令行1 输入qq plug sample，将onQQMessage函数注册到qqbot的响应事件上（必须先在命令行2启动qqbot）
  
  3.启动完毕
  
 使用效果
 
 打开qq客户端，使用另一个qq号向该机器人发送消息输入‘一言’，机器人将返回hitokoto网站的名言、出处等信息.
 
  
  
