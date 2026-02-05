import { useState } from 'react'

function BookSearch(){
    const [bookName, setBookName] = useState('')
    const [author, setAuthor] = useState('')
    const [results, setResults] = useState([])

    const handleSearch = async () => {
        try{
            const response = await fetch('http://127.0.0.1:8000/api/books/search?book_name='+bookName+'&author='+author)
            const data = await response.json()
            console.log(data)
            setResults(data)
        } catch (error) {
            console.error('Error fetching data: ', error)
        }
    }
    return (
        <div style={{padding : '20px'}}>
            <h2>Book Search 🕵️</h2>
            <div style={{margin : '10px'}}>
                <input 
                type="text" 
                placeholder='Book Name' 
                value={bookName} 
                onChange={(e) => setBookName(e.target.value)}
                />
            </div>
            <div style={{margin : '10px'}}>
                <input 
                type="text" 
                placeholder='Author' 
                value={author} 
                onChange={(e) => setAuthor(e.target.value)}
                />
            </div>
            <button onClick={handleSearch}>Search</button>
            <div style={{marginTop : '20px'}}>
                {results.length > 0 ? (
                    results.map((book, index) => (
                        <div 
                            key={index} 
                            style={{
                                border : '1px solid #ccc',
                                padding : '10px',
                                marginBottom : '10px',
                                borderRadius : '5px',
                            }}
                        >
                        <strong>{book.title}</strong> <br/>
                        <em>{book.authors.join(', ')}</em>
                        {console.log('Se ejecuta')}
                        </div>
                    ))
                ) : (
                    <p>No results found</p>
                )}
            </div>
        </div>
    )
}

export default BookSearch