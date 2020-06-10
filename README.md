**Environment**
* Windows 10 (64-bit)
* Anaconda 3.7
* django
* nltk
* numpy
* aiml

**Steps to setup enviornement**
* open command prompt in windows and go to current directory
* create a virtual environment
	conda create -n env python=2.7 anaconda
* activate env
	conda activate env
* install dependencies
	pip install -r requirements.txt


**Project Explanation**
* The project folder contains the cloud server code, android studio project and android apk file.
* The apk file provided can be installed in any mobile device.
* You can generate apk using android studio(link for the explanation is)
	https://www.youtube.com/watch?v=z8QVkvR2Rck&list=PL6gx4Cwl9DGBsvRxJJOzG4r4k_zLKrnxl&index=69
* Import android project and make your changes.
* App contains three activities
* MainActivity : It interacts with the cloud server.
* MapsActivity : Displaying the map and locations of hospitals with routes.
* GPSTracker : To get our location
* Note:: Obtain the key for Google Maps. And change it in AndroidManifest.xml
		android:name="com.google.android.geo.API_KEY"
		android:value="@string/google_maps_key" 
	In function updateplaces() of MapsActivity, change the key tag to your browser key in placesSearchStr string.

**Android interface input output**
* enter the symptoms(how  you  are feeling) through speech.
* if you have any more symptoms press "symptoms" button.
* else u can start diagnosis by pressing diagnosis button.
* answer the questions asked regarding symptoms with yes or no type answers.
* after certain number of questions,the result will be displayed.

**setup pythonanywhere**
* Create an account in pythonanywhere.com and make a zip file of mysite folder
* Upload mysite.zip present in project files to default user folder provided on pythonanywhere
* Open bash console in the folder where mysite.zip is uploaded
* Decompress the compressed folder by using following command in bash console
	~ $ unzip mysite.zip
* Open web tab in pythonanywhere
* Click on Add a new web app link
* Use Manual Configuration when asked for python framework and click next
* Select python version 2.7 and click next to finish creating webapp
* Start a new bash console from consoles tab in pythonanywhere
* Create virtual environment named medicalApp
	~ $ source virtualenvwrapper.sh
	~ $ mkvirtualenv medicalApp
* Now in web tab in Virtualenv slot enter the path to the virtual environment created and replace <user> with appropriate path. 
	/home/<user>/.virtualenvs/medchatbot
* Press start console in virtualenvironment 
* Install the bellow packages in virtual enviroment by entering below commands in opened bash console
	~ $ pip install aiml
	~ $ pip install numpy
	~ $ pip install nltk
	~ $ pip install django
* Now download punkt package in nltk
	~ $ python
	>>> import nltk
	>>> nltk.download()
	Downloader> d punkt
* In web tab of pythonanywhere open wsgi configuration file and replace the code with code provided in wsgi.txt 		provided in project files
* Replace sturl in onCreate() method appropriately.(change the username in url link with the website name on 			pythonanywhere)






