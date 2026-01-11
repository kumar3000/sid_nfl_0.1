# NFL 0.1
Simple, text-based football simulator to practice Python basics.

## Road Map
### 0.1
- Core Library
    - game - simulation that returns relevant statistics
    - player - class w/ player data (contains team object)
    - team - class w/ team data

- main.py
    - Player Creation
        - Debug mode
        - Name
        - Year
    - Draft Process
        - Random for now
    - Seasons loop
        - for seasons < 20
            - seasons += 1
        - Regular Season
        - Postseason
        - Offseason (possibly change teams / contract extensions)

- ToDo:
    - Implement season loop in main.py instead of Season.Start()
    - Offseason
    - College (to determine player rating)