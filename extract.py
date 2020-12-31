from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from xml.etree import ElementTree
import json

def scrapeXML(browser):
  try:
    browser.get('https://www.senate.gov/general/contact_information/senators_cfm.xml')
    result = ElementTree.fromstring(browser.page_source)
    return result
  except RuntimeError as e:
    print("Runtime Error in scraping XML: {0}".format(e))

def formatAddress(address):
  street = ''
  city = ''
  state = ''
  zip = ''

  try:
    a = address.split()
    a_len = len(a)
    if a_len > 0:
      zip = a[a_len - 1]
      state = a[a_len - 2]
      city = a[a_len - 3]
      street = ""
      for i in range(a_len - 3):
        street += a[i]
        if i != a_len - 4:
          street += ' '
  except RuntimeError as e:
    print("Runtime Error in formatting address: {0}".format(e))


  result = [
    {"street": street},
    {"city": city},
    {"state": state},
    {"zip": zip}
  ]

  return result

def getSenator(senator):
  firstName = senator.find('first_name').text
  lastName = senator.find('last_name').text
  chartId = senator.find('bioguide_id').text
  mobile = senator.find('phone').text
  address = senator.find('address').text

  address = formatAddress(address)

  return {
    'firstName' : firstName,
    'lastName' : lastName,
    'fullName' : firstName + ' ' + lastName,
    'chartId' : chartId,
    'mobile' : mobile,
    'address' : address
  }

def getSenators(tree):
  senators = {}
  count = 0
  for senator in tree.iter('member'):
    senators["member" + str(count)] = getSenator(senator)
    count += 1

  return senators

def main():
  try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=webdriver.ChromeOptions())
    tree = scrapeXML(browser)
    json_obj = json.dumps(getSenators(tree))
    print(json_obj)
  except RuntimeError as e:
    print("Runtime Error in main: {0}".format(e))
  except WebDriverException:
    print("WebDriverException error")
  finally:
    browser.quit()



if __name__ == "__main__":
  main()
