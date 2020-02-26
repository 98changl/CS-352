0. Names
Liman Chang   lc931
Manpreet // add information here

1. How we implemented recurive client
For the client, we first created a soeckt connection to the rs DNS server.
While sending DNS queries to the server, if the rs DNS replies with a failure, then the client creates a socket connection to the ts DNS server.

2. Currently known issues with code
No official testing has been performed.

3. Problems we encountered

4. What did we learn?
