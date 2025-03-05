import pandas as pd
import numpy as np

def entropy(data, label):
    houses = pd.unique(data[label])
    total = data.shape[0]
    entropy = 0

    for c in houses:
        n = data[data[label] == c].shape[0]
        if n != 0:
            entropy += -(n/total)*np.log2(n/total)

    return entropy

def information(data, feature, label):
    info = 0
    choices = pd.unique(data[feature])

    for c in choices:
        no_cat_choice = data[data[feature] == c].shape[0]
        entropy_cat_choice = entropy(data[data[feature] == c], label)
        info += (no_cat_choice/size)*entropy_cat_choice

    return info

def max_gain(data, label):
    Info_Gain = {}
    feature_list = data.columns[:-1]

    for feature in feature_list:
        Info_Gain[feature] = (total_entropy - information(data, feature, label))
        
    return max(Info_Gain, key = Info_Gain.get)

def branch(data, max_feature, label):
    branch = {}
    choices = pd.unique(data[max_feature])
    
    for c in choices:
        if len(pd.unique(data[data[max_feature] == c][label])) == 1:
            branch[c] = str(pd.unique(data[data[max_feature] == c][label])[0])
            data = data[data[max_feature] != c]
        else:
            branch[c] = '?'
    return branch, data

def tree(data, root, prev_value, label):
    if data.shape[0] != 0:
        maximum = max_gain(data, label)
        sub_tree, data = branch(data, maximum, label)

        if prev_value != None:
            root[prev_value] = dict()
            root[prev_value][maximum] = sub_tree
            next_root = root[prev_value][maximum]

        else:
            root[maximum] = sub_tree
            next_root = root[maximum]
            
        for key, value in next_root.items():
            if value == '?':
                tree(data[data[maximum] == key], next_root, key, label)
    return root

def prediction(data, tree):
    if type(tree) != str:
        category = list(tree.keys())[0]
        if data[category] not in list(tree[category].keys()):
            return None
        else:
            return prediction(data, tree[category][data[category]])
    else:
        return tree

def accuracy(data, tree, label):
    correct = 0
    unsure = 0
    for i in range(data.shape[0]):
        result = prediction(data.iloc[i], tree)
        if result == data.iloc[i][label]:
            correct += 1
        if result == None:
            unsure += 1
    return 100*correct / data.shape[0], 100*unsure / data.shape[0]
            

Data = pd.read_csv("Tennis.csv")
size = Data.shape[0]
label = Data.columns.values[-1]

print(label)
'''
total_entropy = entropy(Data, label)

Id3 = tree(Data, dict(), None, label)
test_data = pd.read_csv("Congress_data_test.csv")
correct, unsure = accuracy(test_data, Id3, label)
print('Model was %.2f%% correct' % correct)
print('Model was %.2f%% indeterminate' % unsure)
'''