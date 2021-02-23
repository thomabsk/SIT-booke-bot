# SIT-booke-bot

If you want to make the bot work for the other areas, the url has to be changed to an appropriate one. Currently it is set to work at moholt.

You also need the firefox driver for it to work. The one currently included is for linux64. Other drivers can be found on their [github](https://github.com/mozilla/geckodriver/releases/tag/v0.29.0)

For more info on firefox with selenium visit [linuxhint](https://linuxhint.com/using_selenium_firefox_driver/)

For this bot to work you have to make an account at [ibooking](https://ibooking.sit.no/webapp/timeplan/)

1.
Install virtualenv on your machine

2.
Run these commands to start the virtualenv

```
virtualenv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

3.
add a password.py file to your directory and add the following with your number and password

```
passw = "Your-password"
number = "Your-number"
```
4.
Then go into bot.py and add schedules in the setup_schedule() function

```
schedule.every().monday.at("20:00").do(run_bot)
schedule.every().monday.at("21:00").do(run_bot)
```

As an example, the above code will book wednesdays at 20:00 and 21:00.

5. Go to the gym :)