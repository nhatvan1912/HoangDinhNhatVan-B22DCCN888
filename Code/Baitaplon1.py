from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://fbref.com/en/comps/9/2023-2024/stats/2023-2024-Premier-League-Stats')

driver.implicitly_wait(10)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

table = soup.find("table", {'id':'stats_standard'})
headers_1 = [th.get_text() for th in table.find('thead').find_all('tr')[0].find_all('th')]
headers_2 = [th for th in table.find('thead').find_all('tr')[1].find_all('th')]

headers = []
for h2 in headers_2:
    check = 0
    for h1 in headers_1:
        if h1 == h2.get('data-over-header') :
            headers.append(f'{h1} {h2.get_text()}')
            check = 1
    if check == 0:    
        headers.append(h2.get_text())
player_data = []
for row in table.find('tbody').find_all('tr'):
    if row.find('td', {'data-stat': 'player'}):
        player = [td.text if td.text.strip() else "0" for td in row.find_all('td')] 
        minutes_played_text = player[8]
        minutes_played = int(minutes_played_text.replace(',', '')) if minutes_played_text else 0
        player[8] = minutes_played
        if minutes_played > 90:
            player_data.append(player)
            
dfstats = pd.DataFrame(player_data, columns=headers[1:])  

dfstats['Age'] = pd.to_numeric(dfstats['Age'], errors='coerce')  
dfstats = dfstats.sort_values(by=['Player', 'Age'], ascending=[True, False])
dfstats = dfstats.drop(columns=['Matches'])



driver.get('https://fbref.com/en/comps/9/2023-2024/keepers/2023-2024-Premier-League-Stats')

driver.implicitly_wait(10)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

table_keeper = soup.find("table", {'id':'stats_keeper'})
headers_1 = [th.get_text() for th in table_keeper.find('thead').find_all('tr')[0].find_all('th')]
headers_2 = [th for th in table_keeper.find('thead').find_all('tr')[1].find_all('th')]

headers_keeper = []
for h2 in headers_2:
    check = 0
    for h1 in headers_1:
        if h1 == h2.get('data-over-header') :
            headers_keeper.append(f'Keeper {h1} {h2.get_text()}')
            check = 1
    if check == 0:    
        headers_keeper.append(h2.get_text())
player_data = []
for row in table_keeper.find('tbody').find_all('tr'):
    if row.find('td', {'data-stat': 'player'}):
        player = [td.text if td.text.strip() else "0" for td in row.find_all('td')]
        player_data.append(player)
        
df_keeper = pd.DataFrame(player_data, columns=headers_keeper[1:])

df_keeper = df_keeper.drop(columns=['Age', 'Keeper Playing Time MP', 'Keeper Playing Time Starts', 'Keeper Playing Time Min', 'Keeper Playing Time 90s', 'Matches'])
df_keeper.to_csv('resultkeeper.csv')
df_merged_stats = pd.merge(dfstats, df_keeper, on=['Player','Nation', 'Pos', 'Squad', 'Born'], how='left')



driver.get('https://fbref.com/en/comps/9/2023-2024/shooting/2023-2024-Premier-League-Stats')

driver.implicitly_wait(10)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

table_shooting = soup.find("table", {'id':'stats_shooting'})
headers_1 = [th.get_text() for th in table_shooting.find('thead').find_all('tr')[0].find_all('th')]
headers_2 = [th for th in table_shooting.find('thead').find_all('tr')[1].find_all('th')]

headers_shooting = []
for h2 in headers_2:
    check = 0
    for h1 in headers_1:
        if h1 == h2.get('data-over-header') :
            headers_shooting.append(f'Shooting {h1} {h2.get_text()}')
            check = 1
    if check == 0:    
        headers_shooting.append(h2.get_text())
player_data = []
for row in table_shooting.find('tbody').find_all('tr'):
    if row.find('td', {'data-stat': 'player'}):
        player = [td.text if td.text.strip() else "0" for td in row.find_all('td')]
        player_data.append(player)
        
df_shooting = pd.DataFrame(player_data, columns=headers_shooting[1:])

df_shooting = df_shooting.drop(columns=['Age', '90s', 'Matches'])

df_merged_stats = pd.merge(df_merged_stats, df_shooting, on=['Player','Nation', 'Pos', 'Squad', 'Born'], how='left')



driver.get('https://fbref.com/en/comps/9/2023-2024/passing/2023-2024-Premier-League-Stats')

driver.implicitly_wait(10)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

table_passing = soup.find("table", {'id':'stats_passing'})
headers_1 = [th.get_text() for th in table_passing.find('thead').find_all('tr')[0].find_all('th')]
headers_2 = [th for th in table_passing.find('thead').find_all('tr')[1].find_all('th')]

headers_passing = []
for h2 in headers_2:
    check = 0
    for h1 in headers_1:
        if h1 == h2.get('data-over-header') :
            headers_passing.append(f'Passing {h1} {h2.get_text()}')
            check = 1
    if check == 0:    
        headers_passing.append(h2.get_text())
player_data = []
for row in table_passing.find('tbody').find_all('tr'):
    if row.find('td', {'data-stat': 'player'}):
        player = [td.text if td.text.strip() else "0" for td in row.find_all('td')]
        player_data.append(player)
        
df_passing = pd.DataFrame(player_data, columns=headers_passing[1:])

df_passing = df_passing.drop(columns=['Age', '90s', 'Matches'])

df_merged_stats = pd.merge(df_merged_stats, df_passing, on=['Player','Nation', 'Pos', 'Squad', 'Born'], how='left')


driver.get('https://fbref.com/en/comps/9/2023-2024/passing_types/2023-2024-Premier-League-Stats')

driver.implicitly_wait(10)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

table_passing_types = soup.find("table", {'id':'stats_passing_types'})
headers_1 = [th.get_text() for th in table_passing_types.find('thead').find_all('tr')[0].find_all('th')]
headers_2 = [th for th in table_passing_types.find('thead').find_all('tr')[1].find_all('th')]

headers_passing_types = []
for h2 in headers_2:
    check = 0
    for h1 in headers_1:
        if h1 == h2.get('data-over-header') :
            headers_passing_types.append(f'Pass Types {h1} {h2.get_text()}')
            check = 1
    if check == 0:    
        headers_passing_types.append(h2.get_text())
player_data = []
for row in table_passing_types.find('tbody').find_all('tr'):
    if row.find('td', {'data-stat': 'player'}):
        player = [td.text if td.text.strip() else "0" for td in row.find_all('td')]
        player_data.append(player)
        
df_passing_types = pd.DataFrame(player_data, columns=headers_passing_types[1:])

df_passing_types = df_passing_types.drop(columns=['Age', '90s', 'Att', 'Matches'])

df_merged_stats = pd.merge(df_merged_stats, df_passing_types, on=['Player','Nation', 'Pos', 'Squad', 'Born'], how='left')



driver.get('https://fbref.com/en/comps/9/2023-2024/gca/2023-2024-Premier-League-Stats')

driver.implicitly_wait(10)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

table_gca = soup.find("table", {'id':'stats_gca'})
headers_1 = [th.get_text() for th in table_gca.find('thead').find_all('tr')[0].find_all('th')]
headers_2 = [th for th in table_gca.find('thead').find_all('tr')[1].find_all('th')]

headers_gca = []
for h2 in headers_2:
    check = 0
    for h1 in headers_1:
        if h1 == h2.get('data-over-header') :
            headers_gca.append(f'Goal and Shot Creation {h1} {h2.get_text()}')
            check = 1
    if check == 0:    
        headers_gca.append(h2.get_text())
player_data = []
for row in table_gca.find('tbody').find_all('tr'):
    if row.find('td', {'data-stat': 'player'}):
        player = [td.text if td.text.strip() else "0" for td in row.find_all('td')]
        player_data.append(player)
        
df_gca = pd.DataFrame(player_data, columns=headers_gca[1:])

df_gca = df_gca.drop(columns=['Age', '90s', 'Matches'])

df_merged_stats = pd.merge(df_merged_stats, df_gca, on=['Player','Nation', 'Pos', 'Squad', 'Born'], how='left')



driver.get('https://fbref.com/en/comps/9/2023-2024/defense/2023-2024-Premier-League-Stats')

driver.implicitly_wait(10)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

table_defense = soup.find("table", {'id':'stats_defense'})
headers_1 = [th.get_text() for th in table_defense.find('thead').find_all('tr')[0].find_all('th')]
headers_2 = [th for th in table_defense.find('thead').find_all('tr')[1].find_all('th')]

headers_defense = []
for h2 in headers_2:
    check = 0
    for h1 in headers_1:
        if h1 == h2.get('data-over-header') :
            headers_defense.append(f'Defensive Actions {h1} {h2.get_text()}')
            check = 1
    if check == 0:    
        headers_defense.append(h2.get_text())
player_data = []
for row in table_defense.find('tbody').find_all('tr'):
    if row.find('td', {'data-stat': 'player'}):
        player = [td.text if td.text.strip() else "0" for td in row.find_all('td')]
        player_data.append(player)
        
df_defense = pd.DataFrame(player_data, columns=headers_defense[1:])

df_defense = df_defense.drop(columns=['Age', '90s', 'Matches'])

df_merged_stats = pd.merge(df_merged_stats, df_defense, on=['Player','Nation', 'Pos', 'Squad', 'Born'], how='left')



driver.get('https://fbref.com/en/comps/9/2023-2024/possession/2023-2024-Premier-League-Stats')

driver.implicitly_wait(10)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

table_possession = soup.find("table", {'id':'stats_possession'})
headers_1 = [th.get_text() for th in table_possession.find('thead').find_all('tr')[0].find_all('th')]
headers_2 = [th for th in table_possession.find('thead').find_all('tr')[1].find_all('th')]

headers_possession = []
for h2 in headers_2:
    check = 0
    for h1 in headers_1:
        if h1 == h2.get('data-over-header') :
            headers_possession.append(f'Possession {h1} {h2.get_text()}')
            check = 1
    if check == 0:    
        headers_possession.append(h2.get_text())
player_data = []
for row in table_possession.find('tbody').find_all('tr'):
    if row.find('td', {'data-stat': 'player'}):
        player = [td.text if td.text.strip() else "0" for td in row.find_all('td')]
        player_data.append(player)
        
df_possession = pd.DataFrame(player_data, columns=headers_possession[1:])

df_possession = df_possession.drop(columns=['Age', '90s', 'Matches'])

df_merged_stats = pd.merge(df_merged_stats, df_possession, on=['Player','Nation', 'Pos', 'Squad', 'Born'], how='left')



driver.get('https://fbref.com/en/comps/9/2023-2024/playingtime/2023-2024-Premier-League-Stats')

driver.implicitly_wait(10)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

table_playingtime = soup.find("table", {'id':'stats_playing_time'})
headers_1 = [th.get_text() for th in table_playingtime.find('thead').find_all('tr')[0].find_all('th')]
headers_2 = [th for th in table_playingtime.find('thead').find_all('tr')[1].find_all('th')]

headers_playingtime = []
for h2 in headers_2:
    check = 0
    for h1 in headers_1:
        if h1 == h2.get('data-over-header') :
            headers_playingtime.append(f'Playing Time {h1} {h2.get_text()}')
            check = 1
    if check == 0:    
        headers_playingtime.append(h2.get_text())
player_data = []
for row in table_playingtime.find('tbody').find_all('tr'):
    if row.find('td', {'data-stat': 'player'}):
        player = [td.text if td.text.strip() else "0" for td in row.find_all('td')]
        player_data.append(player)
        
df_playingtime = pd.DataFrame(player_data, columns=headers_playingtime[1:])

df_playingtime = df_playingtime.drop(columns=['Age', 'Playing Time Playing Time MP', 'Playing Time Playing Time Min', 'Playing Time Playing Time Mn/MP', 'Playing Time Playing Time Min%', 'Playing Time Playing Time 90s', 'Playing Time Team Success +/-', 'Playing Time Team Success +/-90', 'Playing Time Team Success On-Off', 'Playing Time Team Success (xG) xG+/-', 'Playing Time Team Success (xG) xG+/-90', 'Playing Time Team Success (xG) On-Off', 'Matches'])

df_merged_stats = pd.merge(df_merged_stats, df_playingtime, on=['Player','Nation', 'Pos', 'Squad', 'Born'], how='left')



driver.get('https://fbref.com/en/comps/9/2023-2024/misc/2023-2024-Premier-League-Stats')

driver.implicitly_wait(10)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

table_misc = soup.find("table", {'id':'stats_misc'})
headers_1 = [th.get_text() for th in table_misc.find('thead').find_all('tr')[0].find_all('th')]
headers_2 = [th for th in table_misc.find('thead').find_all('tr')[1].find_all('th')]

headers_misc = []
for h2 in headers_2:
    check = 0
    for h1 in headers_1:
        if h1 == h2.get('data-over-header') :
            headers_misc.append(f'Miscellaneous Stats {h1} {h2.get_text()}')
            check = 1
    if check == 0:    
        headers_misc.append(h2.get_text())
player_data = []
for row in table_misc.find('tbody').find_all('tr'):
    if row.find('td', {'data-stat': 'player'}):
        player = [td.text if td.text.strip() else "0" for td in row.find_all('td')]
        player_data.append(player)
        
df_misc = pd.DataFrame(player_data, columns=headers_misc[1:])

df_misc = df_misc.drop(columns=['Age', '90s', 'Miscellaneous Stats Performance CrdY', 'Miscellaneous Stats Performance 2CrdY', 'Miscellaneous Stats Performance CrdR', 'Miscellaneous Stats Performance Int', 'Miscellaneous Stats Performance TklW', 'Miscellaneous Stats Performance PKwon', 'Miscellaneous Stats Performance PKcon', 'Matches'])

df_merged_stats = pd.merge(df_merged_stats, df_misc, on=['Player','Nation', 'Pos', 'Squad', 'Born'], how='left')

# Xử lý các chỉ số không có giá trị hoặc không áp dụng
df_merged_stats = df_merged_stats.fillna('N/a')
df_merged_stats.to_csv('result.csv')