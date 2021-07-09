# OrganismsSimulation
App which simulates existence of animals and plants on the grid created with Python using PyQt5 for GUI.

#### [Youtube video](https://youtu.be/0OELylNfb1g) which presents the entire game.

## Technologies
Project is created with:
* Python 3.7 
* PyQt5 5.15.4

## File Structure
```bash
OrganismsSimulation
│
└───organisms_simulation
│   │
│   ├───animals
│   │   │   antelope.py
│   │   │   cyber_sheep.py
│   │   │   fox.py
│   │   │   human.py
│   │   │   sheep.py
│   │   │   turtle.py
│   │   │   wolf.py
│   │   └───__init__.py
│   │          
│   ├───grid
│   │   │   click_menu.py
│   │   │   commentator.py
│   │   │   grid_cell.py
│   │   │   grid_is_full_exception.py
│   │   │   position.py
│   │   └───__init__.py
│   │         
│   ├───plants
│   │   │   belladonna.py
│   │   │   grass.py
│   │   │   guarana.py
│   │   │   sosnowsky_hogweed.py
│   │   │   sow_thistle.py
│   │   └───__init__.py
│   │           
│   ├───prev_instances
│   │       saved_instance
│   │       saved_instance.txt
│   │       saved_instance.tzt
│   │
│   ├───world
│   │   │   animal.py
│   │   │   organism.py
│   │   │   plant.py
│   │   │   world.py
│   │   └───__init__.py     
│   │
│   └───__main__.py
│
└─── requirements.txt
```
