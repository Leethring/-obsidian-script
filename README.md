# Obsidian script

The Obisidian script project store operational scripts or code for Obsidian app.

Obsidian is note taking app using local markdown files with Zettelkasten method. When you accumulate thousands of notes, it's hard to adjust them all manually. So we need some scripts to help us automatically manipulate note files, such deleting, modification, adding, etc. This project is for it. 

Most scripts are shell scripts, so you need command line to deal with your notes.

## Delete wiki link in one file

The Obsidian use `[[<note filename>|<display text>]]` wiki link to link each others. You can just use the form of `[[<note filename>]]`, but it's hard to view a note. So we add `|` to change the display text. 

We may delete some linked notes, and the original wiki link is useless. If we want to delete the link and keep the display text, we can use deleteObsidianLink.sh shell script to delete all links in one note file. 

```  shell
$ sh deleteObsidianLink.sh <file.md>
# this script delete all wiki link in the file.md 
# Please change file.md to the file you want to adjust.
```