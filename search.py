#!/usr/bin/env python3

import shodan


class lookup:
    def __init__(self, port='port:102 ', country=None, city=None, page=1):
        if country == None:
            country_str = ''
        else:
            country_str = ' country:' + country
        if city == None:
            city_str = ''
        else:
            city_str = ' city:' + city
        self.str_search = port + country_str + city_str
        self.search(page)

    def search(self, page_s):
        '''
        Main search task
        '''
        SHODAN_API_KEY = 'vKuTMHaEM7dgjGGpe4DsPe4ot2KBulPS'
        try:
            api = shodan.Shodan(SHODAN_API_KEY)
        except:
            raise Exception("Search stopped, check API key and internet connection.")
        results = api.search(self.str_search, page=page_s)
        if results['total'] == 0:
            raise Exception("No results found!")
        out_results = []
        for result in results['matches']:
            ip = result['ip_str']
            location = result['location']
            data = result['data']
            isp = result['isp']
            plc = host(ip, location, data, isp)
            out_results.append(plc)
        self.results = out_results


class host:
    '''
    Class for each host in the search results
    '''

    def __init__(self, ip, location, data, isp):
        self.ip = ip
        self.location = location
        self.data = data
        self.isp = isp
