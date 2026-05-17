import requests   
def get_joke():
    url="https://official-joke-api.appspot.com/random_joke"
    #get a response
    response=requests.get(url)
    #check if the request was succesful
    if response.status_code==200:
        #convert data from json
        data=response.json()
        return f"{data['setup']} 🤣🤣 \n {data['punchline']}"
    else:
        #was not successful
        return "sorry! I could not get a joke for you"
#display the joke in the terminal
def chatbot():
        print("Welcome the the jokebot, type 'joke' to get a joke or 'exit' to quit") 
        while True:
            userinput=input("You:").lower()
            if "joke" in userinput:
                print("Bot:",get_joke())
            elif "exit" in userinput:
                print("Bot:Goodbye for now")
                break
            else:
                print("Bot: I can only tell jokes")
if __name__=="__main__":
    chatbot()
                    
                    
    