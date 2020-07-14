import json
import os
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.DataFrame()

for file in os.listdir('data'):
    with open(os.path.join('data', file)) as infile:
        report = json.load(infile)['data'][0]

    for k in list(report.keys()):
        if 'split' not in k:
            del report[k]

    report['method'] = file.replace('.json', '')
    dataset = dataset.append(report,  ignore_index=True)


rf = dataset[dataset.method == 'rf']
rf_auc = [rf[column].iloc[0] for column in rf if 'average_precision' in column]
rf_mcc = [rf[column].iloc[0] for column in rf if 'mcc' in column]

isoforest = dataset[dataset.method == 'isoforest']
isoforest_auc = [isoforest[column].iloc[0] for column in isoforest if 'average_precision' in column]
isoforest_mcc = [isoforest[column].iloc[0] for column in isoforest if 'mcc' in column]

ocsvm = dataset[dataset.method == 'ocsvm']
ocsvm_auc = [ocsvm[column].iloc[0] for column in ocsvm if 'average_precision' in column]
ocsvm_mcc = [ocsvm[column].iloc[0] for column in ocsvm if 'mcc' in column]

localoutlier = dataset[dataset.method == 'localoutlier']
localoutlier_auc = [localoutlier[column].iloc[0] for column in localoutlier if 'average_precision' in column]
localoutlier_mcc = [localoutlier[column].iloc[0] for column in localoutlier if 'mcc' in column]

data_auc = [rf_auc, ocsvm_auc, localoutlier_auc, isoforest_auc]
fig, ax = plt.subplots()
ax.set_title('AUC-PR')
ax.boxplot(data_auc)
plt.xticks([1, 2, 3, 4], ['Random Forest', 'One-Class SVM', 'Local Outlier Factor', 'Isolation Forest'])
plt.show()

data_mcc = [rf_mcc,  ocsvm_mcc, localoutlier_mcc, isoforest_mcc]
fig, ax = plt.subplots()
ax.set_title('MCC')
ax.boxplot(data_mcc)
plt.xticks([1, 2, 3, 4], ['Random Forest', 'One-Class SVM', 'Local Outlier Factor', 'Isolation Forest'])
plt.show()