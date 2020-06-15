<!--## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price":"Rs. 300 to 700"}
    - slot{"price":"Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - export -->

<!--## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price":"Lesser than Rs. 300"}
    - slot{"price":"Lesser than Rs. 300"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export -->

<!-- ## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price":"Lesser than Rs. 300"}
    - slot{"price":"Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_goodbye -->

<!--## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
    - action_city_search
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price":"Lesser than Rs. 300"}
    - slot{"price":"Lesser than Rs. 300"}
    - action_search_restaurants
* goodbye
    - utter_goodbye-->


<!--## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_city_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price":"More than 700"}
    - slot{"price":"More than 700"}
    - action_search_restaurants
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
* stop

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_city_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price":"More than 700"}
    - slot{"price":"More than 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_city_search
    - utter_ask_price
* restaurant_search{"price":"Rs. 300 to 700"}
    - slot{"price":"Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai", "price":"More than 700"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_city_search
    - slot{"price":"More than 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price":"Rs. 300 to 700"}
    - slot{"cuisine": "chinese"}
    - slot{"price":"More than 700"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city_search
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "mumbai"}
    - slot{"cuisine": "american"}
    - slot{"location": "mumbai"}
    - action_city_search
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"cuisine": "american"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* restaurant_search{"location": "Goa"}
    - slot{"location": "Goa"}
    - action_city_search
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Goa"}
    - slot{"cuisine": "thai"}
* affirm
    - utter_goodbye -->


## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - utter_ask_price
* restaurant_search{"price":"More than 700"}
    - slot{"price":"More than 700"}
    - action_search_restaurants
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - utter_ask_email
* ask_emailid
    - utter_ask_emailid
* email_request{"emailid": "darshika155@gmail.com"}
    - slot{"emailid": "darshika155@gmail.com"}
    - action_send_email
    - export

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Calcutta"}
    - slot{"location": "Calcutta"}
    - action_city_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Calcutta"}
    - slot{"cuisine": "mexican"}
    - utter_ask_email
* dont_send_mail
    - action_dont_send_mail
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_city_search
    - slot{"location": "Chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_verify_cuisine
    - utter_ask_price
* restaurant_search{"price": "than Rs. 300"}
    - slot{"price": "than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - slot{"cuisine": "Italian"}
    - utter_ask_email
* ask_emailid
    - utter_ask_emailid
* email_request{"emailid": "rashmibadri29@gmail.com"}
    - slot{"emailid": "rashmibadri29@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mysore"}
    - slot{"location": "mysore"}
    - action_city_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_verify_cuisine
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "mysore"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_email
* ask_emailid
    - utter_ask_emailid
* email_request{"emailid": "darshika155@gmail.com"}
    - slot{"emailid": "darshika155@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - action_city_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_verify_cuisine
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "coimbatore"}
    - slot{"cuisine": "north indian"}
    - utter_ask_email
* ask_emailid
    - utter_ask_emailid
* email_request{"emailid": "rashmibadri29@gmail.com"}
    - slot{"emailid": "rashmibadri29@gmail.com"}
    - action_send_email

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Srinagar"}
    - slot{"location": "Srinagar"}
    - action_city_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "Srinagar"}
    - slot{"cuisine": "american"}
    - utter_ask_email
* dont_send_mail
    - action_dont_send_mail

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "japanese", "location": "pune"}
    - slot{"cuisine": "japanese"}
    - slot{"location": "pune"}
    - action_city_search
    - action_verify_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - slot{"cuisine": "mexican"}
    - utter_ask_email
* dont_send_mail
    - action_dont_send_mail

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "hyderabad"}
    - slot{"cuisine": "italian"}
    - slot{"location": "hyderabad"}
    - action_city_search
    - action_verify_cuisine
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "italian"}
    - utter_ask_email
* ask_emailid
    - utter_ask_emailid
* email_request{"emailid": "f20140096@alumni.bits-pilani.ac.in"}
    - slot{"emailid": "f20140096@alumni.bits-pilani.ac.in"}
    - action_send_email

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_city_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"cuisine": "american"}
    - utter_ask_email
* ask_emailid
    - utter_ask_emailid
* email_request{"emailid": "badrisutha@yahoo.com"}
    - slot{"emailid": "badrisutha@yahoo.com"}
    - action_send_email

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_city_search
    - action_verify_cuisine
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - utter_ask_email
* dont_send_mail
    - action_dont_send_mail

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - action_city_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "kanpur"}
    - slot{"cuisine": "american"}
    - utter_ask_email
* ask_emailid
    - utter_ask_emailid
* email_request{"emailid": "rashmismilies@gmail.com"}
    - slot{"emailid": "rashmismilies@gmail.com"}
    - action_send_email

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "lucknow"}
    - slot{"location": "lucknow"}
    - action_city_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "lucknow"}
    - slot{"cuisine": "south indian"}
    - utter_ask_email
* dont_send_mail
    - action_dont_send_mail

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "patna"}
    - slot{"location": "patna"}
    - action_city_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_verify_cuisine
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "patna"}
    - slot{"cuisine": "north indian"}
    - utter_ask_email
* ask_emailid
    - utter_ask_emailid
* email_request{"emailid": "rashmismilies@gmail.com"}
    - slot{"emailid": "rashmismilies@gmail.com"}
    - action_send_email

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kochi"}
    - slot{"location": "kochi"}
    - action_city_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "kochi"}
    - slot{"cuisine": "south indian"}
    - utter_ask_email
* dont_send_mail
    - action_dont_send_mail

## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_greet
* restaurant_search{"location": "guwahati"}
    - slot{"location": "guwahati"}
    - action_city_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "guwahati"}
    - slot{"cuisine": "american"}
    - utter_ask_email
* dont_send_mail
    - action_dont_send_mail

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - action_city_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_verify_cuisine
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "ahmedabad"}
    - slot{"cuisine": "italian"}
    - utter_ask_email
* ask_emailid
    - utter_ask_emailid
* email_request{"emailid": "rashmibadri29@gmail.com"}
    - slot{"emailid": "rashmibadri29@gmail.com"}
    - action_send_email

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_city_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - slot{"cuisine": "mexican"}
    - utter_ask_email
* dont_send_mail
    - action_dont_send_mail
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "shimla"}
    - slot{"location": "shimla"}
    - action_city_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "shimla"}
    - slot{"cuisine": "south indian"}
    - utter_ask_email
* dont_send_mail
    - action_dont_send_mail
* affirm
    - utter_goodbye
