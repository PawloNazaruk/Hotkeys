# Peon

## About program
CRUD GUI for managing text replacements, which can be used in windows os (notepad, browsers, etc.)
It also allows for creating templates for matched text replacements.

For example mapping 'tm' with '™' will create matching,
which will be replacing every written 'tm' followed by a space with a ™ symbol.

## Requirements
You need Python with installed Keyboard to use this app.

## How to use
### Tags
Set Tags radio button, then press New and fill both "name" and "Replace to:" fields.
The "Name" value is the text that needs to be written from keyboard followed by a 
space to induce text replacement.
"Replace to:" value is responsible for replacing written name with own content text.
Press Submit.

E.g.

Name: @Lorem

Replace to: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam pellentesque, lectus ut lobortis...

After writing @Lorem followed by a space the @Lorem will be replaced with it's own content:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam pellentesque, lectus ut lobortis...

It is worth to use special character in the name to invoke the replacement only when we want, 
otherwise using only Lorem as a name will invoke replacement each time we write it.


### Vars
Set Vars radio button, then press New and fill both "name" and "Replace to:" fields.
The "Name" value of the Var checks every value from Tag "Replace to:" content text. 
When text is found then replacement will happen.
The "Replace to:" value is resposible for replacing found "Name" value with it's own content text.

E.g.

Name: Lorem ipsum

Replace to: Hello World ipsum

Created Var like this will search every Tag "Replace to" content, if matching will be found then
Tag content will be override with Var "Replace to" value.
Invoking @Lorem will now be replaced to:
Hello World ipsum dolor sit amet, consectetur adipiscing elit. Nam pellentesque, lectus ut lobortis...
Press Submit.

### Feedback
I would appreciate every feedback on pawlonazaruk@gmail.com
Thanks!