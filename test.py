import os
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv
import urllib
from urllib import request  # urllib.requestモジュールをインポート 
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート

load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)

def gpt_connect(input):
    full_url = f'https://lionmaru.blog/対{input}攻略ポイント-vipキャラ対策/'
    url = urllib.parse.quote(full_url, safe=':/')
    response = request.urlopen(url) 
    soup = BeautifulSoup(response) 
    response.close()
    topstories = soup.find('div', class_='cps-post-main-box') 
    scraped = topstories.get_text()

    comp = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role"   : "system",
            "content" : f"あなたは大乱闘スマッシュブラザーズのアシスタントです。ユーザーが指定したキャラの対策を参考記事をベースにかなり短めに回答してください。"},
            {"role"   : "user", 
            "content" : f"キャラ:{input}\n参考記事:{scraped}"}
        ]
    )
    message = comp.choices[0].message.content
    return message

chara_list = ["マリオの","ドンキーコング","リンク","サムス・ダムス","ヨッシー","カービィ","ネス","c-ファルコン","プリン","こどもリンク","ゼルダ","ドクターマリオ","ファルコ","マルスルキナ","ガノンドロフ","ロイ","リュカ","ソニック","メタナイト","スネーク","デデデ","ロボット","ウルフ","ロゼッタ＆チコ","ゲッコウガ","パルテナ","パックマン","クッパjr","カムイ","クラウド","リドリー","キングクルール","しずえ","ガオガエン","ジョーカー","-勇者-","テリー","ベレト・ベレス","ミェンミェン","スティーブ","セフィロス","ホムラヒカリ","カズヤ"]
demo = gr.Interface(
    fn=gpt_connect, 
    inputs= gr.Dropdown(choices = chara_list, label="対策したいキャラを入力してください"),
    outputs="text"
)

demo.launch()