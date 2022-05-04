# -*- coding: utf-8 -*-

import json
import pandas as pd
import requests


def parse_json(url, cert_key):
    url = url \
        + "mgtNo=ME2007E008" \
          + "&type=json" \
          + "&serviceKey=" + cert_key

    req = requests.get(url)
    html = req.text
    data = str(html).replace("body\":", "body\":[").replace("}}}", "}]}}")

    jsonObject = json.loads(str(data))
    # Results contain the required data
    df = pd.json_normalize(jsonObject["response"]["body"])

    return df
