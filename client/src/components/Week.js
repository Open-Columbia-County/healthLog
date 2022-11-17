import React, {useState} from 'react'
import Navbar from './Navbar';

const Week = (props) => {
    const {user} = props;
    const [weekName, setWeekName] = useState('');

    const createWeek = (e) => {
        e.preventDefault();
        console.log('testing function')
    }

    return (
        <div>
            <h2>Health and Mental Well-Being Log</h2>
            <Navbar/>
            <h2>{user.username}, create your week</h2>
            <form onSubmit={createWeek}>
                <div className='d-flex flex-column w-25'>

                    <label>Title</label>
                    <input 
                        type='text' 
                        value={weekName}
                        onChange={(e)=>setWeekName(e.target.value)}
                        />
                        <button>Create Week</button>
                </div>
            </form>
        </div>
    )
}

export default Week