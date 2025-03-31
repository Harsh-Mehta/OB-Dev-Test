# OB-Dev-Test

Using the materials provided write a Python script to perform the following tasks:

1. Connect to the Open Air Quality API (using the provided documentation) and get a list of all countries. Maximum results per API call must be limited to 100. Output the country ‘name’ and ‘id’ to console
2. Implement a function to allow a user to search the results from step 1 using a country name, output ‘name’ and ‘id’ to console
3. Use the ID for ‘United States’ to get a list of all sensors in that location (ID should be obtained using the function from step 2)
4. Output all sensor IDs, names and latitude/longitude for the given region to a HTML page
5. Update function used to complete Step 3 to cache results and pull from the cache if the request is less than 60 seconds old (note, this should not use an existing caching library).

Output must indicate:

- whether data was pulled from cache or live from API endpoint
- how long the result will be stored in cache

Materials:

- Open AQ API documentation: <https://docs.openaq.org/using-the-api/quick-start>
- Open AQ API Swagger UI: <https://api.openaq.org/docs#/v3>
- API key: Issued at start of session
