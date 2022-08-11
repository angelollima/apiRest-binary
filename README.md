* **How use in your machine**

`pip install uvicorn`
`pip install fastapi`

* **How to search for specific urls through the main url**

If you type `http://127.0.0.1:8000/punctuations` will be redirected to this url, which is the same `http://127.0.0.1:8000/punctuations/`!<br />
the same happens here `http://127.0.0.1:8000/letters` -> `http://127.0.0.1:8000/letters/`!<br />
and here `http://127.0.0.1:8000/numbers` -> `http://127.0.0.1:8000/numbers/`!

* **How to search for a particular value**

To search for something specific by the url, do the same as the examples:

for numbers -> `http://127.0.0.1:8000/?number=783`<br />
for punctuation -> `http://127.0.0.1:8000/?punctuation=@`<br />
for letters -> `http://127.0.0.1:8000/?letter=a`

* ***Requesting the api***

>the whole api

response = requests.get('http://127.0.0.1:8000/').json()<br />

>specific

punctuation = response["punctuations"]
