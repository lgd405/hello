import pyecharts.options as opts
from pyecharts.charts import Gauge

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.baidu.com/examples/editor.html?c=gauge
目前无法实现的功能:
1、暂无
"""

(
    Gauge(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(series_name="业务指标", data_pair=[["完成率", 70.5]])
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}%"),
    )
    .render("render/gauge.html")
)