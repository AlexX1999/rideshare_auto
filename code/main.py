from appium_operation import Appium
import time

LOADING_WAITTIME = 5
IMPLICITLY_WAITTIME = 15
START = '上海大学'
END = '静安寺'
RIDESHARE_TYPE = '经济型'


if __name__ == "__main__":
    success = 0
    while not success:
        try:
            app = Appium(deviceName="Android Emulator",
                        apkPath="C:\\Users\\xudon\\Downloads\\gaode.apk",
                        udid="805c6b28",
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

            app.navigate_to_rideshare_page(start=START, end=END)
            app.driver.implicitly_wait(app.waitTime)
            print("Navigation complete")

            app.move_to_top(RIDESHARE_TYPE)
            app.driver.implicitly_wait(app.waitTime)
            print("Move to top complete")

            app.select_all(RIDESHARE_TYPE)
            app.driver.implicitly_wait(app.waitTime)
            print("Select all complete")

            company = ['桔子出行']
            app.extract_pricing_formula(company=company, rideshare_type=RIDESHARE_TYPE)
                
            success = 1

        except Exception as e:
            print(e)
            time.sleep(5)
            del app