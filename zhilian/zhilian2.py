import requests
import pandas as pd
import time

headers = {
    'Cookie': 'zg_did=%7B%22did%22%3A%20%221657bf80bf32b-0c07464aab1c79-34637909-fa000-1657bf80bf41d7%22%7D; adfbid2=0; dywem=95841923.y; sts_deviceid=165e74928251a-07023ad0dce0ff-1134685d-1024000-165e749282a4f; adfcid2=u3782246.k95735843899.a24711517172.pb; campusOperateJobUserInfo=08954e10-ce10-4b10-aced-de364f61a135; zg_08c5bcee6e9a4c0594a5d34b79b9622a=%7B%22sid%22%3A%201544071622583%2C%22updated%22%3A%201544071622954%2C%22info%22%3A%201544071622595%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22landHref%22%3A%20%22http%3A%2F%2Foppo.zhaopin.com%2F%23page1%22%2C%22cuid%22%3A%20%221006555709%22%7D; urlfrom=121113803; urlfrom2=121113803; adfbid=0; ZP_OLD_FLAG=false; dywea=95841923.2427681081263016400.1535383178.1539534932.1545104914.10; dywec=95841923; dywez=95841923.1545104914.10.10.dywecsr=baidupcpz|dyweccn=(not%20set)|dywecmd=cpt|dywectr=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1545104914; sts_sg=1; sts_sid=167bf6df7e1c3-06928a9096e7ce-35657601-1024000-167bf6df7e3129; sts_chnlsid=121113803; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0pRFx0KqiAs0FU99T0000021OOdb00000pMWNm1.THLyktAJdIjA80K85yF9pywdpAqVuNqsusK15ywbPjnkuAf4nj0snjc1Pvn0IHYsPWRkwWfknj6kwju7n1KAnWTkrj6dfHcLPbczf1uaP0K95gTqFhdWpyfqn1DLnjnYrj6snBusThqbpyfqnHm0uHdCIZwsT1CEQLILIz4lpA7ETA-8QhPEUHq1pyfqnHcknHD1rj01FMNYUNq1ULNzmvRqmh7GuZNsmLKlFMNYUNqVuywGIyYqmLKY0APzm1Y1nHb4rf%26tpl%3Dtpl_11535_18778_14772%26l%3D1509949356%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3170348802_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D40%26wd%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D4502; _jzqa=1.1918820833807955200.1537183657.1539534971.1545104915.3; _jzqc=1; _jzqy=1.1537183657.1545104915.3.jzqsr=baidu|jzqct=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98.jzqsr=baidu|jzqct=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98; _jzqckmp=1; __xsptplus30=30.3.1545104914.1545104914.1%232%7Csp0.baidu.com%7C%7C%7C%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%7C%23%236AyUmc-apIgHicJ2K0Yf8HAaWRHjREEC%23; __utma=269921210.535818933.1535879306.1539534970.1545104915.7; __utmc=269921210; __utmz=269921210.1545104915.7.6.utmcsr=baidupcpz|utmccn=(not%20set)|utmcmd=cpt|utmctr=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98; __utmt=1; qrcodekey=57465d37d14c4703829b64c516080ee1; _jzqb=1.2.10.1545104915.1; firstchannelurl=https%3A//passport.zhaopin.com/login; lastchannelurl=https%3A//ts.zhaopin.com/jump/index_new.html%3Futm_source%3Dbaidupcpz%26utm_medium%3Dcpt%26utm_provider%3Dpartner%26sid%3D121113803%26site%3Dnull; JsNewlogin=3019667129; JSloginnamecookie=18810983661; JSShowname=%E7%A8%8B%E6%81%92%E8%B6%85; at=c3e21277ad6e47f995d36eff747f0a81; Token=c3e21277ad6e47f995d36eff747f0a81; rt=2f753ef85f884aa0ab6487719f19707a; JSpUserInfo=386b2e69567146655f700569436d5e6a5c6b4477526f40355075566b266925714a655e700d694d6d5a6a596b48775d6f43355f755b6b5b6950712265217008697e17390aece64a77206f3d355475056b03691f711465077050691b6d0c6a016b14770b6f17350a75056b0b69047137655e700369466d456a0a6b1e77086f4b353a75396b57695a714c652e706169486d5a6a586b5c77576f503558755c6b50695f714f6554707469396d566a586b4a77306f31355475276b23695b7141655a700069406d5c6a596b4877546f4b353c75396b57695a714c653c707c69486d5b6a526b9; uiioit=3772206659635566556754665364577251665163536655675d665e6420722066596354665e670; dyweb=95841923.7.6.1545104930670; __utmb=269921210.7.6.1545104930682; jobRiskWarning=true; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221006555709%22%2C%22%24device_id%22%3A%22165e7492716c0-07ae31e6d5d78b-1134685d-1024000-165e749271e5f%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0pRFx0KqiAs0FU99T0000021OOdb00000pMWNm1.THLyktAJdIjA80K85yF9pywdpAqVuNqsusK15ywbPjnkuAf4nj0snjc1Pvn0IHYsPWRkwWfknj6kwju7n1KAnWTkrj6%22%2C%22%24latest_referrer_host%22%3A%22sp0.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%2C%22%24latest_utm_campaign%22%3A%22121122523%22%7D%2C%22first_id%22%3A%22165e7492716c0-07ae31e6d5d78b-1134685d-1024000-165e749271e5f%22%7D; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1545105005; LastCity=%E5%85%A8%E5%9B%BD; LastCity%5Fid=489; sts_evtseq=14; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%22efc98b5b-826c-4459-8920-196438313b85-sou%22%2C%22funczone%22:%22smart_matching%22}}; GUID=9f27fb01ef05427e94744a2b200051ca',
    'Host': 'fe-api.zhaopin.com',
    'Origin': 'https://sou.zhaopin.com',
    'Referer': 'https://sou.zhaopin.com/?jl=489&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&kt=3',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
url = 'https://fe-api.zhaopin.com/c/i/sou?start={}pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&kt=3&at=c3e21277ad6e47f995d36eff747f0a81&rt=2f753ef85f884aa0ab6487719f19707a&_v=0.32754615&userCode=1006555709&x-zp-page-request-id=94f67db686ed4afd9d52ea4649419497-1545105326115-525588'

job_detail = {'city':[], 'company':[], 'com_url':[], 'size':[],
    'type':[], 'createDate':[], 'eduLevel':[], 'emplType':[],
        'endDate':[],  'jobName':[], 'jobType':[], 'p_url':[],
            'salary':[], 'tags':[], 'timeState':[], 'updateDate':[],
                'welfare':[], 'workingExp':[]}

for i in range(75):#为了简便，此处直接写死了
    url = url.format(i*90)
    try:
        zhilian = requests.get(url.format(i), headers=headers).json()['data']['results']
        for line in zhilian:
            job_detail['city'].append(line['city']['display'])
            job_detail['company'].append(line['company']['name'])
            job_detail['com_url'].append(line['company']['url'])
            job_detail['size'].append(line['company']['size']['name'])
            job_detail['type'].append(line['company']['type']['name'])
            job_detail['createDate'].append(line['createDate'])
            job_detail['eduLevel'].append(line['eduLevel']['name'])
            job_detail['emplType'].append(line['emplType'])
            job_detail['endDate'].append(line['endDate'])
            job_detail['jobName'].append(line['jobName'])
            job_detail['jobType'].append(line['jobType']['display'])
            job_detail['p_url'].append(line['positionURL'])
            job_detail['salary'].append(line['salary'])
            job_detail['tags'].append(line['tags'])
            job_detail['timeState'].append(line['timeState'])
            job_detail['updateDate'].append(line['updateDate'])
            job_detail['welfare'].append(line['welfare'])
            job_detail['workingExp'].append(line['workingExp']['name'])
        print("爬取第{}页".format(i+1))
        time.sleep(1)
    except:
        print("第{}页爬取失败".format(i+1))
        continue
job_df = pd.DataFrame(job_detail)
print(len(job_df))
job_df.to_csv('job.csv', encoding='gbk')
