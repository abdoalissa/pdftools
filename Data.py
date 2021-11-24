from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
مرحبا {}

مرحب بك في {}

يستطيع هذا البوت مساعدتك في بعض خدمات ملفات pdf
مثل تحويل الصور الى ملف pdf
استخدم الامر /help لرؤية المزيد من الخدمات

فقط ارسل ملف pdf او صورة لبدء العمل

By @abdoalissa
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 الصفحة الرئيسية 🏠", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ لمزيد من البوتات ✨", url="https://t.me/abdoalissa")],
        [
            InlineKeyboardButton("كيفية الاستخدام ❔", callback_data="help"),
            InlineKeyboardButton("🎪 حول 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ التواصل مع المطور ♥", url="https://t.me/abdoalissa")],
    ]

    # Help Message
    HELP = """
**الاستخدام**

1) فقط ارسل ملف pdf  لبدء العمل
2) او ارسل صورة لتحويلها لملف pdf

**الوظائف**
1) تدوير صفحات pdf
2) دمج ملفات pdf
3) تشفير ملف pdf
4) فك تشفير ملف pdf
5) تحويل الصور لملفات pdf
"""

    # About Message
    ABOUT = """
**حول هذا البوت** 
Source Code : يرجى التواصل معي :)

Language : [Python](www.python.org)

Developer : @abdoalissa
    """
