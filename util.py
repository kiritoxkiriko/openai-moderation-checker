import openai
import os

CAT_MAP = {
    "hate": "仇恨",
    "hate/threatening": "仇恨-威胁",
    "self-harm": "自我伤害",
    "sexual": "性暗示",
    "sexual/minors": "性暗示-未成年",
    "violence": "暴力",
    "violence/graphic": "暴力-强画面感",
}

PASSCODE = "123456"
API_KEY = "sk-xxxxxxxxxxxx"

if os.environ.get("PASSCODE") is not None:
    PASSCODE = os.environ.get("PASSCODE")

if os.environ.get("API_KEY") is not None:
    openai.api_key = os.environ.get("API_KEY")
else:
    openai.api_key = API_KEY


def check_moderation(text: str):
    response = openai.Moderation.create(
        input=text
    )
    output = response["results"][0]
    for k, v in output["category_scores"].items():
        if isinstance(v, float):
            output["category_scores"][k] = round(v, 3)
    return output


def cal_score(score):
    if score < 0.1:
        return "无"
    elif score < 0.25:
        return "可能性很小"
    elif score < 0.5:
        return "有可能"
    elif score < 0.9:
        return "很有可能"
    else:
        return "极有可能"


def get_res(output) -> dict:
    scores = output["category_scores"]
    res = {}
    for k, v in scores.items():
        if k in CAT_MAP:
            res[CAT_MAP[k]] = cal_score(v)
    return res
