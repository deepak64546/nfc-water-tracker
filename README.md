# NFC Water Tracker

A water tracking app that uses **NFC tags** to make logging water quick and easy. Simply tap your phone on an NFC tag, and your water intake is recorded instantly. A home screen widget updates automatically, so you can track your progress without opening the app.

---

## The Idea

Most water tracking apps require multiple taps to log a drink. I wanted a faster solution that takes just one tap on an NFC tag placed on a desk or water bottle.

---

## How It Works

```text id="f5u2eq"
NFC Tag
    ↓
Phone taps tag
    ↓
App records water intake
    ↓
Home screen widget updates
```

1. An NFC tag is programmed to trigger the app.
2. Tapping the tag records a drink with a timestamp.
3. The app saves the data.
4. The home screen widget displays the updated daily progress.

---

## Technologies Used

| Component    | Technology                |
| ------------ | ------------------------- |
| NFC          | NTAG213 Tags              |
| Automation   | iOS Shortcuts             |
| Widget       | WidgetKit                 |
| Data Storage | App Groups / UserDefaults |

---

## Technical Highlights

* Programmed NFC tags to launch the water logging shortcut with a single tap.
* Used **App Groups** to share data between the app and the WidgetKit extension.
* Designed the system for a simple, low-friction user experience with near-instant logging.

---

## Why I Built It

I often forgot to drink enough water because logging it in an app felt inconvenient. This project removes that friction by letting me log a drink with a single tap while keeping my daily progress visible on my home screen.

---

## Setup

1. Program an NFC tag with the app's shortcut or URL.
2. Place the tag where you normally drink water.
3. Add the widget to your home screen.
4. Tap the tag to log your water intake.

---

## Project Structure

```text id="0z4jzk"
nfc-water-app/
├── app/
├── widget/
├── shortcuts/
└── README.md
```

---

## Concepts Demonstrated

* NFC programming
* iOS automation with Shortcuts
* WidgetKit development
* Shared data using App Groups
* Mobile user experience design
