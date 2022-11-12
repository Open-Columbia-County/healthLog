import React from 'react'
import axios from 'axios'

const ReactConnectTest = () => {
    useEffect(()=> {
        axios.get('http://localhost:8000/food/')
        .then((res) => {
            var data = res.data;
            
            setLoaded(True)
        })
        .catch((err) => {
            console.log('Boo', err)
        })
    })

    return (
        <div>ReactConnectTest</div>
    )
}

export default ReactConnectTest