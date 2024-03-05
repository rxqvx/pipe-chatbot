
#Henrique Kenji 22.121.030-5
#Fernando Chan Lin 22.221.015-5
#Erico Medeiros Correia da Silva 22.221.051-0

from chatbot import ChatBot
myChatBot = ChatBot()
#apenas carregar um modelo pronto
#myChatBot.loadModel()

#criar o modelo
myChatBot.createModel()




print("Bem vindo ao Chatbot PIPE! Minha função é tirar suas dúvidas sobre o programa!")


pergunta = input("\ncomo posso te ajudar?\n")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta + "   ["+intencao[0]['intent']+"]")


while (intencao[0]['intent']!="despedida"):
    pergunta = input("\nposso lhe ajudar com algo a mais?\n")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print(resposta + "   [" + intencao[0]['intent'] + "]")

print("Foi um prazer atendê-lo")
