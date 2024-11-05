# web-crawlers-example
learn crawlers

+ 准备工作
  + 下载chrome浏览器对应应版本的chromedriver
    + 方式一
      + [以本人chrome版本(109.0.5414.168)为例](https://developer.chrome.com/docs/chromedriver/downloads/version-selection)
        + 1.移除版本号最后一部分，拼接到(https://chromedriver.storage.googleapis.com/LATEST_RELEASE_)之后
          + 如下: https://chromedriver.storage.googleapis.com/LATEST_RELEASE_109.0.5414   
          + 得到 109.0.5414.74
        + 2.拼接上一步的返回
          + 如下: https://chromedriver.storage.googleapis.com/index.html?path=109.0.5414.74/
    + 方式二
      + [chromedriver驱动](https://chromedriver.storage.googleapis.com/index.html)
  + 将chromedriver_win32.zip解压后的exe放到项目中，方便使用


+ 学习资料
  + [jackfrued/Python-100-Days](https://github.com/jackfrued/Python-100-Days)
  + [shengqiangzhang/examples-of-web-crawlers](https://github.com/shengqiangzhang/examples-of-web-crawlers)