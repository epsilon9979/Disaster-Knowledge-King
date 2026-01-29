from Step import STEPS
from time import sleep
from parameter import get_para
from pipeline.database import record ###################
import random
import json

data = [
    {'rawquestion': '[\n  {\n    "Question": "Considering the immediate aftermath of the magnitude 7.6 earthquake and tsunami warning in northern Japan, which statement most accurately describes the scope of the damage caused?",\n    "Option_A": "The main damages were limited to minor injuries for roughly 50 individuals and power outages for less than 1,000 homes, with most infrastructure remaining intact.",\n    "Option_B": "The earthquake primarily caused the collapse of 7 homes and localized water pipe damage, but widespread evacuations successfully prevented significant further impact on other structures or utilities.",\n    "Option_C": "The event resulted in dozens of injuries and massive evacuations, extensive damage to thousands of buildings and homes, widespread disruptions to essential utilities like water and electricity, and specific critical infrastructure failures, indicating a broad and severe impact across multiple prefectures.",\n    "Option_D": "The damage was largely confined to the cracking of an airport ceiling and the flooding of one hospital, with only minimal impact on residential buildings or public services.",\n    "Correct_Answer": "C",\n    "Explanation": "The information provided details dozens of injuries, 90,000 evacuations, over 2,300 damaged buildings, thousands of homes losing water and power, and significant infrastructure failures like airport and hospital damage. This comprehensive range of impacts across multiple prefectures demonstrates a broad and severe disaster, which the correct statement accurately summarizes.",\n    "Response_Method": "If personally involved in an earthquake, like the one described, remember to **Drop, Cover, and Hold On**. Immediately drop to your hands and knees. Cover your head and neck under a sturdy table or desk. Hold on until the shaking stops. If outside, move to an open area away from buildings. If in a car, pull over, stop, and stay inside. Be prepared for aftershocks."\n  }\n]', 'county': 'disaster', 'time': 115015, 'title': 'Tsunami warning issued for Japan’s east coast after 7.6-magnitude earthquake | CNN', 'url': 'https://www.cnn.com/2025/12/08/asia/tsunami-warning-japan-earthquake-intl'}, 
    {'rawquestion': '[\n  {\n    "Question": "The devastating bar fire in Crans-Montana during New Year\'s Eve caused extensive damages. Which of the following statements best summarizes the immediate humanitarian impact and the subsequent challenge to the local infrastructure, as described in the key points?",\n    "Option_A": "The fire caused significant property destruction, primarily impacting the bar\'s structure and leading to a prolonged investigation into building safety standards.",\n    "Option_B": "A large number of fatalities and severe burn injuries quickly overwhelmed the regional hospital, necessitating the urgent transfer of dozens of patients to specialized medical facilities in other Swiss cities and neighboring countries.",\n    "Option_C": "The primary damage was the difficulty in identifying victims due to the extreme severity of their burns, which highlighted flaws in national disaster identification protocols.",\n    "Option_D": "The incident led to immediate and drastic revisions of fire safety regulations across Switzerland, particularly regarding the use of pyrotechnics in public venues.",\n    "Correct_Answer": "B",\n    "Explanation": "The chosen answer accurately combines the devastating human toll (fatalities and severe injuries) with the critical strain on the local healthcare system, which was unable to cope. This necessitated urgent patient transfers to specialized facilities both nationally and internationally, directly reflecting the widespread damages described in the key points.",\n    "Response_Method": "If personally involved in a bar fire, prioritize escape immediately. Get low and crawl under smoke to find the nearest clear exit. Before opening doors, feel if they are hot; if so, find another escape route. Once outside, stay out and move to a safe meeting place away from the building. Call emergency services (like 911 or the local equivalent) and report the fire. Do not re-enter for any reason."\n  }\n]', 'county': 'disaster', 'time': 1150206, 'title': 'Swiss send dozens injured in bar fire abroad for treatment', 'url': 'https://www.channelnewsasia.com/world/swiss-send-dozens-injured-in-bar-fire-abroad-treatment-5786951'}
    ]

print("\n in insertquestions ##############################################################")
database = record()
cursor, cnx = database.setting()
amount = get_para('amount_per_category')
interim = get_para('interim')

def id_generator(existed_id):
    valid_num = [i for i in range(0, amount) if i not in existed_id]
    return random.choice(valid_num)

for batch in data:
    sleep(interim)
    rawquestion = json.loads(batch['rawquestion'])[0]
    question = rawquestion["Question"]
    option_A = rawquestion["Option_A"]
    option_B = rawquestion["Option_B"]
    option_C = rawquestion["Option_C"]  
    option_D = rawquestion["Option_D"]
    correct_answer = rawquestion["Correct_Answer"]
    explanation = rawquestion["Explanation"]
    response_method = rawquestion["Response_Method"]
    explanatin_plus_response_method = explanation + "&&&" + response_method
    components = [question, option_A, option_B, option_C, option_D, correct_answer, explanatin_plus_response_method]
    components.append( batch['time'] )
    components.append( batch['title'] )
    components.append( batch['url'] )
    
    table_name = batch['county']
    existed_id = database.fetch(cursor, cnx, table_name, 'id', None)
    id = id_generator(existed_id)
    components.insert(0, id)
    achievement = tuple(components)
    print(achievement)
    database.append(cursor, cnx, achievement, table_name)