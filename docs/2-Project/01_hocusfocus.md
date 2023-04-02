# 🪶 Hocus Focus

> How do you focus so well?"

I can't. At best I can study for 25 minutes. Then I need a break.
But usually 5 minutes of just looking at puppy photos is all I need to cool down my brain

> That's kinda weird, but also sounds cute

Uh, yeah I guess, but it works.

> So, do you use an app for that? Like a pomodoro timer or something?

I tried a few, but I didn't really vibe with them.
Plus, none of them would show me puppies during my break, so I made my own

> Really, how?

I wrote a Python script

> Ok, cool, but like how?

## Setup

Well, first I made a file called `focus.py`.

Then I wrote a little blurb that explains what the code is supposed to do plus some starter code:

```python title="focus.py"
--8<-- "2-Project/focus/01_focus.py"
```

> What's a module?

Oh right, it's just a bundle of all the Python code in a single file.

> Ok, cool. What about that `if name main` thing?

Yeah, it's a little weird, I'm not entirely sure[^1].
I know you don't technically have to have it,
but I read somewhere it's a good thing to have.

[^1]: `if __name__ == "__main__"` is used to tell the Python interpreter to run specific sections of code only when the file is run as the main source file. Sometimes, we want to borrow code from other modules without actually running the borrowed code in our main module, and the `if __name__ == "__main__"` line prevents that. The statement is important to have, but a good explanation would detract from the main focus of the conversation.

I think the idea is you write all your code underneath that `def main():` bit, where the word `pass` is,
then when you run the code, your computer looks for that `if name main` section and sees `main()` and is like
"Oh I should run all the code that's under the `def main():` section".

The `def` is short for `define`, because I'm defining a block of code with a name called `main`

## Timer

> Sure, I sort of get it. But where's all the timer stuff and the puppy photos?

Don't worry I'm getting there. Then I wrote:

```python title="focus.py"
--8<-- "2-Project/focus/02_focus.py"
```

> Ok, wait I think I can read that. You've defined two extra blocks of code called `start_focus` and `start_break`

Yeah, exactly.

> And in the `main` block, the script asks you if you want to start, then you say 'y' for yes, and 'n' for no.
> If you say yes, then it will start the focus timer, and then the break timer.

Yep, and if you say `n` or some other random thing, then the script will just stop.

> But what's with those numbers, the 60, 5, and 25?
> Or does that mean 25 minute focus and 5 minute break?

Yeah, it's 25 minutes times 60 seconds per minute, so you get 1500 seconds. The code only works with seconds, that's why.
Although, now that I think about it, I could probably make the code clearer. Hold on, let me update it:

```python title="focus.py"
--8<-- "2-Project/focus/03_focus.py"
```

Does that make more sense?

> Yeah, a little. But I don't get what the `time.sleep(1)` is for

Oh, so basically I'm telling the code to pause, or `sleep`, for 1 second.
You see how it says `for second in range(SEC_PER_MIN * FOCUS_MIN)` and inside the range is the number of seconds?

The code counts up one by one until the number of seconds, like 1500 in the focus timer,
and every time it counts up, it pauses (`sleep`s) for 1 second. So in total it will sleep for 1500 seconds
for the focus period.

I could have done `time.sleep(1500)` but I wanted to print a message every second.

> Why the dot? And how come you have to import time? Why don't you need to export time?

Time is another module, a python file, that someone else wrote. When I want to use blocks of code that come with the `time` module, I use `module.block`. Also need to explicitly tell the computer that I want to use the `time` module, otherwise how would it know?
And I don't need to export anything, I didn't write my module to be used by other people.

> What about the lines with the `#` symbol?

Oh those are comments to remind me what the code is doing. The computer ignores those, but they're a useful reminder.

So then I ...

> Wait, one last thing. Or maybe a few last things.

Yeah?

> How come you do `second + 1`?
> And what's with the `f` in `f"[FOCUS] {second+1} seconds has passed"`, and the curly brackets?

So, computers start counting from 0, so if I just used `second` without the `+ 1`, the computer would print 

```text
[FOCUS] 0 seconds has passed
[FOCUS] 1 seconds has passed
```

But with the `second + 1`, the computer prints:

```text
[FOCUS] 1 seconds has passed
[FOCUS] 2 seconds has passed
```

> This might be silly, but do you actually print out paper every time you run the script?

Oh lol no, by `print` I mean the script will display some text on the screen.
The script is not a fancy app; there's no buttons or user interface or anything.
It's all completely text-based. It was a fair question.

About the `f` and curly braces, the `f` (short for `format`) tells the computer that to insert insert data inside the curly braces.
Without it, the script would literally print `{second}` instead of an actual number.

```text
[FOCUS] {second} seconds has passed
[FOCUS] {second} seconds has passed
```

And of course, the curly braces surround the placeholder text.

> Ok, thanks, I think that makes sense

Yeah no problem. Coding is kind hard because there's all these extra things you have to remember to write.

## Puppies

> Alright, so I think I get the timer part, but what about the puppies?

Right, so then I added some code to repeat the focus-break sessions however many times I wanted.

```python title="focus.py"
--8<-- "2-Project/focus/04_focus.py"
```

And of course, for the puppies I included some code that opens a browser tab (the `import webbrowser` and `webbrowser.open()` bits) to [https://eyebleach.me/dogs/](https://eyebleach.me/dogs/)

After the break is over, it opens another image showing some [working animals](https://www.animalbehaviorcollege.com/wp-content/uploads/2021/11/DogCatMoney-768x564.jpg) to remind me to get back to work lol.

> Awww the puppies are so cute! But why is it called eyebleach?

Ah, normally people use the site after they accidentally see something traumatizing online.

> ...

😅 

Anyways, that's it. That's the script.

> Neat! Do you think you could help me write some code to do something similar?
> Like, I get what you did, but I wouldn't be able to write that myself

Yeah of course. And don't worry, it took a few tries to get right, coding is hard 😭.
Actually, I could just send you the file, and I'll help you modify it slightly.

What do like to do during breaks? I'm guessing you do other stuff instead of looking at puppy photos.

> Oh I do like to look a pictures, but I prefer looking at [birds with arms](https://www.reddit.com/r/birdswitharms/) when I take study breaks.

And to think you called me weird 🙄