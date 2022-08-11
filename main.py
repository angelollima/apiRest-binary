import uvicorn
from fastapi import FastAPI
from formation import *

app = FastAPI()

@app.get("/")
def everything(letter: str | None=None, number: int | None=None, punctuation: str | None=None):
    all_letters = {letter: f'{ord(letter):08b}' for letter in upper_lower_letters()}
    all_accentuation_letters = {accentuation: f'{ord(accentuation):08b}' for accentuation in words_accent()}
    all_numbers = {number: f"{number:b}" for number in digits()}
    all_punctuation = {punctuation: f'{ord(punctuation):08b}' for punctuation in punctuation_methods()}
    if letter is None and number is None and punctuation is None:
        resposta = ({
            "letters": all_letters,
            "letters_with_accent": all_accentuation_letters,
            "punctuations": all_punctuation,
            "numbers": all_numbers
        })
        return resposta
    else:
        response = []
        for k, v in all_letters.items():
            if k.lower() == letter:
                response.append({k: v})
        for k, v in all_accentuation_letters.items():
            if k == letter:
                response.append({k: v})
        for k, v in all_numbers.items():
            if int(k) == number:
                response.append({k: v})
        for k, v in all_punctuation.items():
            if k == punctuation:
                response.append({k: v})
        return response


@app.get("/letters/")
def letters():
    all_letters = {letter: f'{ord(letter):08b}' for letter in upper_lower_letters}
    all_accentuation_letters = {accentuation: f'{ord(accentuation):08b}' for accentuation in words_accent()}
    return all_letters, all_accentuation_letters


@app.get("/numbers/")
def numbers():
    all_numbers = {number: f"{number:8b}" for number in digits()}
    return all_numbers


@app.get("/punctuations/")
def punctuation():
    all_punctuation = {punctuation: f'{ord(punctuation):08b}' for punctuation in punctuation_methods()}
    return all_punctuation

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)