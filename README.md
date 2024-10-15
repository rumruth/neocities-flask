# neocities-flask
Use Flask on Neocities

## Getting started
Before you can start working on your site you need to do a few simple things to get this code running. I assume you already have Python installed. If not, navigate to [Python's website](https://www.python.org/) and follow their installation instructions.

### 1) Clone or download this repository
Click the `Code` button on the top right to see your options.

### 2) Create and activate your virtual environment
Navigate to the root of the project once downloaded and run `python -m venv .venv`

> **Note:** On some systems you might have both version 2 and 3 of Python installed. In that case your command may look something like this: `python3 -m venv .venv`

Once you have created your virtual environment, activate it. If you're on Windows, run `.venv/Scripts/activate`, and if you're on a Unix-based system run `source bin/activate` (For more specific and up to date instructions refer to [Python's documentation](https://www.python.org/about/gettingstarted/)).

> **Note:** You have to activate your virtual environment every time you want to run your development server.

### 3) Create your environment file
Copy, or rename the included `template.env` file to `.env`.

> **Note:** On some systems you need to enable the "Show hidden files" feature in your file browser. Alternatively, you could drag your working directory into your code editor of choice and have easy access to all the files within.

Once you have done that, substitute `yourusername` and `yourpassword` for your Neocities username and password respectively. Make sure that you do not share this file with anyone!

> **Note:** If you plan to upload this project to a Git repository, make sure you use the included `.gitignore` file or create your own and ignore this file!

### 4) Install your dependencies
This project comes with several dependencies, such as Flask and libsass among a few others. To install all the dependencies you need, run `pip install -r requirements.txt` in your project's root directory.

### 5) Run the development server
You're ready to code!

To start your development server, run `flask --app app --debug run` in your project's root directory. Your console will display the address for your development server which should look something like `* Running on http://127.0.0.1:5000`. If you navigate to that URL in your browser of choice you should see your website!

> **Note:** Every change you make to your site will reload your Flask application automatically with the exception of your SASS styles. To reload manually, quit the current process by pressing `Ctrl + C` in your terminal, and run the command above again.

### 6) Building your website
Before your website can be uploaded to Neocities, it needs to be built.

Once you have made your changes make sure there are no errors in your terminal. Flask will let you know if you edited something incorrectly. You can get support either on the [r/neocities Discord Server](https://discord.gg/df87cxcNnr) or in any coding community of your choice.

Once you made sure you have no errors, start the build script by running `python build.py` (Note: Remember to use the correct command for your appropriate Python version as mentioned in Section 1). Once your script runs, you should see a new directory called `build` created next to your code files in root. Inside are your static files that can now be uploaded to Neocities.

> **Note:** The file paths are optimized for hosting on a server. That means your styles may not load correctly when opening the generated `.html` files locally.

### 7) Publishing your website
Once you have built your website, you can publish it to Neocities. You have multiple options on how to do it.

If you wish to do it automatically (Recommended) all you have to do is run `python publish.py` in your code's root directory. If you have set up your `.env` file correctly, the script will run and tell you which files it uploaded to your Neocities website. The script only uploads files that are not already uploaded to Neocities and files that have otherwise been modified.

> **Note:** The script will attempt to upload any files you have placed in your `build` directory. Do not place files in that directory manually, as `Frozen-Flask` will overwrite or delete them.

If you wish to do it manually, all you have to do is navigate inside your `build` directory, and move all the files within to your Neocities dashboard (Or a mounted directory if you're a [Neocities Supporter](https://neocities.org/supporter)).

> **Note:** If you wish to test how your website looks, you can edit the `TARGET` option in your `.env` file. That option allows the script to upload your site to a subdirectory on your Neocities site. This isn't fully-supported at the moment, however, so navigation may not work as expected.

## Conclusion

This is it! Happy coding!
