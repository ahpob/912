import requests
import os
import json
import time
import datetime
from discord import SyncWebhook

discord_url = os.environ['Discord_Url']
webhook = SyncWebhook.from_url(discord_url)


url = 'https://ticket.melon.com/reservation/popup/tktapi/product/block/summary.json?v=1&prodId=208654&pocCode=SC0002&scheduleNo=100002&seatGradeNo=&corpCodeNo='

headers = {
    'Referer': 'ticket.melon.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}
current_time = datetime.datetime.now()
adjusted_time = current_time + datetime.timedelta(hours=9)
formatted_time = adjusted_time.strftime("%H:%M:%S")
webhook.send(f"{formatted_time} - {initial[i]}")
