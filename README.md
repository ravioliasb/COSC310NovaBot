# NOVABOT, THE ROBOT ASTRONOMER AND GEOGRAPHER
---

# Project Description

Nova is a chatbot that is passionate about teaching astronomy and geography to users. Her implementation of natural language processing in python allows her to understand and answer user questions related to astronomy such as stars, galaxies, black holes and planets, and questions related to geography such as country capitals and geographical records. She is also equipped with Wikipedia, Wolfram and NASA APIs for users who wish to get more detailed information on topics. She was created with the intent to spread basic knowledge about astronomy and geography to individuals who are interested in these fields. 

# Software Development Life Cycle

We chose to use the incremental development life cycle. This life cycle was ideal because we wanted to continuously gather user feedback and make corrective changes throughout development. As part of the agile process, we participated in peer programming since we all had limited experience creating chatbots and wanted to support each other. Our incremental life cycle included a project planning phase, a researching phase, a development phase, a review phase and then a presentation phase. We created a basic chatbot in the first increment and created a GUI for the chatbot in the second increment. In this final increment, I worked on the chatbot alone and added Wikipedia, Wolfram Alpha and NASA APIs. 

# How does Nova work?

Nova was developed in python and uses natural language processing to understand and converse with the user. She takes the input from the user and cleans the sentences into a condensed and easily-readable format. She then compares the input to the questions she has in her questionbank and gives a response based on the similarity between the input and the questionbank questions. All the questions and responses are found inside the corpus.txt file and may be expanded or changed as more astronomy or geography questions are thought of. Also, Wikipedia, Wolfram Alpha and NASA APIs were implemented into the chatbot for those who wish to delve more into the topics.

# Software Design

NovaBot was created in the Python language through PyCharm. We used several libraries including nltk, spacy and pyspellchecker to correct, format and clean user input so that NovaBot would be able to recognize and match it to the appropriate responses in the databank. We also used the Wikipedia and Wolfram APIs to allow users to conduct more advanced searches on topics. Lastly, the NASA API was implemented so that users could view the NASA's astronomical Picture of the Day. 

# Requirements

You will need to download and install NLTK and Spacy in your python IDE before using Nova. You will also need to download en_core_web_lg for Spacy. Once that is complete, you can run main.py and begin using Nova. 

- `pip install nltk`
- `pip install -U spacy`
- `python -m spacy download en_core_web_lg`
- `pip install pyspellchecker`
- `pip install wolframalpha`
- `pip install python-nasa-api`
- `pip install wikipedia`

# Sections

- **Corpus**: Contains a compilation of questions and responses that Nova uses to converse with the user
- **Preprocessor**: This section is in charge of formatting the user input into a more readable format for the system
- **Processor**: This section takes the preprocessed data and tries to match it with its accurate response
- **Main**: This section introduces the user, takes their input, generates the GUI, and manages how the program executes 
- **norm_punc**: This section was taken from the Phrasal library. It normalizes sentences by removing elements such as special characters, extra spaces and apostrophes. 
- **Wikipedia_Api**: This section takes user input, searches for the topic on the Wikipedia database and returns a summary of the topic
- **Wolfram_Api**: This section takes queries from the user and returns the response from Wolfram Alpha's database
- **NASA_API**: This section returns a summary of NASA's Picture of the Day and opens that picture on the user's browser

`Corpus` --> `Preprocessor` --> `Processor` --> `Main`

# Capabilities

- Nova utilizes natural language processing and pattern matching effectively so the user input does not have to match the predefined questions exactly to get an accurate response
   ```
    You: what is nuclear fusion?
    Nova: It is a processes by which the Sun fuses hydrogen atoms to form helium
    You: nuclear fusion
    Nova: It is a processes by which the Sun fuses hydrogen atoms to form helium
   ```
   ```
    You: what is the capital of Canada?'
    Nova: Ottawa`
   ```
- Nova cover a wide range of topics in astronomy, astrophysics and geography
- Nova is easy to refactor and reuse since its structure is very basic. The corpus.txt can be modified to suit any topic of interest
- Nova can recognize inputs even if they have simple spelling errors
   ```
    You: what s the capitall pf jamaica?`
    Nova: Kingston`
   ```
- Nova can recognize user inputs even if they contain special characters 
   ```
    You: what i$ the c@pital of India?
    Nova: New Delhi
   ```
- Nova can recognize the parts of speech of words in the user input
   ```
    You: what is a white dwarf?
    Nova: Parts of Speech:  [('white', 'JJ'), ('dwarf', 'NN')]
   ``` 
- Nova recognizes synonyms of the word "bye" and uses them to find out when the user is done asking questions
- Nova can display Wikipedia summaries when the user types "Wikipedia: " then their topic of choice
   ```
    You: wikipedia: Kingston, Jamaica
    Nova: Kingston is the capital and largest city of Jamaica, located on the southeastern coast of the island. It faces a natural harbour protected by the Palisadoes, a long sand spit which connects the town of Port Royal and the Norman Manley International Airport to the rest of the island. In the Americas, Kingston is the largest predominantly English-speaking city south of the United States.
    The local government bodies of the parishes of Kingston and St. Andrew were amalgamated by the Kingston and St. Andrew Corporation Act of 1923, to form the Kingston and St. Andrew Corporation (KSAC). Greater Kingston, or the "Corporate Area" refers to those areas under the KSAC; however, it does not solely refer to Kingston Parish, which only consists of the old downtown and Port Royal. Kingston Parish had a population of 96,052, and St. Andrew Parish had a population of 555,828 in 2001. Kingston is only bordered by Saint Andrew to the east, west and north. The geographical border for the parish of Kingston encompasses the following communities: Tivoli Gardens, Denham Town, Rae Town, Kingston Gardens, National Heroes Park, Bournemouth Gardens, Norman Gardens, Rennock Lodge, Springfield and Port Royal, along with portions of Rollington Town, Franklyn Town and Allman Town.The city proper is bounded by Six Miles to the west, Stony Hill to the north, Papine to the northeast and Harbour View to the east, which are communities in urban and suburban Saint Andrew. Communities in rural St. Andrew such as Gordon Town, Mavis Bank, Lawrence Tavern, Mt. Airy and Bull Bay would not be described as being in Kingston city.  
    Two districts make up the central area of Kingston: the historic Downtown, and New Kingston. Both are served by Norman Manley International Airport and also by the smaller and primarily domestic Tinson Pen Aerodrome.
   ``` 
- Nova can communicate with Wolfram Alpha when the user types "Wolfram: " then their query
    ```
     You: wolfram: Rigel
     Nova: distance from Earth | 870.4 ly
     apparent magnitude | +0.18 (easily visible to the naked eye)
     absolute magnitude | -6.95 (visual)
     spectral class | B8Ia (supergiant)
     effective temperature | 12000 K
     mass | 5.3×10^31 kg
     27 M_☉
     main sequence lifetime | 2.7 million yr
     end state | black hole
     Bayer name | β Orionis (Beta Orionis)
    ```
- Nova will display a description of NASA's Picture of the Day through her GUI and will display the picture in the user's browser when the user types "Picture of the Day"
    ```
      You: picture of the day
      Nova: Simulating Extreme Spacetimes. What happens when two black holes collide? This extreme scenario occurs in the centers of many merging galaxies and multiple star systems. The featured video shows a computer animation of the final stages of such a merger, while highlighting the gravitational lensing effects that would appear on a background starfield. The black regions indicate the event horizons of the dynamic duo, while a surrounding ring of shifting background stars indicates the position of their combined Einstein ring. All background stars not only have images visible outside of this Einstein ring, but also have one or more companion images visible on the inside. Eventually the two black holes coalesce.  The end stages of such a merger is now known to produce a strong blast of gravitational radiation, providing a new way to see our universe. This Week is: Black Hole Week at NASA
    ```
# Limitations

- Nova can take a while to process user input and output the correct responses since there is a lot of conversion and formatting to be done. The processing time could be lowered by using more efficient functions.
- Nova is somewhat limited to the predefined questions and responses in the corpus.txt. The corpus.txt will have to be expanded to allow Nova to answer more questions.
    ```
     Input: what is a megabyte?
     Nova: I do not understand your question
    ``` 
- Preprocessing, such as spell checking, was not implemented for Wikipedia, Wolfram and NASA APIs.

# New Features 

- **Wikipedia API:** The Wikipedia API was implemented so that users can get more information on topics that interest them. This feature is initiated when the user types "Wikipedia:" or "wikipedia:" then their topic of choice. When initiated, NovaBot will return a summary of the topic directly from the Wikipedia database. 
- **Wolfram API:** The Wolfram Alpha API was implemented so that users can get responses on queries such as "What is the weather in India" or finding out detailed characteristics of stars by typing in the star's name. Wolfram can also be used for conversion between units and calculations when users are trying to comprehend measurements given NovaBot. This feature is initiated when the user types "Wolfram:" or "wolfram:" then their query
- **NASA API:** The NASA API was implemented to allow users to view the Picture of the Day. NASA's Pictures of the Day are astronomical images that are specifically chosen daily to showcase the beauty of the universe. This API helped incorporate a visual element to the NovaBot that helps with the learning experience 
