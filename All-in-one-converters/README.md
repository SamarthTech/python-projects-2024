# ALL IN ONE CONVERTER - README

## Overview

The **ALL IN ONE CONVERTER** is a graphical user interface (GUI) application built using Python's `tkinter` module. It provides users with various conversion tools, including temperature, length, area, weight, and currency converters, as well as quick links to live market charts (Sensex, Nifty, Gold, and Silver). This application is designed for ease of use, offering a simple interface where users can select the type of conversion they need and obtain accurate results.

## Features

- **Temperature Converter**: Converts between Celsius and Fahrenheit.
- **Length Converter**: Converts between multiple units of length (meters, miles, inches, kilometers, etc.).
- **Area Converter**: Converts between multiple units of area (square meters, square kilometers, acres, etc.).
- **Weight Converter**: Converts between multiple units of weight (kilograms, grams, milligrams, etc.).
- **Currency Converter**: Converts between several international currencies (US Dollar, Euro, Indian Rupee, etc.).
- **Live Market Links**: Provides quick access to live market charts for Sensex, Nifty, Gold, and Silver prices.

## Table of Contents

1. [Installation](#installation)
2. [How to Run](#how-to-run)
3. [Features in Detail](#features-in-detail)
   - [Temperature Converter](#temperature-converter)
   - [Length Converter](#length-converter)
   - [Area Converter](#area-converter)
   - [Weight Converter](#weight-converter)
   - [Currency Converter](#currency-converter)
4. [Live Market Charts](#live-market-charts)
5. [Known Issues](#known-issues)

## Installation

1. Ensure that you have **Python 3.x** installed on your system. You can download it from the official Python website: [Python Downloads](https://www.python.org/downloads/).
2. Install the required Python packages:
   - **tkinter**: This is usually bundled with Python, but in case it is not, you can install it by running:
     ```
     sudo apt-get install python3-tk
     ```
   - **urllib**: This is a built-in module in Python 3.x, so no additional installation is needed.


## Features in Detail

### Temperature Converter

This tool allows users to convert between Celsius and Fahrenheit.

- **Input**: Enter the temperature in Celsius or Fahrenheit.
- **Output**: The converted temperature will be displayed in the other unit.
- **Button**: Press "Convert" to perform the calculation, or press "Reset" to clear all inputs.

### Length Converter

This tool converts between different units of length. Supported units include:
- Nautical Miles
- Miles
- Yards
- Feet
- Inches
- Kilometers
- Meters
- Centimeters
- Millimeters

**Usage**:
- Select input and output units from the dropdown.
- Enter the value in the input field and press the "Calculate" button to get the result.

### Area Converter

This tool converts between different units of area. Supported units include:
- Square Meter
- Square Kilometer
- Square Mile
- Square Foot
- Square Inch
- Acre
- Hectare

**Usage**:
- Enter the area value in the input field.
- Select the desired units for conversion (both input and output) from the dropdown menus.
- The result will be displayed in the output field.

### Weight Converter

This tool converts between different units of weight. Supported units include:
- Kilogram (kg)
- Hectogram (hg)
- Decagram (dg)
- Gram (g)
- Centigram (cg)
- Milligram (mg)

**Usage**:
- Enter the weight value in the input field.
- Select the input and output units from the dropdown menus.
- Press the "Calculate" button to perform the conversion.

### Currency Converter

This tool converts between various currencies. Supported currencies include:
- US Dollar (USD)
- Euro (EUR)
- Indian Rupee (INR)
- British Pound Sterling (GBP)
- Japanese Yen (JPY)
- Chinese Yuan Renminbi (CNY)
- Qatar Riyal (QAR)
- Zimbabwe Dollar (ZWD)
- UAE Dirham (AED)

**Usage**:
- Enter the amount to convert.
- Select the input and output currencies from the dropdown menus.
- Press the "Calculate" button to get the converted amount.

> **Note**: This feature relies on an external API for currency exchange rates. Ensure your internet connection is active when using this converter.

## Live Market Charts

This section provides quick access to live market charts for Sensex, Nifty, Gold, and Silver prices.

- **Sensex**: Click the "SENSEX" link to open a browser tab displaying the live Sensex chart.
- **Nifty**: Click the "NIFTY" link to open a browser tab displaying the live Nifty chart.
- **Gold**: Click the "GOLD" link to view live gold price charts.
- **Silver**: Click the "SILVER" link to view live silver price charts.

Hovering over these links changes the color of the text to indicate interaction.

## Known Issues

- **Currency Converter**: API Key is hardcoded, and the URL may change or expire in the future. Ensure to update the API URL if required.
- **Live Market Links**: The market links rely on external websites. If the URLs change or are broken, the application may not open the desired pages.

---
