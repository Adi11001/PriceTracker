# PriceTracker
In this program we will be polling the price of a game on gameloot to see if the price goes below a certain threshold.
If the price is below a threshold the user will get notified using email.
Following are the steps performed
1. Get the html for the website to be scraped
2. Get the price of the product using the tag of its container
3. Check if the price is less than the threshold. If it is then send email else wait for 15 minutes and look again
