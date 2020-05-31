import pickle

list_1 = [1, 2, 3, 4, 5]
list_pkl = open('list.pkl', 'wb')
pickle.dump(list_1, list_pkl)

list_pkl = open('list.pkl', 'rb')
print(pickle.load(list_pkl))