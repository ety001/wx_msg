# wx_msg

简易便捷发送微信模板消息的小玩意儿

利用微信公众平台测试账号，快速发送模板消息提醒。

**适用于树莓派之类的小玩意儿的提醒功能**

**只适合个人或者小团队使用**

1.首先登陆平台，<http://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login>，登陆一下

2.点击『新增测试模板』，根据自己的需要，填写模板，如下图

![新增测试模板](https://raw.githubusercontent.com/ety001/wx_msg/master/img/wx_tmpl.png)

```
{{first.DATA}}
from：{{send.DATA}}
内容：{{text.DATA}}
时间：{{time.DATA}}
{{remark.DATA}}
```

3.在目标文件夹下，执行clone命令下载代码

```
git clone https://github.com/ety001/wx_msg.git
```

4.把代码中的 `tmpl_id`, `appid`, `secret`, `user_id`, `tmpl_data`，都改成你自己的，其中 `tmpl_data` 只需要根据你的模板内容修改data中的项目即可，`value`为空即可

5.测试一下，注意命令中使用的是两个冒号来间隔的

```
python wx_msg.py "first::hi|send::18989|text::hello|time::2015-10-22"
```

![测试成功](https://raw.githubusercontent.com/ety001/wx_msg/master/img/wx.jpg)

# 其他备注事项

你的模板里有几项，最后使用命令的时候，参数必须小于等于模板的项目数，比如我这里设置的模板里有 `first`, `send`, `text`, `time`, `remark`， 那么我在使用命令的时候，就只能使用以上的这些参数

Licence [MIT](https://github.com/ety001/wx_msg/blob/master/LICENSE)

[Blog](http://www.domyself.me)
