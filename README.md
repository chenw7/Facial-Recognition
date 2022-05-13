# Facial-Recognition
If you have previously installed necessary libraries for this program (from the hand tracking program), please skip to step 10.

Here are the steps to follow in order to correctly set up your computer to run the simple face recognition program.

1. Firstly, python must be installed. However, we don't have to directly install it from the python website. Instead, we can install python and pip, quickly and efficiently, both with homebrew.

2. To install homebrew, open your terminal and type in the following command.

        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    Further instructions will be provided in your terminal to assist you in installing homebrew. 

3. To check if homebrew is installed correctly, type the following command into your terminal.
 
        brew help
    
    If an error does not appear, that means homebrew has been successfully installed and you are ready for the next steps.
    If an error appears, repeat step 2 and make sure you followed the instructions provided in your terminal correctly.
    
4. Once homebrew has been installed, we can install both python and pip with entering the following command into your terminal.
 
        brew install python
    
    This command installs the latest version of python, pip, and necessary packages for set up all for you without you needing to do anything. Simply sit back and 
    wait for homebrew to finish installing all the programs and packages for you.
    
5. To test out if python has been correctly installed, type the following command into your terminal.

        python3
    
    If an error does not appear, python has successfully been installed!
    If an error does appear, repeat steps 3-4.

6. Now that python has been installed, it's time to install anaconda which will allow for data science packages to be imported into python. Use the following link to install the latest version of anaconda.

    https://www.anaconda.com/products/individual
    
    Follow the instructions provided by the anaconda installation package and install anaconda on your computer.

7. To check if anaconda has been installed properly, open the anaconda application. The interface should say anaconda navigator and have various options of what IDE to launch.

    If anaconda does not open, reinstall the application (possibly with a different version).

8. Once anaconda has been installed, launch jupyter notebook and a new tab on your browser will be opened. It should look similar to the picture below.
<img width="1145" alt="Screen Shot 2022-03-09 at 8 35 13 AM" src="https://user-images.githubusercontent.com/91576538/157349691-ad95c212-6de1-4f2c-8c7b-139b2470e00b.png">
    
9. Select the location in which you would like to store your python files. Once you have reached the folder/location you would like to store your file, create a new jupyter notebook (On the top left corner, click new, and then click python3). <img width="1156" alt="Screen Shot 2022-03-09 at 9 02 40 AM" src="https://user-images.githubusercontent.com/91576538/157352417-4922dbff-ef54-40de-a57d-6ef63fe3ee02.png">

10. Once your notebook has been created, click on the link below to see the source code to the simple facial recognition program (explanations to the code are included as comments in the source code).

https://github.com/chenw7/Simple-Facial-Recognition/blob/main/Facial%20Recognition%20(Simple).py
        
11. Install the necessary libraries to run the program using pip. Enter the following commands in your terminal.

        pip install opencv-python==3.4.8.29
       
        pip install opencv-contrib-python==3.4.8.29
        
        pip install face_recognition
        
        pip install numpy
        
12. Now that all necessary libraries and accessories for the program have been installed, copy the code into jupyter notebook. 

13. Before you execute the program, notice the code from lines 13 to 23. To personalize your program and recognize faces you want, you will have to modify the code and upload images into the same folder as where you stored the program (detailed instructions are included in step 14). 

14. Firstly, find the two people you would like to have their faces recognized (Let's call them John and Mary for our example). Then, take an image of their face and store it as a jpeg file in the same folder as your program (Should look similar to the following).

<img width="288" alt="Screen Shot 2022-05-13 at 12 13 50 PM" src="https://user-images.githubusercontent.com/91576538/168210023-b07128dd-754f-4412-bce2-e9bb79fe8a39.png">
       
Note that the file has to be in a jpeg format in order for the program to correctly produce a trained face model of your desired person.
       
Then, modify the code from lines 13 to 23 in order for the program to correctly operate. In our case, the two people are named John and Mary and their two corresponding pictures are named John.jpeg and Mary.jpeg. The program will have to be modified like the following.
       
<img width="577" alt="Screen Shot 2022-05-13 at 12 27 41 PM" src="https://user-images.githubusercontent.com/91576538/168211487-3012d169-e03a-4606-9fee-04fcd259ac2b.png">
       

15. The output of the program should appear like somewhat of the following screenshots.

  Faces that were uploaded into the program: Simba, Biden
<img width="1193" alt="Screen Shot 2022-04-08 at 8 30 57 AM" src="https://user-images.githubusercontent.com/91576538/167743608-62504650-251a-49cd-ae15-685bb9f8e53c.png">
  Faces that were recognized by the program: Obama, Biden
<img width="1154" alt="Screen Shot 2022-04-08 at 8 22 20 AM" src="https://user-images.githubusercontent.com/91576538/167743635-eda52388-3647-424a-964b-a7e2aacf50e3.png"> 
<img width="1222" alt="Screen Shot 2022-04-08 at 8 20 34 AM" src="https://user-images.githubusercontent.com/91576538/167743642-b9edde45-2683-4380-8121-750d84e607ec.png">

16. If errors regarding cv2 or any of the other modules still exist, search for solutions on stackoverflow (most solutions to your problems can be found).
