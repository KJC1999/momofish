import json
import string
from Common import debugtalk

data = {
        "guidMergeText": "<color=#275C83><color=#FC6907>样式</color>和<color=#FC6907>等级</color>都相同的英雄可以合并成更高等级的英雄。</color>",
        "tips": "提示",
        "IKnow": "知道了!",
        "shopConfig": "商店也开放了",
        "openBox": "开启黑耀石宝箱",
        "openRank": "排行榜已开启",
        "openTask": "任务已开启",
        "pleaseFinishGuide": "请先完成教学引导",
        "UpgradeHeroTips": "有一个新英雄\n等待上场",
    }

key = list(data.keys())
value = list(data.values())
print(type(len(value)))

# 判断value是否全为中文
for i in range(len(value)):
    if not '\u4e00' <= value[i] <= '\u9fa5':
        print("not all chinese")
    else:
        str = value[i].replace('\n', 'momofish_kjc')
        value[i] = debugtalk.translate_api(str)

# print(value)

for i in range(len(key)):
    data.update({key[i]: value[i]})

print(data)
