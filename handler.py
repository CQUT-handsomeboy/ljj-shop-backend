from nonebot.plugin import on_message
from nonebot.adapters import Event, Bot
from icecream import ic
from nonebot import get_bot, get_driver
from nonebot_plugin_apscheduler import scheduler

driver = get_driver()
bot = None

@driver.on_bot_connect
async def global_qq_bot_replace(_bot: Bot):
    global bot
    qq_account_number = driver.config.qq_account_number
    bot = get_bot(str(qq_account_number))


async def send_msg(msg: str):
    assert bot is not None, "机器人未连接"
    await bot.send_group_msg(
        group_id=driver.config.qq_target_group_number,
        message=msg,
    )


# 消息处理回调
"""
msg = on_message(block=False)
@msg.handle()
async def message_handler(bot: Bot, event: Event):
    pass
"""

# 定时任务
"""
def run_every_15s():
    pass
    
scheduler.add_job(
    run_every_15s, "interval", seconds=5, id="job_1")
"""
