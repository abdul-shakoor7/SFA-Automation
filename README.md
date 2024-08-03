# SFA: Sports For All Automation

## Overview

This project contains a Python script to automate certain tasks on the "SFA: Sports For All" Android application using Appium. The tasks include:

1. Changing the app language from English to Arabic.
2. Browsing between different app screens (Login, Explore by category, Edit Profile).

## Prerequisites

1. **Python** installed on your machine.
2. **Appium Server** installed and running.
3. **Appium-Python-Client** installed. Run `pip install -r requirements.txt` to install dependencies.
4. **Android SDK** installed and set up.
5. **An Android device or emulator** with the "SFA: Sports For All" app installed.
6. **Appium Desktop** or a similar tool to inspect UI elements of the app.

## Setup

1. Clone this repository or download the source code.
2. Navigate to the project directory.
3. Install the required Python packages by running:

   ```bash
   pip install -r requirements.txt
   
4. Download and install the Appium server from Appium's official website.
5. Start the Appium server:
   ```bash
   appium


6. Connect your Android device or start your emulator.
-  For a real device, ensure USB debugging is enabled.
- For an emulator, start it from the Android Studio AVD Manager.


## Usage
Running the Automation Script
To run the automation script, follow these steps:

   1. Ensure the Appium server is running.
   2. Ensure your Android device or emulator is connected. 
   3. Open a terminal or command prompt. 
   4. Navigate to the project directory. 
   5. Run the script using:

   ```bash
   python main.py
