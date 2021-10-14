import json
import requests

url = "https://opentdb.com/api.php?amount=10&category=15&difficulty=easy"

response = requests.get(url=url)
print(response.text)
json_object = json.loads(response.text)

results_arr = json_object["results"]
for results_obj in results_arr:
    question = requests.utils.unquote(results_obj["question"])
    print(question)
    if(results_obj["type"] == "multiple"):
        answers = [results_obj ["correct_answer"]] + results_obj["incorrect_answers"]
        for answer in answers:
            print("\t" + requests.utils.unquote(answer))
    print("***")

    """
    https://opentdb.com/api.php?amount=10&category=15&difficulty=easy
        https is the protocol
        opentdb is the domain
        api.php is the path to the endpoint
        the ? starts the query string
            The client dictates what they want 
            separated with &s
            list of key value pairs
                which are separated by =s
    DJjHECZibWfCWObGLn4Lzj9XUsuzGWph
    
    """

