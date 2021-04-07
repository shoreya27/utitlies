# utitlies
zealthy Assignments Modules

Assignment 1:Write a python class that is able to send an email from the terminal to a given email address
using smtplib library.

Module Name: send_email.py

How to run : Python send_email.py

It will ask 3 arguments from the user

>subject

>body

>recipent

Once all provided by user, email is sent to the recipent from "assignmnt.zelth06@gmail.com"

Expected O/P on CLI:

"Email sent!"

***************************************************************************

---------------------------------------------------------------------------

***************************************************************************

Assignment 2:Write a python class that is able to return the meaning of an English language word provided to it
in the terminal. (Use https://dictionaryapi.dev/)

Module Name: dictionary_search.py

How to run : Python dictionary_search.py

It will ask 1 arguments from the user

>Word ?

Once word is provided, O/P will be printed in expected format

eg:

    Word? Prince

    Prince.Noun.The son of a monarch.

PS: We are dependent on 3rd api here , so it can be possible that for some word there will be no definition on selected index
and we can get runtime error.

***************************************************************************

---------------------------------------------------------------------------

***************************************************************************

Assignment 3:Write a python class that is able to return the flight distance between two cities given their
latitude and longitude coordinates.

I am using 3rd party library: GEOPY (GreatCircle method is used to calculate the distance)


Module Name: city_distance.py

How to run : Python city_distance.py

It will ask 2 arguments from the user

>City 1:

>City 2:

Assumption: I assume that inputs are given in very same format as its given in assignment

Please enter inputs in below format given in example

eg:

    City 1: 51.5074 N, 0.1278 W

    City 2: 48.8566 N, 2.3522 E
    
    Output: City 1 and City 2 are 343.56 km apart

I have included all libraries in requirement.txt file which are being used.

I have create a virtual env on my local system to build the assignment

But you can clone the repo , and directly run individual module from terminal.

***************************************************************************

---------------------------------------------------------------------------

***************************************************************************