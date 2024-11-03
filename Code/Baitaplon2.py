import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv('result.csv')
attributes = df.columns[7:]

# 1. Tìm top 3 cầu thủ có điểm cao nhất và thấp nhất ở mỗi chỉ số

# top3_results = []
# for col in df.columns[2:]:
#     df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# for attr in attributes:
#     top3_highest = df.nlargest(3, attr)[['Player', attr]]
#     for index, row in top3_highest.iterrows():
#         top3_results.append({
#             'Attribute': attr,
#             'Type': 'Highest',
#             'Player': row['Player'],
#             'Value': row[attr]
#         })
#     top3_lowest = df.nsmallest(3, attr)[['Player', attr]]
#     for index, row in top3_lowest.iterrows():
#         top3_results.append({
#             'Attribute': attr,
#             'Type': 'Lowest',
#             'Player': row['Player'],
#             'Value': row[attr]
#         })

# top3_df = pd.DataFrame(top3_results)
# top3_df.to_csv('top3_results.csv', index=False)
# print("Kết quả đã được lưu vào file top3_results.csv")

# 2. Tính trung vị, trung bình, và độ lệch chuẩn của mỗi chỉ số theo từng đội và toàn giải

teams = df['Squad'].unique()

# stats = ['Median', 'Mean', 'Std']
# columns = ['Team']  

# for col in attributes:
#     for stat in stats:
#         columns.append(f'{stat} of {col}')
        
# result_df = pd.DataFrame(columns=columns)

# team_data = ['all']
# for col in attributes:
#     numeric_col = pd.to_numeric(df[col], errors='coerce')
#     team_data.append(numeric_col.median())
#     team_data.append(numeric_col.mean())
#     team_data.append(numeric_col.std())
        
# result_df.loc[0] = team_data

# for i, team in enumerate(teams):
#     team_data = [team]
#     team_df = df[df['Squad'] == team]
    
#     for col in attributes:
#         numeric_col = pd.to_numeric(team_df[col], errors='coerce')
#         team_data.append(numeric_col.median())
#         team_data.append(numeric_col.mean())
#         team_data.append(numeric_col.std())

#     result_df.loc[i+1] = team_data

# result_df.to_csv('results2.csv')
# print("Đã ghi kết quả vào file results2.csv")

# # 3. Vẽ biểu đồ histogram cho mỗi chỉ số

# save_path = f"D:/CodePython/Histograms"

# for attr in attributes:
#     plt.figure(figsize=(10, 6))  
#     df[attr] = pd.to_numeric(df[attr], errors='coerce') 
#     df[attr].dropna().hist(bins=30, color='blue', alpha=0.7)
#     plt.title(f'Histogram of {attr} for all players')  
#     plt.xlabel(attr)  
#     plt.ylabel('Frequency')  
#     plt.grid(False) 
#     safe_attr = attr.replace("/", "_")
#     plt.savefig(f'{save_path}/Allplayers {safe_attr} Histogram.png') 
#     plt.show()  
    
# for team in teams:
#     team_df = df[df['Squad'] == team]  
#     for attr in attributes:
#         plt.figure(figsize=(10, 6)) 
#         team_df[attr] = pd.to_numeric(team_df[attr], errors='coerce')  
#         team_df[attr].dropna().hist(bins=20, color='green', alpha=0.7)  
#         plt.title(f'Histogram of {attr} for {team}') 
#         plt.xlabel(attr)  
#         plt.ylabel('Frequency') 
#         plt.grid(False)  
#         safe_attr = attr.replace("/", "_")
#         plt.savefig(f'{save_path}/{team} {safe_attr} Histogram.png')  
#         plt.show() 

# 4. Tìm đội bóng có chỉ số cao nhất ở mỗi chỉ số

df = pd.read_csv('results2.csv')

mean_columns = [col for col in df.columns if 'Mean of' in col]

best_teams = {}
cnt = {}

for col in mean_columns:
    best_team = df.loc[df[col].idxmax(), 'Team']
    best_value = df[col].max()
    best_teams[col] = (best_team, best_value)
    if best_team in cnt:
        cnt[best_team]+=1
    else: cnt[best_team] = 1

print("Đội có chỉ số trung binh cao nhất cho từng chỉ số:")
for col, (team, value) in best_teams.items():
    print(f"{col}: {team} với giá trị {value}")

list = sorted(cnt, key=lambda i: cnt[i])
print("Đội có phong độ tốt nhất giải ngoại Hạng Anh mùa 2023-2024: " + list[len(list) - 1])
