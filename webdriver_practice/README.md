# webdriver_practice

#### In here there's some scripts, used to automate certain processes


#### **make sure to read the .example files and edit them accordingly before running the scripts**
# **never** put your credentials in a file you don't trust, 
## read the code first!

# spintowin
**crapppy features/TO-DO:**

- [x] get credentials from feli_creds.py
- [x] login to maffiaworld
- [x] spin the wheel of fortune (VIP)
- [x] put money in safe (needs 50cred safe, code 1111)
- [x] login
- [x] spin wheel
- [ ] bank: <del>withdraw</del>, deposit
- [ ] safe: withdraw, <del>deposit</del>
- [ ] spin family wheel
- [ ] **automatically solve captcha**
- [x] get captcha images (not in this repo, will push later)
- [ ] make selenium get captcha images in seperate tab(samesession)
- [ ] find a way to compare images and find the right (green) one
- [x] <del> test RMS on captcha images </del> it's not reliable
	- [ ] test rms again
- [ ] merge with shoot

# shoot
**crappy features/TO-DO:**


- [ ] fix ElementNotInteractableException bug
- [x] get to the shooting range
- [x] while not 'game over'
- [x] find target elements
- [x] extract target positions ('top' and 'left')
- [x] click targets when they show up
- [x] exit when 'game over' message pops up
- [x] add a timer to automate this every 2-3 minutes
- [ ] add a bullets check and stop shooting if theres no bullets left
	- [ ] maybe even make a script that
		- [ ] flies to countries on its own
		- [ ] buys bullets
- [ ] merge with spintowin
	- [ ] but before we merge, finish the script -_-


# make_bullets
**crapppy features/TO-DO:**

- [x] import owned objects
- [x] check what country you're in and whether you own that country's object
- [x] go to bullet factory and start producing
- [x] sleep for 2 hours

