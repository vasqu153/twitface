#TwitFace

Thus far, we have been able to implemented a majority of the client-side interface. This includes Paul’s contributions which have been
 creating a welcome message, as well as a prompt to either create a post to share or chose a post from a pre-generated list.

 UPDATE 12/6/18:
 Up to this point, my contributions included coding the steps needed to authorize the program to interact with the user's Twitter profile. This included creating another app in Twitter, and implementing the oauth2 class to allow special privileges to the program.

 Unfortunately, we were both unable to figure out a solution to an error we continued to hit. After finding proper ways to seek authorization to a user's account, the steps to create the Twitter API object continued to fail, and would deliver an HTTP error 404 while trying to use the object to perform the PostUpdate() command. Since the api has been edited since last year, any documentation that I found to explain the issue proved to be too old. We have settled with the code we have assembled so far, as it displays an ample amount of network communication, and user interface. Unfortunately, it only trips at the final step it needs to deliver on.
