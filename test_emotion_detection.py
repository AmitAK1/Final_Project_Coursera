from EmotionDetection import emotion_detector
def test_emotion_detection():
    test_cases = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear")
    ]

    for text, expected_emotion in test_cases:
        result = emotion_detector(text)
        assert result["dominant_emotion"] == expected_emotion, \
            f"Failed for text: '{text}'"
    print("All emotion detection tests passed successfully!")
#Run the test
test_emotion_detection()
