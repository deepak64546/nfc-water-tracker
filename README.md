# NFC Water Tracker

A physical + digital water intake tracker. Tap your phone on an NFC tag → log a drink → see your daily intake update on a home screen widget. No app to open, no buttons to tap — just a physical tag on your desk or water bottle.

---

## The problem

Every water tracking app requires you to open it, find the right button, and log manually. That friction means you forget. I wanted logging to be as fast as physically possible — one tap with my phone on a tag I placed on my desk.

---

## How it works

```
NFC Tag (physical)
      ↓
Phone taps tag → triggers URL scheme / shortcut
      ↓
App logs intake to local storage
      ↓
Widget reads shared data → updates home screen in real time
```

1. **NFC tags** are programmed with a URL or shortcut trigger
2. Tapping a phone on the tag fires the shortcut automatically — no unlock required if configured
3. The app logs the drink with a timestamp
4. The **home screen widget** reads from shared storage and displays current intake vs. daily goal

---

## What makes this technically interesting

- **NFC tag programming** — encoding tags with the right payload to trigger iOS Shortcuts reliably
- **Widget data sync** — widgets run in a separate process with limited API access; getting live data into a widget requires using shared `UserDefaults` / App Groups correctly, which is a non-obvious constraint
- **No-friction UX** — the whole point is that the interaction takes under one second with zero app navigation

---

## Stack

| Component | Technology |
|-----------|-----------|
| NFC Tags | NTAG213 (standard NFC type 2) |
| Trigger | iOS Shortcuts / NFC automation |
| Widget | WidgetKit (iOS) |
| Storage | App Groups shared UserDefaults |

---

## Setup

1. Program your NFC tag using an NFC writing app (e.g. NFC Tools) with the app's URL scheme
2. Place the tag on your desk, water bottle, or wherever you drink
3. Add the widget to your home screen
4. Tap the tag — intake logs automatically

---

## Why I built this

I kept forgetting to drink water and found every tracking app too much friction. The NFC tag sits on my desk and I tap it every time I fill my water bottle. The widget shows my progress without opening anything. I've used it daily since building it.

---

## Files

```
nfc-water-app/
├── app/               # Main app logic + NFC handling
├── widget/            # WidgetKit extension
├── shortcuts/         # Exported iOS Shortcut file
└── README.md
```
