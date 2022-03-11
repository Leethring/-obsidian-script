# Obsidian script

The Obisidian script project store operational scripts or code for Obsidian app.

[Obsidian](https://obsidian.md) is a note taking app using local markdown files with Zettelkasten method. When you accumulate thousands of notes, it's hard to adjust them all manually. So we need some scripts to help us automatically manipulate note files, such deleting, modification, adding, etc. This project is for it. 

A script can do a task. For example delLink.sh delete wiki link for a file. 

Most scripts are shell scripts, so you need command line to deal with your notes.

## Delete wiki link 

The Obsidian use `[[<note filename>|<display text>]]` wiki link to link each others. You can just use the form of `[[<note filename>]]`, but it's hard to view a note by just using this format. So we add `|` to change the display text. 

If we delete some linked notes, the original wiki links are useless. If we want to delete the links and keep the display text, we can use [delLink.sh](/delLink/delLink.sh) script to delete all links in note files. 

```  shell
$ sh deleteObsidianLink.sh <file.md>
# this script delete all wiki link in the file.md 
# Please change file.md to the file you want to adjust.
```