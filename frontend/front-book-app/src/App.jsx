import { useState, useEffect } from 'react'
import './App.css'

function App() {
  
  useEffect(() => {
    fetch('http://localhost:8000/api/books/search?book_name=Harry Potter&author=J.K. Rowling')
      .then(response => response.json())
      .then(data => {
        console.log(data)
      })
      .catch(error => {
        console.error('Error fetching data:', error)
      })
  }, [])

  return (
    <>
      <h1>Hello World!</h1>
    </>
  )
}

export default App
