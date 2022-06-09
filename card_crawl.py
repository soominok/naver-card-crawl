import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument( '--headless' )
chrome_options.add_argument( '--log-level=3' )
chrome_options.add_argument( '--disable-logging' )
chrome_options.add_argument( '--no-sandbox' )
chrome_options.add_argument( '--disable-gpu' )

driver = webdriver.Chrome()
url = 'https://card-search.naver.com/list'
driver.get(url)

# assert "네이버 신용카드 정보: 313개 카드 검색결과" in driver.title # 해당 사이트 html title이 지정해놓은 title과 맞지 않으면 에러를 내보내도록 하는 예외처리

# driver.close()

elements = driver.find_elements_by_css_selector('#app > div.cards > div > div.tabpanel > ul > li') # 카드 목록
print('신용카드 개수: {}'.format(len(elements)))
# print(elements[0].get_attribute('innerHTML'))


# elementList = elements.find_elements_by_tag_name("li")
#     # el_card_nm = el.find_element_by_css_selector('div.info > a > b')
#     # el_card_desc_summary = el.find_element_by_css_selector('div.info > p')
#     # el_card_annual_fee = el.find_element_by_css_selector('div.info > i')
#     # el_card_rewards = el.find_element_by_css_selector('div.info > span.rewards')
    
# print(elementList)
    
