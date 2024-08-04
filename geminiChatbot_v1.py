import os
import google.generativeai as genai # type: ignore
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

api_key = ""
if not api_key:
    raise ValueError("API key not found in environment variables.")

genai.configure(api_key=api_key)

def startChat(modelName):
    generation_config = {
        "temperature": 1,
        #
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name = modelName,
        # model_name="gemini-1.5-pro",
        #model_name="gemini-1.0-pro",
        #model_name="gemini-1.5-flash",    
        generation_config=generation_config,
    )
    chat_session = model.start_chat(history=[])
    return chat_session

modelIndex = input(f"Merhaba, lutfen asagidaki dil modellerinden birini seciniz.\n1 - GEMINI 1.0 PRO\n2 - GEMINI 1.5 PRO\n 3 - GEMINI 1.5 FLASH\n4 - CIKIS YAP\nUser:")
while True:
    if modelIndex == "1" or modelIndex == "2" or modelIndex == "3" or modelIndex == "4":
        if modelIndex == "4":
            break
        else:
            if modelIndex == "1":
                modelName = "gemini-1.0-pro"
            elif modelIndex == "2":
                modelName = "gemini-1.5-pro"
            elif modelIndex == "3":
                modelName = "gemini-1.5-flash"

            chat_session = startChat(modelName)
            userMessage = input("\nUser: ")
            if userMessage.lower() == "e":
                break
            else:
                responseChat = chat_session.send_message(userMessage)
                print("\nBot: "+responseChat.text)
                print("Press E for exit")   
    else:
        modelIndex = input(f"Bot:Hatali secim yaptiniz. Lutfen asagidaki birini seciniz.\n1 - GEMINI 1.0 PRO\n2 - GEMINI 1.5 PRO\n 3 - GEMINI 1.5 FLASH\n4 - CIKIS YAP\nUser:")

#neganwashere