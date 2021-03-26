import sys

# Q_table defined below
sys.dont_write_bytecode = True

# q_table = {
#     "left-close-front-close-right-close": {
#         "forward": 0,
#         "left": 0,
#         "right": 0
#     },
#     "left-close-front-close-right-medium": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-close-front-close-right-far":{
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-close-front-medium-right-close": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-close-front-medium-right-medium": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-close-front-medium-right-far": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-close-front-far-right-close": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-close-front-far-right-medium": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-close-front-far-right-far": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-medium-front-close-right-close": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-medium-front-close-right-medium": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-medium-front-close-right-far": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-medium-front-medium-right-close": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-medium-front-medium-right-medium": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-medium-front-medium-right-far": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-medium-front-far-right-close": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-medium-front-far-right-medium": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-medium-front-far-right-far": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-far-front-close-right-close": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-far-front-close-right-medium": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-far-front-close-right-far": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-far-front-medium-right-close": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-far-front-medium-right-medium": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-far-front-medium-right-far": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-far-front-far-right-close": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-far-front-far-right-medium": {
#         "forward":0,
#         "left":0,
#         "right":0
#     },
#     "left-far-front-far-right-far": {
#         "forward":0,
#         "left":0,
#         "right":0
#     }
# }
q_table = {
    "left-close-front-tooclose-rightfront-close-right-tooclose-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-close-right-tooclose-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-close-right-tooclose-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-close-right-tooclose-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-close-right-close-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-close-right-close-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-close-right-close-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-close-right-close-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-close-right-medium-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-close-right-medium-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-close-right-medium-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-close-right-medium-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-close-right-far-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-close-right-far-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-close-right-far-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-close-right-far-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-close-right-toofar-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-close-right-toofar-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-close-right-toofar-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-close-right-toofar-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-far-right-tooclose-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-far-right-tooclose-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-far-right-tooclose-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-far-right-tooclose-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-far-right-close-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-far-right-close-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-far-right-close-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-far-right-close-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-far-right-medium-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-far-right-medium-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-far-right-medium-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-far-right-medium-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-far-right-far-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-far-right-far-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-far-right-far-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-far-right-far-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-far-right-toofar-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-far-right-toofar-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-far-right-toofar-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-tooclose-rightfront-far-right-toofar-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-close-right-tooclose-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-close-right-tooclose-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-close-right-tooclose-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-close-right-tooclose-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-close-right-close-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-close-right-close-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-close-right-close-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-close-right-close-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-close-right-medium-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-close-right-medium-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-close-right-medium-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-close-right-medium-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-close-right-far-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-close-right-far-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-close-right-far-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-close-right-far-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-close-right-toofar-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-close-right-toofar-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-close-right-toofar-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-close-right-toofar-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-far-right-tooclose-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-far-right-tooclose-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-far-right-tooclose-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-far-right-tooclose-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-far-right-close-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-far-right-close-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-far-right-close-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-far-right-close-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-far-right-medium-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-far-right-medium-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-far-right-medium-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-far-right-medium-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-far-right-far-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-far-right-far-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-far-right-far-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-far-right-far-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-far-right-toofar-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-far-right-toofar-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-far-right-toofar-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-close-rightfront-far-right-toofar-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-close-right-tooclose-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-close-right-tooclose-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-close-right-tooclose-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-close-right-tooclose-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-close-right-close-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-close-right-close-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-close-right-close-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-close-right-close-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-close-right-medium-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-close-right-medium-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-close-right-medium-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-close-right-medium-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-close-right-far-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-close-right-far-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-close-right-far-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-close-right-far-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-close-right-toofar-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-close-right-toofar-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-close-right-toofar-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-close-right-toofar-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-far-right-tooclose-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-far-right-tooclose-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-far-right-tooclose-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-far-right-tooclose-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-far-right-close-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-far-right-close-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-far-right-close-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-far-right-close-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-far-right-medium-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-far-right-medium-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-far-right-medium-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-far-right-medium-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-far-right-far-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-far-right-far-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-far-right-far-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-far-right-far-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-far-right-toofar-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-far-right-toofar-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-far-right-toofar-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-medium-rightfront-far-right-toofar-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-close-right-tooclose-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-close-right-tooclose-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-close-right-tooclose-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-close-right-tooclose-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-close-right-close-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-close-right-close-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-close-right-close-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-close-right-close-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-close-right-medium-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-close-right-medium-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-close-right-medium-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-close-right-medium-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-close-right-far-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-close-right-far-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-close-right-far-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-close-right-far-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-close-right-toofar-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-close-right-toofar-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-close-right-toofar-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-close-right-toofar-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-far-right-tooclose-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-far-right-tooclose-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-far-right-tooclose-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-far-right-tooclose-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-far-right-close-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-far-right-close-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-far-right-close-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-far-right-close-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-far-right-medium-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-far-right-medium-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-far-right-medium-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-far-right-medium-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-far-right-far-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-far-right-far-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-far-right-far-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-far-right-far-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-far-right-toofar-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-far-right-toofar-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-far-right-toofar-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-close-front-far-rightfront-far-right-toofar-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-close-right-tooclose-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-close-right-tooclose-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-close-right-tooclose-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-close-right-tooclose-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-close-right-close-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-close-right-close-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-close-right-close-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-close-right-close-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-close-right-medium-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-close-right-medium-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-close-right-medium-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-close-right-medium-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-close-right-far-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-close-right-far-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-close-right-far-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-close-right-far-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-close-right-toofar-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-close-right-toofar-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-close-right-toofar-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-close-right-toofar-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-far-right-tooclose-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-far-right-tooclose-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-far-right-tooclose-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-far-right-tooclose-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-far-right-close-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-far-right-close-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-far-right-close-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-far-right-close-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-far-right-medium-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-far-right-medium-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-far-right-medium-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-far-right-medium-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-far-right-far-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-far-right-far-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-far-right-far-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-far-right-far-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-far-right-toofar-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-far-right-toofar-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-far-right-toofar-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-tooclose-rightfront-far-right-toofar-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-close-right-tooclose-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-close-right-tooclose-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-close-right-tooclose-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-close-right-tooclose-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-close-right-close-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-close-right-close-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-close-right-close-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-close-right-close-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-close-right-medium-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-close-right-medium-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-close-right-medium-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-close-right-medium-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-close-right-far-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-close-right-far-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-close-right-far-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-close-right-far-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-close-right-toofar-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-close-right-toofar-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-close-right-toofar-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-close-right-toofar-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-far-right-tooclose-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-far-right-tooclose-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-far-right-tooclose-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-far-right-tooclose-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-far-right-close-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-far-right-close-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-far-right-close-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-far-right-close-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-far-right-medium-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-far-right-medium-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-far-right-medium-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-far-right-medium-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-far-right-far-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-far-right-far-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-far-right-far-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-far-right-far-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-far-right-toofar-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-far-right-toofar-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-far-right-toofar-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-close-rightfront-far-right-toofar-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-close-right-tooclose-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-close-right-tooclose-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-close-right-tooclose-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-close-right-tooclose-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-close-right-close-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-close-right-close-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-close-right-close-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-close-right-close-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-close-right-medium-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-close-right-medium-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-close-right-medium-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-close-right-medium-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-close-right-far-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-close-right-far-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-close-right-far-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-close-right-far-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-close-right-toofar-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-close-right-toofar-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-close-right-toofar-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-close-right-toofar-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-far-right-tooclose-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-far-right-tooclose-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-far-right-tooclose-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-far-right-tooclose-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-far-right-close-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-far-right-close-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-far-right-close-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-far-right-close-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-far-right-medium-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-far-right-medium-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-far-right-medium-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-far-right-medium-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-far-right-far-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-far-right-far-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-far-right-far-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-far-right-far-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-far-right-toofar-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-far-right-toofar-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-far-right-toofar-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-medium-rightfront-far-right-toofar-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-close-right-tooclose-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-close-right-tooclose-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-close-right-tooclose-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-close-right-tooclose-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-close-right-close-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-close-right-close-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-close-right-close-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-close-right-close-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-close-right-medium-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-close-right-medium-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-close-right-medium-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-close-right-medium-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-close-right-far-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-close-right-far-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-close-right-far-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-close-right-far-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-close-right-toofar-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-close-right-toofar-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-close-right-toofar-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-close-right-toofar-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-far-right-tooclose-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-far-right-tooclose-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-far-right-tooclose-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-far-right-tooclose-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-far-right-close-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-far-right-close-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-far-right-close-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-far-right-close-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-far-right-medium-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-far-right-medium-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-far-right-medium-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-far-right-medium-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-far-right-far-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-far-right-far-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-far-right-far-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-far-right-far-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-far-right-toofar-orientation-approaching": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-far-right-toofar-orientation-parallel": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-far-right-toofar-orientation-leaving": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
    "left-far-front-far-rightfront-far-right-toofar-orientation-undefined": {
        "left": 0,
        "forward": 0,
        "right": 0,
    },
}
