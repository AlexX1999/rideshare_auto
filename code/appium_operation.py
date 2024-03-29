from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.touch_action import TouchAction

import time


class Appium:

    def __init__(self, deviceName, apkPath, udid, waitTime=60):
        self.caps = {}
        self.caps["appium:deviceName"] = deviceName
        self.caps["platformName"] = "Android"
        self.caps["appium:app"] = apkPath
        self.caps["appium:appWaitActivity"] = "com.autonavi.map.activity.NewMapActivity"
        self.caps["appium:appPackage"] = "com.autonavi.minimap"
        self.caps["appium:udid"] = udid
        self.caps["appium:ensureWebviewsHavePages"] = True
        self.caps["appium:nativeWebScreenshot"] = True
        self.caps["appium:newCommandTimeout"] = 3600
        self.caps["appium:connectHardwareKeyboard"] = True
        self.waitTime = waitTime


    def __del__(self):
        self.driver.close_app()

    
    def connect(self, serverIP="http://127.0.0.1:4723/wd/hub"):
        self.driver = webdriver.Remote(serverIP, self.caps)


    def click_by_coordinate(self, x=10, y=10):
        TouchAction(self.driver).tap(None, x, y, 1).perform()

    
    def agreement(self):
        # Agree on user policy
        actions = ActionChains(self.driver)
        element = self.driver.find_element(by=AppiumBy.ID, value="com.autonavi.minimap:id/agree")
        actions.move_to_element(element)
        actions.click()
        actions.perform()


    def desktop_icon(self):
        # Show gaode icon on desktop
        actions = ActionChains(self.driver)
        add_auto_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]'
        element = self.driver.find_element(by=AppiumBy.XPATH, value=add_auto_xpath)
        actions.move_to_element(element)
        actions.click()
        actions.perform()


    def location_permission(self):
        # Grant gaode permission for accessing user location while using
        actions = ActionChains(self.driver)
        element = self.driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        actions.move_to_element(element)
        actions.click()
        actions.perform()


    def navigate_to_rideshare_page(self, start, end):
        # Click search bar
        actions = ActionChains(self.driver)
        button_id = 'com.autonavi.minimap:id/maphome_searchbar_bg'
        element = self.driver.find_element(by=AppiumBy.ID, value=button_id)
        actions.move_to_element(element)
        actions.click()
        actions.perform()
        self.driver.implicitly_wait(self.waitTime)
        
        # Enter start address
        xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[4]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText[2]'
        element = self.driver.find_element(by=AppiumBy.XPATH, value=xpath).send_keys(end)
        self.driver.implicitly_wait(self.waitTime)
        
        # Click search
        element = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='搜索')
        actions.move_to_element(element)
        actions.click()
        actions.perform()
        self.driver.implicitly_wait(self.waitTime)
        time.sleep(10)
        
        # Select first option
        xpath = '(//android.view.ViewGroup[@content-desc="路线"])[1]/android.view.View'
        element = self.driver.find_element(by=AppiumBy.XPATH, value=xpath).click()
        self.driver.implicitly_wait(self.waitTime)
        
        # Click start location search bar
        button_id = 'com.autonavi.minimap:id/route_edit_summary_start'
        element = self.driver.find_element(by=AppiumBy.ID, value=button_id).click()
        self.driver.implicitly_wait(self.waitTime)
        time.sleep(10)
        
        # Enter start location
        xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[5]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.EditText'
        element = self.driver.find_element(by=AppiumBy.XPATH, value=xpath)
        element.set_text(start)
        self.driver.implicitly_wait(self.waitTime)
        
        # Click search
        xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[5]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ImageView'
        element = self.driver.find_element(by=AppiumBy.XPATH, value=xpath).click()
        self.driver.implicitly_wait(self.waitTime)
        
        # Skip tutorial
        xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[5]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.FrameLayout[2]'
        element = self.driver.find_element(by=AppiumBy.XPATH, value=xpath).click()
        self.driver.implicitly_wait(self.waitTime)
        # self.click_by_coordinate()
        time.sleep(5)

        # Switch to rideshare
        xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[5]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.FrameLayout[2]'
        element = self.driver.find_element(by=AppiumBy.XPATH, value=xpath).click()
        self.driver.implicitly_wait(self.waitTime)
        time.sleep(10)
        
        # Skip tutorial
        # xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[5]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[5]'
        # element = self.driver.find_element(by=AppiumBy.XPATH, value=xpath).click()
        # self.driver.implicitly_wait(self.waitTime)
        # Click a random spot on the screen to skip tutorial
        self.click_by_coordinate(100, 100)
        time.sleep(3)
        # xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[5]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[5]'
        # element = self.driver.find_element(by=AppiumBy.XPATH, value=xpath).click()
        # Click a random spot on the screen to skip tutorial
        self.click_by_coordinate(100, 100)
        time.sleep(3)

        # Show more options
        xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[5]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[5]'
        element = self.driver.find_element(by=AppiumBy.XPATH, value=xpath).click()


    def move_to_top(self, rideshare_type):
        elements = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.view.View')
        for e in elements:
            if e.text == rideshare_type:
                e.click()
                break

    
    def select_all(self, rideshare_type):
        elements = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.view.View')
        flag = 0
        for e in elements:
            if e.text == rideshare_type and flag == 0:
                flag = 1
            elif e.text == rideshare_type and flag == 1:
                print(e.is_selected())
                if not e.is_selected():
                    e.click()
                    break


    def scroll_down(self):
        screenSize = self.driver.get_window_size()
        screenW = screenSize['width']
        screenH = screenSize['height']

        x = screenW/2
        y1 = int(screenH*0.8)
        y2 = int(screenH*0.4)
        avlst = []
        self.driver.swipe(start_x=x, start_y=y1, end_x=x, end_y=y2, duration=800)


    def collect_text(self):
        text_collection = {}
        old_dict = None

        while old_dict != text_collection:
            old_dict = text_collection.copy()

            elements = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.TextView')
            for element in elements:
                if element.id not in text_collection.keys():
                    text_collection[element.id] = element.text

            self.scroll_down(self.driver)
        return text_collection


    def scroll_up(self):
        screenSize = self.driver.get_window_size()
        screenW = screenSize['width']
        screenH = screenSize['height']

        x = screenW/2
        y1 = int(screenH*0.8)
        y2 = int(screenH*0.4)
        avlst = []
        self.driver.swipe(start_x=x, start_y=y2, end_x=x, end_y=y1, duration=800)
        
        
    def return_to_company_list(self):
        xpath = '//android.view.View[@text="休息日"]'
        flag = 1
        while flag:
            try: 
                element = self.driver.find_element(by=AppiumBy.XPATH, value=xpath).click()
                flag = 0
            except:
                self.scroll_up(self.driver)


    def if_all_visited(self, visit_list):
        return len(visit_list) == sum(visit_list.values())
    

    def extract_pricing_formula(self, company, rideshare_type):
        visited = {}
        price_formula = {}
        for name in company:
            visited[name] = 0

        while not self.if_all_visited(visited):
            elements = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.view.ViewGroup')
            for e in elements:
                if (e.rect['height'] == 129 and e.rect['width'] == 639):
                    sub_es = e.find_elements(by=AppiumBy.CLASS_NAME, value='android.view.View')
                    company_name = sub_es[0].text
                    if company_name in visited and visited[company_name] == 0:
                        buttons = e.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.ImageView')
                        flag = 0
                        for button in buttons:
                            if button.rect['height'] == 32 and button.rect['width'] == 32:
                                flag = 1
                                button.click()
                                time.sleep(5)
                                try:
                                    elements = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.TextView')
                                    elements[-1].click()
                                except:
                                    elements = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.TextView')
                                    elements[-1].click()
                                time.sleep(3)
                                price_formula[company_name] = self.collect_text(self.driver)
                                print(company_name, ' finished!')
                                visited[company_name] = 1

                                # Finished collecting pricing formula for a company, get back to rideshare page
                                xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[5]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/com.uc.webview.export.WebView/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Image'
                                self.driver.find_element(by=AppiumBy.XPATH, value=xpath).click()
                                time.sleep(3)
                                xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[5]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/com.uc.webview.export.WebView/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Image'
                                self.driver.find_element(by=AppiumBy.XPATH, value=xpath).click()

                                time.sleep(10)
                        break
        return price_formula