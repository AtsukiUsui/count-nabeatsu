# count-nabeatsu

1Hzごとカウントするプログラムとカウントした数字が３の倍数であるとき数字を殴るナベアツを表示するプログラムである。

# 実行動画
Youtube：https://youtu.be/xps_Iwk5s80
(過去動画：https://youtu.be/uG8KJMTP5lk)

# 環境

* Raspberry Pi 3B+
* Ubuntu 20.04 LTS
* ROS1


# コードの使用方法

* roscoreの起動
```
$ roscore
```
```
$ cd ~/catkin_ws/src/
$ git clone git@github.com:Raspberrypi-kaihatsu/mypkg1.git
$ cd dice/scripts/
$ chmod +x count.py
$ chmod +x nabeastsu.py
```



* 実行
```
$ rosrun count.py
```
```
$ rosrun nabeatsu.py
```


# 製作者
* Atsuki Usui
* s20C1019fv@s.chibakoudai.jp

# 参考
* ryuichi ueda (https://github.com/ryuichiueda)

# ライセンス
 [BSD 2-Clause "Simplified" License](https://github.com/ShimonShoji/dice/blob/main/COPYING)
