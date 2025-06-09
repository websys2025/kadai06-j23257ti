import requests
API_URL  = "https://api.data.metro.tokyo.lg.jp/v1/Covid19Patient?from=2020-04-01&till=2020-04-30&limit=100" #取得するAPIのURL(e-stat)
#新型コロナウイルス陽性患者発表詳細(2020年4月1日～2020年4月30日まで)　に関するAPI_URL

#東京都オープンデータカタログサイトより引用
#https://portal.data.metro.tokyo.lg.jp/opendata-api/

response = requests.get(API_URL) #出力処理
# Process the response
data = response.json()
print(data)
