import requests

class Loader:

    cookies = {
            '_gid': 'GA1.2.1353964120.1698181040',
            'random_n': 'eyJpdiI6IjNhN0tWYnNmRU91TmJPMXMzNXVySkE9PSIsInZhbHVlIjoiVENvNTFoUDRhOFVVMzBlcVpBYWJtaEJpVVZXUjZ6SEFnSjZSTWRqRVRoYnBKblkwYkM2aWhLQmE3UDd3dFR1LyIsIm1hYyI6ImE4NWI2YjRkZjZkZDY3NzliOGZmMWQ4NmFhYjI2ZDhkOWZmNGVjNzlmMTRmZmEyNzhlOTAzNWUyZTczYTgzZTAiLCJ0YWciOiIifQ%3D%3D',
            '_ga_90WCZ6NHEE': 'GS1.1.1698205998.7.0.1698205998.0.0.0',
            '__gpi': 'UID=00000ca1d0fcb041:T=1698181085:RT=1698205998:S=ALNI_MY24Ork2RAIw8L8vX-aM25t5xgNXg',
            '_ga': 'GA1.2.1956554750.1698155531',
            '__gads': 'ID=135c295f97ef782a:T=1698181085:RT=1698205998:S=ALNI_MZUlXe0LkiFb050D1pU-FDWX7_dGQ',
            '_ga_CN2Z3TL83Y': 'GS1.2.1698206000.5.0.1698206014.46.0.0',
            'XSRF-TOKEN': 'eyJpdiI6IkdrcWtGN2wwaCtFSDZjRG5pc3hDSHc9PSIsInZhbHVlIjoiUXYvUVZudy8rd25OQUZmRUFKUHhMZEtlY3FSaTQyMXRVRkppOU84MzFhNVhrcVNXeFI1M2hOb1JPOGRIcHNzazQzdUtxb29UU3BraFhIbUdlYTN3ZTV4UUd4b3VqbjFySHg1Z1IxVVhucENiYk5TV3U1UXlzZmJHRjA1a2FpTkkiLCJtYWMiOiIwMWIwNDU3Y2QzYTdmMzgxNmMyMTY4ZWE4OWI4YWQ0YjQ5ZGE3Zjk1ZjgxOWQ2NjJlN2VhYmUyMmI5YWI2ZmQ4IiwidGFnIjoiIn0%3D',
            'sssinstagram_session': 'eyJpdiI6IjFpdTNZMmNUcVZ1b2paREFTcUZWR1E9PSIsInZhbHVlIjoiZTNmMFh1eUkrSG5mR2dUSURTTjUvdlExUlRCakpIMzdUWDBHeW1udEtyRm1LR3p1aTF5WVh4TndYQU1XSk5HMzBQZ2RlL3h6eVZMWDgwdHNiR3psMURPYmV2NlVzQkRSWEJNZkttQllRUWJXZVFqV0kwZnBQMlpvUUZDNW5vUjciLCJtYWMiOiIxYmJjN2NiZjc1MjhhY2JkNTZjZDU2MzdkODBjMTg3Y2U3ODQwNmYzYWQ1ZjhkODkxZWE3OTRkZTQxOWFhYTM1IiwidGFnIjoiIn0%3D',
        }
    xsrf_token = ''
    def refresh_cookies(old_cookies):

        headers = {
            'authority': 'sssinstagram.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,uz;q=0.6',
            'cache-control': 'max-age=0',
            # Requests sorts cookies= alphabetically
            # 'cookie': '_gid=GA1.2.1353964120.1698181040; random_n=eyJpdiI6IjNhN0tWYnNmRU91TmJPMXMzNXVySkE9PSIsInZhbHVlIjoiVENvNTFoUDRhOFVVMzBlcVpBYWJtaEJpVVZXUjZ6SEFnSjZSTWRqRVRoYnBKblkwYkM2aWhLQmE3UDd3dFR1LyIsIm1hYyI6ImE4NWI2YjRkZjZkZDY3NzliOGZmMWQ4NmFhYjI2ZDhkOWZmNGVjNzlmMTRmZmEyNzhlOTAzNWUyZTczYTgzZTAiLCJ0YWciOiIifQ%3D%3D; _ga_90WCZ6NHEE=GS1.1.1698205998.7.0.1698205998.0.0.0; __gpi=UID=00000ca1d0fcb041:T=1698181085:RT=1698205998:S=ALNI_MY24Ork2RAIw8L8vX-aM25t5xgNXg; _ga=GA1.2.1956554750.1698155531; __gads=ID=135c295f97ef782a:T=1698181085:RT=1698205998:S=ALNI_MZUlXe0LkiFb050D1pU-FDWX7_dGQ; _ga_CN2Z3TL83Y=GS1.2.1698206000.5.0.1698206014.46.0.0; XSRF-TOKEN=eyJpdiI6IkdrcWtGN2wwaCtFSDZjRG5pc3hDSHc9PSIsInZhbHVlIjoiUXYvUVZudy8rd25OQUZmRUFKUHhMZEtlY3FSaTQyMXRVRkppOU84MzFhNVhrcVNXeFI1M2hOb1JPOGRIcHNzazQzdUtxb29UU3BraFhIbUdlYTN3ZTV4UUd4b3VqbjFySHg1Z1IxVVhucENiYk5TV3U1UXlzZmJHRjA1a2FpTkkiLCJtYWMiOiIwMWIwNDU3Y2QzYTdmMzgxNmMyMTY4ZWE4OWI4YWQ0YjQ5ZGE3Zjk1ZjgxOWQ2NjJlN2VhYmUyMmI5YWI2ZmQ4IiwidGFnIjoiIn0%3D; sssinstagram_session=eyJpdiI6IjFpdTNZMmNUcVZ1b2paREFTcUZWR1E9PSIsInZhbHVlIjoiZTNmMFh1eUkrSG5mR2dUSURTTjUvdlExUlRCakpIMzdUWDBHeW1udEtyRm1LR3p1aTF5WVh4TndYQU1XSk5HMzBQZ2RlL3h6eVZMWDgwdHNiR3psMURPYmV2NlVzQkRSWEJNZkttQllRUWJXZVFqV0kwZnBQMlpvUUZDNW5vUjciLCJtYWMiOiIxYmJjN2NiZjc1MjhhY2JkNTZjZDU2MzdkODBjMTg3Y2U3ODQwNmYzYWQ1ZjhkODkxZWE3OTRkZTQxOWFhYTM1IiwidGFnIjoiIn0%3D',
            'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        }

        response = requests.get('https://sssinstagram.com/', cookies=old_cookies, headers=headers)

        cookies = response.cookies
        
        Loader.xsrf_token = cookies.get('XSRF-TOKEN').replace('%3D', '')
        Loader.cookies = cookies


    def instagram(url):

        headers = {
            'authority': 'sssinstagram.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,uz;q=0.6',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://sssinstagram.com',
            'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-xsrf-token': Loader.xsrf_token,
        }

        json_data = {
            'link': url,
            'token': '',
        }

        response = requests.post('https://sssinstagram.com/r', cookies=Loader.cookies, headers=headers, json=json_data)

        if response.status_code == 419:
            Loader.refresh_cookies(old_cookies=Loader.cookies)
            headers['x-xsrf-token'] = Loader.xsrf_token
            return requests.post('https://sssinstagram.com/r', cookies=Loader.cookies, headers=headers, json=json_data).json()
        else:
            return response.json()

