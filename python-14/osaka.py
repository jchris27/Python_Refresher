import random

prefecture = "Osaka City"

local_specialties = "Takoyaki"

top_attraction = "Universal Studio Japan"

famous_landmark = "Dotonburi"



def random_fun_facts():
    fun_facts = [
        "Osaka is popular because of its underground shopping mall experience that is ultimately one of the greatest tourist attractions.",
        "Osaka was once the capital of Japan",
        "Osaka is home to Universal Studios Japan",
        "One of the largest aquariums in the world is in Osaka"
    ]

    choice = random.choice("0123")

    print(fun_facts[int(choice)])

if __name__ == "__main__":
    random_fun_facts()