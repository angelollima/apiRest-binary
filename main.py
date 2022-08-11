import uvicorn
from fastapi import FastAPI
import string
import json

app = FastAPI()

#soma de binarios

*digits, = string.digits
*punctuation_methods, = string.punctuation
*letters_lowercase, = string.ascii_lowercase
*upper_lower_letters, = "".join(c + c.upper() for c in letters_lowercase)
*words_accent, = "".join(c + c.upper() for c in """
áâãàäåæāăąªçÇcĆčČďđĎĐéÉêÊèÈëËēĒėĖęĘěĚĕĔəƏ
ģĢğĞíÍìÌîÎïÏīĪįĮıİķĶĺĹļĻľĽłŁñÑńŃņŅňŇóÓôÔõÕòÒöÖøØōŌőŐœŒ
ŕŔřŘß§śŚšŠşŞþÞťŤțȚţŢúÚüÜùÙûÛūŪůŮűŰųŲũŨýÝźŹżŻžŽ
""")

@app.get("/")
def everything(letter: str | None=None, number: int | None=None):
    all_letters = {letter: f'{ord(letter):08b}' for letter in upper_lower_letters}
    accentuation_letters = {accentuation: f'{ord(accentuation):08b}' for accentuation in words_accent}
    all_numbers = {number: f'{ord(number):08b}' for number in digits}
    all_punctuation = {punctuation: f'{ord(punctuation):08b}' for punctuation in punctuation_methods}
    if letter is None and number is None:
        resposta = ({
            "letters": all_letters,
            "letters with accent": [accentuation_letters],
            "numbers": all_numbers,
            "punctuations": all_punctuation
        })
        return resposta
        #return {"letters": all_letters, "numbers": all_numbers}
    else:
        response = []
        for k, v in all_letters.items():
            if k.lower() == letter:
                response.append({k: v})
        for k, v in accentuation_letters.items():
            if k == letter:
                response.append({k, v})
        for k, v in all_numbers.items():
            if int(k) == number:
                response.append({k: v})
        return response



"""@app.get("/letters/")
def letters():
    all_letters = {"letters":{letter: f'{ord(letter):08b}' for letter in lista}}
    return all_letters

@app.get("/numbers/")
def numbers():
    all_numbers = {"numbers":{number: f'{ord(number):08b}' for number in digits}}
    return all_numbers"""

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)