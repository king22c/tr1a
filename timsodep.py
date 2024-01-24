import time
import requests

PROXY = ''
PROXIES = {
    'http': PROXY,
    'https': PROXY
}
PROXIES = None


def get_my_ip():
    resp = requests.get(url='https://httpbin.org/ip', proxies=PROXIES)
    ip = resp.json().get('origin', 'Not available')
    return ip


def list_bien_so(offset: int = 0, size: int = 25):
    url = 'https://dgbs.vpa.com.vn/search-api/search/list-announcement-plan'
    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip'
    }
    body = {
        'license_plate': '',
        'province': '01',
        'vehicle': 1,
        'limit': size,
        'offset': offset
    }
    resp = requests.post(url=url, json=body, headers=headers, proxies=PROXIES)
    return resp.json()


def sum_of_number(ns: str):
    ret = 0
    for e in ns:
        ret = ret + int(e)
    return ret


def bien_que(ns: str, hao: int):
    v = ns[hao - 1]
    if v == '1':
        v = '0'
    else:
        v = '1'
    new_ns = ns[:(hao - 1)] + v + ns[hao:]
    return new_ns


def tinh_que(bks: str):
    # print('Check: %s' % bks)
    que_db = {
        1: '111',
        2: '110',
        3: '101',
        4: '100',
        5: '011',
        6: '010',
        7: '001',
        8: '000'
    }
    if len(bks) != 8:
        return False
    thuong = sum_of_number(bks[3:5])
    ha = sum_of_number(bks[5:])
    que_thuong = thuong % 8
    if que_thuong == 0:
        que_thuong = 8
    que_ha = ha % 8
    if que_ha == 0:
        que_ha = 8
    dong = (thuong + ha) % 6
    if dong == 0:
        dong = 6
    que = que_db[que_ha] + que_db[que_thuong]
    return que, bien_que(que, dong)


def tim_bien_so_dep(count=3):
    print('IP: ', get_my_ip())
    page = 0
    found = []
    que = '101111'
    bien = '101011'
    while True:
        if len(found) >= count:
            break
        if page > 0:
            time.sleep(2.0)
        bien_so = list_bien_so(page * 25)
        if not bien_so['content']:
            break
        for x in bien_so['content']:
            q1, q2 = tinh_que(x['bks'])
            if q1 == que:
                print('match: Thien hoa dong nhan')
                if q2 == bien:
                    print('match: Phong hoa gia nhan')
                    found.append(x['bks'])
        page = page + 1
    return found


def tim_bien_so_dep2():
    found = []
    que = '101111'
    bien = '101011'
    for i in range(0, 99999):
        bks = '30X' + str(i).zfill(5)
        q1, q2 = tinh_que(bks)
        if q1 == que:
            print('match: Thien hoa dong nhan')
            if q2 == bien:
                print('match: Phong hoa gia nhan')
                found.append(bks)
    return found
