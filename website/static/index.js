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
    charSpan.innerText = " ";
    wordDiv.appendChild(charSpan);
    wordDiv.classList.add("mx-1") // bootstrap
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

