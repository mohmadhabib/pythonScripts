import requests, user_agent, bs4


r = requests.get("http://codelist.cc", headers={"User-Agent": str(user_agent.generate_user_agent())})
s = bs4.BeautifulSoup(r.text, "lxml")
print(s.title.text)
