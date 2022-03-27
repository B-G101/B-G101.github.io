{% include navigation.html %}


## Idea: Map Geo guesser game
My idea is to create a map guessing game to help the new students at Del Norte learn the map and where there classes are located. This will work for the create task because it will use lists to store the map images and an input and output. The algorithm will be checking if the answer is correct or incorrect. <br>
## Table of Contents
1. [Written Responses](https://b-g101.github.io/create_task#written-responses)
1. [Code Segments](https://b-g101.github.io/create_task#code-segments)
1. [Video Runtime](https://b-g101.github.io/create_task#video-runtime)
1. [Link to the Full Code](https://github.com/nadirahaddach/4Gs/blob/main/templates/maptest.html) 
1. [Initial Brainstorming](https://b-g101.github.io/create_task#initial-brainstorming) <br><br>

### Written Responses
![](https://i.postimg.cc/XYs1Mj3m/Screenshot-2022-02-27-154202.png)
![](https://i.postimg.cc/3rjB58F1/Screenshot-2022-02-27-154400.png)
![](https://i.postimg.cc/fRHsHQPT/Screenshot-2022-02-27-155132.png)
![](https://i.postimg.cc/MKWggrVc/Screenshot-2022-02-27-155730.png)


<br><br>
### Code Segments

* The first program code segment must show how data have been stored in the list.
![](https://i.postimg.cc/3wpGX1L1/Screenshot-2022-02-27-152724.png)
<br>

* The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose.
<br>

![](https://i.postimg.cc/yYMYmHwq/Screenshot-2022-02-27-152944.png)
<br>

* The first program code segment must be a student-developed procedure
![](https://i.postimg.cc/dQ8Kbyff/Screenshot-2022-02-27-153106.png)
![](https://i.postimg.cc/qM4d47Vv/Screenshot-2022-02-27-153146.png)
![](https://i.postimg.cc/brHck7bP/Screenshot-2022-02-27-153256.png)
<br>
* The second program code segment must show where your student-developed procedure is being called in your program.

![](https://i.postimg.cc/zf99MzF5/Screenshot-2022-02-27-153400.png)


<br>

### Video Runtime
Link to the runtime: <br>

https://user-images.githubusercontent.com/89234851/155906449-7b570eee-b7a2-473e-adaa-64c8cdb532ba.mp4



<br><br><br><br>
### Initial Brainstorming
Description: It's a game about guessing the different locations at Del Norte to help new students adapt to their school and learn the map quicker. 
![](https://i.postimg.cc/65kjb3mW/Untitled-drawing.png)
### [Overview of the Create Task](https://apcentral.collegeboard.org/pdf/ap-csp-student-task-directions.pdf?course=ap-computer-science-principles)
Instructions for input from one of the following:
* the user (including user actions that trigger events)
* Example: user will input their guess for what location they think it is

* Use of at least one list (or other collection type) to represent a collection of data that is stored and used to manage program complexity and help fulfill the program’s purpose
* Example: the map image displayed that the user will have to guess will be randomly picked from a list of images (list of image src stored as a string in the python list)

* At least one procedure that contributes to the program’s intended purpose, where you have defined:
* the procedure’s name
* the return type (if necessary)
* one or more parameters
* Example: the procedure will be checking whether or not the guess is correct then displaying the next map image in the game (still need to figure out how to make it iterate through the each map image in the list and allowing the user to guess again)

* An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure
* Example: sequencing: the steps of user inputting their guess then it will display a message based on that guess
selection: the random selecting a random image from the list and displaying it
iteration: making the game have multiple images and be able to have the user guess multiple times until they make it through all the map images in the list

* Calls to your student-developed procedure
* Example: can have a start game button






InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "FirstName": "Bria",
    "LastName": "Gilliam",
    "DOB": "September 27",
    "Residence": "Los Angelus",
    "Email": "briagee101@gmail.com",
    "FavoriteColors": ["Blue", "Sage Green", "Lilac"]
})

InfoDb.append({
    "FirstName": "Allison",
    "LastName": "Huang",
    "DOB": "July 27",
    "Residence": "Irvine",
    "Email": "allisonhuang@gmail.com",
    "FavoriteColors": ["A", "B", "C"]
})

InfoDb.append({
    "FirstName": "Paige",
    "LastName": "McCartin",
    "DOB": "April 30",
    "Residence": "San Diego",
    "Email": "paigey@gmail.com",
    "FavoriteColor": ["A", "B", "C"]
})
