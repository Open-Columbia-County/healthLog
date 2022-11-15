import axios from 'axios';
import React, {useEffect, useState} from 'react'
import { Link, useNavigate } from 'react-router-dom';
import Navbar from './Navbar';

const Dashboard = (props) => {
    const [loaded, setLoaded] = useState(false)
    const {user, setUser, data, setData} = props;
    
    console.log('am I still seeing loggedIn from props', user)

    useEffect(() => {
        console.log('user before in effect', user)
        setUser(user)
        setLoaded(true)
        
    }, [])

    
    return (
        <>
        <h2>Dashboard Placeholder</h2>
        {
            loaded==true?
            <h2>Welcome {user.username}</h2>:null
        }
        </>
    )
}

export default Dashboard