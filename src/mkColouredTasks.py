#cell 1
## ##### EDIT THESE SETTINGS TO CHANGE COLOURS, ETC. ##### ##
## v0.2
## This PYTHON code creates a CSS snippet for Obsidian which will colorise a todo, and prefix set
## text (here we use representative emojis), to make similar tasks more readily identifiable.
##
## We do not suggest that the colour choices made here are very attractive, we encourage users
##   to employ their own aesthetic. Where two tags apply to an item, our expectation is that the
##   the tag which comes later in the `Tags` list will have priority. But the tag for the other
##   group of todos will be marked with the colours of tags in those todos.

#cell 4
Specifications = """
#* @taskscheckboxes mr: 16px
#L0 #L1 #L2 #L3 #L4 #L5 #L6 #L7 #L8 @othertags bg: silver fg: black
#L0 @body bg: black fg: wheat @thistag bg: wheat fg: black @checkbox bg: slategrey @backlink fg: mistyrose
#L1 @body bg: darkred fg: wheat @thistag bg: wheat fg: darkred @checkbox bg: black @backlink fg: mistyrose
#L2 @body bg: indianred fg: white @thistag bg: white fg: indianred @checkbox bg: crimson @backlink fg: white
#L3 @body bg: orange fg: black @thistag bg: black fg: orange @checkbox bg: teal @backlink @backlink fg: olivedrab
#L4 @body bg: gold fg: black @thistag bg: black fg: gold @checkbox bg: royalblue @backlink @backlink fg: olivedrab
#L5 @body bg: darkgreen fg: wheat @thistag bg: wheat fg: darkgreen @checkbox bg: seagreen @backlink fg: mistyrose
#L6 @body bg: paleturquoise fg: black @thistag bg: black fg: paleturquoise @checkbox bg: fuchsia @backlink fg: olivedrab
#L7 @body bg: darkblue fg: yellow @thistag bg: yellow fg: darkblue @checkbox bg: yellow @backlink fg: mistyrose
#L8 @body bg: darkviolet fg: wheat @thistag bg: wheat fg: darkviolet @checkbox bg: wheat @backlink fg: mistyrose

#meet @prefix content: 👥 @thistag bg: black fg: silver
#do @prefix content: 🪚 @thistag bg: black fg: silver
#dowith @prefix content: 🤼 @thistag bg: black fg: silver
#write @prefix content: ✍️ @thistag bg: black fg: silver
#code @prefix content: 🖥️ @thistag bg: black fg: silver
#sm @prefix content: ❓ @thistag bg: black fg: silver
#event @prefix content: 🗓️ @thistag bg: black fg: silver
#project @prefix content: 📽️ @thistag bg: black fg: silver
#dream @prefix content: ⭐ @thistag bg: black fg: silver
#waitfor @prefix content: 🕰️ @thistag bg: black fg: silver
#shop @prefix content: 🛍️ @thistag bg: black fg: silver
#foodshop @prefix content: 🥔 @thistag bg: black fg: silver
#habit @prefix content: 🎠 @thistag bg: black fg: silver
#getdoc @prefix content: 📃 @thistag bg: black fg: silver
#paper @prefix content: 🧻 @thistag bg: black fg: silver
#paper @prefix content: 📘 @thistag bg: black fg: silver
#mesg @prefix content: 📧 @thistag bg: black fg: silver
#deadline @prefix content: ☠️ @thistag bg: linen fg: sienna
""".split("\n")

#cell 6
import re
from pprint import pprint

#cell 8
## Put the tags you want to colorise here, space-separated
## To use all the tags defined below, leave this as an empty string
Tags = ("meet do dowith write code sm event project dream "
        "waitfor shop foodshop habit getdoc paper").split()

#cell 13
ContentByCode = {}

contentByCode = lambda code: (
    ContentByCode[code] if code in ContentByCode else code
)

#cell 14
SpecByProp = {}
SpecByProp["content"] = lambda code: (
    "content: \""+contentByCode(code)+"\"; padding-left: 12px; margin-right: 6px; font-size: 48px;"
)
SpecByProp["bg"]   = lambda word: "background-color: "+word+";"
SpecByProp["fg"]   = lambda word: "color: "+word+";"
SpecByProp["pl"]   = lambda word: "padding-left: "+word+";"
SpecByProp["pr"]   = lambda word: "padding-right: "+word+";"
SpecByProp["ml"]   = lambda word: "margin-left: "+word+";"
SpecByProp["mr"]   = lambda word: "margin-right: "+word+";"
SpecByProp["size"] = lambda word: "font-size: "+word+";"

#cell 16
def templates2fns( *args ):
    return lambda tag: [
        arg.format(**{"tag": tag}) for arg in args
    ]

PathByPart = {}

#cell 17
PathByPart["body"] = templates2fns(
    ".HyperMD-task-line:has(span.cm-tag-{tag})",
    "li.task-list-item:has(a.tag[href=\"#{tag}\"])"
)

#cell 18
PathByPart["prefix"] = templates2fns(
    ".HyperMD-task-line:has(span.cm-tag-{tag}) span:nth-of-type(2):before",
    "li.task-list-item:has(a.tag[href=\"#{tag}\"]) > span:first-of-type:before"
)

#cell 19
PathByPart["checkbox"] = templates2fns(
    ".HyperMD-task-line:has(span.cm-tag-{tag}) input.task-list-item-checkbox",
    "li.task-list-item:has(a.tag[href=\"#{tag}\"]) input.task-list-item-checkbox"
)

#cell 20
PathByPart["taskscheckboxes"] = templates2fns(
    "li.task-list-item:has(a.tag) input.task-list-item-checkbox"
)

#cell 21
PathByPart["alltags"] = templates2fns(
    ".HyperMD-task-line span.cm-hashtag",
    "li.task-list-item:has(a.tag) span.task-description a.tag"
)

#cell 22
PathByPart["othertags"] = templates2fns(
    ".HyperMD-task-line:has(span.cm-tag-{tag}) span.cm-hashtag",
    "li.task-list-item:has(a.tag[href=\"#{tag}\"]) span.task-description a.tag"
)

#cell 23
PathByPart["thistag"] = templates2fns(
    ".HyperMD-task-line:has(span.cm-tag-{tag}) span.cm-hashtag.cm-tag-{tag}",
    "li.task-list-item:has(a.tag[href=\"#{tag}\"]) span.task-description a.tag[href=\"#{tag}\"]"
)

#cell 25
PathByPart["backlink"] = templates2fns(
    "li.task-list-item:has(a.tag[href=\"#{tag}\"]) span.task-extras span.tasks-backlink",
    "li.task-list-item:has(a.tag[href=\"#{tag}\"]) span.task-extras span.tasks-backlink a"
)

#cell 26
PathByPart["allbacklinks"] = templates2fns(
    "li.task-list-item:has(span.tasks-backlink) span.task-extras span.tasks-backlink",
    "li.task-list-item:has(span.tasks-backlink) span.task-extras span.tasks-backlink a"
)

#cell 28
def getTypeWord( specification ):
    if not specification: return []
    words = [
        s
        for s in re.split( r'\s+', specification )
        if s
    ]
    return [
        (
            ("tag",word[1:])       if word[0]  == "#" else
            ("part",word[1:])      if word[0]  == "@" else
            ("property",word[:-1]) if word[-1] == ":" else
            ("value",word)
        )
        for word in words
    ]

Specifications0_1 = map( getTypeWord, Specifications )
Specifications1 = list( filter( lambda i: not not i, Specifications0_1 ) )

#cell 29
print( Specifications1 )

#cell 30
def findSubseqInSeq(subsequence,sequence,spos=0,pos=0,):
    ## print( "findSubseqInSeq:",subsequence[0], sequence[0], pos )
    if spos >= len(subsequence):
        yield []
        return None
    if pos >= len(sequence):
        return None
    if sequence[pos] in subsequence[:spos]:
        if sequence[pos-1] != subsequence[spos-1]: return None
    if subsequence[spos] == sequence[pos]:
        for rest in findSubseqInSeq(subsequence,sequence,spos+1,pos+1):
            yield [pos] + rest
    for rest in findSubseqInSeq(subsequence,sequence,spos,pos+1):
        yield rest

#cell 31
TypeSequence = "tag/part/property/value".split("/")

#cell 32
get = lambda i: lambda a: a[i]

def collectSubsequences(sequence,fkey,fval):
    def f(l):
        keys = list( map( fkey, l ) )
        vals = list( map( fval, l ) )
        ## print( list(keys) )
        ## print( list(vals) )
        seqMatches = findSubseqInSeq( sequence, keys )
        return [
            [ vals[i] for i in seq ]
            for seq in seqMatches
        ]
    return f


## print( Specifications1 )
Specifications1_1 = map(
    collectSubsequences(TypeSequence,get(0),get(1)),
    Specifications1
)
## print( Specifications1_1 )
Specifications2 = [
    i
    for ii in Specifications1_1
    for i in ii
]
print( Specifications2 )

#cell 33
enlist = lambda x: [x]

def enlistAdjacentKV(fkey,fval):
    def f( l ):
        indices = list( map( enlist, map( enlist, range(len( l )) ) ) )
        keys = list( map( fkey, l ) )
        vals = list( map( fval, l ) )
        indexGroups = lambda x,y: (
            x[:-1]+[x[-1]+y[0]]+y[1:] if keys[x[-1][-1]] == keys[y[0][0]] else
            x+y
        )
        iGroups = indices[0]
        for i in indices[1:]: iGroups = indexGroups( iGroups, i )
        return [
            [
                keys[group[0]],
                [ vals[i] for i in group ]
            ]
            for group in iGroups
        ]
    return f

#cell 34
def groupCSS( listOfSpecs ):
    fkey = lambda i: tuple(i[:2])
    fval = lambda i: tuple(i[2:])
    return enlistAdjacentKV( fkey, fval )( listOfSpecs )

Specifications3 = groupCSS( Specifications2 )
print( Specifications3 )

#cell 35
def realise(gkeyspecs):
    body = "  " + "\n  ".join([
        SpecByProp[ propval[0] ](propval[1])
        for propval in gkeyspecs[1]
    ])
    paths = PathByPart[gkeyspecs[0][1]](gkeyspecs[0][0])
    return ("\n\n".join([
        path + " {\n" + body + "\n}"
        for path in paths
    ]))

SpecificationsCSS = "\n\n".join( map(realise, Specifications3 ) )
print( SpecificationsCSS )

#cell 37
## Putting it all together. We open the target .css file, then for each hashtag in `Tags`,
##   we work out how the values for that hashtag apply in the CSS code, and then print
##   that hashtag-specific code to the .css file.

with open( "snippets/task-type-decorations.css", "w" ) as f:
    f.write( SpecificationsCSS )

