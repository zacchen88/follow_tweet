1. 运行 create_Login_session.py 创建一个 twitter_session.json 文件。您需要手动使用您的 Twitter 用户名和密码登录，或者使用双重身份验证 (2FA)。（此步骤无法自动执行，因为 x.com 登录页面受验证码保护。）登录后按 ENTER 键，您应该能够看到一个新文件名：twitter_session.json
2. 运行 follow_twet.py，它将遍历文件 follow_list.txt，所有您想要关注的 Twitter 账号都应该包含在该文件中，每行一个用户名，并使用 @ 符号，例如 @0x985dev

注：
脚本默认会随机延迟 5-10 秒，以避免触发 Twitter 机器人检测，您可以根据需要进行更改
delay = random.randint(5, 10)

如果您想切换到其他 Twitter 账号，只需删除 twitter_session.json 文件，然后运行 ​​create_Login_session.py 并重新登录即可。

如果您有任何疑问或想要订购您的自定义脚本，请联系：https://x.com/0x985dev