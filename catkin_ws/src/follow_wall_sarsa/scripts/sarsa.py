import sys
# Q_table defined below
sys.dont_write_bytecode = True

q_table = {
    "left-close-front-close-right-close": {
        "forward": 0,
        "left": 10,
        "right": 10
    },       
    "left-close-front-close-right-medium": {
        "forward":0,
        "left":0,
        "right":10
    },
    "left-close-front-close-right-far":{
        "forward":0,
        "left":0,
        "right":10
    },
    "left-close-front-medium-right-close": {
        "forward":0,
        "left":10,
        "right":10
    },
    "left-close-front-medium-right-medium": {
        "forward":0,
        "left":0,
        "right":10
    },
    "left-close-front-medium-right-far": {
        "forward":0,
        "left":0,
        "right":10
    },
    "left-close-front-far-right-close": {
        "forward":10,
        "left":0,
        "right":0
    },
    "left-close-front-far-right-medium": {
        "forward":0,
        "left":0,
        "right":10
    },
    "left-close-front-far-right-far": {
        "forward":0,
        "left":0,
        "right":10
    },
    "left-medium-front-close-right-close": {
        "forward":0,
        "left":10,
        "right":0
    },
    "left-medium-front-close-right-medium": {
        "forward":0,
        "left":10,
        "right":10
    },
    "left-medium-front-close-right-far": {
        "forward":0,
        "left":0,
        "right":10
    },
    "left-medium-front-medium-right-close": {
        "forward":0,
        "left":10,
        "right":0
    },
    "left-medium-front-medium-right-medium": {
        "forward":10,
        "left":0,
        "right":0
    },
    "left-medium-front-medium-right-far": {
        "forward":10,
        "left":0,
        "right":0
    },
    "left-medium-front-far-right-close": {
        "forward":0,
        "left":10,
        "right":0
    },
    "left-medium-front-far-right-medium": {
        "forward":10,
        "left":0,
        "right":0
    },
    "left-medium-front-far-right-far": {
        "forward":10,
        "left":0,
        "right":0
    },
    "left-far-front-close-right-close": {
        "forward":0,
        "left":10,
        "right":0
    },
    "left-far-front-close-right-medium": {
        "forward":0,
        "left":10,
        "right":0
    },
    "left-far-front-close-right-far": {
        "forward":0,
        "left":10,
        "right":10
    },
    "left-far-front-medium-right-close": {
        "forward":0,
        "left":10,
        "right":0
    },
    "left-far-front-medium-right-medium": {
        "forward":10,
        "left":0,
        "right":0
    },
    "left-far-front-medium-right-far": {
        "forward":10,
        "left":0,
        "right":0
    },
    "left-far-front-far-right-close": {
        "forward":0,
        "left":10,
        "right":0
    },
    "left-far-front-far-right-medium": {
        "forward":10,
        "left":0,
        "right":0
    },
    "left-far-front-far-right-far": {
        "forward":10,
        "left":0,
        "right":0
    }
}