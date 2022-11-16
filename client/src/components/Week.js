import React from 'react'
import Navbar from './Navbar';

const Week = (props) => {
    const {user} = props;

    return (
        <div>
            <Navbar/>
            <h2>{user.username}, create your week</h2>
        </div>
    )
}

export default Week