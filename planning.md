# Wear It Out Planning
'Wear It Out' is a full-stack, full CRUD application that allows you to log all of your clothing items, and track your outfits. While viewing your clothing items, see how many times you've worn that item. Create outfits with your saved clothing items, and each day, log the outfits you've worn. You can view the outfits you've worn on past days, and save your favorite outfits to use as inspiration for future occasions.  

## Trello Board
Check out my [Trello Board](https://trello.com/b/1XiujYyJ/my-closet-tracker)!

## Wireframes
#### Home Page (logged out view)
![Wear It Out Wireframes](https://github.com/laurencmendoza/wear-it-out/assets/137251999/27d06a88-fc27-4166-97ee-dba60ac0e6a7)
#### Home Page & Clothing Items Menu (logged in view)
![Wear It Out Wireframes (1)](https://github.com/laurencmendoza/wear-it-out/assets/137251999/ac6ac18d-c27f-46f0-a892-9575daae9586)
#### Clothing Items List View
![Wear It Out Wireframes (3)](https://github.com/laurencmendoza/wear-it-out/assets/137251999/853c10ac-fd38-4bbb-87b3-288ae0d9fc31)
#### Clothing Item Details Page
![Wear It Out Wireframes (4)](https://github.com/laurencmendoza/wear-it-out/assets/137251999/805cebd2-11eb-4302-a852-3bb3755a62ba)
#### Add a Clothing Item Form
![Wear It Out Wireframes (5)](https://github.com/laurencmendoza/wear-it-out/assets/137251999/f14f199a-378e-4c3e-9fb5-c93bbc3623bd)
#### Outfit List View
![Wear It Out Wireframes (6)](https://github.com/laurencmendoza/wear-it-out/assets/137251999/a7459173-c20f-44c5-bf3e-ba9f06e33b1f)
#### Create an Outfit Page
![Wear It Out Wireframes (7)](https://github.com/laurencmendoza/wear-it-out/assets/137251999/312a4cba-4840-4931-89b2-87ba8383c299)
![Wear It Out Wireframes (8)](https://github.com/laurencmendoza/wear-it-out/assets/137251999/e834c5e4-eb5b-403c-89d4-5c7c27a4c7ac)
#### Outfit Details Page
![Wear It Out Wireframes (9)](https://github.com/laurencmendoza/wear-it-out/assets/137251999/a25695c8-54ca-458d-9781-e1f46f318cbd)
#### Confirm Delete Page
![Wear It Out Wireframes (10)](https://github.com/laurencmendoza/wear-it-out/assets/137251999/2ea31301-8ca9-4873-ba6f-65016f03e4f5)
#### Outfit Tracker Entries List View
![Wear It Out Wireframes (11)](https://github.com/laurencmendoza/wear-it-out/assets/137251999/1ec25ad6-23e6-496f-9c6c-4162c0400b2b)
#### Outfit Tracker New Entry Form 
![Wear It Out Wireframes (12)](https://github.com/laurencmendoza/wear-it-out/assets/137251999/1a7bb696-2d7a-425a-9194-e415d0f982c3)
![Wear It Out Wireframes (13)](https://github.com/laurencmendoza/wear-it-out/assets/137251999/26b63dbf-f145-4b0f-81ed-2a4228f346ee)
#### Nav Bar Dropdowns (logged in view)
![Wear It Out Wireframes (2)](https://github.com/laurencmendoza/wear-it-out/assets/137251999/cc60b204-6a61-4d44-b2be-4eca6dd57b2f)


## ERD
![Wear It Out ERD](https://github.com/laurencmendoza/wear-it-out/assets/137251999/ecb881b5-9341-4aac-bbaf-bc34db1f91f2)


## User Stories
| #  | Name                                   | Description                                                                                                                                                                                              | Priority | Dependent on # |
| -- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | -------------- |
| 1  | Add a clothing item                    | AAU, I want to be able to create a clothing item on the app                                                                                                                                              | 1        |                |
| 2  | View clothing items                    | AAU, I want to be able to view all of my clothing items                                                                                                                                                  | 1        | 1              |
| 3  | View clothing items by category        | AAU, I want to be able to view all of my clothing items by category (tops, bottoms, full body, shoes, accessories)                                                                                       | 1        | 2              |
| 4  | View clothing item details             | AAU, I want to be able to select a clothing item to view its details                                                                                                                                     | 1        | 2              |
| 5  | Update clothing items                  | AAU, I want to be able to update the information on my clothing items                                                                                                                                    | 1        | 4              |
| 6  | Delete clothing items                  | AAU, I want to be able to delete clothing items from the app                                                                                                                                             | 1        | 4              |
| 7  | Create an outfit                       | AAU, I want to be able to create an outfit using my existing clothing items on the app                                                                                                                   | 1        | 1              |
| 8  | View outfits                           | AAU, I want to be able to view all of my outfits                                                                                                                                                         | 1        | 5              |
| 9  | View outfit details                    | AAU, I want to be able to select an outfit to view the outfit details                                                                                                                                    | 1        | 8              |
| 10 | Update outfits                         | AAU, I want to be able to update my existing outfits                                                                                                                                                     | 1        | 9              |
| 11 | Delete outfits                         | AAU, I want to be able to delete my existing outfits                                                                                                                                                     | 1        | 9              |
| 12 | Track outfits                          | AAU, I want to be able to track the outfits that I wear each day                                                                                                                                         | 1        | 7              |
| 13 | View dates worn for clothing items     | AAU, on the clothing item details page, I want to be able to see the dates in which I’ve worn that item                                                                                                  | 1        | 12             |
| 14 | Upload photos of clothing              | AAU, I want to be able to upload photos of my clothing items                                                                                                                                             | 1        | 1              |
| 15 | Upload photos of outfit                | AAU, I want to be able to upload photos of my outfits                                                                                                                                                    | 1        | 7              |
| 16 | Authentication and authorization       | AAU, I want to be able to log into the application to view my data                                                                                                                                       | 2        | 1              |
| 17 | Custom search for clothing item photos | AAU, I want to search for photos on Google to add to my clothing items                                                                                                                                   | 2        | 1              |
| 18 | Menu for clothing item categories      | AAU, I want the menu of clothing item categories to look like a cartoon closet, where each category is accessed by clicking on the image that matches the category (ex: click on a shirt to access tops) | 2        | 1              |
| 19 | Filter clothing items by color         | AAU, I want to be able to filter my clothing items by color                                                                                                                                              | 3        | 1              |
| 20 | Filter clothing items by tag           | AAU, I want to be able to filter my clothing items by tag                                                                                                                                                | 3        | 1              |
| 21 | Calendar view                          | AAU, I want to be able to access a date through a calendar view to read information from each date (ex:outfits worn on that day) and add information (ex:log outfits for that day)                       | 3        | 7              |
| 22 | Customize menu for clothing items      | AAU, I want to be able to edit the display for my clothing items’ categories (ex: display a dress or a suit for the full body category)                                                                  | 4        | 18             |
