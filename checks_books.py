import pickle

pt = pickle.load(open('pt.pkl', 'rb'))
print(pt.index[:20])  # First 20 book titles
