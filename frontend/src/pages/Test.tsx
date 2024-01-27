import { useEffect, useState } from "react";
export default function Test() {
    const [response, setResponse] = useState('');
    useEffect(() => {
        fetch('http://127.0.0.1:5000/')
            .then(response => response.text())
            .then(
                data => {console.log(data);
                setResponse(data)});
    }, []);
    return <div>{(response)}</div>;
}
