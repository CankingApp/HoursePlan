import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, ticker

my_font = font_manager.FontProperties(fname='../res/light.ttf')
file = open("../jianwei/day_net_signatory.csv", 'r')
df = pd.read_csv("../jianwei/day_net_signatory.csv", encoding='utf-8')
# 输出DataFrame
print(df)

fig = plt.figure()
ax = fig.add_subplot(111)


xdata = df.loc[:, "日期"]
ydata_1 = df.loc[:, "网上签约套数"]
ydata_2 = df.loc[:, "网上签约面积(㎡)"]
ydata_3 = df.loc[:, "住宅签约套数"]
ydata_4 = df.loc[:, "住宅签约面积(㎡)"]

print(str(xdata))
# 设置DataFrame的行名
ax.plot(xdata, ydata_1, 'ro-', label=u'网上签约套数', linewidth=1)
ax.plot(xdata, ydata_3, 'ro--', label=u'住宅签约套数', linewidth=1)


ax2 = ax.twinx()
ax2.plot(xdata, ydata_4, 'bo-', label=u'住宅签约面积(㎡)', linewidth=1)
ax2.plot(xdata, ydata_2, 'bo--', label=u'网上签约面积(㎡)', linewidth=1)

plt.title(u"建委每日网签数据", size=10, fontproperties=my_font)  # 设置表名为“表名”
ax.set_xlabel(u'日期', size=10, fontproperties=my_font)  # 设置x轴名为“x轴名”

ax.set_ylabel(u'套数(套)', size=10, fontproperties=my_font)  # 设置y轴名为“y轴名”
ax2.set_ylabel(u'面积(㎡)', size=10, fontproperties=my_font)  # 设置y轴名为“y轴名”
ax2.legend(loc='upper right', prop=my_font)
ax.yaxis.grid(True)
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))

ax.legend(loc='upper left', prop=my_font)




# 获取列名 即之后的横坐标刻度 [::-1]是用来反转的 因为我想要一个2000-2019的顺序
xlist = list(df.columns[::-1])

print(str(xlist))
#
# # 年末总人口
# # df.loc[]返回的是一个series
# # 这里的末尾使用了[::-1] 即用来反转series
#
#
# # 城镇人口
# city_population = df.loc['城镇人口'][::-1]
# city_population.plot()

# plt.annotate('单位:万人', xy=(15.5, 40000))
plt.tight_layout()
plt.savefig("day_signatory.png")
plt.show()
