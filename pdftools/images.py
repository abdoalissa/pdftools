import os
import shutil
from pyrogram import Client, filters
from pdftools.core import images_to_pdf
from pyrogram.types import Message
from pdftools.callbacks import cancelled

image_converting = {}


@Client.on_message(filters.private & filters.photo & filters.incoming)
async def img2pdf(bot: Client, msg: Message):
    user_id = msg.from_user.id
    if user_id in image_converting and image_converting[user_id]:
        return
    image_converting[user_id] = True
    directory = f"downloads/{msg.from_user.id}_images/"
    output = f"{directory}{user_id}_images.pdf"
    await msg.download(file_name=directory)
    image_msg = await bot.ask(user_id, "الرجاء ارسال المزيد من الصور او اضغط على /create لتوليد ملف pdf. \n\nلالغاء العملية اضغط  /cancel.", reply_to_message_id=msg.message_id)
    while True:
        if await cancelled(image_msg):
            break
        elif image_msg.text and image_msg.text.lower() == "/create":
            image_converting[user_id] = False
            paths = [directory + file for file in os.listdir(directory)]
            await images_to_pdf(paths, output)
            await msg.reply_document(output, caption=f"Converted {len(paths)} images to PDF \n\nBy @abdoalissa")
            break
        elif not image_msg.photo:
            image_msg = await bot.ask(user_id, "هذا الملف ليس صورة الرجاء ارسال صورة او اضغط /cancel.", reply_to_message_id=image_msg.message_id)
            continue
        else:
            await image_msg.download(file_name=directory)
            total_images = len(os.listdir(directory))
            image_msg = await bot.ask(user_id, f"الرجاء ارسال المزيد من الصور او اضغط /create. لالغاء العملية استخدم /cancel. \n\nمجموع الصور حتى الان : {total_images}", reply_to_message_id=image_msg.message_id)
    image_converting[user_id] = False
    shutil.rmtree(directory)
