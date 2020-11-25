# DmitrysMayaScripts
Maya scripts I created as part of learning Python. The scripts are provided free of charge under GPL Licence.


----------- Script #1 - Shield Generator

Created a scattered set of objects from selection. The amount of objects can be adjusted as well as the generation seed.

Installation:

1) Dropt the "shield_Generator.py" in your Documents>maya>Maya####>scripts folder

2) In Maya:
  Script Editor>File>Open Script> select shield_Generator.py and press File>Save Script to Shelf
  
----------- Script #2 / #3 - Animation Tweener / Gear Generator

Animation Tweener - Allows to adjust animation by adding extra frames. Select the frame on the playback slider where you want to adjust the animation and use the slider in the UI to adjust it.
Gear Generator - Allows to generate gears with different amount of teeth and bevel in real time.

Installation:

1) Dropt the "gearClassCreator.py", "tweenerUI.py", and "reusableUI.py" in your Documents>maya>Maya####>scripts folder

2) In Maya:
  In Script Editor write:
          import reusableUI
          reload(reusableUI)
          reusableUI.TweenerUI().show()
          
File>Save Script to Shelf

then

In Script Editor write:
          import reusableUI
          reload(reusableUI)
          reusableUI.GearUI().show()
          
File>Save Script to Shelf

----------- Script #4 - Parts Library

Allows to store a library of geo and import geo from the library in any scene.
Storing geo in the library also creates a snapshot of the object in the library viewer.
The script will create a folder for your library in your Documents>maya folder

Installation:

1) Dropt the "conLib" folder in your Documents>maya>Maya####>scripts folder

2) In Script Editor write:
              from conLib import libUI
              reload(libUI)
              ui = libUI.showUI()
              
              
Thank you for using them! Have a good day!

