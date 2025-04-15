1. Run create_Login_session.py to create a twitter_session.json file. You need to manually login with your twitter username and password and/or 2FA. (This step can not be automatated becuase x.com login page is guaded by CAPTCHA). Press ENTER after login, you should be able to see a new file name: "twitter_session.json
2. Run follow_twet.py，it will go through the file follow_list.txt, all the twitter account you want to follow should be in this file, one username per line, with @  eg. @0x985dev

OPTIONAL:
Script default delay 5-10 second randomly to avoid triggering twitter bot detection, you can change it accordingly
    delay = random.randint(5, 10)

If you want to switch to a different twitter, just need to remove the twitter_session.json file and run create_Login_session.py and login again. 

