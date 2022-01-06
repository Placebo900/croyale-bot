FROM ubuntu:21.04

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get install --yes pip\
    python3.9

COPY analyze_* ./clashroyale_api/
COPY royale.py ./clashroyale_api/
COPY tg_bot.py ./clashroyale_api/
COPY instruction_help ./clashroyale_api/


RUN pip install requests; pip install telebot; pip install PyTelegramBotAPI
CMD cd ./clashroyale_api/ && python3 ./tg_bot.py