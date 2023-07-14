This is a project folder for 0x11-what_happens_when_your_type_google_com_in_your_browser_and_press_enter

Basically  it involves writting an article on what happens when you type https://google.com on your browser


Search Medium
Write

NnejiObioma
Get unlimited access to all of Medium for less than $1/week.
Become a member


What Happens When You Type “https://www.google.com" in Your Browser and Press Enter
NnejiObioma
NnejiObioma

4 min read
·
Just now






Well I know you already know how to type https://www.google.com or better yet, you prefer to type google.com. I mean why type https://www.google.com when I can type google.com and still get the same results.

Have you ever wondered what happens at the backend when you type https://www.google.com and suddenly depending on the speed of your internet connection this appears:


Wala!!!! and you are happy to continue with your search.

In this article I will explain to you what happens when you type https://www.google.com, but before then I will explain the concepts and components needed to make this possible.

DNS Lookup: DNS means Domain Name System; it globally translates human readable names like www.example.com into the numeric IP addresses like 190.0.2.2 that computers use to connect to each other. It is more or less like your phone book.

TCP/IP: TCP/IP stands for Transmission Control Protocol/Internet Protocol; it is a communication protocol that is used to interconnect network devices on the internet. In a private network, it is called an intranet.

Firewall: A firewall is a network security device that monitors and filters incoming and outgoing network traffic based on an organization’s previously established security policies we could also say that it serves as a barrier that sits between a private network and a public internet network.

HTTPS/SSL: HTTPS means Hypertext Transfer Protocol Secure; it is a more secure protocol unlike HTTP. SSL means Secure Sockets Layer (SSL) certificates; this is a standard technology for securing an internet connection by encrypting data sent between a website and a browser. The SSL prevents hackers from stealing sensitive information from your system via the internet.

LOAD BALANCER: A Load balancer is a device that helps to distribute incoming traffic across a group of backend servers in the network. This prevents overloading one server.

WEB SERVER: This is both hardware and software that accepts request via HTTP or HTTPS from a user agent like the web browser and initiates communication by requesting a webpage such as https://google.com and the server response with the page requested or an error message where the page is not found or not reachable.

APPLICATION SERVER: An application server is a server that hosts applications[1] or software that delivers a business application through a communication protocol.

DATABASE: Database Servers are used to store and manage databases that are stored on the server and to provide data access for authorized users.

Now that we have known the various components required let me take you into a deep and fascinating journey on what happens when you type “https://www.google.com".

How does this work:

As you type “https://www.google.com" in your browser, the first step is a DNS (Domain Name System) request. Your browser extracts the hostname, “www.google.com," from the URL and sends a request to a DNS resolver. The resolver then seeks the IP address associated with that domain name, enabling your browser to establish a connection with the server.

Once the connection is established and the IP address is obtained, your browser initiates a TCP/IP (Transmission Control Protocol/Internet Protocol) connection with the server. This connection acts as a reliable communication channel between your browser and the server, ensuring data integrity and delivery.

But before the connection is fully established, your request may encounter a firewall and as explained above, the Firewalls act as a security measure, examining incoming and outgoing network traffic to prevent unauthorized access and potential threats. The firewall analyzes the request and determines whether it should be allowed to proceed. This is important because the security of your network needs to be secured while information is being shared.

In order to secure you access more fully HTTPS and SSL is checked on the site you are accessing to be sure it is properly secure If the URL begins with “https” (Hypertext Transfer Protocol Secure), your browser initiates an HTTPS connection. This involves an SSL (Secure Sockets Layer) handshake, where your browser and the server negotiate encryption protocols and exchange SSL certificates to establish a secure connection. This encryption ensures that your data remains confidential and protected from interception.

Once the security checks are complete, behind the scenes, popular websites like Google often employ load balancers. These devices distribute incoming network traffic across multiple servers to optimize performance and prevent overwhelming any single server. Load balancers ensure efficient utilization of resources and enhance the overall user experience.

Once your request passes through the load balancer and it reaches the appropriate server, a web server takes over. The web server processes the HTTP request, which includes retrieving the requested resource, in this case, Google’s homepage. It interacts with various components and executes scripts to generate the appropriate response.

In complex web applications, an application server often comes into play. It handles the dynamic aspects of the website, executing business logic, processing user input, and interacting with databases. In Google’s case, with its extensive suite of services, an application server may handle tasks like search queries, personalization, and more.

Behind the scenes, databases play a crucial role in storing and retrieving information. In the context of Google, databases store indexed web pages, user preferences, search histories, and more. When you enter a search query, the application server interacts with the database to fetch relevant results.

In conclusion, We have seen what happens when you type “https://www.google.com". please note that it is not limited to to just “https://www.google.com" but any other webpage you are looking for.





NnejiObioma
Written by NnejiObioma
0 Followers
Edit profile
Recommended from Medium
A screenshot of a Threads feed showing posts from Star Wars, Netflix, and Disney.
Zulie Rane
Zulie Rane

What You’re Feeling is Platform Fatigue (Or: Why I’m Not Joining Threads)
It’s October 2022. The skies are red and darkening. Somewhere in a haunted lair, Elon Musk cackles maniacally. Journalists everywhere…

·
6 min read
·
6 days ago
10.5K

260



10 Seconds That Ended My 20 Year Marriage
Unbecoming
Unbecoming

10 Seconds That Ended My 20 Year Marriage
It’s August in Northern Virginia, hot and humid. I still haven’t showered from my morning trail run. I’m wearing my stay-at-home mom…

·
4 min read
·
Feb 16, 2022
53K

829



Lists
Jonah Hill at a premiere, wearing a Cosby sweater and a pink coat, looking either pensive or sinister.

A screenshot of a Threads feed showing posts from Star Wars, Netflix, and Disney.
Staff Picks
395 stories
·
149 saves



Stories to Help You Level-Up at Work
19 stories
·
137 saves



Self-Improvement 101
20 stories
·
253 saves



Productivity 101
20 stories
·
271 saves
You’re Using ChatGPT Wrong! Here’s How to Be Ahead of 99% of ChatGPT Users
The PyCoach
The PyCoach

in

Artificial Corner

You’re Using ChatGPT Wrong! Here’s How to Be Ahead of 99% of ChatGPT Users
Master ChatGPT by learning prompt engineering.

·
7 min read
·
Mar 17
27K

487



four cartoonish images of a white woman in business wear. i like this image because it looks like 4 different social media profiles.
Zulie Rane
Zulie Rane

in

The Startup

If You Want to Be a Creator, Delete All (But Two) Social Media Platforms
In October 2022, during the whole Elon Musk debacle, I finally deleted Twitter from my phone. Around the same time, I also logged out of…

·
8 min read
·
Apr 19
33K

735



5 Ways I’m Using AI to Make Money in 2023
Kristen Walters
Kristen Walters

in

Adventures In AI

5 Ways I’m Using AI to Make Money in 2023
These doubled my income last year

·
9 min read
·
Jun 27
13.9K

227



We Are Not Ready for Threads
John Gorman
John Gorman

in

An Injustice!

We Are Not Ready for Threads
The Instagram-adjacent “Twitter killer” app is also the largest social experiment in human history. How will it end?

·
9 min read
·
6 days ago
4.96K

77



See more recommendations
Help

Status

Writers

Blog

Careers

Privacy

Terms

About

Text to speech

