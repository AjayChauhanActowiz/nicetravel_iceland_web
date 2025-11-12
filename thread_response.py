from curl_cffi import requests
# import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import os
# import sys
# sys.path.append(r"D:\Ajay_chauhan\thread_code")
# import proxies_token

# from dotenv import load_dotenv
# load_dotenv()
# scrapdo_token = os.getenv('scrapdo_token')
# print(scrapdo_token)

cookies = {
    'tk_or': '%22%22',
    'tk_r3d': '%22%22',
    'tk_lr': '%22%22',
    'ntwl_key': 'XJVZ8H',
    'nt_currency': 'ISK',
    'nt_currency_rate': '1',
    'PHPSESSID': '56fa2ae2151d319301220ad59b7e80d0',
    'cookieyes-consent': 'consentid:TmhyYVFaVlNQRUZwTWUwOEt2TVJ2c05TTms0N1RJWU8,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes',
    '_gid': 'GA1.2.823926433.1762937694',
    '_fbp': 'fb.1.1762937694171.751203476792589401',
    '_hjSessionUser_2392511': 'eyJpZCI6ImZkNzc0OTdkLThiODEtNTg0NS1iMWMyLWVmY2JkYThiZGMxMSIsImNyZWF0ZWQiOjE3NjI5Mzc2OTQyMDgsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjSession_2392511': 'eyJpZCI6IjkzNWY5NGZiLWQwMDQtNDJmYy05NTBkLWM4NDIzYTAyMjAwOCIsImMiOjE3NjI5Mzc2OTQyMDksInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
    'nitroCachedPage': '1',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-11-12%2008%3A26%3A23%7C%7C%7Cep%3Dhttps%3A%2F%2Fnicetravel.is%2Ficeland-tours%2Fsouth-coast-waterfalls-black-beach-and-glacier-adventure-private-tour%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fnicetravel.is%2Fproduct-sitemap.xml',
    'sbjs_first_add': 'fd%3D2025-11-12%2008%3A26%3A23%7C%7C%7Cep%3Dhttps%3A%2F%2Fnicetravel.is%2Ficeland-tours%2Fsouth-coast-waterfalls-black-beach-and-glacier-adventure-private-tour%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fnicetravel.is%2Fproduct-sitemap.xml',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F142.0.0.0%20Safari%2F537.36',
    '_gcl_au': '1.1.1540510208.1762937784',
    'tk_ai': '8%2FKm%2BuygXy5KGRI2FVgvNxEY',
    'tk_qs': '',
    '_ga': 'GA1.2.1095678856.1762937694',
    '_ga_C8KGFG59LB': 'GS2.1.s1762937694$o1$g1$t1762938627$j60$l0$h0',
    '_ga_2365987458': 'GS2.1.s1762937694$o1$g1$t1762938627$j60$l0$h1404898921',
    'sbjs_session': 'pgs%3D32%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fnicetravel.is%2F',
    '_gat_gtag_UA_140430988_1': '1',
}
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,gu;q=0.8',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://nicetravel.is/iceland-day-tours-from-reykjavik/',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    # 'cookie': 'tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; ntwl_key=XJVZ8H; nt_currency=ISK; nt_currency_rate=1; PHPSESSID=56fa2ae2151d319301220ad59b7e80d0; cookieyes-consent=consentid:TmhyYVFaVlNQRUZwTWUwOEt2TVJ2c05TTms0N1RJWU8,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; _gid=GA1.2.823926433.1762937694; _fbp=fb.1.1762937694171.751203476792589401; _hjSessionUser_2392511=eyJpZCI6ImZkNzc0OTdkLThiODEtNTg0NS1iMWMyLWVmY2JkYThiZGMxMSIsImNyZWF0ZWQiOjE3NjI5Mzc2OTQyMDgsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_2392511=eyJpZCI6IjkzNWY5NGZiLWQwMDQtNDJmYy05NTBkLWM4NDIzYTAyMjAwOCIsImMiOjE3NjI5Mzc2OTQyMDksInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; nitroCachedPage=1; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-11-12%2008%3A26%3A23%7C%7C%7Cep%3Dhttps%3A%2F%2Fnicetravel.is%2Ficeland-tours%2Fsouth-coast-waterfalls-black-beach-and-glacier-adventure-private-tour%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fnicetravel.is%2Fproduct-sitemap.xml; sbjs_first_add=fd%3D2025-11-12%2008%3A26%3A23%7C%7C%7Cep%3Dhttps%3A%2F%2Fnicetravel.is%2Ficeland-tours%2Fsouth-coast-waterfalls-black-beach-and-glacier-adventure-private-tour%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fnicetravel.is%2Fproduct-sitemap.xml; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F142.0.0.0%20Safari%2F537.36; _gcl_au=1.1.1540510208.1762937784; tk_ai=8%2FKm%2BuygXy5KGRI2FVgvNxEY; tk_qs=; _ga=GA1.2.1095678856.1762937694; _ga_C8KGFG59LB=GS2.1.s1762937694$o1$g1$t1762938627$j60$l0$h0; _ga_2365987458=GS2.1.s1762937694$o1$g1$t1762938627$j60$l0$h1404898921; sbjs_session=pgs%3D32%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fnicetravel.is%2F; _gat_gtag_UA_140430988_1=1',
}

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# token = proxies_token.scrapdo_token
# proxyModeUrl = "http://{}:@proxy.scrape.do:8080".format(token)
## proxyModeUrl = "http://{}:super=true@proxy.scrape.do:8080".format(token)
## proxyModeUrl = "http://{}:super=true&geoCode=us@proxy.scrape.do:8080".format(token)
# proxies = {
#     "http": proxyModeUrl,
#     "https": proxyModeUrl,
# }

# proxy_url = proxies_token.decodo_url
# proxies = {
#     "http": proxy_url,
#     "https": proxy_url,
# }

# scraper_api_token = proxies_token.scraperapi_token
# proxies = {
#     "http": f"http://scraperapi:{scraper_api_token}@proxy-server.scraperapi.com:8001",
#     "https": f"http://scraperapi:{scraper_api_token}@proxy-server.scraperapi.com:8001"
# }

def response_check(start_iteration, num_requests):
    """Perform multiple requests inside one thread to reduce overhead."""
    batch_results = []
    for i in range(num_requests):
        iteration = start_iteration + i
        st = time.time()
        try:
            response = requests.get(
                'https://nicetravel.is/iceland-multi-day-tours/',
                # params=params,
                # headers=headers,
                # cookies=cookies,
                impersonate='tor145',
                # proxies=proxies,
                # verify=False,
                timeout=120
            )
            if fr'ice-cave-iceland-hot-spring-3-day' in response.text:
                return_dict = {
                    'iteration': iteration,
                    'status': response.status_code,
                    'response': 'good',
                    'time_taken': time.time()-st
                }
                batch_results.append(return_dict)
                print(return_dict)
            else:
                return_dict = {
                    'iteration': iteration,
                    'status': response.status_code,
                    'response': 'bad',
                    'time_taken': time.time() - st
                }
                batch_results.append(return_dict)
                print(return_dict)
        except Exception as e:
            return_dict = {
                'iteration': iteration,
                'status': None,
                'response': f'error: {e}',
                'time_taken': time.time() - st
            }
            batch_results.append(return_dict)
            print(return_dict)
    return batch_results

results = []
thread_count = 20
total_requests = 3000
requests_per_thread = 1  # Each worker handles 10 requests

with ThreadPoolExecutor(max_workers=thread_count) as executor:
    futures = []
    for start in range(1, total_requests + 1, requests_per_thread):
        futures.append(executor.submit(response_check, start, requests_per_thread))

    for future in as_completed(futures):
        batch = future.result()
        for result in batch:
            # print(result)
            results.append(result)

# Save results to Excel
file_name = 'nicetravel_pl_feasibility_test'
df = pd.DataFrame(results)
df.to_excel(f'{file_name}.xlsx', index=False)
print(f"Results saved to {file_name}.xlsx")


