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
3. Edit the list of tags at the top of the file, that give the value for the variable `Tags`.
4. Modify the dictionaries for `Parameters[TagText]` for `TagText` corresponding to each tag you defined in `Tags`. Specify for each value, the foreground and background colours you would like for the text and the checkbox. Also specify any prefix you would like to see with this class of tasks.
5. Run the script with the command `python3 mkColouredTasks.py`.
6. In Obsidian open the `Appearance` tab in settings, and scroll down to the bottom. Enable the `task-type-decorations` CSS file.
7. Restart is a good idea at this point.
8. Make a sample task combination on any page in obsidian. I am assuming that you haven't changed the file yet, and that you are using the symbol `༒` to mark tasks as available for management by the `tasks` plugin. Here is an example:
~~~md
- [ ] Some action needing to be done. ༒ #meet  ⏳ 1920-09-29

```tasks
happens on 1920-09-29
```
~~~

Hopefully, the upper and the lower reflection of the same tasks should look similar. The main difference will be that the coloured text block includes the checkbox in the upper expression of the todo, but the in the `tasks` rendering of the todo, the checkbox is outdented to the left, and is not surrounded by the coloured text block.
