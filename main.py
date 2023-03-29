from appium_operation import Appium
import time

LOADING_WAITTIME = 5
IMPLICITLY_WAITTIME = 30

if __name__ == "__main__":
    success = 0
    while not success:
        try:
            app = Appium(deviceName="Android Emulator",
                        apkPath="C:\\Users\\xudon\\Downloads\\gaode.apk",
                        udid="emulator-5554",
                        waitTime=IMPLICITLY_WAITTIME)
            app.connect()
            time.sleep(LOADING_WAITTIME)

            app.agreement()
            time.sleep(LOADING_WAITTIME)
            app.driver.implicitly_wait(app.waitTime)

            app.desktop_icon()
            time.sleep(LOADING_WAITTIME)
            app.driver.implicitly_wait(app.waitTime)

            app.location_permission()
            time.sleep(LOADING_WAITTIME)
            app.driver.implicitly_wait(app.waitTime)

            app.navigate_to_rideshare_page(start='上海大学', end='静安寺')
            app.driver.implicitly_wait(app.waitTime)

            app.move_to_top('经济型')
            app.driver.implicitly_wait(app.waitTime)

            app.select_all('经济型')

            success = 1

        except Exception as e:
            print(e)
            time.sleep(5)
            del app