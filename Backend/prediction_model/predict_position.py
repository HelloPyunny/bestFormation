import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# load data
df = pd.read_csv('../../data/player_data/data_updated.csv')

# set features
selected_features = ['PAC', 'SHO', 'PAS', 'DRI', 'DEF', 'PHY', 'Acceleration',
       'Sprint Speed', 'Positioning', 'Finishing', 'Shot Power', 'Long Shots',
       'Volleys', 'Penalties', 'Vision', 'Crossing', 'Free Kick Accuracy',
       'Short Passing', 'Long Passing', 'Curve', 'Dribbling', 'Agility',
       'Balance', 'Reactions', 'Ball Control', 'Composure', 'Interceptions',
       'Heading Accuracy', 'Def Awareness', 'Standing Tackle', 'Sliding Tackle', 
       'Jumping', 'Stamina', 'Strength', 'Aggression', 'Skill moves', 'GK Diving',
       'GK Handling', 'GK Kicking', 'GK Positioning', 'GK Reflexes']

# set target
target = 'Position'

# Set X and y
X = df[selected_features]
y = df[target]

# train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])
pipeline.fit(X_train, y_train)
print(f"Sample size of [Position] training: {len(X_train)}")

from sklearn.metrics import accuracy_score

y_pred = pipeline.predict(X_test)  # predict test data
accuracy = accuracy_score(y_test, y_pred)  # calculate accuracy
print(f"model accuracy: {accuracy:.4f}") 

def predict_position(new_player_stats: dict):
    name = list(new_player_stats.keys())[0]
    stats = new_player_stats[name]
    
    # change data type to integer
    stats = {key: int(value) for key, value in stats.items()}
    
    new_data = pd.DataFrame([stats])
    prediction = pipeline.predict(new_data[selected_features])[0]
    
    return name, prediction

'''
if __name__ == '__main__':
    sample_input = {
    "Kylian Mbappé": 
        {
        "PAC": 97.0, "SHO": 90.0, "PAS": 80.0, "DRI": 92.0, "DEF": 36.0, "PHY": 78.0, 
        "Acceleration": 97.0, "Sprint Speed": 97.0, "Positioning": 93.0, "Finishing": 94.0, 
        "Shot Power": 90.0, "Long Shots": 83.0, "Volleys": 84.0, "Penalties": 84.0, 
        "Vision": 83.0, "Crossing": 78.0, "Free Kick Accuracy": 69.0, "Short Passing": 86.0, 
        "Long Passing": 71.0, "Curve": 80.0, "Dribbling": 93.0, "Agility": 93.0, 
        "Balance": 82.0, "Reactions": 93.0, "Ball Control": 92.0, "Composure": 88.0, 
        "Interceptions": 38.0, "Heading Accuracy": 73.0, "Def Awareness": 26.0, 
        "Standing Tackle": 34.0, "Sliding Tackle": 32.0, "Jumping": 88.0, "Stamina": 88.0, 
        "Strength": 77.0, "Aggression": 64.0, "Skill moves": 5.0, "Weak foot": 4.0, "Height": 182.0,
        "GK Diving": 0.0, "GK Handling": 0.0, "GK Kicking": 0.0, 
        "GK Positioning": 0.0, "GK Reflexes": 0.0
        }
    }
    name, result = predict_position(sample_input)
    print(f"선수 이름: {name}, 예측된 Position: {result}")
    
    '박준혁':    
        {
        'PAC': 60.0, 'SHO': 30.0, 'PAS': 52.0, 'DRI': 55.0, 'DEF': 62.0, 'PHY': 70.0, 
        'Acceleration': 62.0, 'Sprint Speed': 64.0, 'Positioning': 45.0, 'Finishing': 21.0, 
        'Shot Power': 43.0, 'Long Shots': 33.0, 'Volleys': 20.0, 'Penalties': 25.0, 
        'Vision': 52.0, 'Crossing': 30.0, 'Free Kick Accuracy': 20.0, 'Short Passing': 69.0, 
        'Long Passing': 60.0, 'Curve': 32.0, 'Dribbling': 50.0, 'Agility': 55.0, 
        'Balance': 48.0, 'Reactions': 55.0, 'Ball Control': 60.0, 'Composure': 62.0, 
        'Interceptions': 70.0, 'Heading Accuracy': 70.0, 'Def Awareness': 65.0, 
        'Standing Tackle': 65.0, 'Sliding Tackle': 62.0, 'Jumping': 74.0, 'Stamina': 65.0, 
        'Strength': 80.0, 'Aggression': 63.0, 'Skill moves': 2.0, 
        'GK Diving': 0.0, 'GK Handling': 0.0, 'GK Kicking': 0.0, 
        'GK Positioning': 0.0, 'GK Reflexes': 0.0
        }

'''