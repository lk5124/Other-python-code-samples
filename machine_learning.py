import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier

def fines():

    df = pd.read_csv('train.csv', encoding = "ISO-8859-1")
    df.index = df['ticket_id']
    features = ['fine_amount', 'admin_fee', 'state_fee', 'late_fee','discount_amount', 'clean_up_cost', 'judgment_amount']

    df.compliance = df.compliance.fillna(value=-1)
    df = df[df.compliance!=-1]
    df_X = df[features]
    df_X = df_X.fillna(value = -1)
    df_y = df['compliance']
    df_y = df_y.fillna(value = -1)

    X = df_X
    y = df_y

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
    model = RandomForestClassifier(n_estimators = 20, max_depth = 5).fit(X_train, y_train)
    df_test = pd.read_csv('data.csv', encoding = "ISO-8859-1")
    df_test.index = df_test['ticket_id']

    X_test_ii = df_test[features]

    predicted = model.predict_proba(X_test_ii)

    return pd.Series(data = predicted[:,1], index = df_test['ticket_id'])
