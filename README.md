# Doesnt work with Xenforo Based New UI


I was always lazy to post a detail about my ROM updates on XDA forum.
Then I figured out a sweet solution to feed my laziness. The XDA API!!!

### What do you need to do to get it working?


* There is a `sample_config.env` provided for your use.
* Rename it to `config.env` before you get started
* Grab your XDA Username, Password, fill it in `config.env`
* I will be using XDA Username, Password to fetch the XDA API Key for further use.
* **YOUR PASSWORD IS NEVER STORED ANYWHERE, YOU CAN CHECK THE SOURCE, IF YOU DONT BELIEVE ME**
* For XDA_THREAD_ID well, goto your thread link and grab the integers after t
```
Eg: https://forum.xda-developers.com/redmi-note-5-pro/development/9-0-resurrectionremix-official-7-0-2-t3969287
Thread ID: 3969287
```
* Now that all are set, get a changelog file to post onto XDA
* Add the filename to FILE, now we are almost done.
* Add these all to `config.env` or Environment Variables, both work fine
* For using `config.env`, a sample config is given, follow the same pattern
* Get python3 and pip from your distro's package manager or for windows install python3
`pip install -U requirements.txt`
* Lets get the API Key
`python get_api_key.py`
* Now, go ahead lets create the post!
`python poster.py`
* Your post must be posted on XDA if all things went right!


Thanks:

* [@yshalsager](https://github.com/yshalsager)
* [@shreejoy](https://github.com/shreejoy)

For pointing out this great API did exist! Google didn't show me anything about this API!
