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
        - Name
        - Stats (select from 5* to 1* QB)
    - Draft Process
        - Pick based off * rating
        - Random team
    - Seasons loop
        - for seasons < 20
            - seasons += 1
        - Regularseason
        - Postseason
        - Offseason (possibly change teams / contract extensions)