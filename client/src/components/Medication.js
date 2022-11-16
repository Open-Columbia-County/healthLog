import React, {useState} from 'react'
import Navbar from './Navbar'

const Medication = () => {
    const [medicine, setMedicine] = useState('');
    const [frequency, setFrequency] = useState('');

    const handleSubmit = () => {
        //handle form data
    }

    const showMedicine = () => {
        //handle medicine animations, JQuery?
    }

    return (
        <div>
            <Navbar/>
            <form onSubmit={handleSubmit()} className='border border-dark d-flex flex-column w-50'>
                <div>

                    <label>Medication Name:</label>
                    <input 
                        type='text' 
                        value={medicine}
                        onChange={(e)=> setMedicine(e.target.value)} 
                        />
                </div>
                <div>

                    <label>Frequency Taken:</label>
                    <input 
                        type='text' 
                        value={frequency}
                        onChange={(e)=> setFrequency(e.target.value)} 
                        />
                </div>
                <button className='w-25'>Add medication</button>
            </form>
            <button onClick={showMedicine()}>Current Medications Created</button>
        </div>
    )
}

export default Medication;