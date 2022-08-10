from tokenize import Number
import uvicorn
from fastapi import FastAPI
import string

app = FastAPI()

#soma de binarios

*teste, = string.ascii_lowercase
*teste1, = string.digits
*lista, = "".join(c + c.upper() for c in teste)

@app.get("/")
def everything(letter: str | None=None, number: int | None=None):
    all_letters = {letter: f'{ord(letter):08b}' for letter in lista}
    all_numbers = {number: f'{ord(number):08b}' for number in teste1}
    if letter is None and number is None:
        """thing = {"letters": all_letters}
        other_thing = {"numbers": all_numbers}
        my_dict = {"thing": thing, "other_thing": other_thing}
        return my_dict"""
        return {"letters": all_letters, "numbers": all_numbers}
    else:
        response = []
        for k, v in all_letters.items():
            if k.lower() == letter:
                response.append({k: v})
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
    all_numbers = {"numbers":{number: f'{ord(number):08b}' for number in teste1}}
    return all_numbers"""

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)