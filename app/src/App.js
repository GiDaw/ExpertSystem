import { useState,useEffect } from 'react';
import './App.css';
import axios from 'axios';



function App() {
  const [question, setQuestion] = useState({
    'question': 'Wybierz gatunek gry',
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
  const [end,setEnd] = useState(false)
  const [btnDisable, setBtnDisable] = useState(false)
  const serwerUrl="http://localhost:5000/"


  async function get_question() {
    if(questionId!=6){
      //get page
      setQuestionId(questionId+1);
      await axios.get(serwerUrl+"question/"+questionId.toString())
      .then(function (response){
          setQuestion(response.data);
          setDescription(response.data.description);
          setImage(response.data.image);
  
        })      
        .catch(function (error) {
          console.log(error);
        });
    }
    else{
      //reset to page 1
      setQuestionId(1);
      await axios.get(serwerUrl+"question/0")
      .then(function (response){
          setQuestion(response.data);
          setDescription(response.data.description);
          setImage(response.data.image);
  
        })      
        .catch(function (error) {
          console.log(error);
        });
    }

      
    }
  async function send_answer(answerId) {
    if (questionId == 5)
      {
        //get result
        await axios.post(serwerUrl+"question/"+questionId.toString(),{
          'answer' : answerId
        })
        .then(function (response){
          setQuestion(response.data);
          setBtnDisable(false);
          setDescription(response.data.description);
          setEnd(true);
          setImage(response.data.image);
        })      
        .catch(function (error) {
          console.log(error);
        });
        
      }
      else
      {
        //send answer
        await axios.post(serwerUrl+"question/"+questionId.toString(),{
          'answer' : answerId
        })
        .then(function (response){
          setQuestion(response.data);
          setDescription(response.data.description);
          console.log(response.data.answers);
          setImage(response.data.image);
          setBtnDisable(false);
        })      
        .catch(function (error) {
          console.log(error);
        });
      }

}
  const button_reset = (e)=>{
    e.preventDefault();
    console.log(questionId);
    setBtnDisable(false);
    get_question();
    setEnd(false);
  }

  const button_click = (e,id)=>{
    e.preventDefault();
    setBtnDisable(true);
    setQuestionId(questionId+1);
    send_answer(id);

  }

  const button_hover = (e,id)=>{
    if (id == -1){
      setDescription(question.description);
      setImage(question.image);
    }
    else{
      setAnswerId(id);
      //special case
      if((question.answers[0]['name'] == 'shooter' || question.answers[0]['name'] == 'autoBattler') && (id==2 || id == 4)){
        setDescription(question.answers[0]['description']);
        setImage(question.answers[0]['image']);
      }
      //special case
      else if((question.answers[1]['name'] == 'platform' || question.answers[1]['name'] == 'baseBuilding')&& (id==3 || id == 5) ){
        setDescription(question.answers[1]['description']);
        setImage(question.answers[1]['image']);
      }
      else{
        setDescription(question.answers[id]['description']);
        setImage(question.answers[id]['image']);
      }
    }
  }

  
  useEffect (()=>{
    get_question();
  },[]);
  if (end != true)
  {
      if (question.answers!=null)
        {
          var answers = question.answers.map((a) =>
            <button disabled={btnDisable} className="answerBtn" 
            onMouseLeave={e=>button_hover(e,-1)} 
            onMouseEnter={e=>button_hover(e,a['id'])} 
            onClick={e=>button_click(e,a['id'])}>
            {a['name']}</button>
          );
      }
      //quetion page
      return (
        <div className='main'>
          <div>
            <h1>{question.question}</h1>
            {answers}
            <h2>{description}</h2>
            <img alt="Nie mozna zaladowac obrazu"
             src={serwerUrl+"static/images/"+image}></img>
          </div>
          <h1>System exprecki</h1>
        </div>
      );
      
    }
    //result page
    return (
      <div className='main'>
      <div>
        <h1>{question.question}</h1>
        <h1>{description}</h1>
        <img alt="Nie mozna zaladowac obrazu"
        src={serwerUrl+"static/images/"+image}></img>
        <div>
          <button className="answerBtn" onClick={e => button_reset(e)}>Reset</button>

        </div>
      </div>
      <h1>System exprecki</h1>
    </div>
  );
}

export default App;
