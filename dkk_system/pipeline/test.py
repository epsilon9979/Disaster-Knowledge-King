from google import genai
from google.genai import types
from pydantic import BaseModel
from Step import STEPS
from parameter import get_para
from dotenv import load_dotenv
import os

print("\n in manufacture ##############################################################")

data = [
    {'內容': '\n            A magnitude-7.5 earthquake struck off Japan’s northeastern coast on Monday, injuring more than two dozen people and prompting authorities to issue evacuation orders for more than 100,000 people.\n    \n            The earthquake struck at 11:15 p.m. local time around 44 miles off the northeast coast of the country, at a depth of about 33 miles, according to the United States Geological Survey (USGS).\n    \n            A CNN team in Japan’s capital Tokyo – more than 400 miles away – felt strong tremors during the earthquake, which lasted for longer than 30 seconds.\n    \n            The JMA warned there was a possibility a “large-scale earthquake of magnitude 8 or greater” could occur in Japan this week, but put the probability at 1%.\n    \n            “While it remains deeply uncertain whether a major earthquake will actually occur, we believe it’s essential to take disaster preparedness measures based on the principle that we must protect our own lives,” the agency said.\n    \n            Following the quake, The Japan Meteorological Agency (JMA) issued a tsunami warning for the Pacific coast of Hokkaido, Aomori prefecture and Iwate prefecture.\n    \n            However, the tsunami waves were not as high as feared. A 2.3-foot tsunami was observed at Kuji port in Iwate, while a 1.3-foot tsunami was recorded in Aomori and Hokkaido, the JMA said.\n    \n            After several hours, the JMA downgraded the warning to a tsunami advisory, and by Tuesday morning the advisory was lifted.\n    \n            Evacuation orders were issued for over 114,000 people, Japan’s Fire and Disaster Management Agency said early Tuesday.\n    \n            Japan’s Prime Minister Sanae Takaichi told reporters Tuesday at least 30 people were injured in the quake, warning similar or even stronger tremors could follow.\n    \n            There were several reports from Aomori prefecture of injuries and fires, Chief Cabinet Secretary Minoru Kihara said at a news conference early Tuesday.\n    \n            He said power outages have been reported in Aomori and Iwate and that high-speed train service was suspended between Fukushima and Aomori. Some sections of expressways were also closed, Kihara said.\n    \n            Video by Reuters news agency showed a damaged hotel and buildings in Mutsu, a city in Aomori prefecture, and a car stuck on a damaged highway.\n    \nAs tsunami waves swept the Pacific, some in Asia saw signs of a manga prophecy come true\n\n            Earlier, Kihara urged people in affected areas to evacuate to higher ground or move to safe buildings, such as evacuation shelters.\n    \n            There have been no reports of “abnormalities at this time” at the country’s Higashidōri and Onagawa nuclear power plants, Kihara said. “We have received reports that other nuclear facilities are currently being checked,” he added.\n    \n            Takaichi, who was elected in October, said her government would work closely with local officials to assess the damage and put in place emergency response measures.\n    \n            The government would be “acting as one under the principle of putting human life first,” she said.\n    \n            Japan is no stranger to severe earthquakes. It lies on the Ring of Fire, an area of intense seismic and volcanic activity on both sides of the Pacific Ocean. The worst quake in recent Japanese history was the 9.1-magnitude Tohoku earthquake in 2011 that triggered a major tsunami and nuclear disaster.\n    \n            That quake and tsunami left more than 22,000 people dead or missing and caused reactors at the Fukushima Daiichi nuclear power plant to melt down, releasing radioactive contamination into the surrounding area.\n    \nCNN’s Junko Ogura, Brandon Miller, Lauren Kent and Mitchell McCluskey contributed to this report. \n© 2026 Cable News Network. A Warner Bros. Discovery Company. All Rights Reserved.  CNN Sans ™ & © 2016 Cable News Network.Scan the QR code to download the CNN app on Google Play.Scan the QR code to download the CNN app from the Apple Store.', '上版日期': 115015, 'county': ['disaster'], '標題': 'Tsunami warning issued for Japan’s east coast after 7.6-magnitude earthquake | CNN', '來源網址': 'https://www.cnn.com/2025/12/08/asia/tsunami-warning-japan-earthquake-intl', 'rag_link': 'earthquakes'},
    {'內容': '\n\n      World\n  \n\n\n      World\n  \nPeople mourn behind flowers near the sealed off Le Constellation bar, where a devastating fire left dead and injured during the New Year\'s celebrations in Crans-Montana, Swiss Alps, Switzerland, Friday, Jan. 2, 2026. (AP Photo/Baz Ratner)CRANS-MONTANA, Switzerland: Swiss authorities on Friday (Jan \u200c2) said dozens of people badly burned in a fire in a bar in a ski resort during New Year\'s Eve celebrations - in which 40 people died - were being taken to nearby countries for specialised treatment.Investigators were also closing in on the circumstances of the blaze, which occurred early Thursday in the Alpine town of Crans-Montana."Everything suggests that the fire started from sparklers or Bengal candles" placed in Champagne bottles and waved high, near the low ceiling of the bar, the chief prosecutor of the Wallis region, Beatrice Pilloud, told a press conference.The French managers of the bar, Le Constellation, have been questioned, along with multiple survivors, she said.The details emerged as Switzerland reeled from the tragedy, and as families of the hundreds of people, most of them young, who had been packed into the bar braced for news of their loved ones.The exact number of people who were at the bar when it went up in flames remains unclear. The Crans-Montana website said the venue had a capacity of 300 people plus 40 on its terrace.The fire\'s destruction was so intense that Swiss authorities were not able, in the immediate aftermath, to give a precise number of dead, nor identify the badly burned survivors.But in Friday\'s press conference, Wallis canton regional police commander Frederic Gisler said "at this stage" the death toll was 40, with most of the bodies found inside the bar.Swiss authorities warned it could take days to identify everyone who perished, leaving an agonising wait for family and friends. Online, desperate appeals to find the missing proliferated.Of the 119 people injured - most in a critical condition - \xa0113 were now identified, Gisler said, with officials working "relentlessly" to complete the task.Twenty-four of the injured were being medically evacuated to other countries to help Switzerland\'s overloaded burn facilities, the EU\'s commissioner for crisis management, Hadja Lahbib, said on X.Belgium, France, Germany, Italy, Luxembourg and Romania were among the countries taking in the survivors, she said.The head of the Swiss canton where Crans-Montana is located, Mathias Reynard, told reporters a total of around 50 people would end up being transferred to other European countries "for treatment in special burn units".\xa0Numerous foreign nationals were among the injured -- and were also expected to figure among the dead.Gisler said that, of the injured, 71 were Swiss, 14 were French, 11 were Italian, and there were four Serbs, as well as individual Bosnian, Belgian, Polish, Portuguese and Luxembourg nationals.In 14 cases, the nationality was still unknown, he said.Videos posted online, and viewed by investigators, have pointed to sparklers stuck in Champagne bottles igniting the ceiling being the likely cause.One video showed the low wooden ceiling - covered with soundproofing fabric - catching alight and the flames spreading quickly, but revellers continuing to dance, unaware of the death trap they were in.Once they realised, panic set in.Bystanders described scenes of chaos as people tried to break the windows to escape, while others, covered in burns, poured into the street."Some of our hypotheses have now been confirmed. Indeed, everything suggests that the fire started from the sparklers or Bengal candles that had been placed on the Champagne bottles, which were held too close to the ceiling," the prosecutor, Pilloud, told reporters.The bar\'s French managers - said by multiple sources to be a couple from Corsica - escaped unharmed and were questioned as "witnesses", with no liability established at this stage, she said.Their information explained the layout of the bar, details about recent renovations, and the bar\'s capacity, as well as indications to help with filling out a list of people present at the time of the fire, Pilloud said.As authorities began moving bodies from the burned-out premises in central Crans-Montana, the resort appeared to be enveloped in a stunned silence on Friday."The atmosphere is heavy," Dejan Bajic, a 56-year-old tourist from Geneva who has been coming to the resort since 1974, told AFP.\xa0"It\'s like a small village; everyone knows someone who knows someone who\'s been affected," he said.Locals and tourists who witnessed the aftermath of the tragedy told AFP what they saw."We thought it was just a small fire - but when we got there, it was war," Mathys, from the neighbouring village of Chermignon-d\'en-Bas, said, declining to give his last name. "That\'s the only word I can use to describe it: the apocalypse."Edmond Cocquyt, a Belgian tourist, said he saw bodies "covered with a white sheet" and "young people, totally burned, who were still alive ... screaming in pain".As he laid flowers in memory of the victims in Crans-Montana, Italian Foreign Minister Antonio Tajani told reporters the "absolute priority" was to save the lives of the critically hurt survivors.The objective was also, he said, "to identify those responsible", pointing out that "the use of fireworks, even small ones, in a place like this seems irresponsible".Get our pick of top stories and thought-provoking articles in your inboxStay updated with notifications for breaking news and our best storiesGet WhatsApp alertsJoin our channel for the top reads for the day on your preferred chat appCopyright© Mediacorp 2026. Mediacorp Pte Ltd. All rights reserved.We know it\'s a hassle to switch browsers but we want your experience with CNA to be fast, secure and the best it can possibly be.To continue, upgrade to a supported browser or, for the finest experience, download the mobile app.Upgraded but still having issues? Contact us', '上版日期': 1150206, 'county': ['disaster'], '標題': 'Swiss send dozens injured in bar fire abroad for treatment', '來源網址': 'https://www.channelnewsasia.com/world/swiss-send-dozens-injured-in-bar-fire-abroad-treatment-5786951', 'rag_link': 'home-fires'}
    ]

load_dotenv()
API_key = os.getenv("GEMINI_API_KEY")
gemini_model = get_para('gemini_model')
county_list = get_para('county_list')
table_name = get_para('TABLE_NAME')

gemini_tools = types.Tool(
    google_search = types.GoogleSearch()
)

class question(BaseModel):
    Question: str
    Option_A: str
    Option_B: str
    Option_C: str
    Option_D: str
    Correct_Answer: str
    Explanation: str
    Response_Method: str

def gemini_normal(content):
    response = chat.send_message(content, config = types.GenerateContentConfig(
        response_mime_type = "application/json",
    ))
    # answer = response.text.strip("\n").strip()
    answer = response.text
    tokens = response.usage_metadata.total_token_count
    return [answer, tokens]

def gemini_rag(content):
    response = chat.send_message(
        content, 
        config = types.GenerateContentConfig(
            tools=[
                types.Tool(
                    file_search=types.FileSearch(
                        file_search_store_names=[store.name],
                    )
                )
            ]
    ))
    print(store.name)
    # answer = response.text.strip("\n").strip()
    answer = response.text
    tokens = response.usage_metadata.total_token_count
    return [answer, tokens]

def gemini_search(content):
    response = chat.send_message(content, config = types.GenerateContentConfig(
        tools = [gemini_tools],
    ))
    # answer = response.text.strip("\n").strip()
    answer = response.text
    tokens = response.usage_metadata.total_token_count
    return [answer, tokens]

def gemini_final(content):
    response = chat.send_message(content, config = types.GenerateContentConfig(
        response_schema = list[question],
        response_mime_type = "application/json",
    ))
    # answer = response.text.strip("\n").strip()
    answer = response.text
    tokens = response.usage_metadata.total_token_count
    return [answer, tokens]

series = []
for news in data:
    content = news['內容']
    url = "https://www.ready.gov/" + news['rag_link'] 
    
    client = genai.Client(api_key=API_key)
    chat = client.chats.create(model=gemini_model)
    stores_list = client.file_search_stores.list()
    store = next((s for s in stores_list if s.display_name == "disaster_response_guide"), None)
    prompt1 = f"You are now a global disaster intelligence expert. Please organize the article from link '{news['來源網址']}' into four key points, focusing on the damages caused."
    # prompt2 = "Next, based on these four key points, help me create a multiple-choice question with four options (A, B, C, D) and provide the correct answer."
    prompt2 = "Based on these four key points, create a multiple-choice question with four options, designed so that people can use reasoning to arrive at the answer and understand what happened. Please also provide the correct answer."
    prompt3 = 'Then provide an explanation for the answer in under 70 words, and ensure that "the text does not contain the words \'option\' or \'A, B, C, D\'." '
    prompt4 = f'Next, "based on the knowledge of {news["rag_link"]}, please tell me how to respond if i am personally involved in the case of this article, within 70 words.'
    prompt5 = "Based on the content above, return the 'Question', 'Option_A', 'Option_B', 'Option_C', 'Option_D', 'Correct_Answer', 'Explanation', and 'Response_Method'."
    
    order1 = prompt1
    response1 = gemini_search(order1)
    # print("response1: ", response1[0])
    response2 = gemini_normal(prompt2)
    # print("response2: ", response2)
    response3 = gemini_normal(prompt3)
    # print("response3: ", response3[0])
    response4 = gemini_rag(prompt4)
    # print("response4: ", response4[0])
    response5 = gemini_final(prompt5)
    print("response5: ", response5[0]) ######################################
    print("total token usage: ", response1[1] + response2[1] + response3[1] + response4[1] + response5[1])
    
    questions = {}
    questions['rawquestion'] = response5
    questions['county'] = news['county'][0]
    questions['time'] = news['上版日期']
    questions['title'] = news['標題']
    questions['url'] = news['來源網址']
    series.append(questions)

print(series)

# return series        
                    
                    
        
