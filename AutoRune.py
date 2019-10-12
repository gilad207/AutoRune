import time
import pyautogui
from pyautogui import _window_win
import RunesFetcher

windowTitle = "League of Legends"

RunesTypes = ['Percision', 'Domination']
primaryRunesPositions = {}
secondaryRunesPositions = {}
FirstBonusRunesPositions = {}
SecondBonusRunesPositions = {}
ThirdBonusRunesPositions = {}
buttonsPositions = {}
primaryRunesTypesPositions = {}

def getWindowPosition():
	window = _window_win.getWindow(windowTitle)
	window.restore()
	window.set_foreground()
	rect = window.get_position();
	return [rect[0], rect[1]]
	
windowPosition = getWindowPosition()

def populatePrimaryPositions():
	primaryRunesPositions['Press the Attack'] = \
	primaryRunesPositions['Electrocute'] = \
	primaryRunesPositions['Summon Aery'] = \
	primaryRunesPositions['Grasp of the Undying'] = \
	primaryRunesPositions['Glacial Augment'] = [250,330]
	
	primaryRunesPositions['Lethal Tempo'] = \
	primaryRunesPositions['Predator'] = [290,330]
	
	primaryRunesPositions['Arcane Comet'] = \
	primaryRunesPositions['Aftershock'] = \
	primaryRunesPositions['Kleptomancy'] = [320,330]
	
	primaryRunesPositions['Fleet Footwork'] = \
	primaryRunesPositions['Dark Harvest'] = [340,330]
	
	primaryRunesPositions['Conqueror'] = \
	primaryRunesPositions['Hail of Blades'] = \
	primaryRunesPositions['Phase Rush'] = \
	primaryRunesPositions['Guardian'] = \
	primaryRunesPositions['Unsealed Spellbook'] = [390,330]
	
	primaryRunesPositions['Overheal'] = \
	primaryRunesPositions['Cheap Shot'] = \
	primaryRunesPositions['Nullifying Orb'] = \
	primaryRunesPositions['Demolish'] = \
	primaryRunesPositions['Hextech Flashtraption'] = [250,430]
	
	primaryRunesPositions['Triumph'] = \
	primaryRunesPositions['Taste of Blood'] = \
	primaryRunesPositions['Manaflow Band'] = \
	primaryRunesPositions['Font of Life'] = \
	primaryRunesPositions['Magical Footwear'] = [310,430]
	
	primaryRunesPositions['Presence of Mind'] = \
	primaryRunesPositions['Sudden Impact'] = \
	primaryRunesPositions['Nimbus Cloak'] = \
	primaryRunesPositions['Shield Bash'] = \
	primaryRunesPositions['Perfect Timing'] = [370,430]
	
	primaryRunesPositions['Legend: Alacrity'] =  \
	primaryRunesPositions['Zombie Ward'] =  \
	primaryRunesPositions['Transcendence'] =  \
	primaryRunesPositions['Conditioning'] =  \
	primaryRunesPositions["Future's Marke"] =  [250,520]
	
	primaryRunesPositions['Legend: Tenacity'] =  \
	primaryRunesPositions['Ghost Poro'] =  \
	primaryRunesPositions['Celerity'] =  \
	primaryRunesPositions['Second Wind'] =  \
	primaryRunesPositions["Minion Dematerializer"] =  [310,520]
	
	primaryRunesPositions['Legend: Bloodline'] =  \
	primaryRunesPositions['Eyeball Collection'] =  \
	primaryRunesPositions['Absolute Focus'] =  \
	primaryRunesPositions['Bone Plating'] =  \
	primaryRunesPositions["Biscuit Delivery"] =  [370,520]
	
	primaryRunesPositions['Coup de Grace'] = \
	primaryRunesPositions['Ravenous Hunter'] = \
	primaryRunesPositions['Scorch'] = \
	primaryRunesPositions['Overgrowth'] = \
	primaryRunesPositions['Cosmic Insight'] = [250,600] 
	
	primaryRunesPositions['Cut Down'] = \
	primaryRunesPositions['Waterwalking'] = \
	primaryRunesPositions['Revitalize'] = \
	primaryRunesPositions['Approach Velocity'] = [310,600]
	
	primaryRunesPositions['Last Stand'] = \
	primaryRunesPositions['Gathering Storm'] = \
	primaryRunesPositions['Unflinching'] = \
	primaryRunesPositions['Time Warp Tonic'] = [370,600]
	
	primaryRunesPositions['Ingenious Hunter'] = [300,600]
	primaryRunesPositions['Relentless Hunter'] = [350,600]
	primaryRunesPositions['Ultimate Hunter'] = [400,600]

def populateSecondaryPositions():
	secondaryRunesPositions['Overheal'] = \
	secondaryRunesPositions['Cheap Shot'] = \
	secondaryRunesPositions['Nullifying Orb'] = \
	secondaryRunesPositions['Demolish'] = \
	secondaryRunesPositions['Hextech Flashtraption'] = [580,300]
	
	secondaryRunesPositions['Triumph'] = \
	secondaryRunesPositions['Taste of Blood'] = \
	secondaryRunesPositions['Manaflow Band'] = \
	secondaryRunesPositions['Font of Life'] = \
	secondaryRunesPositions['Magical Footwear'] = [650, 300]
	
	secondaryRunesPositions['Presence of Mind'] = \
	secondaryRunesPositions['Sudden Impact'] = \
	secondaryRunesPositions['Nimbus Cloak'] = \
	secondaryRunesPositions['Shield Bash'] = \
	secondaryRunesPositions['Perfect Timing'] = [720,300]
	
	secondaryRunesPositions['Legend: Alacrity'] = \
	secondaryRunesPositions['Zombie Ward'] = \
	secondaryRunesPositions['Transcendence'] = \
	secondaryRunesPositions['Conditioning'] = \
	secondaryRunesPositions["Future's Market"] = [580,380]

	secondaryRunesPositions['Legend: Tenacity'] = \
	secondaryRunesPositions['Ghost Poro'] = \
	secondaryRunesPositions['Celerity'] = \
	secondaryRunesPositions['Second Wind'] = \
	secondaryRunesPositions['Minion Dematerializer'] = [650, 380]
	
	secondaryRunesPositions['Legend: Bloodline'] = \
	secondaryRunesPositions['Eyeball Collection'] = \
	secondaryRunesPositions['Absolute Focus'] = \
	secondaryRunesPositions['Bone Plating'] = \
	secondaryRunesPositions['Biscuit Delivery'] = [720, 380]
	
	secondaryRunesPositions['Coup de Grace'] = \
	secondaryRunesPositions['Ravenous Hunter'] = \
	secondaryRunesPositions['Scorch'] = \
	secondaryRunesPositions['Overgrowth'] = \
	secondaryRunesPositions['Cosmic Insight'] = [580, 460]
	
	secondaryRunesPositions['Cut Down'] = \
	secondaryRunesPositions['Waterwalking'] = \
	secondaryRunesPositions['Revitalize'] = \
	secondaryRunesPositions['Approach Velocity'] = [650, 460]
	
	secondaryRunesPositions['Ingenious Hunter'] = [630, 460]
	secondaryRunesPositions['Relentless Hunter'] = [680, 460]
	
	secondaryRunesPositions['Last Stand'] = \
	secondaryRunesPositions['Ultimate Hunter'] = \
	secondaryRunesPositions['Gathering Storm'] = \
	secondaryRunesPositions['Unflinching'] = \
	secondaryRunesPositions['Time Warp Tonic'] = [720, 460]
	
def populateBonusRunesPositions():
	FirstBonusRunesPositions['diamond'] = [580,520]
	FirstBonusRunesPositions['axe'] = [645,520]
	FirstBonusRunesPositions['time'] = [710,520]

	SecondBonusRunesPositions['diamond'] = [580,560]
	SecondBonusRunesPositions['shield'] = [645,560]
	SecondBonusRunesPositions['circle'] = [710,560]	
	
	ThirdBonusRunesPositions['heart'] = [580,600]
	ThirdBonusRunesPositions['shield'] = [645,600]
	ThirdBonusRunesPositions['circle'] = [710,600]
	
def populateButtonsPositions():	
	buttonsPositions['edit'] = [440,680]
	buttonsPositions['plus'] = [570,120]
	buttonsPositions['runesList'] = [300,130]
	buttonsPositions['oldPage'] = [300,210]
	buttonsPositions['delete'] = [610,120]
	buttonsPositions['yes'] = [600, 380]
	buttonsPositions['save'] = [510,120]
	buttonsPositions['x'] = [1160,70]
	buttonsPositions['edit name'] = [160,120]
	buttonsPositions['name area'] = [210,120]
	
def populateprimaryRunesTypesPositions():	
	primaryRunesTypesPositions['Precision'] = [230,220]
	primaryRunesTypesPositions['Domination'] = [430,220]
	primaryRunesTypesPositions['Sorcery'] = [630,220]
	primaryRunesTypesPositions['Resolve'] = [830,220]
	primaryRunesTypesPositions['Inspiration'] = [1030,220]

def getSecondaryRunesTypePosition(primaryRuneType, secondaryRuneType):
	runesTypes = ['Precision', 'Domination', 'Sorcery',  'Resolve', 'Inspiration']
	secondaryRunesTypesPositions = [[570,210],[620,210],[670,210],[720,210]]
	runesTypes.remove(primaryRuneType)
	secondaryRuneTypeIndex = runesTypes.index(secondaryRuneType)
	return secondaryRunesTypesPositions[secondaryRuneTypeIndex]
	
def click(location, wait = 0.4, clicks = 1):
		pyautogui.click(location[0] + windowPosition[0], location[1] + windowPosition[1], clicks = clicks)
		time.sleep(wait)

def type(text, wait = 0.7):
		pyautogui.typewrite(text) 
		time.sleep(wait)

primaryTitle, secondaryTitle = RunesFetcher.findRunesTitles()
primary = RunesFetcher.findPrimaryRunes()
secondary = RunesFetcher.findSecondaryRunes()
firstBonus, secondBonus, thirdBonus = RunesFetcher.findBonusRunes()

populatePrimaryPositions()
populateButtonsPositions()
populateprimaryRunesTypesPositions()
populateSecondaryPositions()
populateBonusRunesPositions()

click(buttonsPositions['edit'], wait = 0.6)
click(buttonsPositions['runesList'])
click(buttonsPositions['oldPage'])
click(buttonsPositions['delete'])
click(buttonsPositions['yes'])
click(buttonsPositions['plus'], wait = 1)

click(primaryRunesTypesPositions[primaryTitle], wait = 1)

for rune in primary:
	click(primaryRunesPositions[rune])

click(getSecondaryRunesTypePosition(primaryTitle, secondaryTitle))

for rune in secondary:
	click(secondaryRunesPositions[rune])

click(FirstBonusRunesPositions[firstBonus])
click(SecondBonusRunesPositions[secondBonus])
click(ThirdBonusRunesPositions[thirdBonus])

click(buttonsPositions['edit name'])
click(buttonsPositions['name area'], clicks = 3)
type(RunesFetcher.champion) 
click(buttonsPositions['save'], clicks = 2)
click(buttonsPositions['x'])