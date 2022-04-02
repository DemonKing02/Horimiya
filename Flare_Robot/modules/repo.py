import random
from .. import telethn as aasf
from telethon import events, Button
from telegram.parsemode import ParseMode

HOTTIE_PICS = (
    "https://telegra.ph/file/dfb3f645a161318015b31.jpg",
    "https://telegra.ph/file/0233572f88b43c172be6b.jpg",
    "https://telegra.ph/file/4718ea5902ed433f9cf38.jpg",
    "https://telegra.ph/file/4d1ddeb0d63f54a8dce29.jpg",
    "https://telegra.ph/file/97300050457226a824628.jpg",
    "https://telegra.ph/file/90f945c6e3c4a5e2cb863.jpg",
    "https://telegra.ph/file/c19d18bea30a222a4ceac.jpg",
    "https://telegra.ph/file/1f8f6bd142fd4b104dc95.jpg",
    "https://telegra.ph/file/4fc91fd4a1ac4d25a2a1b.jpg",
    "https://telegra.ph/file/9332b113ddb8555bf6ffe.jpg",
    "https://telegra.ph/file/fbc20e462231564a7407f.jpg",
    "https://telegra.ph/file/45df1a2dcf2e385d5cb7b.jpg",
    "https://telegra.ph/file/89e069ddc5c581a3501ef.jpg",
    "https://telegra.ph/file/2d75f08b6da4ac453a500.jpg",
    "https://telegra.ph/file/4b8a6352daa4597e5b507.jpg",
    "https://telegra.ph/file/4ffaff9bb7f3d7818ef21.jpg",
    "https://telegra.ph/file/a62f6de763dbb2b32dace.jpg",
    "https://telegra.ph/file/7c5715131dd0f188e1582.jpg",
    "https://telegra.ph/file/5f8e2c2e0147d8ec4fa86.jpg",
    "https://telegra.ph/file/30dd0b041aaff87826264.jpg",
    "https://telegra.ph/file/9b9de1bd73e482e45d47e.jpg",
    "https://telegra.ph/file/6a1a542b0846bae071a15.jpg",
    "https://telegra.ph/file/6fa7b00d49c8db42f2bb1.jpg",
    "https://telegra.ph/file/f3e0cedf92b3f234cd84f.jpg",
    "https://telegra.ph/file/60998d8f5520b95aec7f9.jpg",
    "https://telegra.ph/file/2d9f1eb3c8ae1980bf9f6.jpg",
    "https://telegra.ph/file/f830ea186d932a076719a.jpg",
    "https://telegra.ph/file/0cde16e55a50dd22715cd.jpg",
    "https://telegra.ph/file/74fc9c85fd341157fee1c.jpg",
    "https://telegra.ph/file/dd8b72e3976d1fd35615a.jpg",
    "https://telegra.ph/file/1b81b3ff11c45e4e31358.jpg",
    "https://telegra.ph/file/be4e82ab2b9de9cb97fb0.jpg",
    "https://telegra.ph/file/58b3cdf9203431ecfce2a.jpg",
    "https://telegra.ph/file/2fb2fefda863a096b0e42.jpg",
)


@aasf.on(events.NewMessage(incoming=True, pattern="/repo"))
async def repo(e):
    k = f"**Hoi** {e.sender.first_name} **Thx For Using Me Here is our Public repo🔥**"
    BUTTON = [
        [
            Button.url("【►Repo◄】", "https://github.com/Asta-vir/Flare-Robot"),
            Button.url("【►Owner◄】", "https://telegram.me/Asta_Silva02"),
        ]
    ]
    await aasf.send_file(
        e.chat_id,
        file=random.choice(HOTTIE_PICS),
        caption=k,
        parse_mode=ParseMode.HTML,
        buttons=BUTTON,
        reply_to=e,
    )
