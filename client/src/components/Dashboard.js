import axios from 'axios';
import React, {useEffect, useState} from 'react'
import { Link, useNavigate } from 'react-router-dom';
import Navbar from './Navbar';

const Dashboard = (props) => {
    const [loaded, setLoaded] = useState(false)
    const {loggedInUser, data, setData} = props;
    const {user, setUser} = useState()
    console.log('am I still seeing loggedIn', loggedInUser)

    // useEffect(() => {
    //     console.log('user before in effect', user)
    //     setUser(loggedInUser)
    // })

    // console.log('did I set User', user)
    return (
        <>
        </>
    )
}

export default Dashboard