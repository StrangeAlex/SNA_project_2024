from enum import Enum


N_TRACKS = 4
TRACKS = ['Drums', 'Bass', 'Guitar', 'Strings']

# These defaults, which should not be changed, are set when the related 
# variables in the YAML config file are not set. 
DEFAULT_MIDI_PROGRAMS = {
    'Drums': -1,
    'Bass': 34,
    'Guitar': 1,
    'Strings': 83,
}
DEFAULT_SOUNDFONT_PATH = '/usr/share/soundfonts/FluidR3_GM.sf2'


# Pitch tokens have values in the range [0, 130]. Tokens from 0 to 127 represent
# MIDI pitches. Token 60 represents middle C (C4).
# See https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
# for the complete list of MIDI pitches.
class PitchToken(Enum):
    SOS = 128
    EOS = 129
    PAD = 130
    PAD_M = 290


N_PITCH_TOKENS = 291
MAX_PITCH_TOKEN = 127


# Duration tokens have values in the range [0, 98]. Tokens from 0 to 95 have to
# be interpreted as durations from 1 to 96 timesteps.
class DurationToken(Enum):
    SOS = 96
    EOS = 97
    PAD = 98



N_DUR_TOKENS = 99
MAX_DUR_TOKEN = 95


# Dimension of (pitch, duration) token pair
D_TOKEN_PAIR = N_PITCH_TOKENS + N_DUR_TOKENS

# Number of maximum tokens stored in each timestep (14 + SOS and EOS)
MAX_SIMU_TOKENS = 16


# This enum contains edge type indices for each edge type
class EdgeTypes(Enum):
    TRACK = 0 # This has to be interpreted as the starting index
    ONSET = N_TRACKS
    NEXT = N_TRACKS + 1

# N_TRACKS track types + 1 onset edge type + 1 next edge type
N_EDGE_TYPES = N_TRACKS + 2

# lst = [6,13,8,15,10,17,12,7,14,9,16,11,10,17,12,19,14,21,16,11,18,13,20,15,
#         14,21,16,23,18,25,20,15,22,17,24,19,18,25,20,27,22,29,24,19,26,21,28,
#         23,22,29,24,31,26,33,28,23,30,25,32,27,26,33,28,35,30,37,32,27,34,29,
#         36,31,30,37,32,39,34,41,36,31,38,33,40,35,34,41,36,43,38,45,40,35,42,
#         37,44,39,38,45,40,47,42,49,44,39,46,41,48,43,42,49,44,51,46,53,48,43,
#         50,45,52,47,46,53,48,55,50,57,52,47,54,49,56,51,50,57,52,59,54,61,56,
#         51,58,53,60,55,54,61,56,63,58,65,60,55,62,57,64,59,58,65,60,67,62,69,
#         64,59,66,61,68,63,62,69,64,71,66,73,68,63,70,65,72,67,66,73,68,75,70,
#         77,72,67,74,69,76,71,70,77,72,79,74,81,76,71,78,73,80,75,74,81,76,83,
#         78,85,80,75,82,77,84,79,78,85,80,87,82,89,84,79,86,81,88,83,82,89,84,
#         91,86,93,88,83,90,85,92,87,86,93,88,95,90,97,92,87,94,89,96,91,90,97,
#         92,99,94,101,96,91,98,93,100,95,94,101,96,103,98,105,100,95,102,97,104,
#         99,98,105,100,107,102,109,104,99,106,101,108,103,128,129,130]


# Наша "кастомная" матрица
lst = [0, 7, 2, 9, 4, 11, 6, 1, 8, 3, 10, 5, 12, 19, 14, 21, 16, 23, 18, 13, 20, 15, 22, 17, 24, 31, 26, 33, 28, 35, 30, 25, 32, 27, 34, 29, 36, 43, 38, 45, 40, 47, 42, 37, 44, 39, 46, 41, 48, 55, 50, 57, 52, 59, 54, 49, 56, 51, 58, 53, 60, 67, 62, 69, 64, 71, 66, 61, 68, 63, 70, 65, 72, 79, 74, 81, 76, 83, 78, 73, 80, 75, 82, 77, 84, 91, 86, 93, 88, 95, 90, 85, 92, 87, 94, 89, 96, 103, 98, 105, 100, 107, 102, 97, 104, 99, 106, 101, 108, 115, 110, 117, 112, 119, 114, 109, 116, 111, 118, 113, 120, 127, 122, 129, 124, 131, 126, 121, 128, 123, 130, 125, 132, 139, 134, 141, 136, 143, 138, 133, 140, 135, 142, 137, 144, 151, 146, 153, 148, 155, 150, 145, 152, 147, 154, 149, 156, 163, 158, 165, 160, 167, 162, 157, 164, 159, 166, 161, 168, 175, 170, 177, 172, 179, 174, 169, 176, 171, 178, 173, 180, 187, 182, 189, 184, 191, 186, 181, 188, 183, 190, 185, 192, 199, 194, 201, 196, 203, 198, 193, 200, 195, 202, 197, 204, 211, 206, 213, 208, 215, 210, 205, 212, 207, 214, 209, 216, 223, 218, 225, 220, 227, 222, 217, 224, 219, 226, 221, 228, 235, 230, 237, 232, 239, 234, 229, 236, 231, 238, 233, 240, 247, 242, 249, 244, 251, 246, 241, 248, 243, 250, 245, 252, 259, 254, 261, 256, 263, 258, 253, 260, 255, 262, 257, 264, 271, 266, 273, 268, 275, 270, 265, 272, 267, 274, 269, 276, 283, 278, 285, 280, 287, 282, 277, 284, 279, 286, 281, 128, 129, 130]

