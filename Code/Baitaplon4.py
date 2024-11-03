from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# 1.  Thu thập giá chuyển nhượng của các cầu thủ trong mùa 2023-2024 từ trang web https://www.footballtransfers.com

# base_url = "https://www.footballtransfers.com/us/transfers/confirmed/2023-2024/uk-premier-league/fee-to-200000000/"

# transfers = []
# headers = ["Player", "Price"]

# for page_num in range(1, 9):  
#     driver = webdriver.Chrome()
#     driver.get(base_url + str(page_num))
#     driver.implicitly_wait(10)
#     html = driver.page_source
#     soup = BeautifulSoup(html, 'html.parser')
#     table = soup.find("table", {'class':'table table-striped table-hover leaguetable mvp-table transfer-table mb-0'})
    
#     for row in table.find('tbody').find_all('tr'):
#         player_name = row.find_all('td')[0].find('span').get_text()
#         player_price = row.find_all('td')[3].find('span').get_text()
#         transfers.append([player_name, player_price])
# dfstats = pd.DataFrame(transfers, columns=headers)
# dfstats.to_csv('results4.csv')

# 2. Đề xuất phương pháp định giá cầu thủ

df_transfer = pd.read_csv('results4.csv')
df_stats = pd.read_csv('result.csv')

def convert_to_million(value):
    if isinstance(value, str) and value == "Free":
        return 0
    if isinstance(value, str) and value.endswith('K'):
        return float(value[1:-1]) / 1000
    else:
        return float(value[1:-1])
df_transfer['Price'] = df_transfer['Price'].apply(convert_to_million)

matched_data = df_transfer.merge(df_stats, on='Player', how='inner')
matched_data = matched_data.drop(columns=['Unnamed: 0_x', 'Unnamed: 0_y', 'Nation', 'Pos', 'Squad', 'Age', 'Born'])
matched_data.to_csv('resultkeeper.csv', index = False)

features = matched_data.loc[:, matched_data.columns[2:]]
features = features.apply(pd.to_numeric, errors='coerce').fillna(0)  
target = matched_data['Price']

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

player_name = input("Nhập tên cầu thủ để dự đoán giá trị chuyển nhượng: ")

if player_name in df_stats['Player'].values:
    player_stats = df_stats[df_stats['Player'] == player_name].loc[:, matched_data.columns[2:]]
    player_stats = player_stats.apply(pd.to_numeric, errors='coerce').fillna(0)
    
    predicted_price = model.predict(player_stats)
    print(f"Giá trị chuyển nhượng dự đoán cho {player_name}: €{round(predicted_price[0])}M")
else:
    print("Không tìm thấy cầu thủ trong dữ liệu.")