import React, {useRef, useState} from 'react'
import styles from './App.css'
function App(){

  const [message, setMessage] = useState('')

  const[cyber, setCyber] = useState('')
  const inputRef = useRef()
  
  async function submit(e){
    e.preventDefault();
    setMessage(inputRef.current.value)
    console.log(inputRef.current.value)
    setCyber("Your child is being bullied ❤️")

    e.preventDefault();
    const payload = message;
    console.log(payload);
  
    try {
      const response = await fetch("http://127.0.0.1:5000/submit-message", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: inputRef.current.value }),
      });
      const data = await response.json();
      console.log("Response from Flask:", data);
    } catch (error) {
      console.error("Error sending message to Flask:", error);
    }
  }


  return(
    <div style={{backgroundColor: '#86A788'}}>
    <div className='parent_container'>
      <div className='title'><h1>CyberBullying Detector</h1></div>
      <div className='main'>
      <input type='text' ref={inputRef}></input>
      <button className='submit' onClick={submit}>Submit</button>
      </div>
      <div>
        <p className='result'>{cyber}</p>
      </div>
    </div>
  </div>
  )

  
}


export default App