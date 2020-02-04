POS Recognition from Image (POSTagger)

A Django based tool that takes an image as input, extract characters from it and returns output as a single best POS tag for each word.

Technical Stack-

1.Django(Framework)

2.django-crispy-forms

3.Pillow

4.pytz

5.pytesseract

6.nltk(natural language tool-kit)

7.HTML CSS JS


## Running Locally

```bash
git clone https://github.com/sibtc/simple-file-upload.git
```
Go to the directory where manage.py exists and run the following commands-
```bash
pip install -r requirements.txt
```
Important- You must have go to the views.py of POSGenerate app and set path in generate function according to your media directory.

```bash
python manage.py migrate
```
(Run the server)
```bash
python manage.py runserver
```
Result- A POS.txt(text file) will be created in Image_POS_TAGGER.