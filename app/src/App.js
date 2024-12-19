import { useState,useEffect } from 'react';
import './App.css';
import axios from 'axios';



function App() {
  const [question, setQuestion] = useState({
    "question": "Jak ci mija dzien",
    "answers": ["slabo","normalnie","dobrze"],
    "image": "obrazeksrc",
    "description" : "Jak dzisiaj sie cos stalo to mozesz mi powiedziec"
  })
  const [questionId, setQuestionId] = useState(0)

  const serwerUrl="http://localhost:5000/"


  async function get_question() {
      
      await axios.get(serwerUrl+"question/"+questionId.toString())
      .then(function (response){
        setQuestion(response.data);
      })      
      .catch(function (error) {
        console.log(error);
      });

  }

  const button_click = (e)=>{
    e.preventDefault();
    setQuestionId(questionId+1)
    get_question()
  }

  var answers = question.answers.map((q) =>
    <button className="answerBtn" onClick={button_click}>{q}</button>
  );

  useEffect (()=>{
    get_question()
  },[]);

  return (
    <div className='main'>
      <div>
      <a src={question.image}></a>
      <h1>{question.question}</h1>
      {answers}
      <p>Wytłumaczenie:{question.description}</p>

      </div>
    </div>
  );
}

export default App;
