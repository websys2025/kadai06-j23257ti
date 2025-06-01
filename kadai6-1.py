import requests
import pandas as pd
APP_ID = "e7d82909c4b9e45b2e67ebbfb8b3d9c95f112e24" #作成したAPPID
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData" #取得するAPIのURL(e-stat)
params = {
    "appId": "e7d82909c4b9e45b2e67ebbfb8b3d9c95f112e24", #作成したAPPID
    "statsDataId":"0002122522", #作物統計調査、都道府県別の作付面積、10a当たり収量、収穫量及び出荷量（ブロッコリー）
    "metaGetFlg":"Y",#統計データと一緒にメタ情報を取得するかの確認
    "cntGetFlg":"N", #件数取得の有無
    "explanationGetFlg":"Y", #統計表について解説を追記有無
    "annotationGetFlg":"Y", #数値データについての注釈有無
    "sectionHeaderFlg":"1", #データの区切り目印の出力有無
    "replaceSpChars":"0", #特殊文字の置き換え有無(0がデフォルト)
    "lang":"J" #言語設定（今回は日本語）
}
response = requests.get(API_URL, params=params) #API_URLとparamsを取得し、"response"へ
data = response.json() #responceをjson形式で、dataへ
print(data)