Step 1 - clone the repository
step 2 - change directory to django_mongodb (twice)
step 3 - install mongodb and create a database name inteliondb
step 4 -  run the command python manage.py runserver
step 5 - go to url http://127.0.0.1:8000/personapi/
step 6 - enter data inside content text area in the below form and hit post button this will save the data to mongo db database
{
"name": "aaksh",
"dob":"2022-12-09",
"country":"india"
}

step 7 - go to url http://127.0.0.1:8000/export_excel/ this will download the data with updated values.
