"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": (1, 2, 5, 3, 4, 7, 6),
            "answer": 3
        },
        {
            "input": (0, 1, 2, 3),
            "answer": 0
        },
        {
            "input": (99, -99),
            "answer": 1
        },
        {
            "input": (5, 3, 2, 1, 0),
            "answer": 10
        },
    ],
    "Extra": [
        {
            "input": (
                -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79,
                -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58,
                -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37,
                -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16,
                -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                12,
                13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                39,
                40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65,
                66,
                67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92,
                93,
                94, 95, 96, 97, 98, 99),
            "answer": 0
        },
        {
            "input": (
                99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74,
                73,
                72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47,
                46,
                45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20,
                19,
                18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9,
                -10,
                -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31,
                -32, -33, -34, -35, -36, -37, -38, -39, -40, -41, -42, -43, -44, -45, -46, -47, -48, -49, -50, -51, -52,
                -53, -54, -55, -56, -57, -58, -59, -60, -61, -62, -63, -64, -65, -66, -67, -68, -69, -70, -71, -72, -73,
                -74, -75, -76, -77, -78, -79, -80, -81, -82, -83, -84, -85, -86, -87, -88, -89, -90, -91, -92, -93, -94,
                -95, -96, -97, -98, -99),
            "answer": 19701
        },
        {
            "input": (0, 1),
            "answer": 0
        },
        {
            "input": (1, 0),
            "answer": 1
        },
        {
            "input": (
            5, 12, -85, -92, -32, -8, 1, -34, -55, -74, -44, -63, 84, 8, 65, 54, 71, 90, -81, 98, -17, 82, -45, -72, 37,
            26, 91, 97, 64, -62, -24, -70, 42, 56, -67, 0, -78, -87, -57, -56, 67, -2, 11, -16, 7, 13, -1, -46, -54, 16,
            -4, -14, 63, -15, -48, -66, 36, 46, 75, 85, -79, -83, -52, 73, 49, -3, 88, -10, 60, -21, -75, 38, 44, 2,
            -89, -65, -96, -22, -76, -31, -58, 55, 58, 14, -47, 20, 80, -60, 93, 62, -71, 24, 45, -64, 94, 29, -94, -36,
            57, -23, 6, 51, 15, -5, -53, 25, -41, -97, 89, -59, 66, 87, -19, -38, -27, -86, -9, 40, 18, -93, 30, -20,
            81, 34, 3, 92, 77, -25, -49, 74, -51, 17, 41),
            "answer": 4181
        },
        {
            "input": (
            58, -55, -82, 73, 98, -99, -86, 67, 84, 77, -73, -65, -1, 88, -39, 51, 31, -64, -34, 1, 36, -43, 91, 32,
            -88, 6, -93, 56, -7, -58, -3, -11, 78, -48, -96, -20, 20, -36, -50, 70, 86, -15, -74, 76, -32, -42, -57,
            -51, -9, -80, -12, -72, -56, 95, 7, 14, 17, 52, -19, -26, -27, -63, -78, 89, 74, 16, -40, -90, 18, 45, 0,
            42, 33, 61, 26, 68, -23, 2, -98, 54, -61, -54, -44, 47, 38, -38, -77, 55, 23, -76, 24, 69, 9, -79, -87, -35,
            -91, 75, 90, 72, -2, 97, 71, -24, 80, -16, -25, 22, -70, 39, -4, -33, 28, 10, -47, -5, -62, -46, 63, -95,
            34, -18, 37, 85, -49, -28, 4, -71, -60, -22, 12, 99, -13, -31, -29, 49, -97, -59, 62, -92, -69, -30, 94, 13,
            96, 40, 11, 25, 15, -81, -37, 92, 83, 87, 44, -52, 48, -10, 5, -21, 19, 53, 79, 57, -53, 3, 43, 59, 50, -66,
            -85, 81, 60, -17, 29, -14, 93, -83, -84, 8, -94, 64, 46, 65, 82, -41, 41, 66, -68, -75),
            "answer": 8469
        },
        {
            "input": (
            -76, -93, 29, 81, 93, 20, 43, -34, 9, 42, -97, -90, -24, -66, -87, 35, 4, -69, -21, 46, -28, 89, 24, 99,
            -64, 18, -50, 66, -8, -57, 61, -55, -25, 41, 15, 60, -35, 12, 10, -6, 57, -16, 27, -54, -42, 28, 56, -47,
            59, -31, -20, -40, -68, -41, -85, 0, 58, 33, -89, 13, 19, 11, -39, -18, -17, 82, 30, -43, 94, -94, -5, -38,
            -65, -71, 31, 2, 39, 44, -48, -29, -88, -82, 74, -49, 17, 67, -98, -9, 78, -14, -44, 71, 6, 40, 45, -13, 85,
            75, 69, 80, 51, 72, 88, 21, 14, -22, -4, -15, 37, 8, 54, -84, 96, -70, -2, 48, 3, 32, -59, -74, -37, -62,
            -26, -83, -23, 65, 1, 55, 50, -12, 97, -56, 23, -36, -80, -79, 87, 70, 62, 16, -52, -58, -45, 53, -32, -75,
            -60, -61, 86, 73, -81, -1, 76, -95, -77, -72, -63, 90, -86, -11, -27, 64, 68, 79, 38, -46, 83, 91, -53, 47,
            -99, -91, -3, -19, 5, -73, -33, 34, 92, 26, -7, -92, 95, 84, 49, 7, 25, -78, -67, -10, 36, 98, 22, -30,
            -51),
            "answer": 9272
        },
        {
            "input": (
            -1, 69, -75, -40, 63, -57, -52, 45, 4, 8, 19, 31, -94, 68, -68, 43, 56, -62, 59, 97, -39, -99, 77, -32, -72,
            -37, 78, -11, 29, -82, -17, 93, 23, 50, -38, -22, -61, -41, 76, -69, -81, -50, 7, -74, -98, -95, 40, -44,
            64, 21, -33, -42, -8, 47, 2, -65, -97, 34, 42, 3, -85, 55, -71, 20, -88, -73, -29, -91, -90, 71, -13, 51,
            81, 66, 27, 41, -34, -21, -26, 6, 17, 16, 61, -86, -16, -10, 95, 25, 88, -45, -48, 32, 99, 30, 62, -9, -5,
            65, 74, 33, -53, 67, 70, 60, 28, -28, -60, 75, 26, -27, -14, 38, 11, -47, 84, 58, 98, 44, -80, 96, 52, -24,
            -35, 83, -87, 72, -89, -19, 85, -93, -59, -92, -51, -23, -54, 18, -43, 10, 15, -67, -12, 36, -55, 35, 54,
            -78, 24, 86, -25, -64, 91, 73, 9, -84, -30, -76, 0, 14, 79, -7, -18, 13, 87, 80, 37, -83, -49, -77, 82, -2,
            -58, 89, -3, -70),
            "answer": 7206
        },
        {
            "input": (
            -28, -44, -78, -2, 2, 97, 59, -48, -81, -83, -7, 33, 61, -4, -72, 93, -68, -17, 24, 43, -76, -45, 65, 80,
            -37, 58, -88, 19, 50, 60, 63, -55, 36, 57, 20, 27, 83, 28, -52, 13, -90, 16, 18, 62, -3, 70, 22),
            "answer": 466
        },
        {
            "input": (
            30, -90, -84, 49, -56, -30, -83, -79, -60, 5, 53, -59, 97, 28, 35, 78, -94, -57, -51, 0, -95, -91, 69, -41,
            2, 68, -98, -97, 45, 15, -8, 99, -67, 31, -99, 29, -38, -77, -33, -25, -15, 94, -3, 71, 65, -44, 61, -68,
            89, -21, -54, -12, 25, 48, 62, -81, 74, 26, 17, -24, 40, 51, -86, -27, 46, 54, 24, -7, -73, -96, -52, 91,
            -53, 36, -31, 14, 32, 52, 55, -5, 70, 1, -19, 90, -58, -70, -55, 11, 93, 92, -2, 3, -92, 88, 82, -16, 18,
            67, 80, 22, -20, -29, 84, -39, -23, 27, 72, 6, -78, 16, -1, 79, -22, 21, 77, 96, 66, -4, 75, -87, 7, 59, 39,
            -64, 12, 50, 86, -93, 41, -13, -10, 38, -34, 56),
            "answer": 3812
        },
    ]
}
