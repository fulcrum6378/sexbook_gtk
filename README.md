# Sexbook <small>(GTK version)</small>

## Structure

```
Sexbook/
├───── data/                   app data
│      ├── sexbook.db          main database
├───── resources/              declarative scripts and media
│      ├─────── css/
│      ├─────── font/
│      ├─────── lang/
│      ├─────── svg/
│      ├─────── ui/            GTK layouts
├───── sexbook/                imperative scripts (code files)
│      ├─────── base/          abstract classes
│      ├─────── ctrl/          controller (MVC)
│      ├─────── data/          model (MVC)
│      ├─────── page/          pages of the app (GTK application windows)
│      ├─────── stat/          everything related to statistics
```

## Development

1. Install [MSYS2](https://www.msys2.org/).
   Beware that it has multiple environments for Windows; we'll use the `UCRT64` environment.
   Check out [other environments](https://www.msys2.org/docs/environments/).

2. Install these packages using `pacman -S [package]` (msys64\usr\bin\pacman.exe):
    - mingw-w64-ucrt-x86_64-gtk4
    - mingw-w64-ucrt-x86_64-python-gobject
    - mingw-w64-ucrt-x86_64-python-sqlalchemy
    - mingw-w64-ucrt-x86_64-python-yaml
