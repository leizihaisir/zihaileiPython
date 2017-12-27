import pickle

d = dict(name='Bob', age=20, score=88)
# 序列化
pic = pickle.dumps(d)
print(pic)

# 反序列化
print(pickle.loads(pic))
