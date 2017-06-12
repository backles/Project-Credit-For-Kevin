#!/usr/bin/python
#Braden Ackles
#Spring 2017
#Project credit

import sys
import mraa
import upm
import time

#Instantiate new LED Strip
APA102(72, SPIBUS, True)
#GPIO Pins
#Physical		MRAA		Name
#P1-07		7		GPIO(4)
reverseInput = mraa.Gpio(4)
reverseInput.dir(mraa.DIR_IN)
#P1-11		11		GPIO(17)
turnLeftInput = mraa.Gpio(17)
turnLeftInput.dir(mraa.DIR_IN)
#P1-12		12		GPIO(18)
turnRightInput = mraa.Gpio(18)
turnRightInput.dir(mraa.DIR_IN)
#P1-13		13		GPIO(27)
brakeInput = mraa.Gpio(27)
brakeInput.dir(mraa.DIR_IN)

def getstate():
	braking = False
	reversing = False
	turningLeft = False
	turningRight = False
	if reverseInput.read() == 1:
		reversing = True
	if turnLeftInput.read() == 1:
		turningLeft = True
	if turnRightInput.read() == 1:
		turningRight = True
	if brakeInput.read() == 1:
		braking = True
	prioritier(brakeing, reversing, turningLeft, turningRight)


def prioritier(braking, reverse, left, right):
	allOff()
	if braking == True and reverse == False and left == True and right == False:
		brakeLTurn()	#Braking and Turning Left
	elif braking == True and reverse == False and left == False and right == True:
		brakeRTurn()	#Braking and Turning Right
	elif braking == True and reverse == False and left == False and right == False:
		braking()		#braking
	elif braking == False and reverse == True and left == False and right == False:
		reverse()		#reversing
	elif braking == True and reverse == True and left == False and right == False:
		reverseBrake()	#reversing and Braking
	elif braking == False and reverse == False and left == True and right == False:
		turningLeft	#turning left
	elif braking == False and reverse == False and left == False and right == True:
		turningRight()	#turning right
	else:
		allOff()
	pushState()
	
def allOff():
	setAllLeds(0, 0, 0, 0) #Turn them all off

def braking():
	setAllLeds(0, 255, 33, 33)  #Set all lights to Red

def reverse():
	setAllLeds(0, 255, 255, 255)  #Set all lights to white

def reverseBrake():
	setAllLeds(0, 255, 33, 33)  #Set all lights to Red
	setLeds(25, 48, 31, 255, 255, 255) #Set inside to white

def leftTurn():
	setLeds(0, 24, 31, 250, 225, 0) #Set left lights to Yellow

def rightTurn():
	setLeds(48, 72, 31, 250, 225, 0) #Set right lights to Yellow

def brakeLTurn():
	setAllLeds(0, 255, 33, 33)  #Set all lights to Red
	setLeds(0, 24, 31, 250, 225, 0) #Set left lights to Yellow

def brakeRTurn():
	setAllLeds(0, 255, 33, 33)  #Set all lights to Red
	setLeds(48, 72, 31, 250, 225, 0) #Set right lights to Yellow

def main():
	allOff()
	while True:
		getstate()