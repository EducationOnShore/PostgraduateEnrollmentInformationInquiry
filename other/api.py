#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests

"""
@author: Lambert
@file: api.py
@time: 2022/7/30 12:58
"""


def professional_degree_category():
    """
    专业硕士类别获取
    :return:
    """
    url = "https://yz.chsi.com.cn/zsml/pages/getZy.jsp"
    payload = "mldm=zyxw"
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'JSESSIONID=A35CD8CB68020E500EFC938C4AF7622F; TS0197d085=01886fbf6ea0829704742ca45e639184bb404eb6b8ea5cf9d2dda504d93e9181ed26f2a32ea3f767819dc7544700d1650e183c2940846846e3dc700bad6c7a781f22a3554df0418dfee6c3bacf07829e1eb8010d41bd09b2a9d6ab5c3fd230d6a1c234f4ff6fae673e973da305c60d2e8fa6f743b0; zg_did=%7B%22did%22%3A%20%22181d6f3fc42679-04c39a7f218847-1c525635-1aeaa0-181d6f3fc439ba%22%7D; _abfpc=d6b798ab7eae547d492c7f90722e832b32c5465d_2.0; cna=541d9c6fe9c0da5500d6f2df24a99abd; _gid=GA1.3.2112747589.1658995822; zg_a5f21d6abc554e3c9e4c17aade025fd8=%7B%22sid%22%3A%201659074429330%2C%22updated%22%3A%201659074429340%2C%22info%22%3A%201659074429338%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22gaokao.chsi.com.cn%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fgaokao.chsi.com.cn%2F%22%7D; zg_14e129856fe4458eb91a735923550aa6=%7B%22sid%22%3A%201659090383805%2C%22updated%22%3A%201659090385217%2C%22info%22%3A%201659073778534%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.chsi.com.cn%22%7D; zg_0d76434d9bb94abfaa16e1d5a3d82b52=%7B%22sid%22%3A%201659090385801%2C%22updated%22%3A%201659090404170%2C%22info%22%3A%201658995836030%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22fda4d0aa3c9773bdb7f6d5a331795235%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fmy.chsi.com.cn%2Farchive%2Findex.jsp%22%7D; _ga_RNH4PZV76K=GS1.1.1659090386.13.1.1659090444.0; aliyungf_tc=aa2f7d240ae449c84e0ad00f66424abf1b6fe77c8f3ce5ad7a33206a0edab19c; JSESSIONID=557168828E3ACD7938AB613163E69FAC; CHSICC_CLIENTFLAGYZ=fc9afcdd904eaf08d72a2b7f83f224e2; CHSICC02=!FmA0W8QbanbfPeHzYxYLahOzddj6Y/QnYkE4Pswwn150FUGTHSSJMKIOa9NlkbXiZPGh8WbXOTM9QQ==; CHSICC01=!VGmjBFru0QfmyCTzYxYLahOzddj6Y/jpB8SQsRZ4ABWWqa+5GPMgtHmrHxMA8u5fUDvYTkoIbT7CHg==; XSRF-CCKTOKEN=c859df65b7208d83421f9509866c80de; CHSICC_CLIENTFLAGZSML=1f7c0048e2a49f1501a5e6658c46b4ea; acw_tc=2f6fc10b16591561928657643e65c75e8bce8dcb054eaaead1bce56f7f170c; _ga=GA1.3.1772109431.1657168746; TS01d9ac57=01886fbf6e89c1920c40715694a3234f236a1c2fb5135f9713fe19eee108ec3bcd4dd64e4271f54eb2152e442c834184f96d20da45386083a72ab46588de62534f0b4f37d21d6782c462cf9a522a5e610745940f046d822c7fd261085b65ca1ff8098b1927f732d6872a5c7f1ad345904343438e075e22422395902798bc6751e08143a3ed; _ga_YZV5950NX3=GS1.1.1659154397.12.1.1659157197.0; TS01d9ac57=01886fbf6e89c1920c40715694a3234f236a1c2fb5135f9713fe19eee108ec3bcd4dd64e4271f54eb2152e442c834184f96d20da45386083a72ab46588de62534f0b4f37d21d6782c462cf9a522a5e610745940f046d822c7fd261085b65ca1ff8098b1927f732d6872a5c7f1ad345904343438e075e22422395902798bc6751e08143a3ed',
        'Origin': 'https://yz.chsi.com.cn',
        'Referer': 'https://yz.chsi.com.cn/zsml/queryAction.do',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


def academic_master_category():
    """
    学术硕士一级门类
    :return:
    """
    url = "https://yz.chsi.com.cn/zsml/pages/getMl.jsp"
    payload = {}
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Cookie': 'JSESSIONID=A35CD8CB68020E500EFC938C4AF7622F; TS0197d085=01886fbf6ea0829704742ca45e639184bb404eb6b8ea5cf9d2dda504d93e9181ed26f2a32ea3f767819dc7544700d1650e183c2940846846e3dc700bad6c7a781f22a3554df0418dfee6c3bacf07829e1eb8010d41bd09b2a9d6ab5c3fd230d6a1c234f4ff6fae673e973da305c60d2e8fa6f743b0; zg_did=%7B%22did%22%3A%20%22181d6f3fc42679-04c39a7f218847-1c525635-1aeaa0-181d6f3fc439ba%22%7D; _abfpc=d6b798ab7eae547d492c7f90722e832b32c5465d_2.0; cna=541d9c6fe9c0da5500d6f2df24a99abd; _gid=GA1.3.2112747589.1658995822; zg_a5f21d6abc554e3c9e4c17aade025fd8=%7B%22sid%22%3A%201659074429330%2C%22updated%22%3A%201659074429340%2C%22info%22%3A%201659074429338%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22gaokao.chsi.com.cn%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fgaokao.chsi.com.cn%2F%22%7D; zg_14e129856fe4458eb91a735923550aa6=%7B%22sid%22%3A%201659090383805%2C%22updated%22%3A%201659090385217%2C%22info%22%3A%201659073778534%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.chsi.com.cn%22%7D; zg_0d76434d9bb94abfaa16e1d5a3d82b52=%7B%22sid%22%3A%201659090385801%2C%22updated%22%3A%201659090404170%2C%22info%22%3A%201658995836030%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22fda4d0aa3c9773bdb7f6d5a331795235%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fmy.chsi.com.cn%2Farchive%2Findex.jsp%22%7D; _ga_RNH4PZV76K=GS1.1.1659090386.13.1.1659090444.0; aliyungf_tc=aa2f7d240ae449c84e0ad00f66424abf1b6fe77c8f3ce5ad7a33206a0edab19c; JSESSIONID=557168828E3ACD7938AB613163E69FAC; CHSICC_CLIENTFLAGYZ=fc9afcdd904eaf08d72a2b7f83f224e2; CHSICC02=!FmA0W8QbanbfPeHzYxYLahOzddj6Y/QnYkE4Pswwn150FUGTHSSJMKIOa9NlkbXiZPGh8WbXOTM9QQ==; CHSICC01=!VGmjBFru0QfmyCTzYxYLahOzddj6Y/jpB8SQsRZ4ABWWqa+5GPMgtHmrHxMA8u5fUDvYTkoIbT7CHg==; XSRF-CCKTOKEN=c859df65b7208d83421f9509866c80de; CHSICC_CLIENTFLAGZSML=1f7c0048e2a49f1501a5e6658c46b4ea; acw_tc=2f6fc10b16591561928657643e65c75e8bce8dcb054eaaead1bce56f7f170c; _ga=GA1.1.1772109431.1657168746; TS01d9ac57=01886fbf6e41c20cd56e62ce466b24767a24680305767711fbd086901b1af27ca13c92d8ca22207821b474f7744f030d8702c92646be2277c28cb332bbcede3dadfef5267750110f4414411450b5963d7b9bb1762d13a4f539d594242778dad4c8c6b3dc4ef47685a4c8be3002a1ef07187b458e4293b2c670d635fc61ca478d862c1631d0; _ga_YZV5950NX3=GS1.1.1659154397.12.1.1659157675.0; TS01d9ac57=01886fbf6e43f26715c5f159c9b80f761c68be96fbeafe10c577951a31ce75fed2f742751498c2125bed88d18c500f2eb85ca630bc746a372e74ff6beeaf591121563acec3c79e0a92a0b0cb74beabf03c9a63d0a579a71552b98b627e3462fa197895d9f3552ecd4e65cef6652c27d9c4f072496859d543c67a989bd02204b061b830468d',
        'Origin': 'https://yz.chsi.com.cn',
        'Referer': 'https://yz.chsi.com.cn/zsml/queryAction.do',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()


def academic_master_category_second(mldm=''):
    """
    二级分类
    :param mldm: 一级分类
    :return:
    """
    url = "https://yz.chsi.com.cn/zsml/pages/getZy.jsp"

    payload = "mldm="+mldm
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'JSESSIONID=A35CD8CB68020E500EFC938C4AF7622F; TS0197d085=01886fbf6ea0829704742ca45e639184bb404eb6b8ea5cf9d2dda504d93e9181ed26f2a32ea3f767819dc7544700d1650e183c2940846846e3dc700bad6c7a781f22a3554df0418dfee6c3bacf07829e1eb8010d41bd09b2a9d6ab5c3fd230d6a1c234f4ff6fae673e973da305c60d2e8fa6f743b0; zg_did=%7B%22did%22%3A%20%22181d6f3fc42679-04c39a7f218847-1c525635-1aeaa0-181d6f3fc439ba%22%7D; _abfpc=d6b798ab7eae547d492c7f90722e832b32c5465d_2.0; cna=541d9c6fe9c0da5500d6f2df24a99abd; _gid=GA1.3.2112747589.1658995822; zg_a5f21d6abc554e3c9e4c17aade025fd8=%7B%22sid%22%3A%201659074429330%2C%22updated%22%3A%201659074429340%2C%22info%22%3A%201659074429338%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22gaokao.chsi.com.cn%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fgaokao.chsi.com.cn%2F%22%7D; zg_14e129856fe4458eb91a735923550aa6=%7B%22sid%22%3A%201659090383805%2C%22updated%22%3A%201659090385217%2C%22info%22%3A%201659073778534%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.chsi.com.cn%22%7D; zg_0d76434d9bb94abfaa16e1d5a3d82b52=%7B%22sid%22%3A%201659090385801%2C%22updated%22%3A%201659090404170%2C%22info%22%3A%201658995836030%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22fda4d0aa3c9773bdb7f6d5a331795235%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fmy.chsi.com.cn%2Farchive%2Findex.jsp%22%7D; _ga_RNH4PZV76K=GS1.1.1659090386.13.1.1659090444.0; aliyungf_tc=aa2f7d240ae449c84e0ad00f66424abf1b6fe77c8f3ce5ad7a33206a0edab19c; JSESSIONID=557168828E3ACD7938AB613163E69FAC; CHSICC_CLIENTFLAGYZ=fc9afcdd904eaf08d72a2b7f83f224e2; CHSICC02=!FmA0W8QbanbfPeHzYxYLahOzddj6Y/QnYkE4Pswwn150FUGTHSSJMKIOa9NlkbXiZPGh8WbXOTM9QQ==; CHSICC01=!VGmjBFru0QfmyCTzYxYLahOzddj6Y/jpB8SQsRZ4ABWWqa+5GPMgtHmrHxMA8u5fUDvYTkoIbT7CHg==; XSRF-CCKTOKEN=c859df65b7208d83421f9509866c80de; CHSICC_CLIENTFLAGZSML=1f7c0048e2a49f1501a5e6658c46b4ea; acw_tc=2f6fc10b16591561928657643e65c75e8bce8dcb054eaaead1bce56f7f170c; TS01d9ac57=01886fbf6e41c20cd56e62ce466b24767a24680305767711fbd086901b1af27ca13c92d8ca22207821b474f7744f030d8702c92646be2277c28cb332bbcede3dadfef5267750110f4414411450b5963d7b9bb1762d13a4f539d594242778dad4c8c6b3dc4ef47685a4c8be3002a1ef07187b458e4293b2c670d635fc61ca478d862c1631d0; _ga_YZV5950NX3=GS1.1.1659154397.12.1.1659157676.0; _ga=GA1.1.1772109431.1657168746; TS01d9ac57=01886fbf6e43f26715c5f159c9b80f761c68be96fbeafe10c577951a31ce75fed2f742751498c2125bed88d18c500f2eb85ca630bc746a372e74ff6beeaf591121563acec3c79e0a92a0b0cb74beabf03c9a63d0a579a71552b98b627e3462fa197895d9f3552ecd4e65cef6652c27d9c4f072496859d543c67a989bd02204b061b830468d',
        'Origin': 'https://yz.chsi.com.cn',
        'Referer': 'https://yz.chsi.com.cn/zsml/queryAction.do',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


if __name__ == '__main__':
    r = academic_master_category()
    for i in r:
        # print(i['dm'])
        amcs = academic_master_category_second(i['dm'])
        print(amcs)
    pass
