# stat_autofill.py

import sqlite3
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# load data from SQLite
db_file = '../../Data/players.db'
conn = sqlite3.connect(db_file)
# load all the data from players table to DataFrame
df = pd.read_sql_query("SELECT * FROM players", conn)
conn.close()

print("data loaded. data shape:", df.shape)

# Set target and feature
input_cols = ['Position', 'PAC', 'SHO', 'PAS', 'DRI', 'DEF', 'PHY', 'Skill moves', 'Weak foot', 'Height']

# Set target
target_cols = ['Acceleration', 'Sprint Speed', 'Positioning', 'Finishing', 'Shot Power', 
               'Long Shots', 'Volleys', 'Penalties', 'Vision', 'Crossing', 'Free Kick Accuracy',
               'Short Passing', 'Long Passing', 'Curve', 'Dribbling', 'Agility', 'Balance', 
               'Reactions', 'Ball Control', 'Composure', 'Interceptions', 'Heading Accuracy', 
               'Def Awareness', 'Standing Tackle', 'Sliding Tackle', 'Jumping', 'Stamina', 
               'Strength', 'Aggression']

# Set X and y
X = df[input_cols]
y = df[target_cols]

print("Feature and Target set")

# 3. 전처리: 'Position'은 범주형이므로 OneHotEncoding 처리
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['Position'])
    ],
    remainder='passthrough'  # 나머지 숫자형 데이터는 그대로 사용
)

# 4. 모델 파이프라인 구성
# MultiOutputRegressor를 사용해 각 타겟 컬럼에 대해 랜덤 포레스트 회귀를 적용
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', MultiOutputRegressor(RandomForestRegressor(random_state=42)))
])

# 5. 학습/테스트 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. 모델 학습
model.fit(X_train, y_train)

# 7. 모델 평가 (평균 제곱 오차 사용)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# 8. 새로운 플레이어의 입력값으로 나머지 스탯 예측 함수
def predict_player_stats(position, PAC, SHO, PAS, DRI, DEF, PHY, skill_moves, weak_foot, height):
    # 입력 데이터를 DataFrame 형식으로 생성
    input_data = pd.DataFrame({
        'Position': [position],
        'PAC': [PAC],
        'SHO': [SHO],
        'PAS': [PAS],
        'DRI': [DRI],
        'DEF': [DEF],
        'PHY': [PHY],
        'Skill moves': [skill_moves],
        'Weak foot': [weak_foot],
        'Height': [height]
    })
    
    # 예측 수행
    pred = model.predict(input_data)
    # 예측 결과를 타겟 컬럼 이름과 매핑하여 딕셔너리로 반환
    return dict(zip(target_cols, pred[0]))

# 9. 예제 사용법
# 예를 들어, 'ST'(스트라이커) 포지션과 해당 스탯을 가진 플레이어의 나머지 스탯 예측
new_player_stats = predict_player_stats('ST', 80, 85, 78, 82, 60, 70, 3, 4, 180)
print("Predicted stats for the new player:")
for stat, value in new_player_stats.items():
    print(f"{stat}: {value}")