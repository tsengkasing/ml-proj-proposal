import React from 'react';
import ReactDOM from 'react-dom';

import { LineChart, CartesianGrid, XAxis, YAxis, Tooltip, Legend, Line } from 'recharts';

// const data = [
//     {"it": 1, "theta": [0.015, 0.025, 0.025, 0.025], "theta_gradient": [-1.5, -2.5, -2.5, -2.5], "cost": 1.04883125},
//     {"it": 2, "theta": [0.028725, 0.0479, 0.0479, 0.0479], "theta_gradient": [-1.3725, -2.29, -2.29, -2.29], "cost": 0.8800788490625},
//     {"it": 3, "theta": [0.04128225, 0.068876625, 0.068876625, 0.068876625], "theta_gradient": [-1.255725, -2.0976625, -2.0976625, -2.0976625], "cost": 0.7385191503715038},
//     {"it": 4, "theta": [0.052769979375, 0.088091644375, 0.088091644375, 0.088091644375], "theta_gradient": [-1.1487729375, -1.9215019375, -1.9215019375, -1.9215019375], "cost": 0.6197702579899017},
//     {"it": 5, "theta": [0.063278155584375, 0.10569322135625, 0.10569322135625, 0.10569322135625], "theta_gradient": [-1.0508176209375, -1.760157698125, -1.760157698125, -1.760157698125], "cost": 0.5201563851194574},
// ];

class App extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            theta: [],
            thetaGradient: [],
            cost: [],
        };
    }

    componentDidMount() {
        let socket = new WebSocket('ws://127.0.0.1:8765');
        // Connection opened
        socket.addEventListener('open', event => { socket.send('start'); });
        // Listen for messages
        socket.addEventListener('message', event => {
            console.log('Message from server ', event.data);
            const { it, theta, theta_gradient, cost } = JSON.parse(event.data);
            console.log({ it, theta, theta_gradient, cost });
            this.setState({
                theta: [...this.state.theta, Object.assign(theta, {it})],
                thetaGradient: [...this.state.thetaGradient, Object.assign(theta_gradient, {it})],
                cost: [...this.state.cost, {it, cost}],
            });
        });
    }

    render() {
        const { theta, thetaGradient, cost } = this.state;
        const lastTheta = theta[theta.length - 1];
        const lastThetaGradient = thetaGradient[thetaGradient.length - 1];
        const lastCost = cost[cost.length - 1];
        return (
            <div>
                <h3>Theta θ</h3>
                <div className="theta group">
                    <LineChart width={1024} height={250} data={theta}
                      margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="it" />
                      <YAxis />
                      <Tooltip />
                      <Legend />
                      <Line type="monotone" name="θ0" dataKey="0" stroke="#8884d8" />
                      <Line type="monotone" name="θ1" dataKey="1" stroke="#82ca9d" />
                      <Line type="monotone" name="θ2" dataKey="2" stroke="#66ccff" />
                      <Line type="monotone" name="θ3" dataKey="3" stroke="#ffc658" />
                    </LineChart>
                    <div className="latest_value">
                        {lastTheta ? lastTheta.slice(0, 4).map((v, i) => (<div key={i}>θ{i} = {v}</div>)) : ''}
                    </div>
                </div>
                <h3>Theta Gradient</h3>
                <div className="theta_gradient group">
                    <LineChart width={1024} height={250} data={thetaGradient}
                      margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="it" />
                      <YAxis />
                      <Tooltip />
                      <Legend />
                      <Line type="monotone" name="θ0" dataKey="0" stroke="#8884d8" />
                      <Line type="monotone" name="θ1" dataKey="1" stroke="#82ca9d" />
                      <Line type="monotone" name="θ2" dataKey="2" stroke="#8884d8" />
                      <Line type="monotone" name="θ3" dataKey="3" stroke="#82ca9d" />
                    </LineChart>
                    <div className="latest_value">
                        {lastThetaGradient ? lastThetaGradient.slice(0, 4).map((v, i) => (<div key={i}>θ{i} = {v}</div>)) : ''}
                    </div>
                </div>
                <h3>Cost</h3>
                <div className="cost group">
                    <LineChart width={1024} height={250} data={cost}
                      margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="it" />
                      <YAxis />
                      <Tooltip />
                      <Legend />
                      <Line type="monotone" dataKey="cost" stroke="#8884d8" />
                    </LineChart>
                    <div className="latest_value">
                        {lastCost ? lastCost['cost']: ''}
                    </div>
                </div>
            </div>
        );
    }
}

ReactDOM.render(<App />, document.getElementById('root'));
