import requests

url= "https://docs.google.com/forms/d/e/1FAIpQLScvEHphzCvv6iy_z4wwChnd6JSFUCGofX5YITzNRJ2Q0_6O7A/formResponse"
form_data= {
    "entry.153093268": ["test1","test3"],
    "entry.1659636260": "test4",
    "entry.800382510": "Giang Nguyễn"
    # "fvv": 1,
    # "pageHistory": 0,
    # "fbzx": 2885560646669376540
}
print(requests.post(url, data=form_data).status_code)