import RPi.GPIO as GPIO
import jtalk
import socket
import random
import time

# センサーの設定
GPIO_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)

host = '127.0.0.1'
port = 10500

# juliusに接続する準備
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

# 天気予報の情報を取得する関数


def weather_forecast(when, where):
    # code ...
    # returnで"今日の天気は○○です"的な文字列を取得する予定
    return 'weather'

# スケジュール情報を取得する関数


def tell_schedule(when):
    # code ...
    # returnで"今日の予定は○○です"的な文字列を取得する予定
    return 'schedule'


# どこかでトリガー用意して、そこで「もしセンサーで人を検知したらこのファイルを出力する」って処理を作ったらwhileいらんくなって処理軽くなりそう
while True:
    if (GPIO.input(GPIO_PIN) == GPIO.HIGH):
        # 時間に応じて分岐する処理を作る
        jtalk.jtalk(u'おはようございます')
        time.sleep(1)
        # 最終的にweather_forecast()関数を入れ込む
        jtalk.jtalk(u'今日の天気は晴れです')
        time.sleep(1)
        # 最終的にtell_schedule()関数を入れ込む
        jtalk.jtalk(u'今日の予定はミーティングです')
        break
    # elif (GPIO.input(GPIO_PIN) == GPIO.LOW):
    #     print('0')

GPIO.cleanup()
