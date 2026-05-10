# 📥 My Downloads Folder is a Mess

!!! warning "✏️ Section in progress"

    This section is incomplete. Please come back soon.

## 🎯 The Problem

It was clean two weeks ago, I swear.
But yet again, my downloads folder has become a mountainous dump of assorted images, videos, documents, audio files, app installers, spreadsheets, and what might possibly be a virus or two??
My friend has a chronic hoarding problem and even they held an intervention for me 😖.

![My Downloads Folder](./img/03_downloads_folder-landfill_collab_media-unsplash.jpg)

> Fig 1. My downloads folder. Maybe the intervention was warranted ...
>  
> Photo by <a href="https://unsplash.com/@collab_media?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Collab Media</a> on <a href="https://unsplash.com/photos/a-close-up-of-smoke-GmqezLxud8g?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

It's gotten so bad that everytime I muster up the motivation to clean it, the sheer number and diversity of content in the folder makes me question why I had the gall to even try.
I just really dread having to manually prune away uneeded files and sort away the rest into the right spots elsewhere in my computer. It's a benign enough problem that I can procrastinate it without consequence, but it just gets worse with every new download. (Yeah, yeah I know I should put things in the right spot when I first download it, but I haven't yet unlocked 'discpline' and 'organization' in my skill tree 🤷‍♀️).

It would be pretty nice if I could at least group the files into bins like "Office Work", "Audio", "Video", "Images", and "Apps", etc. But even forcing myself to spend time doing that step is pretty daunting, especially when I have so many other things to do.

Of course, the biggest issue is I know that even if I get super motivated and power through it, the folder will become a landfill of files in two weeks. The last intervention was super cringe, I don't think I could handle another one 😭.

If only there was an easy, repeatable, and automatic way to organize my downloads folder ...

## 🤚 Before We Begin

As always before a new project, create a new folder on your computer, then open the folder in VS Code.

## 🐍 The Code

As a general rule, it's a good idea to develop your code in a low stakes setting.
Especially since we will be working with files, it's unfortunately easy to command your computer
to do something you didn't intend because we can mistakes when writing code and our computer
is not smart enough to not follow our mistaken instructions.

So, we should create some test files. We _could_ do this by hand, but why not automate this first?

```python title="downloadsfolder.py" linenums="1"
--8<-- "downloads_0.py"
```

After running the code, you should see a new folder named `downloads`

```python title="downloadsfolder.py" linenums="1"
--8<-- "downloads_1.py"
```

```python title="downloadsfolder.py" linenums="1"
--8<-- "downloads_2.py"
```

```python title="downloadsfolder.py" linenums="1"
--8<-- "downloads_3.py"
```

### Improving Code Organization

We have some duplication where we define a bunch of filetypes for our random file generator,
and again we have lists of filetypes in our `match` statement.

We can actually remove this duplication and simultaneously improve the flow of our code
if we think a bit more carefully about how we choose to organize our data.

A **dictionary** is a data structure which maps keys to values.
This was discussed in the previous chapter, so go back and re-read if you need a refresher.

We can use a dictionary to define the mapping of categories to filetypes.
Something like this:

```python
{
    ".pdf": "docs",
    ".docx": "docs",
    ".wav": "audio",
    # ...etc
}
```

However, even this has quite a bit of duplication and is a bit annoying to type.
Instead, we can reverse the mapping:

```python
{
    "docs": {".pdf", ".docx"},
    "audio": {".wav"}
}
```

which hopefully seems a bit more intuitive to write down anyways.
Then we dynamically generate the "filetype -> category" table using some extra code.

```python title="downloadsfolder.py" linenums="1"
--8<-- "downloads_4.py"
```

Et voila, I no longer need the intervention for my downloads folder.

## 🪞 Reflection

