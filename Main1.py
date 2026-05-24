import requests   
def get_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        return f"🤷‍♀️🤦‍♀️ {data['text']}"
    else:
        return "sorry! I could not get a fact for you"
def chatbot():
        print("Welcome to the factbot, type 'fact' to get a fact or 'exit' to quit") 
        while True:
            userinput=input("You:").lower()
            if "fact" in userinput:
                print("Bot:"[get_fact()])
            elif "exit" in userinput:
                print("Bot:Goodbye for now")
                break
            else:
                print("Bot: I can only tell facts")
if __name__=="__main__":
    chatbot()
                    
                    
    