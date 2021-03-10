import pyecharts.options as opts
import pandas as pd


from pyecharts.charts import Line

file = open("../jianwei/day_net_signatory.csv", 'r')
df = pd.read_csv("../jianwei/day_net_signatory.csv", encoding='utf-8')
# 输出DataFrame
xdata = df.loc[:, "日期"]
ydata_1 = df.loc[:, "网上签约套数"]
ydata_3 = df.loc[:, "住宅签约套数"]


(
    Line()
    .add_xaxis(xaxis_data=xdata)
    .add_yaxis(
        series_name=u"网上签约套数",
        stack="总量",
        color="#2196F3",
        y_axis=ydata_1,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),

    )
    .add_yaxis(
        series_name="住宅签约套数",
        color="#BBDEFB",
        y_axis=ydata_3,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=True),
    )

    .set_global_opts(
        title_opts=opts.TitleOpts(title="建委每日网签数据"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
    .render("day_signatory.html")
)
print(str(xdata))
print("*************************************************************************")

print(str(ydata_1))
print("*************************************************************************")
print(str(ydata_3))
