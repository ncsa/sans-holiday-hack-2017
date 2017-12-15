Wunorse Openslae
====================
Hint 1: Many people don't know this, but most of us elves have multiple jobs here in the North Pole. In addition to working in Santa's workshop, I also work as a help desk support associate for the North Pole Elf Database site. I answer password reset requests, mostly from other elves.
Hint 2: One time, I got a weird email with a JavaScript alert and my account got hacked. Fortunately, Alabaster was able to add some filtering on the system to prevent that from happening again. I sure hope he tested his changes against the common evasion techniques discussed on the [XSS filter evasion cheat sheet](https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet).
Hint 3: It's never a good idea to come up with your own encryption scheme with cookies. Alabaster told me he uses JWT tokens because they are super secure as long as you use a long and complex key. Otherwise, they could be cracked and recreated using any old framework like [pyjwt](https://github.com/jpadilla/pyjwt) to forge a key.
Hint 4: The interface we use lets us query our directory database with all the employee information. Per Santa's request, Alabaster restricted the search results to just the elves and reindeer. Hopefully, he secured that too. I found an article recently talking about [injection against similar databases](https://pen-testing.sans.org/blog/2017/11/27/understanding-and-exploiting-web-based-ldap).

Pepper Minstix
====================
Hint 1: I'm so excited for the new email system that Alabaster Snowball set up for us. He spent a lot of time working on it. Should make it very easy for us to share cookie recipes. I just hope that he cleared up all his dev files. I know he was working on keeping the dev files from search engine indexers.
Hint 2: The new email system's authentication should be impenetrable. Alabaster was telling me that he came up with his own encryption scheme using AES256, so you know it's secure.
Hint 3: AES256? Honestly, I don't know much about it, but Alabaster explained the basic idea and it sounded easy. During decryption, the first 16 bytes are removed and used as the initialization vector or "IV." Then the IV + the secret key are used with AES256 to decrypt the remaining bytes of the encrypted string.
Hint 4: Hmmm. That's a good question, I'm not sure what would happen if the encrypted string was only 16 bytes long.
Hint 5: Every year when Santa gets back from delivering presents to the good girls and boys, he tells us stories about all the cookies he receives. I love everything about cookies! Cooking them, eating them, editing them, decorating them, you name it!

Minty Candycane
====================
Hint 1: I have a very important job at the North Pole: GDPR compliance officer. Mostly I handle data privacy requests relating to Santa's naughty and nice list. I maintain the documents for compliance on the North Pole file store server.
Hint 2: The North Pole Police Department works closely with Santa on the naughty and nice list infractions. Mild naughty events are "1 coal" infractions, but can reach as high as "5 coal" level.
Hint 3: I'm still a little shaken up from when I had to call them in the other day. Two elves started fighting, pulling hair, and throwing rocks. There was even a super atomic wedgie involved! Later we were told that they were Munchkin Moles, though I'm still not sure I can believe that.
Hint 4: Unrelated, but: have you had the pleasure of working with JSON before? It's an easy way to programmatically send data back and forth over a network. There are simple JSON import/export features for almost every programming language!
Hint 5: One of the conveniences of working with JSON is that you can edit the data files easily with any text editor. There are lots of online services to convert JSON to other formats too, such as CSV data. Sometimes the JSON files need a little coaxing to get the data in the right format for conversion, though.

Sparkle Redberry
====================
Hint 1: We're excited to debut the new Letters to Santa site this year. Alabaster worked hard on that project for over a year. I got to work with the development version of the site early on in the project lifecycle.
Hint 2: Near the end of the development we had to rush a few things to get the new site moved to production. Some development content on the letter page should probably have been removed, but ended up marked as hidden to avoid added change control paperwork.
Hint 3: Alabaster's primary backend experience is with Apache Struts. I love Apache and have a local instance set up on my home computer with a web shell. Web shells are great as a backdoor for me to access my system remotely.  I just choose a really long complex file name so that no one else knows how to access it.
Hint 4: A simple web shell is to create a PHP file in the web root with `<?php echo "<pre>" . shell_exec($_GET['e']) . "</pre>"; ?>`. Then, I visit the URL with my commands. For example, *http://server/complexFileName.php?e=ls*.
Hint 5: There are lots of different web shell tools available. [You can get a simple PHP web shell that is easy to use here](https://gist.github.com/joswr1ght/22f40787de19d80d110b37fb79ac3985).
Hint 6: That business with Equal-Facts Inc was really unfortunate. I understand there are a lot of different exploits available for those vulnerable systems. Fortunately, Alabaster said he tested for CVE-2017-5638 and it was NOT vulnerable. Hope he checked the others too.
Hint 7: Apache Struts uses XML. I always had problems making proper XML formatting because of special characters. I either had to encode my data or escape the characters properly so the XML wouldn't break. I actually just checked and there are lots of different exploits out there for vulnerable systems. [Here is a useful article](https://pen-testing.sans.org/blog/2017/12/05/why-you-need-the-skills-to-tinker-with-publicly-released-exploit-code).
Hint 8: Pro developer tip: Sometimes developers hard code credentials into their development files. Never do this, or at least make sure you take them out before publishing them or putting them into production. You also should avoid reusing credentials for different services, even on the same system.

Holly Evergreen
====================
Hint 1: Nmap has default host discovery checks that may not discover all hosts.  To customize which ports Nmap looks for during host discovery, use `-PS` with a port number, such as `-PS123` to check TCP port 123 to determine if a host is up.
Hint 2: Alabaster likes to keep life simple. He chooses a strong password, and sticks with it.
Hint 3: The Letters to Santa server is limited in what commands are available. Fortunately, SSH has enough flexibility to make access through the Letters server a fruitcake-walk.
Hint 4: Have you used port forwarding with SSH before? It's pretty amazing! [Here is a quick guide](https://help.ubuntu.com/community/SSH/OpenSSH/PortForwarding).
Hint 5: Windows users can use SSH port forwarding too, using PuTTY! [Here is a quick guide for Windows users](https://blog.devolutions.net/2017/04/how-to-configure-an-ssh-tunnel-on-putty.html).
Hint 6: Sometimes it's better to use a Linux system as the SSH port forwarder, and interact with a Linux system from a Windows box. For example, running `ssh -L :445:SMBSERVERIP:445 username@sshserver` will allow you to access your Linux server's IP, which will forward directly to the SMB server over SSH.
Hint 7: Linux systems can also interact with a Windows server using the smbclient utility: `smbclient -L smbserverorforwarder -U username`.

Sugarplum Mary
====================
Hint 1: The Elf As A Service (EAAS) site is a new service we're experimenting with in the North Pole. Previously, if you needed a special engineer for toy production, you would have to write a memo and distribute it to several people for approval. All of that process is automated now, allowing production teams to request assistance through the EAAS site.
Hint 2: The EAAS site uses XML data to manage requests from other teams. There is a sample request layout available that you can download. Teams just customize the XML and submit!
Hint 3: I think some of the elves got a little lazy toward the go-live date for EAAS. The sample XML data doesn't even include a DTD reference.
Hint 4: XML processing can be complex. I saw an interesting article recently on the [dangers of external XML entities](https://pen-testing.sans.org/blog/2017/12/08/entity-inception-exploiting-iis-net-with-xxe-vulnerabilities).

Shinny Upatree
====================
Hint 1: I'm still a little angry with Alabaster for reprimanding me for a security violation. He still checks his email from the EMI system!
Hint 2: He tells us not to install unnecessary software on systems, but he's running IIS with ASPX services on the EMI server, and Microsoft Office!
Hint 3: Personally, I don't use Microsoft Word. I'll take vim and LaTeX any day. Word does have its advantages though, including some of the Dynamic Data Exchange features for transferring data between applications and obtaining data from external data sources, including executables.

