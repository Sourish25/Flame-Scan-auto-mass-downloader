# Manhwa Downloader

## Overview

Download and enjoy your favorite manhwa offline with the Manhwa Downloader! This Python script allows you to save entire manhwa websites, making it easy to read your preferred stories without needing an internet connection.

## How to Use

1. **Install Required Packages:**
   - Make sure you have Python installed on your computer.
   - Open your command prompt and run the following commands:
     ```
     pip install requests
     pip install beautifulsoup4
     ```

2. **Download the Script:**
   - Click on the green "Code" button on this GitHub page.
   - Choose "Download ZIP" and extract the contents to your computer.

3. **Customize the Script:**
   - Open the `download_websites.py` file in a text editor.
   - Replace the placeholder values for `base_url`, `start_range`, and `end_range` with your manhwa website details.

4. **Run the Script:**
   - Open your command prompt and navigate to the folder where the script is located using the `cd` command.
   - Run the script by entering:
     ```
     python download_websites.py
     ```
     (or `python3` if you're using Python 3)

5. **Find Your Downloads:**
   - Your downloaded manhwa will be organized in separate folders within the `downloaded_websites` directory.

## Example Setup

Suppose you want to download manhwa chapters from "https://examplemanhwa.com/chapter-" starting from chapter 10 to chapter 20.

- Open `download_websites.py` and set:
  ```python
  base_url = "https://examplemanhwa.com/chapter-"
  start_range = 10
  end_range = 20
  ```

- Run the script as explained in step 4.

Now you have your favorite manhwa chapters downloaded and ready to read offline!
