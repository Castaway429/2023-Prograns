//Where the answer goes
const questionP = document.getElementById("QuestionP");
//Where the question goes
const answerP = document.getElementById("AnswerP");
//Basically our whole screen
const container = document.getElementById("container");
//Previous questions index
var prevQuestion;
//Container for the button
const btnContainer = document.getElementById("btnContainer");
//Dynamically created Button
var button = document.createElement("button");
//Constant screen button
const rerollBtn = document.getElementById("rerollBtn");


//Where our questions will go
let qnaArray =
[ 
  ["Q: What is another name for Muhammad (SAW)? ", "A: Messenger, Rasoolullah, Saadiq, Ameen, Nabe "],
  ["Q: What is the first Sura in the Holy Quran?", "A: Surah Fatiha"], 
  ["Q: In Islamic calendar A.H. refers to:", "A: After Hijrah"],
  ["Q: Who was the first person to call the Adhan", "A: Bilal ibn Rabah (RA)"],
  ["Q: What is the first month of the Islamic calendar", "A: Muharram"], 
  ["Q: Who was İbrahim (AS) son", "A: Ismaeel (AS)"],
  ["Q: How many juz are there in the Quran", "A: 30"],
  ["Q: Name one type of person women don't have to wear their hijab in front of", "A: Father, brother, husband"], 
  ["Q: What are angels made out of?", "A: Noor (Light)"],
  ["Q: Which Prophet was ordered to build an ark?", "A: Prophet Nuh (AS)"],
  ["Q: How many prophets are mentioned in the quran?", "A: 25"], 
  ["Q: During Hajj which direction do you walk around the Kaaba (Counterclockwise or Clockwise)", "A: Counterclockwise"],
  ["Q: Which uncle of the Prophet Muhammad (SAW) protected him", "A: Abu Talib (RA)"],
  ["Q: Which discipline studies the life of the Prophet (SAW)", "A: Sirah"], 
  ["Q: Who was the first person that believed in the Prophet (SAW) and accept Islam", "A: Khadija (RA)"],
  ["Q: Which Prophet drove a car?", "A: None of them"],
  ["Q: What is the name of the Islamic call to prayer?", "A: Adhan"], 
  ["Q: Which surah/chapter does not have bismillah at the start", "A: Tawbah"],
  ["Q: Where is the Kaaba built?", "A: Makkah"],
  ["Q: What is the infinite water source in Makkah called", "A: ZamZam"],
  ["Q: What month was the Quran revealed", "A: Ramadan"],
  ["Q: Is fish halal or haram", "A: Halal"], 
  ["Q: In which Islamic Month is Hajj performed", "A: Dhul Hijjah"], 
  ["Q: On Which Islamic Date is Eid Al-Fitr Celebrated", "A: The 1st of Shawwal"],
  ["Q: Who purchased and freed Bilal (RA)", "A: Abu Bakr (RA)"],
  ["Q: How old was the Prophet (SAW) when he passed away?", "A: 63"], 
  ["Q: Which Prophet could speak to animals", "A: Prophet Sulayman (AS)"],
  ["Q: How old was the Prophet (SAW) when he became a Prophet", "A: 40"],
  ["Q: How many surahs are in the Quran?", "A: 114"], 
  ["Q: What is the longest surah in the Qur'an?", "A: Surah Al' Baqarah"],
  ["Q: What does “Surah” mean", "A: Chapter"],
  ["Q: What are the sayings of the prophet Muhammad(SAW) called?", "A: Hadith"], 
  ["Q: The first surah to ever be revealed was", "A: Surah Alaq"],
  ["Q: Who was the first Prophet in Islam?", "A: Adam (AS)"],
  ["Q: What are the followers of Islam called?", "A: Muslims"], 
  ["Q: What do you call the funeral prayer", "A: Salat al-Janazaa"],
  ["Q: What is the Islamic calendar dependant on", "A: The Lunar Cycle / The Moon"],
  ["Q: Who was the last prophet?", "A: Prophet Muhammad"], 
  ["Q: Where was Prophet Muhammad (SAW) born?", "A: Makkah"],
  ["Q: When will the Day of Judgement occur?", "A: Only Allah knows"],
  ["Q: Is the Black Stone in the Kaaba (Part of Cave Hira or a Meteorite)", "A: A meteorite"], 
  ["Q: Which Prophet is known as “Father of Prophets”", "A: Prophet İbrahim (AS)"],
  ["Q: What is the name of the Prophet (SAW) father", "A: Abdullah"],
  ["Q: What is the most authentic source of knowledge for Muslims.", "A: The Quran"], 
  ["Q: Where was the original Qibla", "A: Jerusalem (Masjid Al-Aqsa)"],
  ["Q: What is the term for the charity Muslims are required to give yearly", "A: Zakat"],
  ["Q: What is the term for the Islamic declaration of faith?", "A: Shahada"], 
  ["Q: What is the pilgrimage done outside of Hajj season", "A: Umrah"],
  ["Q: What is the term for the Muslim community?", "A: Ummah"],
  ["Q: Where is the masjid of rasoolullah located?", "A: Medina"], 
  ["Q:What is the islamic term for the concept of faith? ", "A: Iman"],
  ["Q: Which prophet is known for being swallowed by a giant fish after trying to escape Allah's command?", "A: Prophet Yunus"],
  ["Q: How many prayers are there in one day?", "A: 5"], 
  ["Q: What is the prayer prayed after dawn called?", "A: Fajr"],
  ["Q: What is the prayer prayed at noon called?", "A: Zuhr"],
  ["Q: What is the late afternoon prayer called", "A: Asr"], 
  ["Q: What is the evening prayer called", "A: Isha"],
  ["Q: What important day is during the last 10 days of Ramadan", "A: Laylat al-Qadr"],
  ["Q: Which prophet split the moon?", "A: Prophet Muhammad (SAW)"], 
  ["Q: What is the first pillar of Islam", "A: Belief / Shahada"],
  ["Q: What is the 2nd pillar of Islam", "A: Prayer / Salah"],
  ["Q: Which Surah is known as “The Elephant”", "A: Al-Fil"], 
  ["Q: What is the term used to refer to food that is permissible to eat?", "A: Halal"],
  ["Q: What day of the week is Jummah held?", "A: Friday"],
  ["Q: What’s the shortest surah in the Quran", "A: Surah al-Kawthar"], 
  ["Q: Who is Dajjal?", "A: False messiah"],
  ["Q: What language is the Quran written in", "A: Arabic"],
  ["Q: What did the people of Makkah worship before Rasoolullah (SAW)?", "A: Idols"], 
  ["Q: How many names of Allah are there", "A: 99"],
  ["Q: What is the name of the magical horse that’s the prophet (SAW) used", "A: Buraq"],
  ["Q: Who was the first male to accept Islam", "A: Abu Bakr (RA)"], 
  ["Q: What is the name of the angel of who brought down revelation to the Prophet (SAW)", "A: Jibrarel"],
  ["Q: Which Surah is known as “The Women”", "A: Surah An-Nisa"],
  ["Q: Who was the khalifah/ ruler after Rasoolullah (saw) died", "A: Abu Bakr (RA)"], 
  ["Q: How many eids are there in a year", "A: 2"],
  ["Q: Who was the mother of Rasoolullah (SAW)", "A: Aminah"],
  ["Q: What does Bismillah mean?", "A: In the name of Allah"], 
  ["Q: What does Allahu Akbar mean?", "A: Allah is greater than everything"],

];

//Where the used questions will go
let qnaUsedArray =[];

function displayQuestion()
{
  //Get the length of our qnaArray 
  let qnalen = qnaArray.length;
  //Get a random number within the qnaArray
  let choiceOfQuestion = Math.floor(Math.random() * qnalen);


  //Based on Math.rand retrieve that qna question
  let retrievedQuestion = qnaArray[choiceOfQuestion];

  //Change the inner HTML of our elements to the correct question and answer
  questionP.innerHTML = retrievedQuestion[0];
  answerP.innerHTML = retrievedQuestion[1];

  //Add the question and answer to the UsedArray
  qnaUsedArray.push(qnaArray[choiceOfQuestion]);
  
  //Remove from qnaArray
  qnaArray.splice(choiceOfQuestion, choiceOfQuestion);

  //Remove later
  console.log(qnalen);
}

function resetQuestions()
{
  //Make the empty array full
  qnaArray = qnaUsedArray;
  //Make the full array empty
  qnaUsedArray = [];
  //Remove button from screen
  btnContainer.removeChild(button);
  //Readd reroll button
  btnContainer.appendChild(rerollBtn);
  //Reset header
  document.getElementById("header").innerHTML = "Click the buttons to Reroll!";
  //Reroll a question
  displayQuestion();
}

rerollBtn.addEventListener("click", function() {
  let qnalen = qnaArray.length;
  questionP.innerHTML = "";
  answerP.innerHTML = "";

  displayQuestion();

  if (qnalen == 1)
  {
    //Display on screen
    document.getElementById("header").innerHTML = "Last Question Displayed. Reset to see again!";
    //Button inner HTML
    button.innerHTML = "Reset Button!";
    questionP.innerHTML = "";
    answerP.innerHTML = "";
    //Adds button to the screen
    btnContainer.appendChild(button);
    //Unadded the reroll button
    btnContainer.removeChild(rerollBtn);
  }

});

button.addEventListener("click", resetQuestions);

