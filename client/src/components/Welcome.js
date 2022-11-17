import React from 'react'
import Navbar from './Navbar';

const Welcome = () => {
    return (
        <div className='container'>
            <div className='row'>
                <div className='d-flex flex-column'>
                    <div className='border border-dark rounded mx-auto my-3 column col-12 col-sm-12 col-md-10 col-lg-10'>
                        <Navbar/>
                    </div>
                    <div className='border border-dark rounded d-flex flex-column align-items-start mx-auto px-4 py-2 my-3 column col-12 col-sm-10 col-md-10 col-lg-10'>
                    <p>Everyday we are bombarded by different things.  Good and bad.  Keeping track of your health can help you find patterns and can help you and medical professionals better understand what is going on.</p>
        <p>This application is intended to help you keep track of your health.  You will find a universal bank of symptoms that you can add to your logs.  We are constantly improving and adding new features to this site. Any changes made will not change or remove your logs</p>
        <p>Feel free to take a look at the example accounts to get a feel for what this application can do for you.</p>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Welcome;
