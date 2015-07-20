# random_name_generator
The `rng.py` file creates a random name generator that can be used in a classroom setting to select students. 
Each time a name is chosen, it will be removed from `self.NAMES` and added to `self.USED`. 
All names will be added back into `self.NAMES` when each name has been chosen at least once.

### Use

* Replace `self.NAMES` with the names that you wish to be randomly generator.
* Colors are randomly generated
* Speed is created via `time.sleep` method which takes in one parameter (how long to delay)

### Run With
> python3 rng.py