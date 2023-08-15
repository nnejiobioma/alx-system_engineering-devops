Postmortem Incident report
NnejiObioma
NnejiObioma

2 min read
·
Just now


Save




Postmortem Incident Report: Downtime on April 20, 2023 EAT time-zone

Issue Summary: On April 20, 2023, our organization intranet went down that lasted for almost 8 hours. During this time all users where not able to access the intranet. Although no data was lost but services where interrupted. Users where not able to access the intranet for personal and business activities. The root cause of this was that a file was deleted in the file server.

Timeline of outage (All the times are in EAT time-zone):

5:00 PM: A user called that he is not able to access the intranet.
5:15 PM: Our team on ground began investigating the issue.
8:30 PM: Our team could not find the root cause of the problem, they had to go home.
April 21, 2023

7:00 AM: On resumption the issue was escalated to our IT department in Headquarters.
8:30 AM: It was discovered that a user mistakenly deleted a file in the life SQL server.
8:45 AM: file server restore was initiated to the previous day.
9:00AM: After restore it was confirmed that the intranet is back again and all can access it.

Photo by John Cobb on Unsplash
Root Cause: The root cause of the incident was a technician mistakenly deleted a file from the life server during clean up at the end of the day thinking that he is still working on the test file. And this resulted in inability of users to access the intrant.

Impact: The outage affected all users who were attempting to access the intranet during the downtime for various activity.

Resolution: To prevent a similar incident from occurring in the future, the following steps can be taken:

Ensure that all technicians work on the test server first, confirm that all is working well before they apply the fix to the life server.
Ensure that all services are tested before the close of work.
Services should be tested at intervals during implementation and troubleshooting. This will ensure that failure of services isnoticed on time.
