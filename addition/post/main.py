# https://codingbat.com/pref
"""
uname: qohhorovusmonjon@gmail.com
pw1: qwer123*
dosavecreate: Create Account
"""
import httpx

d = {
"uname": "nimadir2689@gmail.com",
"pw1": "123456",
"dosavecreate": "Create Account"
}

response = httpx.post("https://codingbat.com/pref",data=d, headers={"Cookie": "JSESSIONID=368F53882C4F870B42B22095D0631FB9"})
print(response.status_code)