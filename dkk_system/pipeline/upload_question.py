from Step import STEPS
from time import sleep
from parameter import get_para
import random
import json

class insertquestions(STEPS): 
    
    def process(self, data, database):
        print("\n in insertquestions ##############################################################")
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
            option_A = "A) " + rawquestion["Option_A"]
            option_B = "B) " + rawquestion["Option_B"]
            option_C = "C) " + rawquestion["Option_C"]  
            option_D = "D) " + rawquestion["Option_D"]
            correct_answer = "正確答案： " + rawquestion["Correct_Answer"] + ")"
            explanation = rawquestion["Explanation"]
            if rawquestion.get("Response_Method") != None:
                response_method = rawquestion["Response_Method"]
                explanatin_plus_response_method = explanation + "&&&" + response_method
            else:
                explanatin_plus_response_method = explanation
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