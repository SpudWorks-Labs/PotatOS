# PotatoOS; Developer Logs

**NOTE:** All time is in ***UTC***


## Developer Log

### 2026/09/28
* 16:00
    - Started to rebuild PotatOS from the ground-up now
      that there is a bit more knowledge on what I need for
      a complete Operating System that suits my needs.

* 16:26
    - Finished writing the base architectre for PotatOS.
    - I will run it by the Local AI to ensure I did not
      forget anything and make it more "well-written."

* 19:58
    - Starting to create a template window for the
      OS/Program. Asked the following models for a boiler-
      plate script to kickstart the development. The
      following models were givent the prompt "Please
      generate a simple textual terminal tui in python":

      * **Gemini:** Pro model with extended thought
      - provided by Google.
      * **ChatGPT:** With the thinking mode enabled
      - provided by OpenAI.
      * **Claude:** Using Sonnett 5.5 with extra effort
      - provided by Anthropic.

    - ChatGPT already failed by using curses instead of the
      explicit textual constraint. I told it I wanted
      textual and it returned a somewhat - albeit a little
      off - template. It created an options like page with
      a page selector on the left and a page renderer on
      the right.

    - Claude returned a simple To-Do application for the
      template using textual. Nothing else too interesting
      about this.

    - Gemini also decided to give curses a recomendation so
      I had to correct that too. Interestingly, it returned
      a game-like main menu for the system status,
      networking logs and settings as well as an exit
      button.

    - Neither of them gave desired results so I will try a
      new one.

* 20:42
    - I will now give those models a new prompt: "Please
      generate boilerplate for a textual command prompt
      interface for a basic terminal."

    - Gemini generated a nice version that I like, sleek,
      seemless. However the command prompt box is a little
      out-of-bounds. It allows for mock commands and has
      terminal coloring. A decent starting point.

    - ChatGPT has done the same, but a little better. It
      allows basic system commands and has a help menu
      instead of listing the commands for the help output.
      It also has terminal coloring and I think this one
      is much better and will be the base.

    - Claude has created a perfect version. It allows basic
      system commands and even `cd`. The only issue is the
      help command is broken. This will be the base that is
      worked off of though.

    - I will use these to "Frankenstein" my own terminal
      app after I get a template screen for an empty window
      waiting to be filled.

---

### 2026/09/30

* 19:55
    - Started to write the custom base window.

* 20:36
    - Finished a quick template, now decided to begin the 
      program for MaSH
      