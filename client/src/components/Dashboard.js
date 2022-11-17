import axios from 'axios';
import React, {useEffect, useState} from 'react'
import { Link, useNavigate } from 'react-router-dom';
import Navbar from './Navbar';

const Dashboard = (props) => {
    const [loaded, setLoaded] = useState(false);
    const [start, setStart] = useState(false);
    const {user, setUser, data, setData} = props;
    
    console.log('am I still seeing loggedIn from props', user)

    useEffect(() => {
        console.log('user before in effect', user)
        setUser(user);
        setLoaded(true);
        
    }, [])

    const slide = () => {
        //create slide down animation
        setStart(!start);
        
    }

    
    return (
        <div className='w-50 mx-auto border border-dark'>
            {
                loaded==true?
                <h2>Welcome {user.username}</h2>:null
                
            }
            <Navbar/>

            <button onClick={slide} className='text-center'>
                Getting Started
            </button>
            {
                start == true?
                <div className='text-center'>
                    
                    <h5>1st Steps</h5> 
                    <ol>
                        <li>Create this weeks base log</li>
                        <li>Create todays post and add content</li>
                        <li>Now you are ready to add other details</li>
                    </ol>
                    <h5>Adding your Moods/Symptoms</h5>
                    <p>
                        This is all in 1 step. You get to add you mood
                        to each symptom you chose to add
                    </p>
                    <h5>Adding/Logging your Medications</h5>
                    <p>
                        You may need to add your medication to the master list
                        if you don't already see it
                    </p>
                    <p>
                        Once added, choose it from the drop down to log that you have taken it
                    </p>
                    <h5>Are you a diabetic? Update you profile to enable sugar tracking</h5>
                    <p>
                        Once you enable sugar tracking, you can then add this to you daily posts
                    </p>
                </div>
                : null
            }
        </div>
    )
}

export default Dashboard