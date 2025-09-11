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

