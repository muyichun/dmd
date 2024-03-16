import numpy as np

# 创建一个布尔数组
bool_array = np.array([[True, False, True,False,True],
                       [False, True, False,True,True]])

# 将布尔数组压缩为字节数组
packed_data = np.packbits(bool_array, axis=None)

# 打印压缩后的数据
print(packed_data)