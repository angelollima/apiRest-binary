import uvicorn
import asyncio
from fastapi import FastAPI
from ascii import *

app = FastAPI()

@app.get("/")
async def everything(letter: str | None=None, number: int | None=None):
    all_letters = {letter: f'{ord(letter):08b}' for letter in upper_lower_letters()}
    all_accentuation_letters = {accentuation: f'{ord(accentuation):08b}' for accentuation in words_accent()}
    all_numbers = {number: f"{number:b}" for number in digits()}
    all_punctuation = {punctuation: f'{ord(punctuation):08b}' for punctuation in punctuation_methods()}
    if letter is None and number is None:
        resposta = ({
            "letters": all_letters,
            "letters with accent": [all_accentuation_letters],
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
                response.append({k, v})
        for k, v in all_numbers.items():
            if int(k) == number:
                response.append({k: v})
        return response


@app.get("/letters/")
def letters():
    all_letters = {letter: f'{ord(letter):08b}' for letter in upper_lower_letters}
    all_accentuation_letters = {accentuation: f'{ord(accentuation):08b}' for accentuation in words_accent()}
    return all_letters, all_accentuation_letters


@app.get("/numbers/")
def numbers():
    all_numbers = {number: f"{number:08b}" for number in digits()}
    return all_numbers


@app.get("/punctuation/")
def punctuation():
    all_punctuation = {punctuation: f'{ord(punctuation):08b}' for punctuation in punctuation_methods()}
    return all_punctuation


async def main():
    config = uvicorn.Config("main:app", host="127.0.0.1", port=8000, reload=True)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())