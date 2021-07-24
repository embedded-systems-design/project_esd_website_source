---
---

## Update google drive links in assignments

Search  in in regex mode in  \*.html, exclude "wiki_content"

```html
<body>[\s\S]*<a href="https://docs[\s\S]*</body>
```

<!--
old search looks for all bodies.
```html
<body>[\s\S]*</body>
```
-->


## Replace with:

### 304

```html
<body><p><a href="https://drive.google.com/drive/folders/1TVr7REF6BWR8ws08xPQv3DqH4GkyDeV9?usp=sharing">Course Documents</a></p></body>
```

### 314
```html
<body><p><a href="https://drive.google.com/drive/folders/1TekJ1H85sDuqsEHQWjnegGeaC1NPiFVE?usp=sharing">Course Documents</a></p></body>
```

scan git commit for text that is removed and add to assignment text


## Search for mis-formatted bodies with broader search

Search  in in regex mode in  \*.html, exclude "wiki_content"

```html
<body>[\s\S]*</body>
```

## Replace manually with:

catme, attendance, and cumulative catchall assignments don't need links.

```html
<body><p><a href="https://drive.google.com/drive/folders/1TVr7REF6BWR8ws08xPQv3DqH4GkyDeV9?usp=sharing">Course Documents</a></p></body>
```

## Check .ismcc file for

* files that are not needed
* web resources that are not pertinent
* ESD F18
* ESD S19

## Test import

* convert start date
* import
    * settings
    * syllabus
    * assignments
    * quizzes
    * question banks
    * rubrics
    * events
* for 314, convert Jan 7 to Aug 26
* for 304 convert Aug 20 to Aug 26

## Update Settings

* Calendar Start and stop
* Make course unavailalbe outside of start and stop
* participate only within window
* Navigation:
    * Home
    * Announcements
    * Assignments
    * Quizzes
    * Pages
    * People
    * Grades
    * Piazza

## Align Assignment Groups

## Create Teams

## Move old announcements to new info somewhere.

## Move old pages to new info somewhere.


## Clean up rubrics and learning outcomes

## Find external links

## Remove dates from quizzes

## Search for variables
\{\%[\s]*[\S]*[\s]*\%\}

{%POINTS%}
{%DATE%}
{%SEMESTER%} (Fall/Spring)
{%YEAR%}
{%COURSENUM%}
{%SECTIONNUM%}
{%SEMYEAR%} (F19/S20)
{%TOPIC%}
{%COURSENAME%} (Embedded Systems Design Project I Embedded Systems Design Project II)

## fix bullets

search for ```-   ```
replace with ```* ```

## fix empty headers

\#[\s]*\n

* done

## Remove \&nbsp

* done

## Remove >

```
[\n\r][\s]*>
```

* done

## Look through old resources and relink

### find and replace docs.google.com

* done for 3x4, still need to do for blog

### find and replace drive.google.com

* done for 3x4, still need to do for blog

## Fix Points in syllabus

## Fix Dates in syllabus

## After converting to docx, look for numbering problems and missing <br>

## Blog: search for "\n\\\r", replace with '\n\n'