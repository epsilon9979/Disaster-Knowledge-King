from Step import Pipeline
from pipeline.cnn_resources_api import get_resource_int
from pipeline.disaster_resources_api import get_resource_dkk   
from pipeline.resources_api import get_resource
from pipeline.data_update import filter
from pipeline.large_language_model1 import manufacture
from pipeline.large_language_model2 import manufacture_plus
from pipeline.upload_question import insertquestions
from pipeline.database import record

def main(): 
    inputs = {} 
    
    for round in range(7):
        steps = [
            [get_resource(), get_resource(), get_resource(), get_resource_int(), get_resource_dkk(), get_resource_dkk(), get_resource_dkk()][round],
            filter(),
            [manufacture(), manufacture(), manufacture(), manufacture(), manufacture_plus(), manufacture_plus(), manufacture_plus()][round],
            insertquestions(),
        ] 
        
        print('\n','round ', round)
        database = record()
        a = Pipeline(steps)
        a.run(database, round)
    
    
if __name__ == '__main__':
    main()
    