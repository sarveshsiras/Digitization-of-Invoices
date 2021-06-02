# Digitization-of-Invoices, <br> A deep learning based approach

## Project Description:
- Correctly recognizing the scanned copy of given invoice and its overall template using a table detection deep learning model.
- Optical Character Recognition - recognizing the text and numbers present in the documents.
- Important to identify which piece of text corresponds to which extracted field (like prices of goods, total amount, etc.).
- Identifying the table structure as well as all the values present inside the table.
- Storing extracted information in a retrievable format like an Excel Sheet so that further computations can be done over data by seller/buyer.

## Dependancies 
~~~python:
  pip install flask
  pip install pymongo
  pip install pandas
  pip install boto3
  pip install pytesseract
~~~

## Prerequisites for the deployed model

- PyTorch - Version: 1.4.0
- CUDA enabled (v10.0)
- Torch Vision v0.5.0
- Tesseract v4.0

Deployed model Link - https://www.kaggle.com/sarveshsiras/deployed-model

## Configuration for the application

- Add your secret key and access key in the aws_credentials.py (This will be used to store uploaded invoice on the s3 bucket)
- Add your mongodb credentials in config.py ( This will be used to store the user information on MongoDB cluster )

## Starting the application

~~~python
  git clone "https://github.com/sarveshsiras/Digitization-of-Invoices.git"
  cd 'Digitization-of-Invoices'/
  python app.py
~~~




