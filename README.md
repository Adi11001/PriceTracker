# PriceTracker
In this program we will be polling the price of a game on gameloot to see if the price goes below a certain threshold.
If the price is below a threshold the user will get notified using email.
Following are the steps performed
1. Get the html for the website to be scraped
2. Get the price of the product using the tag of its container
3. Check if the price is less than the threshold. If it is then send email else wait for 15 minutes and look again


Email Related Fields:
1. sender_email : Email id from where you want the notification to be sent
2. sender_app_password = App password of the sender emailid. Remember app password is different from password. Google how to get one for your mail id
3. receiver_email = Email id where you want to receive the notification
