# -*- coding: utf-8 -*-  
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontManager
from pylab import mpl
import subprocess

# def get_matplot_zh_font():
#     fm = FontManager()
#     mat_fonts = set(f.name for f in fm.ttflist)
#     output = subprocess.check_output('fc-list :lang=zh -f "%{family}\n"', shell=True)
#     zh_fonts = set(f.split(',', 1)[0] for f in output.split('\n'))
#     available = list(mat_fonts & zh_fonts)
#     return available

def set_matplot_zh_font():
    available = ['Arial Unicode MS'] # get_matplot_zh_font()
    if len(available) > 0:
        mpl.rcParams['font.sans-serif'] = [available[0]]    # 指定默认字体
        mpl.rcParams['font.family']='sans-serif' 
        mpl.rcParams['axes.unicode_minus'] = False          # 解决保存图像是负号'-'显示为方块的问题