## ##### EDIT THESE SETTINGS TO CHANGE COLOURS, ETC. ##### ##
## This PYTHON code creates a CSS snippet for Obsidian which will colorise a todo, and prefix set
## text (here we use representative emojis), to make similar tasks more readily identifiable.
##
## We do not suggest that the colour choices made here are very attractive, we encourage users
##   to employ their own aesthetic. Where two tags apply to an item, our expectation is that the
##   the tag which comes later in the `Tags` list will have priority. But the tag for the other
##   group of todos will be marked with the colours of tags in those todos.

## Put the tags you want to colorise here, space-separated
Tags = "meet do dowith write code sm event project dream waitfor shop foodshop habit getdoc".split()

## I am going to define some colours, because I want to reuse some colours across particular
## tag types. It's good to do this, rather than get lost in the hexadecimal specs for colours.
##
White = "white"
Black = "black"

Red   = "red"
Green = "green"
Blue  = "blue"

Yellow = "yellow"

DarkRed     = "#830000"
StrongRed   = "#c80000"
Gold        = "#838300"
DarkViolet  = "#630063"
DarkGreen   = "#008300"
DarkBlue    = "#000083"
SkyBlue     = "#a8b8ea"
LightBlue   = "#dfdff8"
Turquoise   = "#4c8383"
Wheat       = "#f5deb3"
LightYellow = "#dedea8"
LightGreen  = "#def8df"
Brown       = "#964B00"

## ##### DEFINE THE PARAMETER SETTINGS FOR EACH HASHTAG TYPE ##### ##

Parameters = {}
#-------------------------------------- For meetings
TagText = "meet"
Parameters[TagText] = {
  "categoryNAME": TagText.upper(),       ## We define this one for a nice heading to the CSS group
  "categoryName": TagText,               ## We need this to identify just the elements around this tag
  "prefix": "👥",                       ## This is the prefix emoji you want for this hashtag
  "backgroundColour": DarkRed,           ## The background colour for the task listing
  "foregroundColour": White,             ## The foreground colour for the task listing
  "checkboxBackgroundColour": Gold,      ## The background colour for the checkbox - i.e. its body
  "checkboxForegroundColour": White      ## The colour for the outline of the checkbox
}
#-------------------------------------- For general things to do
TagText = "do"
Parameters[TagText] = {
  "categoryNAME": TagText.upper(),
  "categoryName": TagText,
  "categoryTag":  "#"+TagText,
  "prefix": "🪚",
  "backgroundColour": Gold,
  "foregroundColour": White,
  "checkboxBackgroundColour": StrongRed,
  "checkboxForegroundColour": Blue
}
#-------------------------------------- For things to do with others
TagText = "dowith"
Parameters[TagText] = {
  "categoryNAME": TagText.upper(),
  "categoryName": TagText,
  "categoryTag":  "#"+TagText,
  "prefix": "🤼",
  "backgroundColour": Gold,
  "foregroundColour": White,
  "checkboxBackgroundColour": StrongRed,
  "checkboxForegroundColour": Blue
}
#-------------------------------------- For things you need to write
TagText = "write"
Parameters[TagText] = {
  "categoryNAME": TagText.upper(),
  "categoryName": TagText,
  "categoryTag":  "#"+TagText,
  "prefix": "✍️",
  "backgroundColour": LightYellow,
  "foregroundColour": DarkRed,
  "checkboxBackgroundColour": Yellow,
  "checkboxForegroundColour": StrongRed
}
#-------------------------------------- For programs or snippets we need to write
TagText = "code"
Parameters[TagText] = {
  "categoryNAME": TagText.upper(),
  "categoryName": TagText,
  "categoryTag":  "#"+TagText,
  "prefix": "👩‍💻",
  "backgroundColour": LightYellow,
  "foregroundColour": Black,
  "checkboxBackgroundColour": Black,
  "checkboxForegroundColour": Black
}
#-------------------------------------- For things to do someday / maybe
TagText = "sm"
Parameters[TagText] = {
  "categoryNAME": TagText.upper(),
  "categoryName": TagText,
  "categoryTag":  "#"+TagText,
  "prefix": "❓",
  "backgroundColour": White,
  "foregroundColour": Black,
  "checkboxBackgroundColour": Wheat,
  "checkboxForegroundColour": White
}
#-------------------------------------- For events - things that happen at a time, e.g. a concert
TagText = "event"
Parameters[TagText] = {
  "categoryNAME": TagText.upper(),
  "categoryName": TagText,
  "categoryTag":  "#"+TagText,
  "prefix": "🗓️",
  "backgroundColour": "#838300",
  "foregroundColour": "#f3f3f3",
  "checkboxBackgroundColour": "#c80000",
  "checkboxForegroundColour": "#0000e8"
}
#-------------------------------------- A multi-step activity, usually with a goal
TagText = "project"
Parameters[TagText] = {
  "categoryNAME": TagText.upper(),
  "categoryName": TagText,
  "categoryTag":  "#"+TagText,
  "prefix": "📽️",
  "backgroundColour": LightBlue,
  "foregroundColour": Turquoise,
  "checkboxBackgroundColour": White,
  "checkboxForegroundColour": Black
}
#-------------------------------------- Because I don't express these often, I am making room
TagText = "dream"
Parameters[TagText] = {
  "categoryNAME": TagText.upper(),
  "categoryName": TagText,
  "categoryTag":  "#"+TagText,
  "prefix": "⭐",
  "backgroundColour": White,
  "foregroundColour": StrongRed,
  "checkboxBackgroundColour": Gold,
  "checkboxForegroundColour": StrongRed
}
#-------------------------------------- Events, outcomes I am waiting for from others / the world
TagText = "waitfor"
Parameters[TagText] = {
  "categoryNAME": TagText.upper(),
  "categoryName": TagText,
  "categoryTag":  "#"+TagText,
  "prefix": "🕰️",
  "backgroundColour": Wheat,
  "foregroundColour": DarkGreen,
  "checkboxBackgroundColour": LightGreen,
  "checkboxForegroundColour": DarkBlue
}
#-------------------------------------- Things I should buy at the earliest opportunity
TagText = "shop"
Parameters[TagText] = {
  "categoryNAME": TagText.upper(),
  "categoryName": TagText,
  "categoryTag":  "#"+TagText,
  "prefix": "🛍️",
  "backgroundColour": DarkViolet,
  "foregroundColour": White,
  "checkboxBackgroundColour": DarkGreen,
  "checkboxForegroundColour": White
}
#-------------------------------------- Food I should buy at the earliest opportunity
TagText = "foodshop"
Parameters[TagText] = Parameters["shop"].copy()
Parameters[TagText]["categoryNAME"] = TagText.upper()
Parameters[TagText]["categoryName"] = TagText
Parameters[TagText]["categoryTag"]  = "#"+TagText
Parameters[TagText]["prefix"]       = "🥔"
#-------------------------------------- Activities that are part of ongoing habit-construction
TagText = "habit"
Parameters[TagText] = {
  "categoryNAME": TagText.upper(),
  "categoryName": TagText,
  "categoryTag":  "#"+TagText,
  "prefix": "🎠",
  "backgroundColour": Wheat,
  "foregroundColour": Brown,
  "checkboxBackgroundColour": Brown,
  "checkboxForegroundColour": White
}
#-------------------------------------- Documents to "get" from the appropriate source
TagText = "getdoc"
Parameters[TagText] = {
  "categoryNAME": TagText.upper(),
  "categoryName": TagText,
  "categoryTag":  "#"+TagText,
  "prefix": "📃",
  "backgroundColour": DarkBlue,
  "foregroundColour": White,
  "checkboxBackgroundColour": Turquoise,
  "checkboxForegroundColour": White
}
#--------------------------------------


## ##### DO NOT EDIT BELOW THIS LINE (UNLESS YOU WANT TO) ##### ##

## This format defines the CSS specifications for one hashtag, but parameterised
##   by %s whenever there is a value to fill in.

Format = """
/* === %s === */
.HyperMD-task-line:has(span.cm-tag-%s) span:nth-of-type(2):before {
  content: "%s ";
  background-color: "#c0a0a0";
  padding-left: 6px;
}
li.task-list-item:has(a.tag[href="#%s"]) > span:first-of-type:before {
  content: "%s ";
  background-color: "#c0a0a0";
  padding-left: 6px;
  margin-left: 6px;
}
.HyperMD-task-line:has(span.cm-tag-%s) {
  background-color: %s !important;
  color: %s  !important;
  border-radius: 6px;
  padding-left: 6px;
}
li.task-list-item:has(a.tag[href="#%s"]) {
  background-color: %s !important;
  color: %s  !important;
  border-left: none !important;
  /* border-radius: 6px;
  padding: 6px; */
}
.HyperMD-task-line:has(span.cm-tag-%s) input.task-list-item-checkbox {
  background-color: %s !important;
  color: %s  !important;
  border-left: none !important;
  border-radius: 6px;
  padding: 6px;
}
li.task-list-item:has(a.tag[href="#%s"]) input.task-list-item-checkbox {
  background-color: %s !important;
  color: %s  !important;
  border-left: none !important;
  /* border-radius: 6px;
  padding: 6px; */
  /* margin-inline-start: 0 !important; */
  /* left: -45px; */
}
li.task-list-item:has(a.tag[href="#%s"]) span {
  padding-left: 6px !important;
}
a.tag[href="#%s"] {
  background-color: %s !important;
  color: %s !important;
  border-radius: 4px;
  padding: 0 4px;
}

/* Live Preview */
span.cm-hashtag.cm-tag-%s {
  background-color: %s !important;
  color: %s !important;
  border-radius: 4px;
  /* padding: 0px 6px; */
}
/*
.markdown-source-view.mod-cm6 .HyperMD-list-line[data-task*="%s"] {
  background-color: %s !important;
  color: %s  !important;
  border-left: 4px solid #8b5cf6;
  border-radius: 6px;
  padding: 6px;
}
*/
\n
"""

## The following variable defines the order in which the values from
##   the dict for a given hashtag are mapped on to "%s" codes in the
##   format specification.

TemplateArgumentFeatures = \
  (
    "categoryNAME " +
    "categoryName prefix " +
    "categoryName prefix " +
    "categoryName backgroundColour foregroundColour " +
    "categoryName backgroundColour foregroundColour " +
    "categoryName checkboxBackgroundColour checkboxForegroundColour " +
    "categoryName checkboxBackgroundColour checkboxForegroundColour " +
    "categoryName " +
    "categoryName foregroundColour backgroundColour " +
    "categoryName foregroundColour backgroundColour " +
    "categoryName backgroundColour foregroundColour"
   ).split(" ")

## Putting it all together. We open the target .css file, then for each hashtag in `Tags`,
##   we work out how the values for that hashtag apply in the CSS code, and then print
##   that hashtag-specific code to the .css file.

with open( "../snippets/task-type-decorations.css", "w" ) as f:
  for tag in Tags:
    if tag not in Parameters: continue
    templateArguments =  tuple( [ Parameters[tag][feature] for feature in TemplateArgumentFeatures ] )
    f.write( Format % templateArguments )

