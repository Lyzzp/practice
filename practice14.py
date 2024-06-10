# encoding:utf-8
"""
@Time:2024/6/9 21:11
@Project:PyCharm
@Name:practice14
@AUTH:lyzzp
"""
import pandas as pd


def check_method():
    print("check")


def set_method():
    print("set")


def add_method():
    print("add")


keyword_to_method = {
    'check': check_method,
    'set': set_method,
    'add': add_method,
}

# 导入pandas库，用于数据处理
import pandas as pd

# 从Excel文件中读取测试用例数据，创建DataFrame对象
df = pd.DataFrame(pd.read_excel('客户端_测试用例_导入模板.xlsx'))

# 填充DataFrame中缺失的值，确保数据连续
df.ffill(axis=0, inplace=True)

# 根据用例名称对数据进行分组，以便按用例处理测试步骤
grouped = df.groupby('用例名称')

# 遍历每个用例，进一步遍历每个用例的步骤
for case, group in grouped:
    for step in group:
        # 跳过字符串类型的步骤，只处理DataFrame行
        if isinstance(step, str):
            continue
        # 将步骤转换为字符串，准备处理
        enuStep = str(step.loc[:, '用例步骤'])
        # 输出步骤信息，用于调试
        print(enuStep, type(enuStep))
        # 循环处理步骤中的每个关键词
        while enuStep:
            for key in keyword_to_method.keys():
                # 如果关键词存在于步骤中，执行对应的方法
                if key in enuStep:
                    method = keyword_to_method.get(key)
                    if method:
                        method()
            # 处理完当前步骤后，跳出循环，处理下一个步骤
            else:
                break
            # 分隔处理过的步骤和下一个步骤
            print('===========')


#为了从后往前拼接二进制值，并比较它与预期值，我们首先需要确定起始位和结束位在二维数组中的确切位置。
# 然后，我们需要提取这个范围内的所有位值，并按照从后往前的顺序拼接它们。
# 最后，我们将拼接得到的二进制值转换为整数，并与预期值进行比较。
def get_concatenated_binary_value(array, start_row, start_col, end_row, end_col):
    """
    从二维数组的指定区域中提取位值，从后往前拼接成一个二进制字符串，并返回其整数值。

    参数:
    array -- 二维数组
    start_row, start_col -- 起始位置的行索引和列索引（包含）
    end_row, end_col -- 结束位置的行索引和列索引（包含）

    返回:
    拼接后的二进制值的整数值
    """
    # 验证输入有效性
    if not (0 <= start_row <= end_row < len(array) and 0 <= start_col <= end_col < len(array[0])):
        raise ValueError("Invalid start or end position.")

    # 初始化拼接的二进制字符串
    concatenated_binary = ""

    # 遍历指定区域，从后往前提取位值并拼接
    for row in range(end_row, start_row - 1, -1):  # 从后往前遍历行
        for col in range(end_col, start_col - 1, -1):  # 从后往前遍历列
            bit_value = str(array[row][col])  # 提取当前位的值（0或1）
            concatenated_binary += bit_value  # 拼接二进制字符串

    # 将二进制字符串转换为整数值
    binary_value = int(concatenated_binary, 2)
    return binary_value


# 示例
array = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    # ... 假设其他行也是类似的二进制数据 ...
]

# 起始位和结束位（例如，获取3x3区域的值，从后往前拼接）
start_row, start_col = 2, 1
end_row, end_col = 4, 3

# 预期值
expected_value = 0b10101010  # 这是一个二进制字面量，相当于十进制的170

# 获取指定区域内的值的二进制拼接值，并转换为整数
actual_value = get_concatenated_binary_value(array, start_row, start_col, end_row, end_col)

# 比较实际值与预期值
if actual_value == expected_value:
    print("The actual value matches the expected value.")
else:
    print(f"The actual value {actual_value} does not match the expected value {expected_value}.")

#在这个示例中，get_concatenated_binary_value 函数接受一个二维数组和起始/结束位置的索引，
# 然后遍历这个区域，并从后往前拼接每个位的值。
# 拼接完成后，它将二进制字符串转换为整数，并返回这个整数值。然后，这个整数值与预期值进行比较。
#请注意，此代码假设你的二维数组仅包含0和1，并且起始和结束位置是有效的。
# 此外，如果二维数组的大小不是8x8，你需要确保起始和结束位置在数组边界内。