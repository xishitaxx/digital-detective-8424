# Mission 7 - How computers communicate

## 1. Task / objective
Explain core networking concepts, observe connectivity and DNS lookup safely without exposing private info, and describe how a website loads in 5-7 steps.

## 2. Work completed
Completed the networking concepts table, ran connectivity and DNS lookup checks for example.com with private details omitted, and wrote a step-by-step website loading explanation.

## 3. Commands / tools used
* **ping:** Used to check basic network reachability and round-trip response to a public host.
* **nslookup / dig:** Used to query DNS records for example.com.
* **Terminal / VS Code / Git:** Used to run checks, write notes, and commit/push Mission 7.

## 4. My understanding
A connectivity test checks whether packets can reach a remote host and return, while a DNS lookup shows how a domain name maps to network address records. DNS is essential when typing a website name because browsers and network routers route traffic using IP addresses rather than human-readable domain names.

### Task 7.1: Network concepts
| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| LAN | A network covering a small area, such as a home, lab or office | Home or lab local network |
| MAN | A network covering a city or large campus area | City-wide or large campus network |
| WAN | A network covering large geographical areas | The Internet connecting distant networks |
| DNS | Translates a domain name into an IP address | Resolving example.com to its IP address |
| Router | Connects networks and forwards data between them | Home or edge router forwarding traffic to the ISP |
| Protocol | A set of rules devices follow to communicate | HTTP/HTTPS or TCP/IP |
| Packet switching | Data is divided into packets that travel across a network | Web responses split into packets and reassembled |
| Client-server | A client requests a service and a server provides it | Browser requesting a page from a web server |

### Task 7.2: Connectivity and DNS observations
* **Connectivity test:** Confirmed reachability to `example.com` with responses returned (no local IP or Wi-Fi details included).
* **DNS lookup:** Displayed domain query details and resolved address records for `example.com`.
* **Role of DNS in browser:** Converts the typed domain name into an IP address so the client can connect to the right server.

### Task 7.3: What happens when you open a website
1. You enter a website address in your web browser (the client), which parses the address and chooses the appropriate protocol such as HTTPS.
2. If the browser or operating system does not already have a cached answer, the client queries DNS to translate the domain name into an IP address.
3. Using network protocols (such as TCP/IP and TLS), your device sends packets through your local network and router toward that IP address.
4. The destination web server receives the request and processes what resource or page is being asked for.
5. The server packages the response into packets and sends them back across the network and router to your device.
6. The client browser reassembles the response, applies the protocol rules, and renders the web page on your screen.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.
