import { useState,useEffect } from 'react';
import './App.css';
import axios from 'axios';



function App() {
  const [question, setQuestion] = useState({
    'question': 'Wybierz gatunek gry.',
    'answers': [{'name':'RPG','id':0, 'description': 'Gry w których gramy jedna lub drużyna postaci, rozwijając naszą postać czy drużyne w walce i poznając świat z ich strony'}, 
                {'name':'RoqueLike','id':1,'description':'Gry z randomowymi wygenorowanymi poziomamy przez co każda rozgrywka jest inna'}, 
                {'name':'RTS','id':2,'description':'Gry w których wcialmy się w dowódce miasta czy armii i musimy użyc strategii aby pokonać przeciwnika'} ],
    'image': 'Gatunek.jpg',
    'description' : 'Jaki gatunek gry chcesz zagrac?'
  })
  const [questionId, setQuestionId] = useState(0)
  const [answerId, setAnswerId] = useState(-1)
  const [description, setDescription] = useState(question.description)
  const [image, setImage] = useState(question.image)
  const serwerUrl="http://localhost:5000/"


  async function get_question() {
      
      await axios.get(serwerUrl+"question/"+questionId.toString())
      .then(function (response){
        setQuestion(response.data);
        setDescription(response.data.description)
      })      
      .catch(function (error) {
        console.log(error);
      });

  }
  async function send_answer(answerId) {
      
    await axios.post(serwerUrl+"question/"+questionId.toString(),{
      'answer' : answerId
    })
    .then(function (response){
      setQuestion(response.data);
      setDescription(response.data.description)
    })      
    .catch(function (error) {
      console.log(error);
    });

}


  const button_click = (e,id)=>{
    e.preventDefault();
    setQuestionId(questionId+1)
    send_answer(answerId)
  }
  const button_hover = (e,id)=>{
    if (id == -1){
      setDescription(question.description)
      setImage(question.image)
    }
    else{
      setAnswerId(id)
      setDescription(question.answers[id]['description'])
      setImage(question.answers[id]['image'])
    }
  }

  var answers = question.answers.map((a) =>
    <button className="answerBtn" 
    onMouseLeave={e=>button_hover(e,-1)} 
    onMouseEnter={e=>button_hover(e,a['id'])} 
    onClick={e=>button_click(e,a['id'])}>
    {a['name']}</button>
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
      <p>Wytłumaczenie:</p>
      <p>{description}</p>
      <img src={serwerUrl+"static/images/"+image}></img>
      </div>
    </div>
  );
}

export default App;
