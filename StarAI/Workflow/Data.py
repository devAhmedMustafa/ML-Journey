import pandas as pd
from StarAI.Utils.StrUtils import *
from StarAI.Utils.FrameUtils import *
from sklearn.model_selection import train_test_split

feature_map = {}


def choose_features(df: pd.DataFrame, y_feature, ignored):
    y = df[y_feature]
    x = df.drop(columns=ignored+[y_feature], axis=1)

    return x, y


def normalize_data(df):
    for feature in df:

        if df[feature].dtype != "object":
            continue

        df[feature] = upper_feature(df[feature])

        if feature not in feature_map:
            feature_map[feature] = {}

        idx = 0

        casted = np.array(df[feature])
        for x in casted:

            if x not in feature_map[feature]:
                feature_map[feature][x] = str_to_int(x)

            casted[idx] = feature_map[feature][x]

            idx += 1

        df[feature] = casted

    return df


def clean_data(path, y_feature, ignored, test_size=0.3):
    df = pd.read_csv(path)
    df = normalize_data(df)

    x, y = choose_features(df, y_feature, ignored)

    return train_test_split(x, y, test_size=test_size, random_state=1234)
