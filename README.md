# Vizzini.py

```
VIZZINI: Let me put it this way: have you ever heard of Plato, Aristotle, Socrates?

MAN IN BLACK: Yes.

VIZZINI: Morons. 
```

A starter bot for [Battle of Bits](http://battleofbits.com), written in Python
3 and Flask.

[![Build Status](https://travis-ci.org/battleofbits/vizzini.py.png?branch=master)](https://travis-ci.org/battleofbits/vizzini.py)

## Prerequistes

- A [Heroku][heroku_signup] account
- A [Battle of Bits][bits_signup] account
- A mind like a steel trap

## Heroku setup

This guide assumes you've installed the [Heroku Toolbet][belt]. Create a new
heroku application from inside this directory.

```bash
git clone https://github.com/battleofbits/vizzini.py.git
cd vizzini.py
heroku create
```

Deply the application to Heroku, making sure to scale up the web process to one
dyno.

```bash
git push heroku master
heroku ps:scale web=1
heroku open
```

You now have a working bot! It will play endless games of Four Up. However,
it's AI is very basic. Don't expect to win any games.

## Battle of Bits Setup

