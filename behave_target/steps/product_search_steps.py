from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

@given(u'that we have gone to {site}')
def step_impl(context, site):
    context.site = site
    context.browser = webdriver.Chrome()
    if not site.startswith("http"):
        site = "https://" + site
    context.browser.get(site)
    time.sleep(5)

@when(u'we search for "{category}"')
def step_impl(context, category):
    element_id = "search"
    search_input = context.browser.find_element(By.ID, element_id)
    search_input.clear()
    search_input.send_keys(category)
    search_input.send_keys(Keys.RETURN)
    time.sleep(5)

@then(u'we find products from "{company}"')
def step_impl(context, company):
    page = context.browser.page_source
    assert company.upper() in page.upper()

@then(u'we find products from "{company}" in cart')
def step_impl(context, company):
    page = context.browser.page_source
    assert company.upper() in page.upper()

@then(u'we add the third product to cart')
def step_impl(context):
    #identify element
    l = context.browser.find_element("xpath",'//div[@class="styles__StyledRow-sc-wmoju4-0 kVSHGU"]/div[3]/div/div/div[2]/div/div/button')
    #perform click
    l.click()

    time.sleep(5)

    context.browser.get("https://www.target.com/cart")
    time.sleep(5)

