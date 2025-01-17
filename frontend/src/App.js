import React, {useRef, useState} from 'react'
import styles from './App.css'
function App(){

  const [message, setMessage] = useState('')

  const[cyber, setCyber] = useState('')
  const inputRef = useRef()
  
  function submit(e){
    e.preventDefault();
    setMessage(inputRef.current.value)
    console.log(inputRef.current.value)
    setCyber("Your child is being bullied ❤️")
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