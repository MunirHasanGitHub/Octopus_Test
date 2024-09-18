# Octopus_Test
This python script is designed to
1. retreive all outage using an API GET call to a outage info URL
2. retreive information about a site using an API GET call to a site info URL
3. combine the information about a site and the outages that have been recorded and POST that information to outage site URL

To do the API calls. The import request library to do a GET and POST url calls. The API key was in the environment variable and used to grant access to the API call.

When data is recieved from an API GET call, the data is stored in a list and also written to a csv file. The CSV file allows the data to be human readable and inspected later for debugging.

In order to combine the site info and the outage data. I did the following
- the outage data is sorted by outage begin time
- once sorted by begin time, I filtered the list to only contain outages after '2022-01-01T00:00:00.000Z'
- then a for loop is used to check if the site device id is one of the outage recorded, if so that outage is appened to a site outage list.

The site outage list is posted to the URL.

To test the URL for errors I did the following
1. removed the key to check for 403 error
2. changed the url to an incorrect site to get 404 error
3. changed the data to an incorrect JSON format got 400 error
4. loop the python code to write the same information a 5 times, this then gave 500 error
