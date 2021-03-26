# coding=UTF-8
"""
@Time：2021/3/22 13:25
@Author：Administrator
@Project:pythonProject1
@Name:practice5 
"""
import numpy as np
from matplotlib import colors
from sklearn import svm
from sklearn.svm import SVC
from sklearn import model_selection
import matplotlib.pyplot as plt
import matplotlib as mpl


def load_data():
    # 导入数据
    data = np.loadtxt(r'C:\Users\Administrator\Downloads\iris.data', dtype=float, delimiter=',',
                      converters={4: iris_type})

    return data


def iris_type(s):
    # 数据转为整型，数据集标签类别由string转为int
    it = {b'Iris-setosa': 0, b'Iris-versicolor': 1, b'Iris-virginica': 2}
    return it[s]

    # 定义分类器


def classifier():
    clf = svm.SVC(C=0.5,  # 误差项惩罚系数
                  kernel='linear',  # 线性核 kenrel="rbf":高斯核
                  decision_function_shape='ovr')  # 决策函数

    return clf


def train(clf, x_train, y_train):
    # x_train：训练数据集
    # y_train：训练数据集标签
    # 训练开始
    clf.fit(x_train, y_train.ravel(), sample_weight=None)  # 同flnumpy.ravelatten将矩阵拉平


def show_accuracy(a, b, tip):
    acc = a.ravel() == b.ravel()
    print(a)
    print(b)
    print(acc)
    print('%s Accuracy:%.3f' % (tip, np.mean(acc)))


def print_accuracy(clf, x_train, y_train, x_test, y_test):
    # print(x_train)
    show_accuracy(clf.predict(x_train), y_train, 'traing data')
    show_accuracy(clf.predict(x_test), y_test, 'testing data')
    # print(x_train)
    # print(y_train.ravel())
    # print(clf.predict(x_train))


def draw(clf, x):  # 写完一个函数要运行，否则报错：函数未定义
    '''
    print(x.shape)
    (150, 2)
    '''
    iris_feature = 'sepal length', 'sepal width', 'petal lenght', 'petal width'
    x1_min, x1_max = x[:, 0].min(), x[:, 0].max()  # 第0列的范围
    x2_min, x2_max = x[:, 1].min(), x[:, 1].max()  # 第1列的范围

    x1, x2 = np.mgrid[x1_min:x1_max:200j, x2_min:x2_max:200j]  # 生成网格采样点
    grid_test = np.stack((x1.flat, x2.flat), axis=1)  # 测试点
    '''
    print(grid_test.shape)
    (40000, 2)
    '''
    # print('grid_test:\n', grid_test)
    z = clf.decision_function(grid_test)
    # print('the distance to decision plane:\n', z)
    grid_hat = clf.predict(grid_test)  # 预测分类值 得到【0,0.。。。2,2,2】
    '''
    print(grid_hat.shape)
    (40000,)
    '''
    # print('grid_hat:\n', grid_hat)
    grid_hat = grid_hat.reshape(x1.shape)  # reshape grid_hat和x1形状一致
    # 若3*3矩阵e，则e.shape()为3*3,表示3行3列
    cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
    '''
    x3 = np.mgrid[x1_min:x1_max:200j, x2_min:x2_max:200j]  # 生成网格采样点
    print(x3.shape)
    (2, 200, 200)
    print(x1.shape)
    print(x2.shape)
    print(grid_hat.shape)
    (200, 200)
    (200, 200)
    简单理解为x1+x2=x3
    (200, 200)
    '''

    cm_dark = mpl.colors.ListedColormap(['g', 'b', 'r'])
    print(grid_hat.shape)
    plt.pcolormesh(x1, x2, grid_hat, cmap=cm_light)  # pcolormesh(x,y,z,cmap)这里参数代入
    # x1，x2，grid_hat，cmap=cm_light绘制的是背景。
    plt.scatter(x[:, 0], x[:, 1], c=np.squeeze(y), edgecolor='k', s=50, cmap=cm_dark)  # 样本点
    plt.scatter(x_test[:, 0], x_test[:, 1], s=120, facecolor='none', zorder=10)  # 测试点
    plt.xlabel(iris_feature[0], fontsize=20)
    plt.ylabel(iris_feature[1], fontsize=20)
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    plt.title('svm in iris data classification', fontsize=30)
    plt.grid()
    plt.show()


# 训练四个特征：
data = load_data()
x, y = np.split(data, (4,), axis=1)  # x为前四列，y为第五列，x为训练数据，y为数据标签
# data=(150,5),x=(150,4),y=(150,1)

# x_train,x_test,y_train,y_test = 训练数据，测试数据，训练数据标签，测试数据标签
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, random_state=1,
                                                                    test_size=0.3)  # 数据集划分成70%30%测试集
clf = classifier()  # 声明svm分类器对象
train(clf, x_train, y_train)  # 启动分类器进行模型训练

print_accuracy(clf, x_train, y_train, x_test, y_test)

# 训练两个特征（用于画图展示）
data = load_data()
# print(np.shape(data))
x, y = np.split(data, (4,), axis=1)  # x为前四列，y为第五列，x为训练数据，y为数据标签
# print(np.shape(x))
# print(np.shape(y))
x = x[:, :2]  # 只要前两个特征，此时只训练前两个特征，用于画图
# print(np.shape(x))
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, random_state=1, test_size=0.3)
clf = classifier()
train(clf, x_train, y_train)
print_accuracy(clf, x_train, y_train, x_test, y_test)
draw(clf, x)
