# Introduction

> So, you landed on this GitHub page, huh? Odds are you sent me some type of document – probably something technical. And let's be frank, it probably resembled a hot mess. Hell, I might've straight up ignored it because my eyes hurt just glancing at it. 
> 
> Don’t cry into your cereal just yet. I was once like you. Diving into Google Docs, slapping together words, and smugly hitting that send button thinking I was the Shakespeare of tech docs. Spoiler alert: I wasn’t.
> 
> You made a boo-boo, champ. But guess what? Here's your chance to level up. Markdown is about to be your new best friend. Let's get you sorted.*

Already know what the hell you're doing? [[#FOR REAL?!|Skip!]]

---
## What is Markdown?

Listen up, numbnuts. Markdown is this badass lightweight markup language that lets you jazz up your pathetic plaintext docs.

Forget those prissy WYSIWYG editors like Microsoft Word, where you prance around clicking cutesy buttons and see the changes like some instant magic trick. Nah, Markdown ain't that hand-holding garbage. With Markdown, you gotta get your hands dirty. Chuck in some Markdown syntax, and _then_ you tell your text how to strut its stuff. Get with the times or get lost.

---
## Getting Started

Hey genius, I ain't your babysitter. Odds are you've got enough years on you to know your left from right. Time to pull yourself together and quit being a damn sheep. Here's a brain dead tutorial for you. Click the damn link and stop embarrassing yourself.

[Brain-Dead Markdown Tutorial](https://www.markdowntutorial.com/)

---
## Note Taking Applications

Look at you, finishing the tutorial and strutting around like you're the next Markdown Messiah. Newsflash: Nobody cares. I especially don't. Just make sure you stop sending me the trainwreck docs that landed you here in the first place.

You're pondering where to pen down your so-called "expertise"? Go on, chicken-scratch in Notepad. But, heads up: when you ship it my way, it's gonna shimmer for me – but for you? A jumbled disaster that resembles the aftermath of a dumpster fire. Too lazy to find a proper platform? Here, use this and save us all the headache: [Dillinger - Markdown Editor](https://dillinger.io/).

For the slightly-less clueless, there's [Obsidian](https://obsidian.md/). Why I use it?

- It doesn't make your text look like garbage while you write.
- Saves notes on your local storage, genius.
- Can handle HTML code, so you can get all fancy and shit.
- Has a 'Tags' system that even _you_ can use to filter docs.

---
## FOR REAL?!

Damn, you're still hanging around? Kudos to you, kid. Want a gold star? How 'bout I hit you with more unsolicited tips and tables to spruce up that boring-ass life of yours?

Well here's a little table of contents for the rest of this stuff because I'm gunna jump all over. 

- [Markdown Cheat Sheet](#Markdown%20Cheat%20Sheet)
- [HTML Cheat Sheet](#HTML%20Cheat%20Sheet)
- [Backups](#Backups)

---
### Markdown Cheat Sheet
#### Basic Shit
All Markdown applications support these elements.

|Element|Markdown Syntax|
|---|---|
|Heading |`# H1   ## H2   ### H3`|
|Bold|`**bold text**`|
|Italic|`*italicized text*`|
|Blockquote|`> blockquote`|
|Ordered List|`1. First item   2. Second item   3. Third item   `|
|Unordered List|`- First item   - Second item   - Third item   `|
|Code|`` `code` ``|
|Horizontal Rule|`---`|
|Link|`[title](https://www.example.com)`|
|Image|`![alt text](image.jpg)`|
#### Advanced Shit
Not all Markdown applications support these elements.

|Element|Markdown Syntax|
|---|---|
|Table|`\| Syntax \| Description \|   \| ----------- \| ----------- \|   \| Header \| Title \|   \| Paragraph \| Text \|`|
|Fenced Code Block|` ```   {     "firstName": "John",     "lastName": "Smith",     "age": 25   }   ``` `|
|Footnote|`Here's a sentence with a footnote. [^1]      [^1]: This is the footnote.`|
|Heading ID|`### My Great Heading {#custom-id}`|
|Definition List|`term   : definition`|
|Strikethrough|`~~The world is flat.~~`|
|Task List|`- [x] Write the press release   - [ ] Update the website   - [ ] Contact the media`|
|Emoji|`That is so funny! :joy:`|
|Highlight|`I need to highlight these ==very important words==.`|
|Subscript|`H~2~O`|
|Superscript|`X^2^`|

> **NOTE:** I stole these tables. [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

---
### HTML Cheat Sheet
#### Basic Tags
| Tag                       | Description                                                   |
|---------------------------|---------------------------------------------------------------|
| `<html> </html>`          | Creates an HTML document                                      |
| `<head> </head>`          | Sets off the title & other info that isn't displayed          |
| `<body> </body>`          | Sets off the visible portion of the document                  |
| `<title> </title>`        | Puts name of the document in the title bar                    |
#### Body Attributes
| Tag                       | Description                                                   |
|---------------------------|---------------------------------------------------------------|
| `<body bgcolor=?>`        | Sets background color                                         |
| `<body text=?>`           | Sets text color                                               |
| `<body link=?>`           | Sets color of links                                           |
| `<body vlink=?>`          | Sets color of visited links                                   |
| `<body alink=?>`          | Sets color of active links                                    |
#### Text Tags
| Tag                       | Description                                                   |
|---------------------------|---------------------------------------------------------------|
| `<pre> </pre>`            | Creates preformatted text                                     |
| `<h1> </h1>` to `<h6> </h6>`| Creates headlines                                             |
| `<b> </b>`                | Creates bold text                                            |
| `<i> </i>`                | Creates italicized text                                      |
| `<tt> </tt>`              | Creates typewriter-style text                                |
| `<code> </code>`          | Used to define source code                                   |
| `<cite> </cite>`          | Creates a citation                                           |
| `<address> </address>`    | Creates address section                                       |
| `<em> </em>`              | Emphasizes a word                                            |
| `<strong> </strong>`      | Emphasizes a word                                            |
| `<font size=?> </font>`   | Sets size of font                                            |
| `<font color=?> </font>`  | Sets font color                                              |
| `<font face=?> </font>`   | Defines the font used                                        |
#### Links
| Tag                                                       | Description                                   |
|-----------------------------------------------------------|------------------------------------------------|
| `<a href="URL">clickable text</a>`                        | Creates a hyperlink to a URL                   |
| `<a href="mailto:EMAIL_ADDRESS">clickable text</a>`        | Creates a hyperlink to an email address        |
| `<a name="NAME">`                                         | Creates a target location within a document    |
| `<a href="#NAME">clickable text</a>`                      | Creates a link to that target location         |
#### Formatting
| Tag                       | Description                                                   |
|---------------------------|---------------------------------------------------------------|
| `<p> </p>`                | Creates a new paragraph                                      |
| `<br>`                    | Inserts a line break                                         |
| `<blockquote> </blockquote>`| Puts content in a quote                                      |
| `<div> </div>`            | Used to format block content with CSS                         |
| `<span> </span>`          | Used to format inline content with CSS                        |

> **NOTE:** Stole this shit too. [From here](https://web.stanford.edu/group/csp/cs21/htmlcheatsheet.pdf). I was extra lazy too. Didn't even make the tables myself. Thanks ChatGPT. Probably should proof read them to make sure it formatted it right... Or I can go play video games. K byeee!

---
### Backups

So here's basically how I have shit running on my setup. I could break this down more but I don't want to. 

1. Download Google Drive
2. Create your Obsidian vault on the Google drive
3. Download Github Desktop
4. Create a Private Github repo and regularly push all updates made to that vault
	- This allows for there to be two copies of your notes at all times. One copy on the repo and one on the Google drive. 