# CuriosityAssessment

Game to measure curiosity in children of the age group 3-8. The rep currently contains scenario 1 of the game, scenario 2&3 are wip. 



##Dependencies
- Python3
- Pygame
- Pyaudio
- Google cloud speech api

## Android
-  RAPT
-  In the process of converting it to Kivy


## Background
While there is a large corpus of literature talking about the theory of curiosity, various models and types of curiosity, few talk about measuring curiosity. The most common practice currently is to use self reported questionnaires of epistemic curiosity. Amongst digital tools, a digital adaptation of the Fish Tank Task is used to measure curiosity. The challenges with the fish task is that 1. It is not open source, 2. It is too long (45+ minutes i.e 1.5 hours if used pre and post test), and 3. Kids tend to lose interest in such a long assessment task. This is an attempt to develop a short game (<5 min) to come up with a measure of curiosity in kids belonging to the age group 3-8 years. 

## Why measure Curiosity 
- Measuring curiosity helps us understand how curious behaviors are related to other behaviors, such as exploration, anxiety, interest, deprivation. 
- Scientific curiosity has a positive association with learning, and hence having accurate measures of curiosity could directly influence digital learning design techniques. 
- This can be used as a pre-test and/or post-test measure for other studies involving playtesting of games, evaluation of learning applications. The idea is to use a separate scenario of the game pre-test and post-test. 
- It opens the avenue to sense physiological measures of participants, facial expression, and audio, and build a real time sensing model of curiosity. 
- It sounds like fun.

## Game behaviors associated with curiosity
Game behaviors associated with children’s curiosity 
Through our literature review on curiosity, measuring epistemic curiosity, types of curiosity, uncertainty in game design, I formed a list of game behaviors that have a positive association with curiosity. These are inspired from self report questionnaires used for curiosity. These are also inspired from the pre-test questionnaire that Zhen Bai (from the SCIPR group) modified for children. This is not exhaustive : 

- Interacting with novel sensory interactions / sensory experiences such as touch, sight, and sound - deviating from regular.
- Physically manipulating machinery in the game. Finding out how complicated machines work.
- Interacting with intricate, mysterious, and contradictory stimulus. 
- Attempting to find out why an object behaves that way. 
- Exploring an object to figure out its general use. 
- Interacting with an object the participant is not familiar with. 
- Asking questions about things the participant does not understand. 
- Spending more time to attempt to bridge the information gap; comfort with uncertainty or hidden information. 

The possibility of these behaviors was built into a game. 


## Game 
Game 
The idea is to build 3-4 child-friendly scenarios of games with ‘hidden objects’. Illustrated below is the first game I implemented. 

###Scenario 
Santa Claus has lost some his presents. They come in all colors, and are gift wrapper. Can you help them find them? Additionally, can you shake them to figure out what’s inside? 

###Gameplay
The game is a 1-screen game space where kids go around to find presents. Some of them are easy to find and are clearly visible. Some are tougher, and need manipulations (such as using the key to open the chest, or move the ambiguous clock) to find. After the participant collects a present, they get a pop-up, where they can shake the object to listen to what is inside. They can either guess the object, or skip it. If they guess it, I use speech recognition to validate their responses, and there is feedback. They can also ask questions about the present. The idea is to have the game respond automatically, but currently we have the researcher responding. The number of presents in the game is not fixed, and new presents keep popping up, because we also want to measure how long participants engage with the game.

### Logging 
On the back - end, we log every curiosity behavior that is observed. These are the curiosity behaviors in the game :

- Interacting with novel sensory interactions / sensory experiences such as touch, sight, and sound - deviating from regular. 
- Novel objects interacted with (animated presents, and objects with sound). 
- Ambiguous objects interacted with (the clock, and the paper stroll). 
- Number of manipulations (Key, axe, tree, present shaking). 
- Number of attempts made to answer the guessing puzzle. 
- Number of questions asked. 
- Number of questions that aided the hypothesis of what’s inside. 
- Number of hidden presents found. 
- Time spent exploring the game. 
- If the objects were mapped to their correct use (example, axe). 

Every interaction is written to a log file with mouse coordinates. Every type of score is logged, (example, manipulated objects = 4, time spent = 4:06).


