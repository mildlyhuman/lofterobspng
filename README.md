**原理**

Lofter显示缩略图时不考虑alpha通道，显示大图时不仅考虑alpha，还有纯色黑背景。weibo贴https://www.weibo.com/6568544726/J7ylj00n0 提出可以通过把（灰度的）RGB压进alpha而RGB全白色逃避目前的图片检测。

**“安装”**

需要python3和numpy包。

python3：https://www.python.org/downloads/

numpy：安装python3后在命令行（windows的cmd，OSX的terminal）输入`pip3 install --user numpy`并回车。如果pip3找不到，替换成pip。

**使用**

假设要处理的图片在/home/myname/Documents/mypic.jpg

在命令行输入`cd /home/myname/Documents/; python obspng.py mypic.jpg`
