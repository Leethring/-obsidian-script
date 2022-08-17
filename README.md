# Obsidian script

The Obisidian script project store operational scripts or code for Obsidian app.

[Obsidian](https://obsidian.md) is a note taking app using local markdown files with Zettelkasten method. When you accumulate thousands of notes, it's hard to adjust them all manually. So we need some scripts to help us automatically manipulating note files, such as deleting, modification, adding, etc. This project is for it. 

A script can do a task. For example _delLinkLeftDisplay.sh_ delete wiki link of note files.

Most scripts are shell scripts, so you need command line to deal with your notes.

## Delete wiki link 

The Obsidian use `[[<note filename>|<display text>]]` wiki link to link each others. You can just use the form of `[[<note filename>]]`, but it's hard to view a note by just using this format. So we add `|` to change the display text. 

If you delete some linked notes, the original wiki links are useless. If you want to delete the links and keep the display text, we can use [delLinkLeftDisplay.sh](/src/delLinkLeftDisplay.sh) script to delete all links in note files. 

```  shell
$ sh delLinkLeftDisplay.sh  <file.md>
# this script delete all wiki link in the file.md 
# Please change file.md to the file you want to adjust.
```

## Others

- _addTitle.sh_ add filename to the start of the note files. 
- _capitalizeWords.sh_ capitalizes the first letter of words in the first line.
- [addSeeAlso.py](/src/addSeeAlso.py) add a See Also section to notes in current directory.