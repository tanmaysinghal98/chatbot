<!--- Make sure to update this training data file with more training examples from https://forum.rasa.com/t/rasa-starter-pack/704 -->

## intent:goodbye <!--- The label of the intent -->
- Bye 			<!--- Training examples for intent 'bye'-->
- Goodbye
- See you later
- Bye bot
- Goodbye friend
- bye
- bye for now
- catch you later
- gotta go
- See you
- goodnight
- have a nice day
- i'm off
- see you later alligator
- we'll speak soon
- got to go

## intent:greet
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- Good morning
- hi again
- hi folks
- hi Mister
- hi pal!
- hi there
- greetings
- hello everybody
- hello is anybody there
- hello robot
- hola
- namaste


## intent:thanks
- Thanks
- Thank you
- Thank you so much
- Thanks bot
- Thanks for that
- cheers
- cheers bro
- ok thanks!
- perfect thank you
- thanks a bunch for everything
- thanks for the help
- thanks a lot
- amazing, thanks
- cool, thanks
- cool thank you

## intent:affirm
- yes
- yes sure
- absolutely
- for sure
- yes yes yes
- definitely


## intent:ls
- Show the directory
- List the content of this directory
- ls the directory
- Show files of this folder
- display files
- what are the contents
- List
- show files
- show contents
- please show files
- can you please show files in the current working directory
- show me files in this directory


## intent:cd
- Go to [Applications](directory)
- Go to [Public](directory)
- change directory to [Image](directory)
- enter [var](directory) folder
- change current directory to [bin](directory)
- change workspace to [etc](directory)
- goto [User](directory)
- goto [Downloads](directory)
- goto [music](directory)
- enter into [tmp](directory) folder
- goto [library](directory)
- change directory to [Downloads](directory)
- change the current directory to [Desktop](directory)
- Enter to [Music](directory)
- Goto [Movies](directory) folder
- change the workspace to [private](directory) folder
- please change the current working directory to [dev](directory)
- can you please change the directory to [Volumes](directory)
- open [goa](directory) folder
- open [rasa](directory)
- expand [tanmay](directory)
- goto folder [hi](directory)
- goto [desktop](directory)
- enter [applications](directory)
- open [ghanta](directory)
- open [bhaja](directory)
- open [wjegfl](directory)


## intent:back
- please go back
- go back
- back
- previous folder
- folder up
- directory up

## intent:pwd
- show me the current path
- where am i now
- in which folder am i
- show me the path
- display path
- what is my location
- what is the current path
- path
- current path
- show path
- show current path
- display current path
- show me my current working directory


## intent:speedtest
- speed test
- speedtest
- what is the speed of the internet
- what is ping rate
- what is download speed
- what is upload speed
- how fast is the internet
- speed of net
- is internet fast enough
- test the internet
- is internet working
- please perform the speed test
- perform speedtest
- what is internet speed
- test internet
- please run a speedtest
- run a speed test
- is the internet fast
- run a speedtest

## intent:news
- news
- get latest news
- tell latest news
- tell news
- keep me updated
- what is happening around me
- updates
- get me latest headlines
- top headlines
- headlines
- updates
- current affairs
- current news
- daily feeds
- feeds
- get me latest updates
- get me the latest news


## intent:mkdir
- create folder
- new folder
- new Directory
- create a new directory
- make folder
- make a new folder
- make Directory
- create a folder named [Downloads](new_folder)
- new folder [Tanmay](new_folder)
- make directory with name [Applications](new_folder)
- please make a new folder and keep the name of folder [Goa](new_folder)
- create a new directory with name [India](new_folder)
- create a new folder [tanmay](new_folder)
- create a folder named [lauda](new_folder)
- create a new folder [rushabh](new_folder)
- create a folder named [djhf](new_folder)
- create a folder named [laudrglaa](new_folder)
- create a folder named [ljrgefjqerauda](new_folder)
- create a folder named [oweuro](new_folder)




## intent:new_folder_mkdir
- name of new directory is [Pakistan](new_folder)
- [Pictures](new_folder)
- [Music](new_folder)
- [Downloads](new_folder)
- [Movies](new_folder)
- [madarchod](new_folder)
- keep [US](new_folder) as the name
- name should be [Australia](new_folder)
- keep it [Kenya](new_folder)
- it should be named [Priyanshi](new_folder)

## regex:new_folder
- [a-zA-Z]+

## regex:directory
- [a-zA-Z]+
