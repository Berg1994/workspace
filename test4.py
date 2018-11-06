import time

from selenium import webdriver


def take_screenshot(url, save_fn="capture.png"):
    # browser = webdriver.Firefox() # Get local session of firefox
    # 谷歌浏览器截取当前窗口网页

    browser = webdriver.Chrome()
    # phantomjs截取整张网页
    # browser = webdriver.PhantomJS()
    browser.maximize_window()
    browser.get(url)  # Load page
    # 将页面的滚动条拖到最下方，然后再拖回顶部
    browser.execute_script("""
        (function () {
            var y = 0;
            var step = 100;
            window.scroll(0, 0);

            function f() {
                if (y < document.body.scrollHeight) {
                    y += step;
                    window.scroll(0, y);
                    setTimeout(f, 100);
                } else {
                    window.scroll(0, 0);
                    document.title += "scroll-done";
                }
            }

            setTimeout(f, 1000);
        })();
    """)

    for i in range(30):
        if "scroll-done" in browser.title:
            break
        time.sleep(10)

    browser.save_screenshot(save_fn)

if __name__ == '__main__':
    take_screenshot("https://www.brookings.edu/research/a-policy-at-peace-with-itself-antitrust-remedies-for-our-concentrated-uncompetitive-economy/")