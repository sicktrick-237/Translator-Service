import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from urllib.parse import quote
from time import sleep
url = 'https://translate.google.com'

def lang_set(lang):
    languages_set = {'afrikaans':'af','albanian':'sq','amharic':'am','arabic':'ar','armenian':'hy','azerbaijani':'az','basque':'eu','belarusian':'be','bengali':'bn','bosnian':'bs','bulgarian':'bg','catalan':'ca','cebuano':'ceb','chichewa':'ny','chinese (simplified)':'zh-CN','chinese (traditional)':'zh-TW','corsican':'co','croatian':'hr','czech':'cs','danish':'da','dutch':'nl','english':'en','esperanto':'eo','estonian':'et','filipino':'tl','finnish':'fi','french':'fr','frisian':'fy','galician':'gl','georgian':'ka','german':'de','greek':'el','gujarati':'gu','haitian creole':'ht','hausa':'ha','hawaiian':'haw','hebrew':'iw','hindi':'hi','hmong':'hmn','hungarian':'hu','icelandic':'is','igbo':'ig','indonesian':'id','irish':'ga','italian':'it','japanese':'ja','javanese':'jw','kannada':'kn','kazakh':'kk','khmer':'km','korean':'ko','kurdish (kurmanji)':'ku','kyrgyz':'ky','lao':'lo','latin':'la','latvian':'lv','lithuanian':'lt','luxembourgish':'lb','macedonian':'mk','malagasy':'mg','malay':'ms','malayalam':'ml','maltese':'mt','maori':'mi','marathi':'mr','mongolian':'mn','myanmar (burmese)':'my','nepali':'ne','norwegian':'no','pashto':'ps','persian':'fa','polish':'pl','portuguese':'pt','punjabi':'pa','romanian':'ro','russian':'ru','samoan':'sm','scots gaelic':'gd','serbian':'sr','sesotho':'st','shona':'sn','sindhi':'sd','sinhala':'si','slovak':'sk','slovenian':'sl','somali':'so','spanish':'es','sundanese':'su','swahili':'sw','swedish':'sv','tajik':'tg','tamil':'ta','telugu':'te','thai':'th','turkish':'tr','ukrainian':'uk','urdu':'ur','uzbek':'uz','vietnamese':'vi','welsh':'cy','xhosa':'xh','yiddish':'yi','yoruba':'yo','zulu':'zu'}
    if lang.lower() in languages_set:
            return languages_set[lang.lower()]
    return False
    
    
def gen_url(tl,text):
    url = 'https://translate.google.com/#view=home&op=translate&sl=en&tl='+tl+'&text='
    trans_text = quote(text,safe='')
    return url+trans_text



def translate_service(url):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    sleep(1)
    res = driver.find_element_by_class_name('homepage-content-wrap')
    sleep(1)
    htmpage = driver.execute_script("return arguments[0].innerHTML;",res)

    soup = BeautifulSoup(htmpage,'html5lib')
    input_div = soup.find('div',{'class':'source-target-row'})
    try:
        inp = input_div.find('div',{'class':'tlid-results-container results-container'})
        translated_text = (inp.find('div',{'class':'result-shield-container tlid-copy-target'})).span.span.text
        return translated_text
    except:
        return False

flg = True
while flg:
    get_text = (input('Enter the text you want to translate (English): '))[:5000]
    get_lang = input('Which language you want to translate in : ')

    if get_lang and lang_set(get_lang):
        url = gen_url(lang_set(get_lang),get_text)
        trans_text = translate_service(url)
        if trans_text:
            print('\n' + get_text + ' -> ' + trans_text)
        else:
            print('Error in Translating Service')
        sleep(2)
    else:
        print("Language Not Available")
        sleep(2)
    prompt = input('Do you want to translate some more crap ?')
    if prompt.lower() == 'y' or prompt.lower() == 'yes':
        flg = True
    else:
        flg = False
