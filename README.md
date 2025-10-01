# Decorating Tasks in Obsidian

This repository contains code from a small project designed to allow users to colorise and to add prefixes to tasks in Obsidian on a per-category basis, and for those effects to flow through to lists of tasks showing up in queries made via the `tasks` plugin.
The developers are Fiona Maier and T. Mark Ellison - ChatGPT was a collaborator as well.

## The Problem - List Callouts don't Survive `tasks` Processing

Using the `List Callouts` community plugin in Obsidian we can add emblems and colours to categories of list items, where the categories are defined by a single space-separated letter beginning the text part of the list item. It works for both tasks and bulleted list items.

Unfortunately, we do not see the effects of the list item passed through tasks managed by the widely-used `tasks` plugin. Here is a screen shot with the original definition of some todo-s showing the decoration applied using the `List Callout` plugin, and their undecorated form in the tasks query below.

<img width="881" height="246" alt="image" src="https://github.com/user-attachments/assets/a9580aab-970b-44ab-9eda-1d527d34808a" />


## The Solution - Supplementing the CSS Cascade

The solution is to identify the right element-class-context combination, and use this to code supplementary CSS style specifications to decorate tasks for colour and to add prefixes to the task text.

<img width="881" height="294" alt="image" src="https://github.com/user-attachments/assets/30cd0f88-c3de-46b0-bf0c-9d3d77f9bedc" />

## Conditioning Style by Hashtag

As seen in the above example, not all tags have to receive the same decoration. In fact, because the hashtags of a task are expressed in the features and values of elements, we can identify which elements relate to particular tags, and specify their styles separately.

Thus the decoration is dependent on, and reflects, the tags used in a task (so long as CSS for those tags is established) by the program `mkColouredTasks.py`.

## How to Use

1. Download the file `mkColouredTasks.py` from the `src/` directory in this repository.
2. Place it in a sister directory to the `snippets` directory which lies in your `.obsidian` directory in your vault. The python script cannot be in the `snippets` directory itself, or the snippets will not load.
3. Modify the variable `Specifications` to be a list of specifications for how hashtags affect formatting. The details are given below.
4. Run the script with the command `python3 mkColouredTasks.py`.
5. In Obsidian open the `Appearance` tab in settings, and scroll down to the bottom. Enable the `task-type-decorations` CSS file.
6. Restart is a good idea at this point.
7. Make a sample task combination on any page in Obsidian. I am assuming that you haven't changed the file yet, and that you are using the symbol `༒` to mark tasks as available for management by the `tasks` plugin. Here is an example:
~~~md
- [ ] Some action needing to be done. ༒ #meet  ⏳ 1920-09-29

```tasks
happens on 1920-09-29
```
~~~

Hopefully, the upper and the lower reflection of the same tasks should look similar. The main difference will be that the coloured text block includes the checkbox in the upper expression of the todo, but the in the `tasks` rendering of the todo, the checkbox is outdented to the left, and is not surrounded by the coloured text block.

### Specification Format

For atomic lexemes are used in expressions:

hashtag section attribute value, where
hashtag ::= "#" word,
section ::= "@" word,
attribute ::= word ":", and
value ::= word. Here word is any sequence non-space characters.
The following syntax is presumed:

hashtag+ (section+ (attribute value)+)+ where + is the Kleene plus symbol, indicating that the lexical type occurs one or more times in a row. All lexemes are assumed to be space-separated.
All subsequences of the form hashtag section attribute value are calculated. For each subsequence, the section is used to determine a CSS path parameterised by the hashtag. All the attribute-value combinations for this CSS path are then combined into a CSS specification for the path.

For example `#meet @prefix content: 👥 @thistag bg: black fg: silver` says that for the `#meet` hashtag, add a prefix with content being the emoji "👥", and also, on the tag `#meet` as opposed to other tags in the task line, make the background black, and the foreground (text) silver.

The `Specifications` string can contain multiple lines. Blank lines are ignored. Each other line can contain a separate specification.

Any CSS4 colour name can used for the `value` of a relevant item, e.g. "fg:" or "bg:". We use these abbreviations rather than the full CSS names for these attributes to make it easier to fit full specifications on a single line.
