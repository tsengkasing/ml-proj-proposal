# Gradient Descent Visualization

 ![](https://img.shields.io/badge/Numpy-1.15.x-brightgreen.svg?style=flat-square) ![](https://img.shields.io/badge/pandas-0.23.4-brightgreen.svg?style=flat-square) ![](https://img.shields.io/badge/websockets-7.0-brightgreen.svg?style=flat-square)

## Abstract

*Gradient Descent* is a crucial part in *machine learning*. With the method of *Gradient Descent*, we can make *linear Regression* and *logical Regression* more effective.

In this project, we are trying to visualize the process of *Gradient Descent*. Like the value change in the **Theta** or the **Gradient** of each iteration and even the **cost** in each iteration.



## Methodology

Briefly speaking, we will put a callback function inside the *gradient descent* function and the callback function will be called in each **iteration**. 

We build a front-end web page to visualize the data. The communication is maintained by **WebSocket**.

We setup a *websocket* between the web page and the backend python script.

In each **iteration**, the backend will send a message (including the theta, cost, etc) to front-end. Then the web page can add the new data on the graph.





## Tiny Demo



![gradient_descent](https://user-images.githubusercontent.com/10103993/48656043-b043f500-ea5a-11e8-8b82-948afc8dec83.gif)

### Get started

#### Front-end Setup

- Install Node.js [link](https://nodejs.org/en/download/current/)
- Install dependency
  ```bash
  cd 2-Gradient-Descent-Visualization/demo/front-end
  npm install parcel -g
  npm install
  ```
- Build front-end
  ```bash
  parcel index.html
  ```

#### Install libraries

- [NumPy](http://www.numpy.org/)
- [Pandas](https://pandas.pydata.org/)

```bash
pip install numpy pandas
```

#### Run 

```bash
python server.py
```

Then, Open browser with URL ``http://localhost:1234``