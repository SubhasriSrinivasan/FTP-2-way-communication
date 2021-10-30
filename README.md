# FTP-2-way-communication

# What is FTP?

The term file transfer protocol (FTP) refers to a process that involves the transfer of files between computers 
over a network. The process works when one party allows another to send or receive files over the internet.

# Why do we use FTP?

* FTP is a TCP based service and there is no UDP component to it. Even though UDP is fast, 
there is data loss throughout the transmission of files hence TCP is preferred.
* Multiple transactions can be performed from the client to the server and vice versa simultaneously.
* FTP is capable of sending large files unlike UDP.

* It makes sure that the data is never lost.

# Insights of our project

Initially we had made a simple FTP two way communication program using python programming
language. \
This helps the user to transfer files of any extension and any file size between 
a client and a server located in his 'own' local machine.
	Here the word ```own``` is stressed because there was a flaw in our project. Which was,
the user could only communicate between the client and the server on his own machiine, and 
could not access others' servers which would have been more beneficial and time reducing.

So to tackle this issue, we have come across a soltion. We have used a cloud platform and hosted our server part 
of our code online. What this does is it makes our server accessible from any machine as long as the correct ip
address is noted. Moreover it reduces the time taken to upload/download any file from the server.

# Screenshots of our project
* File Upload:

![WhatsApp Image 2021-10-29 at 10 56 24 PM](https://user-images.githubusercontent.com/71788604/139527773-fae3426e-15e7-4372-805c-980a1dccd712.jpeg)

* File Upload process:

![WhatsApp Image 2021-10-29 at 10 55 31 PM](https://user-images.githubusercontent.com/71788604/139527797-cfade13c-05dc-4841-9815-e9cebb05fece.jpeg)

* File Download:

![WhatsApp Image 2021-10-29 at 10 58 17 PM](https://user-images.githubusercontent.com/71788604/139527811-aec4b310-a5ba-45ff-be8b-d4d912e96ef9.jpeg)

* File Download process:

![WhatsApp Image 2021-10-29 at 10 59 32 PM](https://user-images.githubusercontent.com/71788604/139527822-b7050ac1-1150-4559-9472-b7d9d1ff254a.jpeg)




