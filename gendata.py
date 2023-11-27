import random
from unidecode import unidecode
import requests
import json
def import_data_from_file(filename):
    text_file = open(filename, "r")
    temp = text_file.read().splitlines()
    text_file.close()
    return temp

# load name
female_names = import_data_from_file("./data/name/female.dat")
male_names = import_data_from_file("./data/name/male.dat")
lastnames = import_data_from_file("./data/name/lastname.dat")
cities = import_data_from_file("./data/location/city.dat")
occupations = import_data_from_file("./data/occupation.dat")
uni= import_data_from_file("./data/uni.dat")
purposes = ["Partner Technology Discussion/Contact","Internal Team Meeting","Find jobs in multinational cooperations / oversea","Increase salary","Promotion"]
# print(random.choice(lastnames) + " " + random.choice(female_names))
ages = ["18-23","23-30","30+"]

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

def gen_email(firstname,lastname):
    return unidecode(firstname).replace(" ","").lower() + unidecode(lastname).lower() + str(random_with_N_digits(random.randint(1,4))) + "@gmail.com"


def gen_facebook(firstname,lastname):
    return "facebook.com/" + unidecode(firstname).replace(" ","").lower() + "." + unidecode(lastname).lower() + str(random_with_N_digits(random.randint(1,4)))
def gen_profile() :
    lastname = random.choice(lastnames)
    firstname = random.choice(male_names)
    name = str(lastname) + " " + str(firstname) 
    bachelor_degree = random.choice(uni)
    master_degree = ""
    age = random.choice(ages)
    city = random.choice(cities)
    occupation = random.choice (occupations)
    if age == "18-23":
        experience = random.choice(["0","1","1.5","2"])
        if experience == "2":
            salary = random.choice (["5.000.000 - 9.000.000 VND","10.000.000 - 19.000.000 VND"])
        else:
            salary = random.choice (["< 5.000.000 VND","5.000.000 - 9.000.000 VND"])
        monthly_expense = random.choice(["2.000.000 VND","3.000.000 VND"])
    elif age == "23-30" :
        experience = random.choice(["1","2","3","4","5", "5+"])
        if experience == "4" or experience == "5" or experience == "5+" :
            salary = random.choice(["20.000.000 - 39.000.000 VND","> 40.000.000 VND"])
        elif experience == "1":
            salary = random.choice(["< 5.000.000 VND","5.000.000 - 9.000.000 VND"])
        else:
            salary = random.choice(["10.000.000 - 19.000.000 VND","20.000.000 - 39.000.000 VND"])
        monthly_expense = random.choice(["2.000.000 VND","3.000.000 VND","5.000.000 VND"])
    elif age == "30+":
        experience = random.choice(["3+","5+","10+"])
        salary = random.choice(["20.000.000 - 39.000.000 VND","> 40.000.000 VND"])
        monthly_expense = random.choice(["2.000.000 VND","3.000.000 VND","5.000.000 VND","8.000.000 VND"])
    ielts_level = random.choice(["5.0","5.5","6.0","6.5","7.0","7.5"])
    number_of_student = random.choice(["3-5","6-10","10-15","16-25","I want to study 1-1"])
    purpose = random.sample(purposes,random.randrange(1,5))
    # purpose = random.choice(purposes)
    method = random.choice(["Online","Face-to-face","Both"])
    class_time = random.choice(["Weekday evenings","Weekends"])
    learning_time = random.choice(["< 7 hours per week","8 - 14 hours per week","> 15 hours per week"])
    english_center = random.choice(["Apollo","VUS", "British Council","WWE", "GLN", "APEX", "The IELTS Workshop", "IPP", "AMA"])
    connect_with_recruiter = random.choice(["Yes","No"])
    cv_proofread = random.choice(["Yes","No"])
    joining_community = random.choice(["Yes","No"])

    # contact_method = random.choice(["Phone","Email","Facebook"])
    contact_method = random.choice(["Phone","Email","Facebook"])
    if contact_method == "Phone":
        contact_detail = "84" + random.choice(["9","3","1","2"]) + str(random_with_N_digits(8))
    elif contact_method == "Email": 
        contact_detail = gen_email(firstname,lastname)
    elif contact_method == "Facebook":
        contact_detail = gen_facebook(firstname,lastname)

    profile = {
        "entry.415556574": name,
        "entry.776697816": bachelor_degree,
        "entry.2006494093": master_degree,
        "entry.638413579": age,
        "entry.1476399588": city,
        "entry.992718012": occupation,
        "entry.639928952": experience,
        "entry.1770192502": salary,
        "entry.67804573" : ielts_level,
        "entry.1909742391": monthly_expense,
        "entry.1272455700": number_of_student,
        "entry.1755257017": purpose,
        "entry.321927448" : method,
        "entry.920837141" : class_time,
        "entry.1033342085": learning_time,
        "entry.116184900": english_center,
        "entry.1247531446": connect_with_recruiter,
        "entry.523225776": cv_proofread,
        "entry.1899388092": joining_community,
        "entry.961767779": contact_method,
        "entry.1335516143": contact_detail
    }
    return profile

def submit(url, data):
    try:
        response = requests.post(url, data = data)
        print("Submitted successfully")
        print(response.status_code)
        return True
    except:
        print("Error!")
        print(response.status_code)
        return False

'''----------------------------------------------------------------------'''
print("Running script...", flush = True)

url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLScv8pr5SPKSv7i8K8EdG9FxCo1ofvspNcd4zmtcX_C-xZ6LMg/formResponse"
data_gen=gen_profile()
print(json.dumps(data_gen, ensure_ascii=False,indent=4).encode('utf8').decode())
data_test = {
    "entry.415556574": "Nguyễn Công Trường Giang",
    "entry.776697816": "",
    "entry.2006494093": "",
    "entry.638413579": "23-30",
    "entry.1476399588": "Hà Nội",
    "entry.992718012": "DevOps Engineer",
    "entry.639928952": "5+", 
    "entry.1770192502": "10.000.000 - 19.000.000 VND",
    "entry.67804573": "7.0",
    "entry.1909742391": "3.000.000 VND",
    "entry.1272455700": "I want to study 1-1",
    "entry.1755257017": "Internal Team Meeting",
    "entry.321927448": "Online",
    "entry.920837141": "Weekends",
    "entry.1033342085": "< 7 hours per week",
    "entry.116184900": "IPP",
    "entry.1247531446": "Yes",
    "entry.523225776": "Yes",
    "entry.1899388092": "Yes",
    "entry.961767779": "Email",
    "entry.1335516143": "giangnct@mobio.io"
}
submit(url, data_gen)
