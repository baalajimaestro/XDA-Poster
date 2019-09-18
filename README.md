# Hello XDA!

I was always lazy to post a detail about my ROM updates on XDA forum.
Then I figured out a sweet solution to feed my laziness. The XDA API!!!

### What do you need to do to get it working?

* Your import place to lookout is [XDA API](https://api.xda-developers.com/explorer/)
* Get your OAuth2 Token by pressing the button on the Right Corner, thats your XDA_API_KEY
* Grab your PostID from the same website, use the GET Request of `/v3/threads/threadinfo`
* For threadid well, goto your thread link and grab the integers after t
```Eg: https://forum.xda-developers.com/redmi-note-5-pro/development/9-0-resurrectionremix-official-7-0-2-t3969287
Thread ID: 3969287```
* Now that all are set, get a changelog file to post onto XDA
* Add the filename to Environment Variable FILE, now we are almost done.
* Get python3 and pip from your distro's package manager or for windows install python3
``pip install requests`
* Now, go ahead lets create the post!
`python poster.py`
* Your post must be posted on XDA if all things went right!
