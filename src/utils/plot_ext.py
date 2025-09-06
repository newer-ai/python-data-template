import matplotlib
import matplotlib.font_manager as fm
import numpy as np

ZH_FONTS = np.array(["Microsoft YaHei", "PingFang SC"])


def config_plt():
    """
    配置matplotlib：

    - 设置统计图默认大小
    - 设置中文字体
    """
    set_plt_size()
    set_plt_zh_font()


def set_plt_size():
    """设置matplotlib的大小"""
    matplotlib.rcParams["figure.figsize"] = [10, 6]


def set_plt_zh_font():
    """设置matplotlib的中文字体"""
    fonts = np.array(
        [
            fm.FontProperties(fname=font).get_name()
            for font in fm.findSystemFonts(fontpaths=None, fontext="ttf")  # type: ignore
        ]
    )

    mask = np.isin(ZH_FONTS, fonts)

    if np.any(mask):
        font = ZH_FONTS[mask][0]
        matplotlib.rcParams["font.sans-serif"] = [font]
        matplotlib.rcParams["axes.unicode_minus"] = False  # 解决负号显示为方块的问题
    else:
        raise Exception("找不到中文字体")
