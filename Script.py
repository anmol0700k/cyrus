class script(object):   
    HELP_TXT = """๐ท๐ด๐ {}
๐ท๐ด๐๐ด ๐ธ๐ ๐๐ท๐ด ๐ท๐ด๐ป๐ฟ ๐ต๐พ๐ ๐ผ๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐."""
    ABOUT_TXT = """โฏ ๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด: {}
โ ๐ข๐๐พ๐บ๐๐๐ : <a href=https://t.me/Anmol0700>[ษชษดแดษชแดษด แดแดษดส ๊ฑแดแดสแด]</a>
โ ๐ซ๐บ๐๐๐๐บ๐๐พ : ๐ฏ๐๐๐๐๐ ๐ฅ 
โ ๐ซ๐๐ป๐๐บ๐๐ : ๐ฏ๐๐๐๐๐๐บ๐ ๐บ๐๐๐๐ผ๐๐ ๐ข.๐ฃ๐ฉ.๐ฃ 
โ ๐ฒ๐พ๐๐๐พ๐ : Heroku 
โ ๐ฃ๐บ๐๐บ๐ป๐บ๐๐พ : <a href=https://www.mongodb.com/>๐ฌ๐๐๐๐๐ฃ๐ก ๐ฅ๐๐พ๐พ ๐ณ๐๐พ๐</a>
โ ๐ก๐๐๐๐ฝ ๐ฒ๐๐บ๐๐๐ : ๐ต9.8 [BeTa]"""
    SOURCE_TXT = """<b>NOTE:</b>
- ๐ง๐ต๐ถ๐ ๐๐ ๐ก๐ผ๐ ๐ ๐ข๐ฝ๐ฒ๐ป ๐ฆ๐ผ๐๐ฟ๐ฐ๐ฒ ๐ฃ๐ฟ๐ผ๐ท๐ฒ๐ฐ๐. 
- Source -  <a href=https://t.me/+zSBT7Ednrf9kN2Y1>[ษชษดแดษชแดษด แดแดษดส ๊ฑแดแดสแด]</a>
<b>DEVS:</b>
- <a href=https://t.me/+zSBT7Ednrf9kN2Y1>[ษชษดแดษชแดษด แดแดษดส ๊ฑแดแดสแด]</a>"""

    FILE_TXT = """โค ๐๐๐ฅ๐ฉ: ๐๐ข๐ฅ๐ ๐๐ญ๐จ๐ซ๐ ๐๐จ๐๐ฎ๐ฅ๐../

<b>๐ฑ๐ ๐๐๐ธ๐ฝ๐ถ ๐๐ท๐ธ๐ ๐ผ๐พ๐ณ๐๐ป๐ด ๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐๐๐พ๐๐ด ๐ต๐ธ๐ป๐ด๐ ๐ธ๐ฝ ๐ผ๐ ๐ณ๐ฐ๐๐ฐ๐ฑ๐ฐ๐๐ด ๐ฐ๐ฝ๐ณ ๐ธ ๐๐ธ๐ป๐ป ๐ถ๐ธ๐๐ด ๐๐พ๐ ๐ฐ ๐ฟ๐ด๐๐ผ๐ฐ๐ฝ๐ด๐ฝ๐ ๐ป๐ธ๐ฝ๐บ  ๐๐พ ๐ฐ๐ฒ๐ฒ๐ด๐๐ ๐๐ท๐ด ๐๐ฐ๐๐ด๐ณ ๐ต๐ธ๐ป๐ด๐.๐ธ๐ต ๐๐พ๐ ๐๐ฐ๐ฝ๐ ๐๐พ ๐ฐ๐ณ๐ณ ๐ต๐ธ๐ป๐ด๐ ๐ต๐๐พ๐ผ ๐ฐ ๐ฟ๐๐ฑ๐ป๐ธ๐ฒ ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐๐ด๐ฝ๐ณ ๐๐ท๐ด ๐ต๐ธ๐ป๐ ๐ป๐ธ๐ฝ๐บ ๐พ๐ฝ๐ป๐  ๐พ๐ ๐๐พ๐ ๐๐ฐ๐ฝ๐ ๐๐พ ๐ฐ๐ณ๐ณ ๐ต๐ธ๐ป๐ด๐ ๐ต๐๐พ๐ผ ๐ฐ  ๐ฟ๐๐ธ๐๐ฐ๐๐ด ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐๐พ๐ ๐ผ๐๐๐ ๐ผ๐ฐ๐บ๐ด ๐ผ๐ด ๐ฐ๐ณ๐ผ๐ธ๐ฝ ๐พ๐ฝ ๐๐ท๐ด ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐๐พ ๐ฐ๐ฒ๐ฒ๐ด๐๐ ๐ต๐ธ๐ป๐ด๐...//</b>

โชผ ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐?๐ โบ

โช /plink โบโบ <b>๐๐ด๐ฟ๐ป๐ ๐๐พ ๐ฐ๐ฝ๐ ๐ผ๐ด๐ณ๐ธ๐ฐ ๐๐พ ๐ถ๐ด๐ ๐ป๐ธ๐ฝ๐บ.</b>
โช /pbatch โบโบ <b>๐๐๐ด ๐๐พ๐๐ ๐ผ๐ด๐ณ๐ธ๐ฐ ๐ป๐ธ๐ฝ๐บ ๐๐ธ๐๐ท ๐๐ท๐ธ๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ.</b>
โช /batch โบโบ <b>๐๐พ ๐ฒ๐๐ด๐ฐ๐๐ด ๐ป๐ธ๐ฝ๐บ ๐ต๐พ๐ ๐ผ๐๐ป๐๐ธ๐ฟ๐ป๐ด ๐ต๐ธ๐ป๐ด๐.</b>

โชผ ๐๐ฑ๐๐ฆ๐ฉ๐ฅ๐ โบ

<code>/batch https://t.me/dmx_bots https://t.me/Anmol0700</code>

๐ฒ๐๐ด๐ณ๐ธ๐๐ โบโบ <a href=https//t.me/Anmol0700><b>ษชษดแดษชแดษด แดแดษดส ๊ฑแดแดสแด</b></a>"""
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and แฉแแฉแญ  will respond whenever a keyword is found the message

<b>NOTE:</b>
1. This bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>

โข <code>/g_filter off</code> use this commoand + on/off in your group to control global filter in your group"""
   
    BUTTON_TXT = """Help: <b>Buttons</b>

-this bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:xxxxxxxxxxxx)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """**๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐ ๐พ๐ฝ/๐พ๐ต๐ต ๐ผ๐พ๐ณ๐๐ป๐ด..
<u>USE THIS COMMAND ON YOUR GROUP</u>

โข /autofilter on - autofilter enable in yor chat
โข /autofilter off - autofilter disable in your chat 

๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐ ๐ธ๐ ๐๐ท๐ด ๐ต๐ด๐ฐ๐๐๐๐ด ๐๐พ ๐ต๐ธ๐ป๐๐ด๐ ๐ฐ๐ฝ๐ณ ๐๐ฐ๐๐ด  ๐๐ท๐ด ๐ต๐ธ๐ป๐ด๐ ๐ฐ๐๐๐พ๐ผ๐ฐ๐๐ธ๐ฒ๐ฐ๐ป๐ป๐ ๐ต๐๐พ๐ผ ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐๐พ ๐ถ๐๐พ๐๐ฟ. ๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐๐๐ด ๐๐ท๐ด ๐ต๐พ๐ป๐ป๐พ๐๐ธ๐ฝ๐ถ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐ ๐๐พ ๐พ๐ฝ ๐ฐ๐ฝ๐ณ ๐พ๐ต๐ต ๐๐ท๐ด ๐ฐ๐๐๐พ๐ต๐ธ๐ป๐๐ด๐ ๐ธ๐ฝ ๐๐พ๐๐ ๐ถ๐๐พ๐๐ฟ../

๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐ :-
โบโบ /set_template - ๐๐ด๐ ๐ฒ๐๐๐๐พ๐ผ ๐ธ๐ผ๐ณ๐ฑ ๐๐ด๐ผ๐ฟ๐ป๐ฐ๐๐ด ๐ต๐พ๐ ๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐. 
โบโบ /get_template - ๐ถ๐ด๐ ๐ฒ๐๐๐๐ด๐ฝ๐ ๐ธ๐ผ๐ณ๐ฑ ๐๐ด๐ผ๐ฟ๐ป๐ฐ๐๐ด ๐พ๐ต ๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐.

๐ฒ๐๐ด๐ณ๐ธ๐๐ :- <a href=https://t.me/printvh>แดแดแด?ษชแด๊ฑ แดแดฉแดแดแดแด</a>**"""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of this bot

<b>Commands and Usage:</b>
โข /id - <code>get id of a specifed user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""

    ADMIN_TXT = """<b>ษดแดแดแด:</b>
<code>Tสษชs Mแดแดแดสแด Oษดสส Wแดสแดs Fแดส Mส Aแดแดษชษดs</code>

๐ <u><b>Basic Command</b></u>
โข /logs - <code>แดแด ษขแดแด แดสแด สแดแดแดษดแด แดสสแดส๊ฑ</code>
โข /stats - <code>แดแด ษขแดแด ๊ฑแดแดแดแด๊ฑ แด๊ฐ ๊ฐษชสแด๊ฑ ษชษด แดส.</code>

๐๏ธ <u><b>Database & Server Command</b></u>
โข /status - <code>แดแด ษขแดแด sแดแดแดแดs แดา sแดสแด?แดส</code>
โข /stats - <code>แดแด ษขแดแด แดแดแดแดแดสแด๊ฑแด ๊ฑแดแดแดแด๊ฑ</code>
โข /delete - <code>แดแด แดแดสแดแดแด แด ๊ฑแดแดแดษช๊ฐษชแด ๊ฐษชสแด ๊ฐสแดแด แดส.</code>
โข /deleteall - <code>แดแด แดแดสแดแดแด แดสส ๊ฐษชสแดs ๊ฐสแดแด แดส.</code>
โข /users - <code>แดแด ษขแดแด สษช๊ฑแด แด๊ฐ แดส แด๊ฑแดส๊ฑ แดษดแด ษชแด๊ฑ.</code>
โข /chats - <code>แดแด ษขแดแด สษช๊ฑแด แด๊ฐ แดส แดสแดแด๊ฑ แดษดแด ษชแด๊ฑ</code>
โข /channel - <code>แดแด ษขแดแด สษช๊ฑแด แด๊ฐ แดแดแดแดส แดแดษดษดแดแดแดแดแด แดสแดษดษดแดส๊ฑ</code>"""

    US_CHAT_TXT = """<b>ษดแดแดแด:</b>
<code>Tสษชs Mแดแดแดสแด Oษดสส Wแดสแดs Fแดส Mส Aแดแดษชษดs</code>

๐ฏ <u><b>Chat & User</b></u>
โข /broadcast - <code>แดแด สสแดแดแดแดแด๊ฑแด แด แดแด๊ฑ๊ฑแดษขแด แดแด แดสส แด๊ฑแดส๊ฑ</code>
โข /group_broadcast - <code>แดแด สสแดแดแดแดแดsแด แด แดแดssแดษขแด แดแด แดสส แดแดษดษดแดแดแดแดแด ษขสแดแดแดs</code>
โข /leave  - <code>แดแด สแดแดแด?แด ๊ฐสแดแด แด แดสแดแด.</code>
โข /disable  -  <code>แดแด แดษช๊ฑแดสสแด แด แดสแดแด.</code>
โข /invite - <code>Tแด ษขแดแด แดสแด ษชษดแด?ษชแดแด สษชษดแด แดา แดษดส แดสแดแด แดกสแดสแด แดสแด สแดแด ษชs แดแดแดษชษด.</code>
โข /ban_user  - <code>แดแด สแดษด แด แด๊ฑแดส.</code>
โข /unban_user  - <code>แดแด แดษดสแดษด แด แด๊ฑแดส.</code>
โข /restart - <code>Tแด Rแดsแดแดสแด แด Bแดแด</code>
โข /usend - <code>Tแด Sแดษดแด แด Mแดssษขแดแด แดแด Pแดสแดษชแดแดสแดส Usแดส</code>
โข /gsend - <code>Tแด Sแดษดแด แด Mแดssแดษขแด แดแด Pแดสแดษชแดแดสแดส Cสแดแด</code>"""

    G_FIL_TXT = """<b>ษดแดแดแด:</b>
<code>Tสษชs Mแดแดแดสแด Oษดสส Wแดสแดs Fแดส Mส Aแดแดษชษดs</code>

๐ฅ <u><b>Adv Global Filter </b></u>
โข /gfilter - <code>แดแด แดแดแด ษขสแดสแดส าษชสแดแดสs</code>
โข /gfilters - <code>แดแด แด?ษชแดแดก สษชsแด แดา แดสส ษขสแดสแดส าษชสแดแดสs<code>
โข /delg - <code>แดแด แดแดสแดแดแด แด sแดแดแดษชาษชแด ษขสแดสแดส าษชสแดแดส</code>
โข /delallg - <code>แดแด แดแดสแดแดแด แดสส ษขสแดสแดส ๊ฐษชสแดแดส๊ฑ</code>
"""

    STATUS_TXT = """<b>แโบ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code></b>
<b>แโบ ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐: <code>{}</code></b>
<b>แโบ ๐๐พ๐๐ฐ๐ป ๐ฒ๐ท๐ฐ๐๐: <code>{}</code></b>
<b>แโบ ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐ฑ</b>
<b>แโบ ๐ต๐๐ด๐ด ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐ฑ</b>"""
    LOG_TEXT_G = """#๐๐๐ฐ๐๐ซ๐จ๐ฎ๐ฉ
    
<b>แโบ ๐๐ซ๐จ๐ฎ๐ฉ โชผ {a}(<code>{b}</code>)</b>
<b>แโบ ๐ ๐๐ โชผ @{c}
<b>แโบ ๐๐จ๐ญ๐๐ฅ ๐๐๐ฆ๐๐๐ซ๐ฌ โชผ {d}</b>
<b>แโบ ๐๐๐๐๐ ๐๐ฒ โชผ {e}</b>

By {f}
"""
    LOG_TEXT_P = """#๐๐๐ฐ๐๐ฌ๐๐ซ
    
<b>แโบ ๐๐ - <code>{}</code></b>
<b>แโบ ๐๐๐ฆ๐ - {}</b>
<b>แโบ ๐๐ - @{}</b>

By @{} """
   
    ZOMBIES_TXT = """๐ท๐ด๐ป๐ฟ ๐๐พ๐ ๐๐พ ๐บ๐ธ๐ฒ๐บ ๐๐๐ด๐๐

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
โข /inkick - command with required arguments and i will kick members from group.
โข /instatus - to check current status of chat member from group.
โข /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
โข /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
โข /dkick - to kick deleted accounts."""

    IMAGE_TXT = """โค ๐๐๐ฅ๐ฉ: Iแดแดษขแด

๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐ข๐๐ ๐๐ ๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐ข ๐๐๐๐๐๐ข 

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐?๐:

โช ๐ฉ๐๐๐ ๐๐พ๐๐ฝ ๐๐พ ๐บ ๐๐๐บ๐๐พ ๐๐ ๐พ๐ฝ๐๐ โจ

๐ฌ๐บ๐ฝ๐พ ๐ป๐ <a href=https://t.me/Anmol0700 ษชษดแดษชแดษด แดแดษดส ๊ฑแดแดสแด</a>"""

    RESTRIC_TXT = """โค ๐๐๐ฅ๐ฉ: Mแดแดแด ๐ซ

๐๐๐๐๐ ๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐๐ ๐ ๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐ ๐๐๐ ๐๐ ๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐๐๐๐๐ข.

โช/ban: ๐ณ๐ ๐ป๐บ๐ ๐บ ๐๐๐พ๐ ๐ฟ๐๐๐ ๐๐๐พ ๐๐๐๐๐.
โช/unban: ๐ณ๐ ๐๐๐ป๐บ๐ ๐บ ๐๐๐พ๐ ๐๐ ๐๐๐พ ๐๐๐๐๐.
โช/tban: ๐ณ๐ ๐๐พ๐๐๐๐๐บ๐๐๐๐ ๐ป๐บ๐ ๐บ ๐๐๐พ๐.
โช/mute: ๐ณ๐ ๐๐๐๐พ ๐บ ๐๐๐พ๐ ๐๐ ๐๐๐พ ๐๐๐๐๐.
โช/unmute: ๐ณ๐ ๐๐๐๐๐๐พ ๐บ ๐๐๐พ๐ ๐๐ ๐๐๐พ ๐๐๐๐๐.
โช/tmute: ๐ณ๐ ๐๐พ๐๐๐๐๐บ๐๐๐๐ ๐๐๐๐พ ๐บ ๐๐๐พ๐.

โค ๐ญ๐๐๐พ:
๐ถ๐๐๐๐พ ๐๐๐๐๐ /tmute ๐๐ /tban ๐๐๐ ๐๐๐๐๐๐ฝ ๐๐๐พ๐ผ๐๐ฟ๐ ๐๐๐พ ๐๐๐๐พ ๐๐๐๐๐.

โ๐ค๐๐บ๐๐๐๐พ: /๐๐ป๐บ๐ 2๐ฝ ๐๐ /๐๐๐๐๐พ 2๐ฝ.
๐ธ๐๐ ๐ผ๐บ๐ ๐๐๐พ ๐๐บ๐๐๐พ๐: ๐/๐/๐ฝ. 
 โข ๐ = ๐๐๐๐๐๐พ๐
 โข ๐ = ๐๐๐๐๐
 โข ๐ฝ = ๐ฝ๐บ๐๐"""


    PIN_TXT ="""<b>PIN MODULE</b>
<b>๐ฟ๐ธ๐ฝ ๐ฐ ๐ผ๐ด๐๐๐ฐ๐ถ๐ด../</b>

<b>๐ฐ๐ป๐ป ๐๐ท๐ด ๐ฟ๐ธ๐ฝ ๐๐ด๐ฟ๐ป๐ฐ๐๐ด๐ณ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐ ๐ฒ๐ฐ๐ฝ ๐ฑ๐ด ๐ต๐พ๐๐ฝ๐ณ ๐ท๐ด๐๐ด::</b>

<b>๐๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐ ๐ฐ๐ฝ๐ณ ๐๐๐ฐ๐ถ๐ด๐</b>

โ /pin :- ๐๐พ ๐ฟ๐ธ๐ฝ ๐๐ท๐ด ๐ผ๐ด๐๐๐ฐ๐ถ๐ด ๐พ๐ฝ ๐๐พ๐๐ ๐ฒ๐ท๐ฐ๐๐
โ /unpin :- ๐๐พ ๐๐ฝ๐ฟ๐ธ๐ฝ ๐๐ท๐ด ๐ฒ๐๐๐๐ด๐ด๐ฝ๐ ๐ฟ๐ธ๐ฝ๐ฝ๐ด๐ณ ๐ผ๐ด๐๐ฐ๐ฐ๐ถ๐ด"""

    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>

โข /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

โข These commands works on both pm and group.
โข These commands can be used by any group member."""

    TTS_TXT = """Help: <b> TTS ๐ค module:</b>

Translate text to speech

<b>Commands and Usage:</b>

โข /tts <text> : convert text to speech

<b>NOTE:</b>

โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข IMDb can translate texts to 200+ languages."""

    PINGS_TXT ="""<b>๐ Ping:</b>

Helps you to know your ping ๐ถ๐ผโโ๏ธ

<b>Commands:</b>

โข /alive - To check you are alive.
โข /ping - To get your ping.
<b>๐นUsage๐น :</b>

โข This commands can be used in pms and groups
โข This commands can be used buy everyone in the groups and bots pm
โข Share us for more features"""

    TELE_TXT = """<b>โซ๏ธHELP: Telegraphโช๏ธ</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

๐คง /telegraph - Send me this command reply with Picture or Vide Under (5MB) 

<b>NOTE:</b>

โข This Command Is Available in goups and pms
โข This Command Can be used by everyone"""

    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""

    PURGE_TXT = """<b>Purge</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

โ /purge :- Delete All Messages From The Replied To Message, To The Current Message"""

    CREATOR_REQUIRED = """โ<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "โ **Arguments Required**"
      
    KICKED = """โ๏ธ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """๐ฎ Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """โ<b>เดเดจเตเดจเต Admin เดเดเตเดเดคเตเดค เดธเตเดฅเดฒเดคเตเดคเต เดเดพเตป เดจเดฟเดเตเดเดฟเดฒเตเดฒ เดชเตเดเตเดตเดพ Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """โ๏ธ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>เดเดชเตเดชเต เดเดฒเตเดฒเดพเด เดเดเดฟเดเตเดเตเดฎเดพเดฑเตเดฑเดฟ เดคเดฐเดพเด...</b>"""
      
    CARB_TXT = """โพ๏ธ๐๐๐๐ฃ ๐๐ข๐ฅ ๐๐๐ฅ๐๐ข๐กโฝ๏ธ
๐ฒ๐ฐ๐๐ฑ๐พ๐ฝ ๐ธ๐ ๐ฐ ๐ต๐ด๐๐๐๐๐ด ๐๐พ ๐ผ๐ฐ๐บ๐ด ๐๐ท๐ด ๐ธ๐ผ๐ฐ๐ถ๐ด ๐ฐ๐ ๐๐ท๐พ๐๐ฝ ๐ธ๐ฝ ๐๐ท๐ด ๐๐พ๐ฟ ๐๐ธ๐๐ท ๐๐พ๐๐๐ด ๐๐ด๐๐๐.
๐ต๐พ๐ ๐๐๐ธ๐ฝ๐ถ ๐๐ท๐ด ๐ผ๐พ๐ณ๐๐ป๐ด ๐น๐๐๐ ๐๐ด๐ฝ๐ณ ๐๐ท๐ด ๐๐ด๐๐ ๐ฐ๐ฝ๐ณ ๐๐ด๐ฟ๐ป๐ ๐๐พ ๐ธ๐ ๐๐ธ๐๐ท /carbon ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ ๐๐ท๐ด ๐ฑ๐พ๐ ๐๐ธ๐ป๐ป ๐๐ด๐ฟ๐ป๐ ๐๐ธ๐๐ท ๐๐ท๐ด ๐ฒ๐ฐ๐๐ฑ๐พ๐ฝ ๐ธ๐ผ๐ฐ๐ถ๐ด"""

    FOND_TXT = """โพ๏ธ๐๐๐๐ฃ ๐๐ข๐ฅ ๐๐ข๐ก๐ง๐ฆโฝ๏ธ
๐ต๐พ๐ฝ๐ ๐ธ๐ ๐ฐ ๐ผ๐พ๐ณ๐๐ป๐ด ๐ต๐พ๐ ๐ผ๐ฐ๐บ๐ด ๐๐พ๐๐ ๐๐ด๐๐ ๐๐๐๐ป๐ธ๐๐ท.
๐ต๐พ๐ ๐๐๐ด ๐๐ท๐ฐ๐ ๐ต๐ด๐๐๐๐๐ด ๐๐๐ฟ๐ด /font <your text> ๐๐ท๐ด๐ฝ ๐๐พ๐๐ ๐๐ด๐๐ ๐ธ๐ ๐๐ด๐ฐ๐ณ๐."""

    SHARE_TXT = """โพ๏ธ๐๐๐๐ฃ ๐๐ข๐ฅ ๐ฆ๐๐๐ฅ๐ ๐ง๐๐ซ๐งโฝ๏ธ

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐?๐:
โข /share - ๐๐๐๐๐ข ๐๐๐๐ ๐ฐ๐๐ข ๐๐๐ก๐ ๐๐ ๐๐๐๐ ๐๐๐๐ ๐ฒ๐๐๐๐๐๐ """




    


    
