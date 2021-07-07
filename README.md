



<h1 align="center">AMR-Url_Uploader</h1>
<p align="center">
  <a href="https://github.com/Avipatilpro/FileStreamBot">
    <img src="https://socialify.git.ci/satyushree/AMR-Url_Uploader/image?description=1&font=Bitter&forks=1&issues=1&logo=https%3A%2F%2Ftelegra.ph%2Ffile%2F8eddfc57dde92ec6e288e.jpg&pattern=Brick%20Wall&pulls=1&stargazers=1&theme=Dark" alt="Cover Image" width="550">
  </a>
  
  <p align="center">
    A simple url uploader bot with permenent thumbnail support .
    <br />
   </strong></a>
    <br />
    <a href="https://github.com/satyushree/AMR-Url_Uploader/issues">Report a Bug</a>
    |
    <a href="https://github.com/satyushree/AMR-Url_Uploader/issues">Request Feature</a>
  </p>
</p>

<hr>




```
Scrapped some code from @SpEcHIDe's AnyDLBot Repository
Made with Python3
```
**My Features**:

👉 All Supported Video Formats of <a href="https://rg3.github.io/youtube-dl/supportedsites.html"><img src="https://badgen.net/badge/Name/Link"></a>

👉 Upload as file from any HTTP link

## Deploy 

## ♢ How to make your own :

Either you could locally host or deploy on [Heroku] By Clicking `Deploy on Heroku` Given below
<br>

#### ♢ Click on This Drop-down and get more details

<br>
<details>
  <summary><b>Deploy on Heroku :</b></summary>


1. Fork This Repo
2. Click on Deploy Easily

<h4> So Follow Above Steps 👆 and then also deply other wise not work</h4>

Press the below button to Fast deploy on Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

then goto the <a href="#mandatory-vars">variables tab</a> for more info on setting up environmental variables. </details>


<details>
  <summary><b>Host it on VPS Locally :</b></summary>

```py
git clone https://github.com/Satyamurthi/AMR-Url_Uploader
cd AMR-Url_Uploader
virtualenv -p python3 VENV
. ./VENV/bin/activate
pip install -r requirements.txt
cp sample_config.py config.py
--- EDIT config.py values appropriately ---
python bot.py
```

and to stop the whole bot,
 do <kbd>CTRL</kbd>+<kbd>C</kbd>

Setting up things

If you're on Heroku, just add these in the Environmental Variables
or if you're Locally hosting, create a file named `.env` in the root directory and add all the variables there.
An example of `.env` file:

```py
API_ID=12345
API_HASH=esx576f8738x883f3sfzx83
BOT_TOKEN=55838383:yourtbottokenhere
LOG_CHANNEL=-100
AUTH_USERS=your_user_id
```
  </details>


<details>
  <summary><b>Vars and Details :</b></summary>

`API_ID` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.

`API_HASH` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.

`BOT_TOKEN` : Get the bot token from [@BotFather](https://telegram.dog/BotFather)

`LOG_CHANNEL` : Create a new channel (private/public), add [@missrose_bot](https://telegram.dog/MissRose_bot) as admin to the channel and type /id. Now copy paste the ID into this field.

`AUTH_USERS` : Your Telegram User ID

 Option Vars

`UPDATES_CHANNEL` : Put a Public Channel Username, so every user have to Join that channel to use the bot. Must add bot to channel as Admin to work properly.

`TIME_LIMIT` : For time to next process in second

`DEF_WATER_MARK_FILE` : Name you want (Ex:- @All_Movie_Rockers)

`DEF_THUMB_NAIL_VID_S` : Link of the photo

 
<details>
  <summary>SCREENSHOTS</summary>
                
              *If "True"  - Screenshot will be uploaded

              *If "False" - Screenshot will not be uploaded
</details>
</details>
<details>
  <summary><b>How to Use :</b></summary>

:warning: **Before using the  bot, don't forget to add the bot to the `BIN_CHANNEL` as an Admin**
 
`/start` : To check if the bot is alive or not.

To get an instant stream link, just forward any media to the bot and boom, its fast af.

### Channel Support
Bot also Supported with Channels. Just add bot Channel as Admin. If any new file comes in Channel it will edit it with **Get Download Link** Button. </details>


- [Aʟʟ Mᴏᴠɪᴇ Rᴏᴄᴋᴇʀs](https://telegram.me/All_Movie_Rockers)

## Accounts

* [YouTube](https://youtube.com/channel/--)
* [GitHub](https://github.com/Satyamurthi)
* [Telegram](https://telegram.me/shreevish)

## Credits

* [Shrimadhav UK](https://github.com/SpEcHIDe)
* [Pyrogram](https://github.com/pyrogram/pyrogram)
