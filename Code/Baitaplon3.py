from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import seaborn as sns
from sklearn.decomposition import PCA

# # 1. Phân loại các cầu thủ thành các nhóm có chỉ số giống nhau
# df = pd.read_csv('result.csv')
# features = df.loc[:, df.columns[7:]]
# features = features.map(lambda x: pd.to_numeric(x, errors='coerce')).fillna(0)

# scaler = StandardScaler()
# scaled_features = scaler.fit_transform(features)

# inertia = []
# for k in range(2, 11):
#     kmeans = KMeans(n_clusters=k, random_state=42)
#     kmeans.fit(scaled_features)
#     inertia.append(kmeans.inertia_)

# plt.plot(range(2, 11), inertia, marker='o')
# plt.title('Phương pháp Elbow')
# plt.xlabel('Số cụm')
# plt.ylabel('Inertia')
# plt.show()

# for k in range(2, 11):
#     kmeans = KMeans(n_clusters=k)
#     kmeans.fit(scaled_features)
#     print(f"Silhouette Score cho {k} cụm: {silhouette_score(scaled_features, kmeans.labels_)}")
    
    
# # 2. Sử dụng thuật toán PCA giảm số chiều dữ liệu xuống 2 chiều, vẽ hình phân cụm các điểm dữ liệu
# pca = PCA(n_components=2)
# pca_result = pca.fit_transform(scaled_features)

# pca_df = pd.DataFrame(pca_result, columns=['PC1', 'PC2'])
# kmeans = KMeans(n_clusters = 5)
# kmeans.fit(pca_result)
# pca_df['Cluster'] = kmeans.labels_

# plt.figure(figsize=(8, 6))
# sns.scatterplot(x='PC1', y='PC2', hue='Cluster', data=pca_df, palette='viridis')
# plt.title('PCA of Player Clusters')
# plt.show()

# 3. Chương trình Python vẽ biểu đồ rada so sánh cầu thủ
def radar_chart(player1_data, player2_data, attributes, player1_name, player2_name):
    num_vars = len(attributes)

    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    player1_data += player1_data[:1]
    player2_data += player2_data[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    ax.fill(angles, player1_data, color='red', alpha=0.25)
    ax.fill(angles, player2_data, color='blue', alpha=0.25)

    ax.plot(angles, player1_data, color='red', linewidth=2, label=player1_name)
    ax.plot(angles, player2_data, color='blue', linewidth=2, label=player2_name)

    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes)

    plt.legend(loc='upper right')
    plt.title(f'{player1_name} vs {player2_name} Comparison')
    plt.show()

df = pd.read_csv('result.csv')

player1_name = input("Nhập tên cầu thủ thứ nhất: ")
player2_name = input("Nhập tên cầu thủ thứ hai: ")

attributes = []
while True:
    attribute = input("Nhập tên thuộc tính (hoặc 'xong' để kết thúc): ")
    if attribute.lower() == 'xong':
        break
    attributes.append(attribute)

player1_data = df[df['Player'] == player1_name][attributes].values.flatten().tolist()
player2_data = df[df['Player'] == player2_name][attributes].values.flatten().tolist()

radar_chart(player1_data, player2_data, attributes, player1_name, player2_name)