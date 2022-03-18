const sentenceDisplayElement = document.getElementById("quoteDisplay"); // stores the quotedisplay box as an element


function renderSentence(jsonQuote) { 
  //Gets the list of words and creates span objects of each letter, each of 
  //which are encapsulated in a div
  const wordsArr = JSON.parse(jsonQuote); //converts the JSON string into a javascript object
  sentenceDisplayElement.innerText = null; // clears the previous sentence
  let charNum = 0;
  let wordCharNum = 0
  let wordNum = 0
  wordsArr.forEach((word, i) => { // Creates the dive for each word, and numbers them with attributes
    wordCharNum = 0
    const wordDiv = document.createElement("div");
    wordDiv.classList.add("d-inline")
    wordDiv.classList.add("word")
    sentenceDisplayElement.appendChild(wordDiv);
    wordDiv.setAttribute("data-word-num", wordNum);
    wordDiv.setAttribute("extraCharacters", 0)
    word.split("").forEach((character, j) => { 
      /*Each letter is converted into a span, and numbered by their position in the sentence and 
      thier poistion in the word*/
      const charSpan = document.createElement('span');
      charSpan.setAttribute("word-char-num", wordCharNum);
      charSpan.setAttribute("data-char-num", charNum);
      charSpan.innerText = character;
      wordDiv.appendChild(charSpan);
      ++charNum;
      ++wordCharNum;
    });
    const charSpan = document.createElement('span')
    charSpan.setAttribute("word-char-num", wordCharNum);
    charSpan.setAttribute("data-char-num", charNum);
    charSpan.setAttribute("is-Space", true);
    charSpan.innerHTML = '&nbsp';
    wordDiv.appendChild(charSpan);
    // wordDiv.classList.add("mx-1") // bootstrap
    ++charNum;
    ++wordCharNum
    wordNum++

})}

function whichWord (charnum) { 
  /* A line of code that is repeatedly used. It will error if the 
  user has reached the end of a sentence, so  sends a null to act as a sentence end flag*/
  try {
    whichWord = currentSpan.parentElement.getAttribute("data-word-num")
    return whichWord
  } catch (e) {
    return null
  }
}

function letterTimeToWpm (time) {
  time = parseInt(time)
  return (12000/time) 
  // (1/5)/(time/60000) = (1/5) * (60000/time)
  // (1*60000)/(5*time)
  //  60000/5*time
  //  12000 / time
} 




// [{ word: x, wordTime: null, incorrectWord: null, typedWord: null, letters: new Array(x.length) }]
// letters: [{ letter: 'A', time: 0, speed: 0 }, {}, {}]
// letters: [12, 234, 435, 3453, 345] current

function processTest (wordsDict, testTime) {
  let amountOfCorrectLetters = 0
  let amountOfLetters = 0
  let amountOfCorrectedLetters = 0
  let amountofExtraLetters = 0
  let amountOfIncorrectLetters = 0
  let amountOfLettersIncSpace = 0
  let amountofMissedLetters = 0
  for (let i = 0; i < wordsDict.length; i++) {
    for (let ii = 0; ii < wordsDict.at(i).word.length; ii++) {
      if ((wordsDict.at(i).word.at(ii)) && (wordsDict.at(i).typedWord.at(ii))) {
        if ((wordsDict.at(i).typedWord.at(ii) === wordsDict.at(i).incorrectWord.at(ii)) && (wordsDict.at(i).incorrectWord.at(ii) === wordsDict.at(i).word.at(ii))) {
          // correct letter
          ++amountOfCorrectLetters
          wordsDict.at(i).letters[ii] = [wordsDict.at(i).letters.at(ii), "correct"]
        } else if ((wordsDict.at(i).typedWord.at(ii) === wordsDict.at(i).word.at(ii)) && (wordsDict.at(i).incorrectWord.at(ii) !== wordsDict.at(i).word.at(ii))) {
          // corrected letter
          ++amountOfCorrectedLetters
          wordsDict.at(i).letters[ii] = [wordsDict.at(i).letters.at(ii), "corrected"] 
        } else if ((wordsDict.at(i).typedWord.at(ii) !== wordsDict.at(i).word.at(ii))) {
          ++amountOfIncorrectLetters
          wordsDict.at(i).letters[ii] = [wordsDict.at(i).letters.at(ii), "incorrect"] 
        }     
      }  
    }
  }
  wordsDict.forEach((word, index) => {
    if (word.typedWord.length > word.word.length) {
      for (let i = ((word.word.length)-1); i < word.typedWord.length-1; i++) {
        wordsDict.at(index).letters.push([null, "extra"])
        ++amountofExtraLetters
      }
    } else if (word.typedWord.length < word.word.length) {
      for (let i = ((word.typedWord.length)-1); i < word.word.length; i++) {
        wordsDict.at(index).letters[i] = [null, "missed"]
        ++amountofMissedLetters
      } 
    }
  })


  wordsDict.forEach((word, index) => {
    word.typedWord.split('').forEach((letter) => {
      ++amountOfLetters
      ++amountOfLettersIncSpace
    })
    ++amountOfLettersIncSpace
  })

  let amountOfLettersInCorrectWordsIncSpaces = 0
  let arrayofwhichlettersarecorrect = []
  wordsDict.forEach((word, index) => {
    arrayofwhichlettersarecorrect[index] = true
    word.letters.forEach((letter) => {
      if (letter[1] !== "correct") {
        arrayofwhichlettersarecorrect[index] = false
      }
    })  
    if (arrayofwhichlettersarecorrect[index] === true) {
      amountOfLettersInCorrectWordsIncSpaces = amountOfLettersInCorrectWordsIncSpaces + word.letters.length + 1
    }
  })

  let wpm = ((amountOfLettersInCorrectWordsIncSpaces/5)/(testTime/60000))
  let rawWpm = ((amountOfLettersIncSpace/5)/(testTime/60000))
  let accuracy 
  if ((amountOfCorrectedLetters+amountOfIncorrectLetters+amountofExtraLetters+amountofMissedLetters) === 0) {
    accuracy = 100
  } else {
    accuracy = (((amountOfCorrectLetters)/(amountOfCorrectLetters+amountOfCorrectedLetters+amountOfIncorrectLetters+amountofExtraLetters+amountofMissedLetters))*100)
  }

  
        
        
  const processedTest = wordsDict.map((x, index) => { // x = { word: x, wordTime: null, incorrectWord: null, typedWord: null, letters: new Array(x.length) }
    let wordspeed = (x.typedWord.length/5)/(x.wordTime/60000)
    
    const lettersProcessed = x.letters.map((letterPair, i) => {
      return {correctLetter: x.word.at(i), time: letterPair.at(0), speed: letterTimeToWpm(letterPair.at(0)), type: letterPair.at(1), typedLetter: x.typedWord.at(i), incorrectLetter: x.incorrectWord.at(i)}
    })
    

    return { ...x, letters: lettersProcessed, wordSpeed: wordspeed, wordCorrect: arrayofwhichlettersarecorrect.at(index)}
  }) 

  const dataToSend = JSON.stringify({ testTime, testRawSpeed: rawWpm, testSpeed:wpm, testAcc:accuracy, processedTest });
  console.log(JSON.parse(dataToSend))
  return dataToSend
  

  // { testTime: xxx, processedTest: processedTest }
}

