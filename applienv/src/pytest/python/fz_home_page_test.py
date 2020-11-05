from applitools.selenium import Target, eyes
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
 
def test_verify_home_page(eyes, driver):
    eyes.open(driver, "FlyDubai IBE", "Verify Home Page")
    eyes.check("FZ IBE Home page", Target.window())
    eyes.close(False)
      
def test_verify_search_widget(eyes, driver):
    eyes.open(driver, "FlyDubai IBE", "Verify Search Widget")
    eyes.check("FZ Search Widget", Target.region('div.widgetBoxWrapper'))
    eyes.close(False)
 
def test_verify_manage_booking_widget(eyes, driver):
    eyes.open(driver, "FlyDubai IBE", "Verify Manage Booking Widget")
    driver.find_element_by_css_selector('div.widgetBoxWrapper > ul li:nth-of-type(2)').click()
    eyes.check("FZ Manage Booking Widget", Target.region('div.widgetBoxWrapper'))
    eyes.close(False)
 
def test_verify_checkin_widget(eyes, driver):
    eyes.open(driver, "FlyDubai IBE", "Verify Checkin Widget")
    driver.find_element_by_css_selector('div.widgetBoxWrapper > ul li:nth-of-type(3)').click()
    eyes.check("FZ Manage Booking Widget", Target.region('div.widgetBoxWrapper'))
    eyes.close(False)
 
def test_verify_flight_status_widget(eyes, driver):
    eyes.open(driver, "FlyDubai IBE", "Verify Flight Status Widget")
    driver.find_element_by_css_selector('div.widgetBoxWrapper > ul li:nth-of-type(4)').click()
    eyes.check("FZ Manage Booking Widget", Target.region('div.widgetBoxWrapper'))
    eyes.close(False)
    
def test_verify_search_ow_results_page(eyes, driver):
    eyes.open(driver, "FlyDubai IBE", "Verify Flight listing page")
    driver.find_element_by_css_selector('div.widgetBoxWrapper .radio-oneway-div').click()
    driver.find_element_by_css_selector('div.widgetBoxWrapper #airport-destination').click()
    driver.find_element_by_css_selector('.DestinationAirlist li[data-value=\'MCT\']').click()
    driver.execute_script('date = new Date();date.setDate(date.getDate()+20);document.getElementById("FormModel_DepartureDate").value=""+date')
    driver.find_element_by_css_selector("div.widgetBoxWrapper input[value='Search']").click()
    WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.tripSummaryBox')))
    eyes.check("FZ Manage Booking Widget", Target.window())
    eyes.close(False)