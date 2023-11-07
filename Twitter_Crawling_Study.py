import json
import requests
from urllib import parse


headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Authorization':'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'Content-Type':'application/json',
    'Cookie':'_ga=GA1.2.215535419.1697192789; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; guest_id=v1%3A169719279222917261; guest_id_marketing=v1%3A169719279222917261; guest_id_ads=v1%3A169719279222917261; g_state={"i_p":1697201865183,"i_l":1}; kdt=K6Qyijqmt2F0FSjimAkxUFrgI2oazxxGy0plgNOR; auth_token=c347d612d7839a861d0f892a809c77ecdc39d890; ct0=10297bffa822a373d931d79b1d45a92f0d985c1c036eb0186f8ba948b501e76299ff2a942dbbaf086e0e01fb8d1cc32ffb3d11d0d30ac64a60da4e938e41aab36824ab7830eccb018958ea3a274a69ee; twid=u%3D1712787670102052864; _gid=GA1.2.1094178523.1697964581; lang=en; personalization_id="v1_cHGf4u2AazDGNNNKS0CETg=="',
    'Referer':'https://twitter.com/BTS_twt',
    'Sec-Ch-Ua':'"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'X-Client-Transaction-Id':'nEWMgi7NOriTi2k22ToGZQDT9vhwoFHgKzyQfUlK3aYL7bidTd9urzGoX27BWTzuPMg2epxYqOLh9+v0dCJIMKkPsyJ8nQ',
    'X-Csrf-Token':'10297bffa822a373d931d79b1d45a92f0d985c1c036eb0186f8ba948b501e76299ff2a942dbbaf086e0e01fb8d1cc32ffb3d11d0d30ac64a60da4e938e41aab36824ab7830eccb018958ea3a274a69ee',
    'X-Twitter-Active-User':'yes',
    'X-Twitter-Auth-Type':'OAuth2Session',
    'X-Twitter-Client-Language':'en'
}


params = {
    'variables': {"screen_name":"bts_twt",
                  "withSafetyModeUserFields":True}, # variables 를 받는 key값({"screen_name":"bts_twt","withSafetyModeUserFields":True})이 텍스트 형태임
    'features': {"hidden_profile_likes_enabled":True,
                 "hidden_profile_subscriptions_enabled":True,
                 "responsive_web_graphql_exclude_directive_enabled":True,
                 "verified_phone_label_enabled":False,
                 "subscriptions_verification_info_is_identity_verified_enabled":True,
                 "subscriptions_verification_info_verified_since_enabled":True,
                 "highlights_tweets_tab_ui_enabled":True,
                 "creator_subscriptions_tweet_preview_api_enabled":True,
                 "responsive_web_graphql_skip_user_profile_image_extensions_enabled":False,
                 "responsive_web_graphql_timeline_navigation_enabled":True},
    'fieldToggles': {"withAuxiliaryUserLabels":False}
        }


url = 'https://twitter.com/i/api/graphql/G3KGOASz96M-Qu0nwmGXNg/UserByScreenName'

res = requests.get(url, params=params)
print(res.text)



# params = {
#           "userId":"335141638", # 계정 아이디의 고유 넘버
#           "count":20,
#           "cursor":"DAABCgABF9DJzRg__-cKAAIWab6nhZqQAggAAwAAAAIAAA",
#           "includePromotedContent":True,
#           "withQuickPromoteEligibilityTweetFields":True,
#           "withVoice":True,
#           "withV2Timeline":True
#           }


# url = 'https://twitter.com/i/api/graphql/VgitpdpNZ-RUIp5D1Z_D-A/UserTweets'

# params_text = json.dumps(params) # 딕셔너리 형태에서 json 형태로 변환(사실 안 해도 출력값 잘 뽑혀서 필요없는 과정이긴 함)
# params_text = parse.quote(params_text) # URL 인코딩

# # print(params_text)

# res = requests.get(url + '?variables=' + params_text) # 정상적으로 response 200 나와서 헤더 추가 안함. 만약에 print(res) 해봐도 응답 안 하면 Headers 탭의 Request Headers 긁어모아서 헤더 정리해줘야 됨   

# print(res.status_code)
# print(res.text)